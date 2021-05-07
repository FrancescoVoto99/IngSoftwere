import os
import pickle

from operatore.controller.ControlloreOperatore import ControlloreOperatore


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
        def _is_selected_operatore(operatore):
            if operatore.id == id:
                return True
            return False
        self.lista_operatori.remove(list(filter(_is_selected_operatore, self.lista_operatori))[0])

    def get_operatore_by_index(self, index):
        return self.lista_operatori[index]

    def get_lista_operatori(self):
        return self.lista_operatori

    def save_data(self):
        with open('listaoperatori/data/lista_operatori_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_operatori, handle, pickle.HIGHEST_PROTOCOL)