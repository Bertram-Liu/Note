from flask import Flask, render_template

app = Flask(__name__)


@app.route('/01-var')
def var():
    return render_template("01-var.html", name='MM.ZH', age=18)


@app.route('/02-var')
def var02():
    # 字符串
    name = "小泽Maria"
    # 数字
    age = 16
    # 小数
    salary = 50000
    # 列表
    list = ["保健", "大保健", "按摩"]
    # 元组
    tup = ("大肠刺身", "小肠刺身")
    # 字典
    dic = {
        "MSN": "美少女战士",
        "XMX": "巴拉巴拉小魔仙",
    }

    dog = Animal()
    dog.name = "猫咪"

    gender = "男"

    # return render_template('02-var.html',name=name,age=age,salary=salary,list=list,dic=dic,tup=tup,dog=dog)

    print(locals())

    str = render_template('02-var.html', params=locals())
    print(str)
    return str


@app.route('/03-for')
def for_views():
    list = [
        {
            "name": "老魏",
            "age": 44,
            "gender": "男"
        },
        {
            "name": "波波",
            "age": 36,
            "gender": "男"
        },
        {
            "name": "小泽Maria",
            "age": 30,
            "gender": "男",
        },
        {
            "name": "蒙蒙.ZH",
            "age": 18,
            "gender": '女'
        }
    ]

    return render_template('03-for.html',list=list)

@app.route("/04-parent")
def parent():
    return render_template("04-parent.html",name="吕泽Maria")

@app.route("/05-child")
def child():
    return render_template("05-child.html",name="老魏Maria")

class Animal(object):
    name = None

    def eat(self):
        return self.name + "正在吃饭"


if __name__ == "__main__":
    app.run(debug=True)
