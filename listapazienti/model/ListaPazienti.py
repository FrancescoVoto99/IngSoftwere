import os
import pickle


class ListaPazienti():

    def __init__(self):
        super(ListaPazienti, self).__init__()
        self.lista_pazienti = []
        if os.path.isfile('listapazienti/data/lista_pazienti.pickle'):
            with open('listapazienti/data/lista_pazienti.pickle', 'rb') as f:
                self.lista_pazienti = pickle.load(f)

    def aggiungi_paziente (self, paziente):
        self.lista_pazienti.append(paziente)

    def rimuovi_paziente_by_cf (self, cf):
        def _is_selected_paziente(paziente):
            if paziente.cf == cf:
                return True
            return False
        self.lista_pazienti.remove(list(filter(_is_selected_paziente(), self.lista_pazienti))[0])

    def get_paziente_by_index(self, index):
        return self.lista_pazienti[index]

    def get_lista_pazienti(self):
        return self.lista_pazienti

    def save_data(self):
        with open('listapazienti/data/lista_pazienti.pickle', 'wb') as handle:
            pickle.dump(self.lista_pazienti, handle, pickle.HIGHEST_PROTOCOL)