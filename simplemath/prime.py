"""A very simple prime number library."""


def is_prime(n: int) -> bool:
    if n < 1:
        return False
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
    return True
