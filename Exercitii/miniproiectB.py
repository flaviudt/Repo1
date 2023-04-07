# TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
# finalizează_task(nume) - se va sterge din dict
# afișează_todo_list() - doar cheile
# afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
# Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
# Dacă acesta răspunde nu - la revedere
# Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict


class TodoList:
    todo: {}

    def adauga_task(self, nume, descriere):
        todo = dict()
        todo[nume] = descriere
        print(todo)

    # def finalizeaza_task(self,nume):
    #     todo :{}
    #     del todo[nume]
    #     print(todo)

    def afiseaza_todo_list(self):
        return


task1 = TodoList()
task1.adauga_task('invata', 'saptamana 4,curs OOP')
task1.adauga_task('mananca', 'mic-dejun')
# task1.finalizeaza_task('invata')
