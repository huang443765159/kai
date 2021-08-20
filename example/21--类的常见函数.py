class Abc(object):

    def __init__(self):
        super().__init__()
        self._motors = {1: 'CID_1', 2: 'CID_2'}

    def __getitem__(self, motor_id):
        # if motor_id in self._motors.keys():
        #     return self._motors[motor_id]
        # else:
        #     return None
        return motor_id

    def __len__(self):
        return 100#len(self._motors)


kkk = Abc()
print(kkk[1])
# print(len(kkk))


class DictDemo(object):

    def __init__(self, key, value):
        super().__init__()
        self.dict = dict()
        self.dict[key] = value

    def __getitem__(self, key):
        # 定义获取值的方法
        return self.dict[key]

    def __setitem__(self, key, value):
        # 定义赋值方法
        self.dict[key] = value

    def __len__(self):
        return len(self.dict)

    def get_dict_value(self, key):
        return self.dict[key]

    def get_length(self):
        return len(self.dict)


dict_demo = DictDemo('flower', 7)
print(dict_demo['flower'])
dict_demo['name'] = 8  # 赋值
print(dict_demo['name'])
print(len(dict_demo))
