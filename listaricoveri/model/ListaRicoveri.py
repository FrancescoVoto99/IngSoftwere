import pickle
from datetime import date

from listapazienti.controller.ControlloreListaPazienti import ControlloreListaPazienti
from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from paziente.Controller.ControllorePaziente import ControllorePaziente
from ricovero.controller.ControlloreRicovero import ControlloreRicovero


class ListaRicoveri():

    def __init__(self):
        super(ListaRicoveri, self).__init__()
        self.lista_ricoveri = []

    def aggiungi_ricovero(self):
        controller_pazienti = ControlloreListaPazienti()
        for element in controller_pazienti.get_lista_pazienti():
            controller_paziente = ControlloreRicovero(element)
            if controller_paziente.is_ricoverato(element.cf):
                self.lista_ricoveri.append(element)

    def get_ricovero_by_index(self, index):
        return self.lista_ricoveri[index]

    def get_lista_ricoveri(self):
        return self.lista_ricoveri

    def save_data(self):
        with open('listaricoveri/data/lista_ricoveri_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_ricoveri, handle, pickle.HIGHEST_PROTOCOL)