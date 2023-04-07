def is_prime(nr):
    if nr < 2:
        return False
    for i in range(2, nr):
        if nr % i == 0:
            return False
    return True


def get_n_primes(n):
    genereted_numbers = 0
    num = 2
    while genereted_numbers < n:

        if is_prime(num):
            print(num)
            genereted_numbers += 1
        num += 1


print(is_prime(13))
get_n_primes()
