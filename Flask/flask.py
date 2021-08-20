from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/admin')  # localhost:5050/admin
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<int:guest>')  # localhost:5050/guest/{guest}
def hello_guest(guest):
    return 'Hello {} as Guest'.format(guest)


@app.route('/test/<float:test>')  # localhost:5050/test/{test}
def hello_test(test):
    return 'Hello {} as Guest'.format(test)


@app.route('/user/<name>')  # localhost:5050/user/Yan 网页显示hello_guest函数的return
def hello_user(name='Yan'):  # url_for 跳转到其它函数
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=1))


if __name__ == '__main__':
    app.run(debug=True, port=5050)
