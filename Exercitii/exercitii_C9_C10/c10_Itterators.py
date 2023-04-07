# Iteratorii = sunt niste obiecte (clase) care implementeaza un protocol iterativ, adica implementeaza
# metodele magice __iter__ si __next__, aruncand o exceptie de tip __StopIteration__ in momentul cand
# executia ajunge la sfarsitul elementelor iteratorului


def is_prime(nr):
    if nr < 2:
        return False
    for i in range(2, int(nr * 0.5) + 1):
        if nr % i == 0:
            return False
    return True


def get_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    print(primes)


class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.num = 2

    def __iter__(self):  # ca sa putem crea obiect iterator cu functia iter()
        return self

    def __next__(self):
        """Next presupune 3 operatii:
        - verificarea daca nr e prim
        - incrementarea numarul actual
        - daca am ajuns la final, raise StopIteration"""
        while self.generated_numbers < self.n:
            self.num += 1
            if is_prime(self.num):
                self.generated_numbers += 1
                return self.num
        raise StopIteration


prime_it = PrimeIterator(7)
for elem in prime_it:
    print(elem)