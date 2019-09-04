from flask import Flask, make_response, redirect, request, render_template, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "aixieshaxiesha"


@app.route('/')
def index():
    return "这是首页"


@app.route('/01-resp')
def resp_views():
    # 通过 make_response 创建响应对象
    # resp = make_response('响应给客户端的内容')

    # 通过 重定向 创建响应对象
    resp = redirect("http://www.baidu.com")
    return resp


@app.route('/02-setcookie')
def setcookie():
    # 保存 uname 的值为 xiaozemaria,存期为1年
    resp = make_response("保存cookie成功")
    resp.set_cookie('uname', 'xiaozemaria', 60 * 60 * 24 * 365)
    return resp


@app.route('/03-getcookie')
def getcookie():
    if 'uname' in request.cookies:
        uname = request.cookies['uname']
        return "uname的值为：" + uname
    return "没有查询到键为uname的cookie"


@app.route('/04-delcookie')
def delcookie():
    resp = make_response('删除cookie成功')
    resp.delete_cookie('uname')
    return resp


@app.route('/05-login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 检查cookies中是否有 uname
        if 'uname' in request.cookies:
            uname = request.cookies['uname']
            if uname == 'admin':
                return "欢迎%s回来" % uname
            else:
                resp = make_response(render_template('05-login.html'))
                resp.delete_cookie('uname')
                return resp
        return render_template('05-login.html')
    else:
        uname = request.form['uname']
        upwd = request.form['upwd']

        if uname == 'admin' and upwd == 'admin':
            resp = make_response('登录成功')
            if 'isSaved' in request.form:
                resp.set_cookie('uname', uname, 60 * 60 * 24 * 180)
            return resp
        return "登录失败"


@app.route('/06-setsession')
def setsession():
    session['uname'] = 'xiaozemaria'
    return "设置session成功"


@app.route('/07-getsession')
def getsession():
    if 'uname' in session:
        uname = session['uname']
        return "session中的uname为:" + uname
    return "session中没有uname的值"


@app.route('/login', methods=['GET', 'POST'])
def login_views():
    if request.method == 'GET':
        # 获取请求源地址,如果没有的话则为 / ,将数据保存进session
        url = request.headers.get('Referer', '/')
        session['url'] = url

        # 判断session中是否有登录信息
        if 'uname' in session:
            # session 中有登录信息
            return redirect(url)
        else:
            # session 中没有登录信息,继续判断cookie
            if 'uname' in request.cookies:
                # cookies 中有登录信息
                # 获取cookies中的数据继续判断
                uname = request.cookies['uname']
                if uname == "admin":
                    # cookies中的数据是准确的
                    # 将uname保存进session中
                    # 从哪来回哪去
                    session['uname'] = uname
                    return redirect(url)
                else:
                    # 清除cookies中的登录信息,回登录页面
                    resp = make_response(render_template('login.html'))
                    resp.delete_cookie('uname')
                    return resp
            else:
                # cookies 中没有登录信息
                return render_template('login.html')
    else:
        # 接收信息
        uname = request.form['uname']
        upwd = request.form['upwd']
        # 判断登录信息
        if uname == 'admin' and upwd == 'admin':
            # 登录成功
            # 将信息保存进session
            session['uname'] = uname
            # 创建响应对象
            url = session['url']
            resp = redirect(url)
            # 判断是否要保存进cookie
            if 'isSaved' in request.form:
                resp.set_cookie('uname', uname, 60 * 60 * 24 * 365)
            return resp
        else:
            # 登录失败
            return render_template('login.html')


@app.route('/test')
def test_views():
    # 判断session中是否有登录信息
    uname = session.get('uname', None)
    return render_template('test.html', uname=uname)


@app.route('/logout')
def logout_views():
    # 创建响应对象
    url = request.headers.get("Referer", '/')
    resp = redirect(url)

    if 'uname' in request.cookies:
        resp.delete_cookie('uname')
    if 'uname' in session:
        del session['uname']

    return resp


if __name__ == "__main__":
    app.run(debug=True)
