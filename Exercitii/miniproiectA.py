# Mașină
# Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori disponibile (set), înmatriculată (bool)
#    Culoare = gri - toate mașinile când ies din fabrică sunt gri
#    Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
#    Culori disponibile = alege tu 5-7 culori
#    Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
#    Înmatriculată = False
# Constructor: model, viteza_maxima
# Metode:
# descrie() - se vor printa toate atributele, în afară de culori_disponibile
# înmatriculare() - va schimba atributul înmatriculată în True
# vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare, dacă viteza e mai mare decât viteza_max - masina va accelera până la viteza maximă
# franeaza() - mașina se va opri și va avea viteza 0


class Masina:
    culoare = 'gri'
    viteza_actuala = 0
    culori_disponibile = {'rosie', 'alba', 'albastra', 'negra', 'galbena'}
    marca = 'Dacia'
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Masina {self.marca}, modelul {self.model}, culoarea {self.culoare}, viteza actuala {self.viteza_actuala}, inmatriculata:{self.inmatriculata}')

    def inmatriculare(self):
        print('Am inmatriculat masina!')
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
            print(f'Am vopsit masina.Acum are culoarea {culoare}')
        else:
            print(f'Nu avem culoarea {culoare} disponibila')

    def accelereaza(self,viteza):
        if viteza < self.viteza_maxima:
            self.viteza_actuala = viteza
            print(f'Masina atinge viteza {viteza} km/h')
        elif viteza < 0 :
            print('Eroare')
        else:
            self.viteza_actuala = self.viteza_maxima
            print('Am atins viteza maxima!')

    def franeaza(self):
        print('Am oprit masina.')
        self.viteza_actuala = 0


masina1 = Masina(1310,120)
masina1.descrie()
masina1.inmatriculare()
masina1.descrie()
masina1.vopseste('rosie')
masina1.accelereaza(100)
masina1.descrie()
masina1.franeaza()
masina1.descrie()

