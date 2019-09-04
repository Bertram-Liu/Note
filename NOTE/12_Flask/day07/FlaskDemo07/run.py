from flask import Flask, make_response, redirect, request

app = Flask(__name__)

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
    resp.set_cookie('uname','xiaozemaria',60*60*24*365)
    return resp

@app.route('/03-getcookie')
def getcookie():
    if 'uname' in request.cookies:
        uname = request.cookies['uname']
        return "uname的值为："+uname
    return "没有查询到键为uname的cookie"

@app.route('/04-delcookie')
def delcookie():
    resp = make_response('删除cookie成功')
    resp.delete_cookie('uname')
    return resp

if __name__ == "__main__":
    app.run(debug=True)