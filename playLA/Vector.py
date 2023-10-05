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

    def __mul__(self, k):
        return Vector([k * v_i for v_i in self])

    def __rmul__(self, k):
        return self * k

    def __pos__(self):
        return self * 1

    def __neg__(self):
        return self * -1

    @classmethod
    def zero(cls, dimension):
        return Vector(dimension * [0])

    def __iter__(self):
        return self._values.__iter__()

    def __repr__(self):
        return f"Vector({self._values})"

    def __str__(self):
        return f"({', '.join(str(e) for e in self._values)})"
