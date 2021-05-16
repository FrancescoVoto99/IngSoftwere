from datetime import datetime

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione


class ControlloreRicovero():

    def __init__(self, ricovero):
        self.model = ricovero

    def is_ricoverato(self, paziente_cf):
        controllore_lista_prenotazioni = ControlloreListaPrenotazioni()
        for prenotazione in controllore_lista_prenotazioni.get_lista_delle_prenotazioni():
            if prenotazione.paziente.cf == paziente_cf:
                return True
        return False

    def get_finericovero_string(self):
        finericovero_data = datetime.fromtimestamp(self.model.finericovero)
        return "Fine ricovero {}/{}/{}".format(finericovero_data.day, finericovero_data.month, finericovero_data.year)