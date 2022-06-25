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
