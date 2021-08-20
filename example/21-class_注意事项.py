class Car(object):
    # obeject 必须添加

    def __init__(self, make, model, year):
        self._make = make
        # 下划线保护类属性在外面不调用，想调用或者修改用函数完成
        self._model = model
        self._year = year
        self._odometer_reading = 70
        self.odometer_reading = 0

    def get_model(self):
        # 命名首字母不可以大写，调用一般用get，改写一般用set
        return self._model

    def set_model(self, model):
        self._model = model

    def update_odometers(self, mileage):
        self.odometer_reading = mileage
        # 首次出现的变量最好都在初始变量中出现


class Postgraduate(object):
    # 继承

    def __init__(self, *, sno, name, teacher):
        super().__init__(sno=sno, name=name)
        # 继承的时候都加上谁 = 谁 避免出错,*代表后边想用必须加谁等于谁
        self.teacher = teacher
