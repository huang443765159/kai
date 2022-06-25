from enum import Enum, IntEnum


class A(Enum):
    a = 1
    b = 2


print(A.a.value)
print(A.a.name)
print(A(1))
