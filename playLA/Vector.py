import math
from ._global import EPSILON


class Vector:
    def __init__(self, ls):
        # 复制一份防止引用的外部列表修改导致向量被修改
        self._values = list(ls)

    def __len__(self):
        """返回向量长度"""
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __add__(self, vec2):
        n = len(self._values)
        assert n == len(vec2), \
            "vectors must be same"

        return Vector([(v_i + u_i) for v_i, u_i in zip(self, vec2)])

    def __sub__(self, vec2):
        n = len(self._values)
        assert n == len(vec2), \
            "vectors must be same"

        return Vector([(v_i - u_i) for v_i, u_i in zip(self, vec2)])

    def dot(self, vec2):
        """向量的点乘：两个向量相乘"""

        assert len(self) == len(vec2),\
            "the vector lenght must be same..."

        return sum((x_i * y_i) for x_i, y_i in zip(self, vec2))

    def __mul__(self, k):
        return Vector([k * v_i for v_i in self])

    def __rmul__(self, k):
        return self * k

    def __truediv__(self, k):
        """向量除法：self / k"""
        return self * (1 / k)

    def __pos__(self):
        return self * 1

    def __neg__(self):
        return self * -1

    @classmethod
    def zero(cls, dimension):
        return Vector(dimension * [0])

    def norm(self):
        """求向量的模"""
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        """向量归一化"""
        # 分母不能为0，防止浮点数精度问题，采用EPSILON
        if self.norm() < EPSILON:
            raise ZeroDivisionError("normalize error...the vector nor is zero...")

        # 防止引用问题：乘self相当于拷贝了一份
        # 不能使用self / self.norm的原因：此前向量类只定义了乘法
        # return 1 / self.norm() * self

        # 定义除法操作后
        return self / self.norm()

    def __iter__(self):
        return self._values.__iter__()

    def __repr__(self):
        return f"Vector({self._values})"

    def __str__(self):
        return f"({', '.join(str(e) for e in self._values)})"
