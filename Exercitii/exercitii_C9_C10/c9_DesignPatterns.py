# Design Patterns = sunt un set de "good practices" dupa care se ghideaza scrierea de cod in OOP
# sunt conventii/strategii folosite pentru rezolvarea problemelor recurente, nu sunt implementare in sine


# Creational DP:
# - ofera o modalitate de a crea obiecte ascunzand logica de creere; astfel programul are mai multa flexibilitate
# in a decide ce obiecte trebuie create
# - 2 sub-categorii: class-creation si object-creation
# - cele mai uzuale astfel de DP sunt: Singleton, Factory Method, Abstract Factory Method, etc.


# Singleton = pattern care permite crearea unei singure instante a unei clase pe durata executiei programului
# - util in a limita accessul concurent la anumite resurse, creand un punct de acces global (de ex: accesul la o baza de date)
class SingletonClass:
    __instance = None
    sector = "IT"

    def __init__(self, name):  # initializam attribute, chemat in momentul instantei obiectului
        self.name = name

    def __new__(cls, *args):  # initializam clasa, metoda magica __new__ se apeleaza inaintea __init__
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

obj1 = SingletonClass("JavaScript")
print(obj1.name)
print(obj1.sector)
print(obj1)
print(id(obj1))

obj2 = SingletonClass("Python")
print(obj2.name)
print(obj2.sector)
print(obj2)
print(id(obj2))

print(obj1.name)
print(obj1 == obj2)
print(obj1 is obj2)

obj3 = SingletonClass("Assembly")
print(obj1.name)
print(obj2.name)
print(obj3.name)


# Structural DP:
# - se ocupa cu organizarea claselor si obiectelor pentru a crea structuri mai ample si mai scalabile,
# oferind functionalitati noi
# - printre aceste DP se regasesc: Adapter Method, Bridge Method, Proxy Method


# Proxy = pattern care controleaza si administreaza accesul la obiectele pe care le protejeaza
from abc import ABC, ABCMeta, abstractmethod


class AbstractCar(ABC):
    #     __metaclass__ = ABCMeta
    @abstractmethod
    def drive(self):
        #         pass
        raise NotImplementedError("You should implement this:).")


class Car(AbstractCar):
    def drive(self):
        print("You are drving the car.")


class Driver:
    def __init__(self, age):
        self.age = age


class ProxyCar(AbstractCar):
    def __init__(self, driver: Driver):
        self.car = Car()
        self.driver = driver

    def drive(self):
        if self.driver.age < 18:
            print("Sorry little driver, you are too young to drive. (you gotta grow a bit more)")
        else:
            self.car.drive()


driver = Driver(16)
print(driver.age)
car = Car()  # Daca instantiem direct clasa Car, nu avem constrangere asupra varstei
car.drive()

proxy_car = ProxyCar(
    driver)  # Asa ca nu instantiem direct Car, ci instantiem ProxyCar, aceasta verificand varsta soferului
proxy_car.drive()

new_driver = Driver(20)
proxy_car = ProxyCar(new_driver)
proxy_car.drive()



# Implementati clasele necesare si simulati comportamentul unui student care vrea sa studieze intr-o
# Universitate dar ii este permis doar daca are banii necesari in cont pentru a-si plati taxa de
# scolarizare (de 3000)
class University:
    def studying_in_university(self):
        print("Studying hard in Uni.....")


class UniversityProxy:
    def __init__(self, balance):
        self.balance = balance

    def studying_in_university(self):
        print("Proxy in action, checking if student has funds for paying the tax")
        if self.balance >= 3000:
            self.university = University()
            self.university.studying_in_university()
        else:
            print("GO to work, you need more money!!")


uni_proxy = UniversityProxy(1000)
uni_proxy.studying_in_university()

uni_proxy.balance = 5000
uni_proxy.studying_in_university()


# Behavioral DP:
# - se refera la modul de comunicare dintre obiecte, identificand tiparele comune si atribuind
# responsabilitati obiectelor
# - astfel de DP sunt: Observer Method, Iterator Method, Chain of responsability Method


# Observer = pattern care permite definirea unui mecanism de observare intre obiecte, ce permite
# trimiterea de notificari obiectelor "observator" (observer) despre evenimentele noi ale obiectului
# "observabil" (observable)

class ObservablePerson:
    name = "Default User"

    def __init__(self):
        self._observers = []

    def __str__(self):
        return f"I am {self.name}"

    def register_observer(self, observer):
        self._observers.append(observer)  # inregistram un observer

    def notify_observers(self, message):
        for obs in self._observers:  # fiecare Observer este notificat
            obs.notify(self, message)  # prin apelul functiei notify din clasa Observer


class Observer:
    def __init__(self, name, observable):
        self.name = name
        observable.register_observer(self)  # in momentul instantierii Observerului, acesta este
        # inregistrat in lista de observeri ai obiectului Observable

    def notify(self, observable, message):
        print(f"Observer: {self.name} Got message: {message} from observable obj: {observable}")


subject = ObservablePerson()
observer_obj1 = Observer("obs1", subject)
observer_obj2 = Observer("obs2", subject)

subject.notify_observers("An event occured....")  # in momentul apelului ambele obiecte observer primesc notificare


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # cum e afisat cu print obiectul
        return f"My name is {self.name} and I am {self.age} years old"

    def __repr__(self):  # cum e evaluat obiectul
        return self.__str__()


p = Person("Ioan", 60)
print(p.name)
print(p.age)
print(p)  # pt a afisa un string personalizat, suprascriem __str__