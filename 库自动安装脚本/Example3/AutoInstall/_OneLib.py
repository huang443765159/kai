import os
import re
import threading

from Example3.Utils.CONST import CONST
from Example3.Utils.Signals import Signals


class OneLib:

    def __init__(self, lib: str):
        self._lib = lib
        self._sign = Signals()
        self._is_checking = False
        self._ts = 0
        # THREAD
        self._thread = threading.Thread(target=self._working, daemon=True)
        self._thread.start()

    def check_lib(self):
        thread = threading.Thread(target=self._working, daemon=True)
        thread.start()

    def _working(self):
        if self._is_checking:
            print(f'{self._lib} IS_CHECKING')
            return
        self._is_checking = True
        if not os.path.exists(os.path.join(CONST.TAR_FILE, self._lib)):
            os.system(f"cd {CONST.TAR_FILE}; git clone {os.path.join(CONST.GIT_PATH, self._lib)}")
        else:
            os.system(f"cd {os.path.join(CONST.TAR_FILE, self._lib)}")
        result = os.popen(f'python3 -m pip list | grep {self._lib}')
        version = result.readline().split(' ')[-1] if result else ' '
        self._sign.now_lib.emit(self._lib, version)
        with open(os.path.join(CONST.TAR_FILE, self._lib, 'setup.py'), 'r') as f:
            lines = f.read()
            latest_version = re.findall(r'version+=(.+)', lines)[0]
            latest_version = re.split(f'["",]', latest_version)[1]
            can_be_updated = [int(i) for i in re.split(r'[.]', version)] == [int(i) for i in
                                                                             re.split(r'[.]', latest_version)]
            self._sign.latest_lib.emit(self._lib, latest_version, can_be_updated)
        self._is_checking = False

    def install(self):
        self._sign.is_installing.emit(self._lib, True)
        result = os.popen(f'cd {os.path.join(CONST.TAR_FILE, self._lib)}; python3 -m pip install .').read()
        install_success = re.findall(r'Successfully installed', result)
        self._sign.is_installed.emit(self._lib, True if install_success else False)

    def get_check_lib(self) -> bool:
        return self._is_checking
