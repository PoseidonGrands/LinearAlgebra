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






