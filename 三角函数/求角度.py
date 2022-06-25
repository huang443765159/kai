import math

a = 1
b = 1
c = math.sqrt(a * a + b * b)
A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - a * a - b * b) / (-2 * a * b)))

print(A)
print(B)
print(C)
"""
a = 202
b = 3
c = 202.2

计算 周长 用公式: P=a+b+c
P = 407.2

计算 面积 用公式: A=sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))/4
A = 302.46725178108

计算 阿尔法 用公式: alpha=acos((pow(b, 2)+pow(c, 2)-pow(a, 2))/(2*b*c))
alpha = 85.753240187924 角度 (1.4966763855328 弧度)

计算 贝塔 用公式: beta=acos((pow(a, 2)+pow(c, 2)-pow(b, 2))/(2*a*c))
beta = 0.84862211761942 角度 (0.014811250057705 弧度)

计算 伽马 用公式: gamma=acos((pow(a, 2)+pow(b, 2)-pow(c, 2))/(2*a*b))
gamma = 93.398137694456 角度 (1.6301050179993 弧度)

"""