from playLA.Vector import Vector

if __name__ == "__main__":
    v1 = Vector([2, 3])
    v2 = Vector([1, 4])
    k = 2

    print(f"{v1} + {v2} = {v1 + v2}")
    print(f"{v1} - {v2} = {v1 - v2}")
    print(f"{v1} * {k} = {v1 * k}")
    print(f"+{v1} = {+v1}")
    print(f"-{v1} = {-v1}")

    v_zero = Vector.zero(2)
    print(f"{v1} + {v_zero} = {v1 + v_zero}")

    v3 = Vector([5, 2])
    print(f"norm{v3} = {v3.norm()}")
    print(f"norm{v_zero} = {v_zero.norm()}")

    v4 = Vector([5, 2])
    print(f"normalize{v4} = {v4.normalize()}")
    # 验证有效性：是否真的是单位向量，长度为1
    print(v4.normalize().norm())
    print(v2.normalize().norm())

    # print(v_zero.normalize())

    print(v1.dot(v2))
    print(v1 * v2)





