import gevent 


def foo():
    print("Running in foo")
    gevent.sleep(3)
    print("foo again")

def bar():
    print("Running in bar")
    gevent.sleep(2)
    print("bar again")

f = gevent.spawn(foo)
b = gevent.spawn(bar)

gevent.joinall([f,b])

