import os
import re
import platform
import threading

from Example4.ToolInstaller.Utils.CONST import CONST
from Example4.ToolInstaller.Utils.CONST import MONTH_MAP
from Example4.ToolInstaller.Utils.Signals import Signals


class _Const:
    PYTHON3_PATH = '/usr/bin/python3'
    system = platform.system()
    machine = platform.machine()
    if system == 'Darwin' and machine == 'arm64':
        PYTHON3_PATH = '/opt/homebrew/bin/python3'


class OneLib:

    def __init__(self, lib: str):
        self._lib = lib
        self._is_checking = False
        self._release = dict()
        self._sign = Signals()
        # THREAD
        self._thread = threading.Thread(target=self._working, daemon=True)
        self._thread.start()

    def _working(self):
        if self._is_checking:
            print(f'{self._lib} IS_CHECKING')
            return
        self._is_checking = True
        if os.path.exists(os.path.join(CONST.TAR_FILE, self._lib)):
            os.system(f"cd {CONST.TAR_FILE}; rm -rf {self._lib}")
        os.system(f"cd {CONST.TAR_FILE}; git clone {os.path.join(CONST.GIT_PATH, self._lib)}")
        result = os.popen(f'{_Const.PYTHON3_PATH} -m pip list | grep {self._lib}').readline()
        version = result.rsplit()[1] if result else ''
        self._sign.pip3_version.emit(self._lib, version)
        with open(os.path.join(CONST.TAR_FILE, self._lib, 'setup.py'), 'r') as f:
            lines = f.read()
            latest_version = re.findall(r'version+=(.+)', lines)[0]
            latest_version = re.split(f'["",]', latest_version)[1]
            if version:
                can_be_updated = not [int(i) for i in re.split(r'[.]', version)] == [int(i) for i in
                                                                                     re.split(r'[.]', latest_version)]
            else:
                can_be_updated = True
        # RELEASE_VERSION
        git_result = os.popen(f'cd {os.path.join(CONST.TAR_FILE, self._lib)}; git log')
        commit, date = '', ''
        for one_line in git_result.readlines():
            if 'commit' in one_line:
                commit_info = one_line.split()
                if commit_info[0] == 'commit':
                    commit = commit_info[1]
            elif 'Date' in one_line:
                date_info = re.split(r'[ :]', one_line)
                date = date_info[-2] + '.' + MONTH_MAP[date_info[5]] + '.' + date_info[6] + '.' + date_info[7] + '.' + \
                    date_info[8]
            self._release[commit] = date
        self._sign.git_versions.emit(self._lib, latest_version, can_be_updated, self._release)
        self._is_checking = False

    def install(self, lib: str, lib_version: str):
        self._sign.is_installing.emit(self._lib, True)
        if lib_version in self._release.values():
            commit = [key for key, value in self._release.items() if lib_version == value][0]
            result = os.popen(f'cd {os.path.join(CONST.TAR_FILE, self._lib)}; git reset --hard {commit}')
            if 'Unstaged changes after reset' in result.readline():
                print('回退版本成功')
        result = os.popen(f'cd {os.path.join(CONST.TAR_FILE, self._lib)}; {_Const.PYTHON3_PATH} -m pip install .').read()
        install_success = re.findall(r'Successfully installed', result)
        self._sign.is_installed.emit(self._lib, True if install_success else False)

    def get_checking(self) -> bool:
        return self._is_checking
