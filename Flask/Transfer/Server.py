from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        print(dict(result))  # 将网页输入的东西打印出来  网页捕捉的按键事件从python获取都是夹带数据的，获取到数据之后就证明按键捕捉了
        return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(port=5010)
