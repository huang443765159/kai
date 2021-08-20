import os
import sys
import time
from platform import platform
if 'debian' in platform():
    sys.path.append('/home/pi/Desktop/')
elif 'generic' in platform():
    sys.path.append('Desktop/')
import getpass
import pexpect
from multiprocessing.dummy import Pool as ThreadPool  # 创建并行的线程池
from GITTOOL._Tools import NUC, SBC_BOT, SBC_PUMP, PIP_PATH, PACKAGE_PATH_RASP, PACKAGE_PATH_UBUNTU, PACKAGE_PATH_MAC
STACK_NAME = {1: NUC, 2: SBC_BOT, 3: SBC_PUMP}


class GitTool(object):

    def __init__(self, ts_clone):
        self._ts_clone = ts_clone
        # INPUT
        self._user = input('请输入GIT用户名： ')
        self._password = getpass.getpass('请输入GIT密码： ')
        self._stack_name_id = input('请选择要检查更新的stack_id--1: NUC, 2: SBC_BOT, 3: SBC_PUMP: ')
        # PIP_PATH/PACKAGR_PATH
        self._pip_path = os.path.abspath(PIP_PATH)
        self._package_dir = ''
        if 'debian' in platform():
            self._package_dir = os.path.abspath(PACKAGE_PATH_RASP)
        elif 'generic' in platform():
            self._package_dir = os.path.abspath(PACKAGE_PATH_UBUNTU)
        else:
            self._package_dir = os.path.abspath(PACKAGE_PATH_MAC)

    def _update_repo(self, repo_name):
        repo_name = f'XYZ-{repo_name}'
        if os.path.exists(f'{self._package_dir}/{repo_name}'):
            os.chdir(f'{self._package_dir}/{repo_name}')
            child = pexpect.spawn(f'git pull')
            child.expect('Username')
            child.sendline(self._user)
            child.expect('Password')
            child.sendline(self._password)
            os.system(f'{self._pip_path} install .')
        else:
            os.chdir(self._package_dir)
            child = pexpect.spawn(f'git clone https://github.com/WillEEEEEE/{repo_name}')
            child.expect('Username')
            child.sendline(self._user)
            child.expect('Password', timeout=None)
            child.sendline(self._password)
            time.sleep(self._ts_clone)
            if os.path.exists(f'{self._package_dir}/{repo_name}/setup.py'):
                print('setup')
                os.chdir(f'{self._package_dir}/{repo_name}')
                os.system(f'{self._pip_path} install .')

    def check_stack(self):
        if int(self._stack_name_id) in STACK_NAME.keys():
            print('CHECK STACK')
            pool = ThreadPool(12)
            pool.map(self._update_repo, STACK_NAME[int(self._stack_name_id)])
            pool.close()
            pool.join()
        else:
            print('\033[1;33m [ERROR ID]: {}\033[0m'.format(self._stack_name_id))


if __name__ == '__main__':
    _git = GitTool(12)
    _git.check_stack()
