import os
import pickle


class ListaOperatori():

    def __init__(self):
        super(ListaOperatori, self).__init__()
        self.lista_operatori = []
        if os.path.isfile('listaoperatori/data/lista_operatori_salvata.pickle'):
            with open('listaoperatori/data/lista_operatori_salvata.pickle', 'rb') as f:
                self.lista_operatori = pickle.load(f)

    def aggiungi_operatore (self, operatore):
        self.lista_operatori.append(operatore)

    def rimuovi_operatore_by_id (self, id):
        for operatore in self.lista_operatori:
            if operatore.id == id:
                self.lista_operatori.remove(operatore)
                return True
        return False

    def get_operatore_by_index(self, index):
        return self.lista_operatori[index]

    def get_lista_operatori(self):
        return self.lista_operatori

    def save_data(self):
        with open('listaoperatori/data/lista_operatori_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_operatori, handle, pickle.HIGHEST_PROTOCOL)