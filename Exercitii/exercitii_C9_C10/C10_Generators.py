# Generatorii = sunt functii care creeaza iteratori
# foloseste keyword-ul yeild in loc de return, diferenta fiind ca executia functiei continua dupa yield,
# valoarea de returnat fiind memorata la fiecare pas
# similar cu it, valorile generatorului rezultat pot fi accesate doar prin iterare, acesta este si momentul
# in care valorile sunt generate

def gen_func():
    yield 111
    print("Am generat 111")


gen_func()  # Atentie! daca doar rulam/apelam generatorul, ne afiseaza obiectul, nu valorile generate

for val in gen_func():   # valorile se genereaza doar in momentul in care iteram peste generator
    print(f"Valoarea yield-uita(returnata) este: {val}")