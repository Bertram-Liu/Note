from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/00-page')
def page():
    return render_template("00-page.html")

@app.route('/01-request')
def request_views():
    # print(request)
    # print("=================")
    # print(dir(request))

    print("scheme:" , request.scheme)
    print("method:", request.method)
    print("args:", request.args)
    print("form:", request.form)
    print("cookies:", request.cookies)
    print("files:" , request.files)
    print("path:" , request.path)
    print("full_path:" , request.full_path)
    print("url:" , request.url)
    print("headers:" , request.headers)
    print("User-Agent:" , request.headers['User-Agent'])

    # 判断 Referer 在 request.headers中是否存在
    if 'Referer' in request.headers:
        print("Referer:" , request.headers['Referer'])

    url = request.headers.get('Referer','/')
    print("返回到:" , url)

    return "获取请求对象成功"

@app.route('/02-page')
def page02():
    return render_template("02-page.html")

@app.route('/02-get')
def get_views():
    # 接收前端传递过来的 kw 的参数值
    kw = request.args.get('kw','暂无')
    return "传递过来的参数值为:"+kw

@app.route('/03-page')
def page03():
    return render_template("03-page.html")

@app.route('/03-post',methods=['POST','GET'])
def post_views():
    uname = request.form['uname']
    upwd = request.form['upwd']
    return "用户名称:%s, 用户密码:%s" % (uname,upwd)

@app.route('/04-login',methods=['GET','POST'])
def login():
    # 通过request.method来判断用户的请求方式是什么
    # 用户的请求方式代表着用户的请求意图
    # 如果是 get 请求的话,则渲染 04-login.html 给用户
    # 如果是 post 请求的话,接收请求提交过来的数据进行处理
    if request.method == 'GET':
        return render_template('04-login.html')
    else:
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        return "uname:%s,upwd:%s" % (uname,upwd)

if __name__ == "__main__":
    app.run(debug=True)








