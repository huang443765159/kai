from random import randint


class Die(object):

    def __init__(self, die_sides=6):
        super().__init__()
        self.die_sides = die_sides

    def roll_die(self):
        return randint(1, self.die_sides)


die = Die()
die1 = Die()
die2 = Die()
for i in range(10):
    print(die.roll_die())

c = list()
for y in range(1):
    result = die.roll_die() + die1.roll_die() + die2.roll_die()
    # 只有返还结果才可以相加，没有返还值是没办法相加的
    c.append(result)
print(c)