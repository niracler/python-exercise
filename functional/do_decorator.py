# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = round(time.time() * 1000)
        ret = fn(*args, **kw)# 相当于是将原函数插到了这里？
        end = round(time.time() * 1000)
        print("%s execute %d ms" % (fn.__name__, end - start))
        return ret
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功？？？')