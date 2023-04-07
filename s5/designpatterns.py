# Design Patterns
#
# 1.	Singleton
#
# Se da urmatoarea clasa:
#
#
# class PresedinteRomania:
#
#     def __str__(self):
#         return "Eu sunt presedintele Romaniei"
#
#     def say_hello(self):
#         return f'Salut! {self}'
# 
# In momentul de fata, daca incercam sa cream mai multe obiecte din clasa aceasta, vom putea:
#
# a = PresedinteRomania()
# b = PresedinteRomania()
#
# print(f'ID(a) = {id(a)}')
# print(f'ID(b) = {id(b)}')
# print(f'Acelasi obiect? {a is b}')
# 
# Scopul acestui exercitiu este sa modificam clasa de mai sus folosind DP Singleton pentru a obtine mereu acelasi obiect:
# -	Vom folosi functia `__new__` (adevaratul constructor din Python)
# -	Vom tine singurul obiect pe clasa (cls), si il vom crea doar la prima apelare a lui __new__
# -	La orice alta apelare, vom returna obiectul deja existent
#
#
# 2.	Factory Pattern
#
# Acest pattern ne permite sa cream un obiect dintr-o clasa folosind o alta clasa (fabrica). Fabrica are posibilitatea de a crea obiecte din mai multe clase (de obicei aceste clase sunt siblings, adica mostenesc de la acelasi parinte).
#
#
# Vom implementa urmatorele clase:
# -	English/French/Spanish Translator – clase care stiu sa traduca cuvinte din romana in limba specificata
# -	translations va fi un dictionar cu acele cuvinte, exemplu `{ “masina”: “car” }` – se poate hardcoda in clasa
# -	localize va fi o functie care pentru un parametru de intrare, ne va da traducerea lui in acea limba (exemplu `input(“masina”)` returneaza “car”)
#
# -	TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa) numita get_translator(language) – in functie de parametrul language, returneaza un translator object.
#
#
# factory = TranslatorFactory()
#
# english_trans = factory.get_translator('en')
# spanish_trans = factory.get_translator('es')
#
# print(f'In engleza zicem {english_trans.localize("masina")}')
# print(f'In spaniola zicem {spanish_trans.localize("masina")}')
# 
# 3.	Generators
#
# Implementati un generator pentru loteria 6/49 si noroc:
# -	Primele 6 apelari catre generator vor da cate un numar intre 1 si 49 (inclusiv
# -	Ultima apelare va da un singur numar de “noroc” format din 7 cifre
#
# 4.	Context Managers
#
# Se da un fisier text hello.txt, care contine un text scurt. Deschideti fisierul si cititi continutul, folosind urmatoarele 2 metode:
# -	try - finally
# -	Fisierul se deschide inainte de try, folosind functia open
# -	In interiorul try citim continutul folosind functia read
# -	In finally se inchide fisierul
# -	with (context manager)
# -	Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fisierul, pentru ca context managerul face asta pentru noi.
# 5.	Decorators
# Implementati urmatorii decoratori:
# -	timeit – decorator care masoara timpul de executie al unei functii
# -	logger – decorator care printeaza argumentele de intrare, si rezultatul unei functii
#
# 6.	Decorators extra
#
# Implementati o clasa User, cu urmatoarele cerinte:
# – constructorul va primi nume, email, parola, si data nasterii
# – o metoda login, care va primi email si parola ca parametrii; daca acestea sunt corecte, userul va fi marcat ca logat
# – o metoda get_info, care va returna toate informatiile despre user DOAR DACA acesta este logat, folosind un decorator `@require_login`
# – o metoda logout, fara params, care delogheaza userul.
#
#
# Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, si dupa inca o logare.
