import os
import re

# OS注意：os.popen 非阻塞代码， os.system为阻塞代码
b = '/Users/huangkai/Desktop/FormatREC/_Records/CARS/FTAlpha2020.stl'
print(os.path.basename(b).split('.')[0])
# FTAlpha2020
c = 'XYZSwitches3         2021.10.16.18.31'
