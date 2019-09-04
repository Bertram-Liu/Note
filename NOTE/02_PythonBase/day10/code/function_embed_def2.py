# function_embed_def.py

# 此示例示意在函数内部可以用def语句来创建函数,
# 在函数内部直接可以使用这个函数
def fn_outer():
    print("fn_outer被调用")
    # 在此处...
    def fn_inner():
        print("fn_inner被调用!")

    fn_inner()
    fn_inner()
    print("fn_outer调用结束")
    return fn_inner  # 返回内部创建的函数的引用关系

fx = fn_outer()  # fx 绑定谁?
fx()  # 调用 fn_inner()

print("程序结束")