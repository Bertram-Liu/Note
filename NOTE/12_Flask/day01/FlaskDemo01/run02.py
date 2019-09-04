from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    return "这是run02中的index访问路径"

def show(name):
    """
    xxxx  xxxx
    :param name: 表示用户名称
    :return:
    """
    return "xxxx"

if __name__ == "__main__":
    app.run(debug=True)