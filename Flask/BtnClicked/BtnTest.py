# from flask import Flask, render_template
#
# app = Flask(__name__)
#
#
# @app.route('/switch')
# def test():
#     return render_template('test.html')
#
#
# @app.route('/chem_a')
# def chem_a():
#     print('chem_a clicked')
#     return 'Nothing'
#
#
# @app.route('/chem_b')
# def chem_b():
#     print('chem_b clicked')
#     return 'Nothing'
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5010)

# flask CBV
from flask import Flask, render_template, views, request

app = Flask(__name__)


class Login(views.MethodView):

    def get(self):
        return render_template('test.html')


class Chem(views.MethodView):

    def get(self):
        self.chem_a_clicked()
        return render_template('test.html')

    def chem_a_clicked(self):
        print('clicekd')
        return 'Nothing'


app.add_url_rule("/test", view_func=Login.as_view(name='test'))
app.add_url_rule("/chem_a", view_func=Chem.as_view(name='chem_a'))


if __name__ == '__main__':
    app.run("0.0.0.0", 9527, debug=True)
