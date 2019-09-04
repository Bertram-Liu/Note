from flask import Flask,render_template

# 创建一个Flask的程序实例,以便接收用户的请求和响应
# 要将当前运行的模块文件作为Flask的程序示例
app = Flask(__name__)


# @app.route() : Flask中的路由定义,用于匹配用户的访问路径,'/'表示整个网站的跟路径
# def index() : 匹配上路由之后要执行的操作函数 - 视图函数(Views),视图函数中必须要返回一个字符串
# @app.route('/index')
# def index():
#     return "Hello World"


@app.route('/show/<name>/<age>')
def show(name, age):
    print("name:", name)
    print("age:", age)
    return "接收数据成功!"


@app.route('/calculate/<num1>/<int:num2>')
def calculate(num1, num2):
    # 注意:路由中传递进来的参数一律都是字符串类型
    # print("type:", type(num1))
    # print("type:", type(num2))

    # 将 num1 和 num2 转换成 int 类型
    # 因为使用了类型转换器,所以可以不用转换
    # num1 = int(num1)
    # num2 = int(num2)

    r1 = num1 + num2
    r2 = num1 - num2
    r3 = num1 * num2
    r4 = num1 / num2
    r5 = num1 % num2

    str = "<h1>%s + %s = %s</h1>" % (num1, num2, r1)
    str += "%s - %s = %s<br>" % (num1, num2, r2)
    str += "%s * %s = %s<br>" % (num1, num2, r3)
    str += "%s / %s = %s<br>" % (num1, num2, r4)
    str += "%s %% %s = %s<br>" % (num1, num2, r5)

    return str


# http://127.0.0.1:5000
# http://127.0.0.1:5000/index
# http://127.0.0.1:5000/数字
# http://127.0.0.1:5000/index/数字
@app.route('/')
@app.route('/index')
@app.route('/<int:page>')
@app.route('/index/<int:page>')
def show_page(page=1):
    return "您当前要看的页数为第%d页" % page


@app.route('/temp')
def temp():
    return render_template("temp.html")


if __name__ == "__main__":
    # app.run : 启动Flask的服务,默认会在本机开启5000端口
    # debug=True , 可选参数,将启动方式改为调试模式
    app.run(debug=True)
