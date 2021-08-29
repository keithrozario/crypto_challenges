def gcd(x: int, y: int) -> int:
    """
    Calculates the GCD of two integers, x and y
    """
    if x > y:
        print(f"Calculating for : {x-y} and {y}")
        return gcd(x-y, y)
    elif y > x:
        print(f"Calculating for : {y-x} and {x}")
        return gcd(y-x, x)
    elif x == y:
        print(f"Match: {y} and {x}")
        return x


if __name__ == '__main__':
    num_1 = 66528
    num_2 = 52920
    z = gcd(num_1, num_2)
    print(f"Found GCD of {num_1} and {num_2} as: {z}")

