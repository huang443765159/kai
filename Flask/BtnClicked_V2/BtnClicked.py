from flask import Flask, render_template, views, url_for, redirect


app = Flask(__name__)

# 每点击一次按钮则初始化一次页面，相当于初始化一次类，所以类内部的动态变量都不可用

dev_ena = dict()
for i in range(7):
    dev_ena[i] = False

json_data = dict()
json_data[0] = '#chem_a'
json_data[1] = '#chem_b'
json_data[2] = '#chem_wax'
json_data[3] = '#chem_wheel'
json_data[4] = '#l2_1'
json_data[5] = '#l2_2'
json_data[6] = '#wheel'


class Login(views.MethodView):

    def get(self):
        return render_template("switch.html")


class ChemA(views.MethodView):

    def __init__(self):
        self._cid = 0

    def get(self):
        self.chem_a()
        return render_template('switch.html')

    def chem_a(self):
        dev_ena[self._cid] = not dev_ena[self._cid]
        print('chem_a', dev_ena[self._cid])
        return 'Nothing'


class ChemB(views.MethodView):

    def __init__(self):
        self._cid = 1

    def get(self):
        self.chem_b()
        return render_template('switch.html')

    def chem_b(self):
        dev_ena[self._cid] = not dev_ena[self._cid]
        print('chem_b', dev_ena[self._cid])
        return 'Nothing'


class ChemWax(views.MethodView):

    def __init__(self):
        self._cid = 2

    def get(self):
        self.chem_wax()
        return render_template('NewSwitch.html')

    def chem_wax(self):
        dev_ena[self._cid] = not dev_ena[self._cid]
        print('chem_wax', dev_ena[self._cid])
        return 'Nothing'


class ChemWheel(views.MethodView):

    def __init__(self):
        self._cid = 3

    def get(self):
        self.chem_wheel()
        return render_template('NewSwitch.html')

    def chem_wheel(self):
        dev_ena[self._cid] = not dev_ena[self._cid]
        print('chem_wheel', dev_ena[self._cid])
        return 'Nothing'


class L21(views.MethodView):

    def __init__(self):
        self._cid = 4

    def get(self):
        self.l2_1()
        return render_template('NewSwitch.html')

    def l2_1(self):
        dev_ena[self._cid] = not dev_ena[self._cid]
        print('l2_1', dev_ena[self._cid])
        return 'Nothing'


class L22(views.MethodView):

    def __init__(self):
        self._cid = 5

    def get(self):
        self.l2_2()
        return render_template('NewSwitch.html')

    def l2_2(self):
        dev_ena[self._cid] = not dev_ena[self._cid]
        print('l2_2', dev_ena[self._cid])
        return 'Nothing'


class Wheel(views.MethodView):

    def __init__(self):
        self._cid = 6

    def get(self):
        self.wheel()
        return {'cid': 'false'}

    def wheel(self):
        dev_ena[self._cid] = not dev_ena[self._cid]
        print('wheel', dev_ena[self._cid])
        return 'Nothing'


class StopAll(views.MethodView):

    def get(self):
        self.stop_all()
        return {'status': 'ok'}

    @staticmethod
    def stop_all():
        for cid in dev_ena:
            dev_ena[cid] = False
        print('stop_all')
        return 'Nothing'


class Refresh(views.MethodView):

    def __init__(self):
        self._dev_ena = dict()

    def get(self):
        for cid, ena in dev_ena.items():
            self._dev_ena[json_data[cid]] = ena
        return self._dev_ena


app.add_url_rule('/login', view_func=Login.as_view(name='login'))
app.add_url_rule('/chem_a', view_func=ChemA.as_view(name='chem_a'))
app.add_url_rule('/chem_b', view_func=ChemB.as_view(name='chem_b'))
app.add_url_rule('/chem_wax', view_func=ChemWax.as_view(name='chem_wax'))
app.add_url_rule('/chem_wheel', view_func=ChemWheel.as_view(name='chem_wheel'))
app.add_url_rule('/l2_1', view_func=L21.as_view(name='l2_1'))
app.add_url_rule('/l2_2', view_func=L22.as_view(name='l2_2'))
app.add_url_rule('/wheel', view_func=Wheel.as_view(name='wheel'))
app.add_url_rule('/stop_all', view_func=StopAll.as_view(name='stop_all'))
app.add_url_rule('/refresh', view_func=Refresh.as_view(name='refresh'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
