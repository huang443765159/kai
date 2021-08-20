from flask import Flask, render_template, views
import random

app = Flask(__name__)


class _Login(views.MethodView):

    @staticmethod
    def get():
        return render_template('1.html',
                               water=0,
                               raw_a=0,
                               raw_b=0,
                               raw_wax=0,
                               raw_whl=0,
                               mix_a=0,
                               mix_b=0,
                               mix_wax=0,
                               mix_whl=0)


class _Liquid(views.MethodView):

    @staticmethod
    def post():
        return {"WATER": {4: random.randint(0, 10)},
                'RAW_CHEM': {0: random.randint(10, 20), 1: 0, 2: 0, 3: 0},
                'MIXED_CHEM': {0: random.randint(20, 30), 1: 0, 2: 0, 3: 0}}


app.add_url_rule('/', view_func=_Login.as_view(name='/'), methods=['GET'])
app.add_url_rule('/liquid', view_func=_Liquid.as_view(name='liquid'), methods=['POST'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
