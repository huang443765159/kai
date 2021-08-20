# 在for里面是虚函数，带参数的会把之前的变量覆盖掉，要用一下方法

# 带信号测试

def print_num(num):
    print(num)


for i in range(10):
    sign_num_connect(lambda x, _i=i: print_num(num=_i))
