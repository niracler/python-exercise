# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @width.getter
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @height.getter
    def height(self):
        return self._height

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
