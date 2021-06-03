import os
import pickle

from operatore.controller.ControlloreOperatore import ControlloreOperatore

# Classe responsabile della gestione dei dati
# relativi alla lista degli operatori

class ListaOperatori():

    def __init__(self):
        super(ListaOperatori, self).__init__()
        self.lista_operatori = []
        if os.path.isfile('listaoperatori/data/list_operatori_salvata.pickle'):
            with open('listaoperatori/data/list_operatori_salvata.pickle', 'rb') as f:
                self.lista_operatori = pickle.load(f)

    def aggiungi_operatore (self, operatore):
        self.lista_operatori.append(operatore)

    def rimuovi_operatore_by_id (self, id):
        for operatore in self.lista_operatori:
            if operatore.id == id:
                self.lista_operatori.remove(operatore)
                return True
        return False

    def check_cf (self, text):
        for element in self.get_lista_operatori():
            if element.cf == text:
                return True
        return False

    def search_operatore_by_nomecognome(self, nome, cognome):
        for operatore in self.lista_operatori:
            controller = ControlloreOperatore(operatore)
            if controller.get_nome_operatore() == str(nome) and controller.get_cognome_operatore() == str(cognome):
                return self.lista_operatori(operatore)

    def get_operatore_by_index(self, index):
        return self.lista_operatori[index]

    def get_operatore_number(self):
        return len(self.lista_operatori)

    def get_operatore_by_id(self, id):
        for operatore in self.get_lista_operatori():
            if operatore.id==id:
                return operatore

    def get_lista_operatori(self):
        return self.lista_operatori

    def save_data(self):
        with open('listaoperatori/data/list_operatori_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_operatori, handle, pickle.HIGHEST_PROTOCOL)