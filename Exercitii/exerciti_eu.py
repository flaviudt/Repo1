# C04_EX02:  Given a number n=15, write a loop that prints the number and decreases it
# until it hits 0 by:
# - 2 in case the number is divisible by 5
# - 3 if it is even;
# - 1 if it is odd.

# n = 15
# while n > 0:
#     print(n)
#     if n % 5 == 0:
#         n -= 2
#     elif n % 2 == 0:
#         n -= 3
#     else:
#         n -= 1





# C05_EX01: Avand lista lst = [3,5,12,13,6,29,30,44,19,21] data ca argument, scrieti o functie care sa afiseze numerele divizibile cu 3.
# OUT: 3 12 6 30 21

# lst = [3,5,12,13,6,29,30,44,19,21]
# print(lst)
# def div_3(nr):
#     for nr in lst:
#         if nr%3 == 0:
#             print(nr)
#             print(f'Numarul {nr} este multiplu de 3')
#         else:
#             print(f'Numarul {nr} nu este multiplu de 3')
#
# div_3(lst)

## v2

# lst = [3,5,12,13,6,29,30,44,19,21]
# def divizibil_3 (lst):
#     for i in lst:
#         if i % 3 == 0:
#             print(i)
#
# divizibil_3(lst)





# Incerci pana maine seara sa citesti de la tastatura elementele si sa afisezi o lista?
# Intr-o functie

# lista1 =[]
#
# def citire_elemente ():
#     nr = 1
#     while nr != 0:
#         nr = int(input('Introduceti nr:'))
#         lista1.append(nr)
#     print(lista1)
#
# citire_elemente()
#




## Citire lista de n elemente de la tastatura


# n = int(input('n= '))
# lista = []
#
# for x in range(n):
#     lista.append(input('Introdu un numar: '))
# print(lista)
#




class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_name(self):
        print(f'My name is {self.name} and I am {self.age} years old')

person1 = Person('Flaviu',26)
person1.print_name()

class Student(Person):

    def __init__(self,name, age, grade, scolarship):
        super().__init__(name, age)
        self.grade = grade
        self.scolarship = scolarship

    def show_finances(self):
        return self.scolarship

my_s = Student('Flaviu',26,10,1000)
print(my_s.show_finances())

class Employee(Person):

    def __init__(self,name, age, rate, hours):
        Person.__init__(self, name, age)
        self.rate = rate
        self.hours = hours

    def show_finances(self):
        return self.rate * self.hours

my_e = Employee('Flaviu', 26, 50, 45)
print(my_e.show_finances())
my_e.print_name()


