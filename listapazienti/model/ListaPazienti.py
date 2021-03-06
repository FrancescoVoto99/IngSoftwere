import os
import pickle

# Classe responsabile della gestione dei dati
# relativi alla lista dei pazienti

class ListaPazienti():

    def __init__(self):
        super(ListaPazienti, self).__init__()
        self.lista_pazienti = []
        if os.path.isfile('listapazienti/data/lista_pazienti_salvata.pickle'):
            with open('listapazienti/data/lista_pazienti_salvata.pickle', 'rb') as f:
                self.lista_pazienti = pickle.load(f)

    def aggiungi_paziente (self, paziente):
        self.lista_pazienti.append(paziente)

    def get_paziente_by_cf(self, cf):
        for paziente in self.get_lista_pazienti():
            if paziente.cf.upper() == cf:
                return paziente

    def get_paziente_by_index(self, index):
        return self.lista_pazienti[index]

    def get_lista_pazienti(self):
        return self.lista_pazienti

    def check_cf(self, cf):
        for paziente in self.get_lista_pazienti():
            if paziente.cf.lower() == cf.lower():
                return True
        return False

    def save_data(self):
        with open('listapazienti/data/lista_pazienti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_pazienti, handle, pickle.HIGHEST_PROTOCOL)