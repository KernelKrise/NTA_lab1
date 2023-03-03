from random import randint


def gcd(a: int, b: int) -> int:
    rest = a % b
    while rest != 0:
        a = b
        b = rest
        rest = a - (b * int(a / b))
    return b


def is_prime(p: int, k: int = 10) -> bool:
    if p <= 1 or p == 4:
        return False
    if p <= 3 or p in (5, 7, 11, 13):
        return True
    if p % 2 == 0 or p % 3 == 0 or p % 5 == 0 or p % 7 == 0 or p % 11 == 0 or p % 13 == 0:
        return False

    d = p - 1
    s = 0
    while d % 2 == 0:
        d = d // 2
        s += 1

    for i in range(k):
        x = randint(2, p - 2)

        if gcd(x, p) > 1:
            return False

        x_r = pow(x, d, p)
        if x_r == 1 or x_r == p - 1:
            continue

        for _ in range(1, s):
            x_r = pow(x_r, 2, p)
            if x_r == p - 1:
                break
            elif x_r == 1:
                return False
        else:
            return False
    return True


def test_divs(n: int) -> int or bool:
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    for prime_number in small_primes:
        if n % prime_number == 0:
            return prime_number
    return True


if __name__ == "__main__":
    print(test_divs(323324583518541583))
    print(is_prime(9621744377587719835533673707134721157123))
