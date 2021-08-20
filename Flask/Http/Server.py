from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['test']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('test')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True, port=5050)

# 使用浏览器打开test.html， 然后输入名字就可以跳转到success函数， 网页显示success函数的返回 welcome
