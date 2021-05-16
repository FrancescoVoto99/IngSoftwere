import os
import pickle
from datetime import date

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from listaricoveri.model.ListaRicoveri import ListaRicoveri


class ControlloreListaRicoveri():

    def __init__(self):
        super(ControlloreListaRicoveri, self).__init__()
        self.model = ListaRicoveri()
        if os.path.isfile('listaricoveri/data/lista_ricoveri_salvata.pickle'):
            with open('listaricoveri/data/lista_ricoveri_salvata.pickle', 'rb') as f:
                lista_ricoveri_salvata = pickle.load(f)
            self.model.lista_prenotazioni = lista_ricoveri_salvata

    def aggiungi_ricovero(self):
        self.model.aggiungi_ricovero()

    def get_ricovero_by_index(self, index):
        return self.model.get_ricovero_by_index(index)

    def get_lista_dei_ricoveri(self):
        return self.model.get_lista_ricoveri()

    def save_data(self):
        self.model.save_data()