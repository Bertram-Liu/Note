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

fn_outer()
# fn_inner()  # 出错

print("程序结束")