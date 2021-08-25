import os


# 获取当前文件绝对路径
print(__file__)
# 获取当前path
print('***获取当前path***')
print(os.getcwd())
print(os.path.abspath(os.path.dirname(__file__)))


print('***获取上级目录***')
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))
print(os.path.abspath(os.path.join(__file__, '../..')))

print('***获取上上级目录***')
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))

path = '/Users/huangkai/Desktop/2/'  # 属于文件所在绝对路径
files = os.listdir(path)  # 返回的一个列表，该文件下所有文件

print(os.path.expanduser('~/Documents'))  # 获取Users后的路径


n = 0
for file in files:
    old_name = path + files[n]
    new_name = path + str(n + 1) + '.jpg'
    os.rename(old_name, new_name)
    print(old_name, new_name)
    n += 1
