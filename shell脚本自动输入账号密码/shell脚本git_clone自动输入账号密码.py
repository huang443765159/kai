import os
import getpass

a = '1'
b = '2'


result = os.popen(f'git clone https://github.com/WillEEEEEE/XYZ-VISUAL\n << {a}\n << {b}')  # 错误演示
print(result.read())

password = getpass.getpass('输入密码')
