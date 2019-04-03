# 为了调用一个父类方法，可以使用super函数，比如

result = [lambda x: i * x for i in range(4)]

print([m(3) for m in result])
