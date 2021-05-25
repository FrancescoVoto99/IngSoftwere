import json
import os
import pickle



class ListaPrenotazioniArchiviate():
    def __init__(self):
        super(ListaPrenotazioniArchiviate, self).__init__()
        self.lista_prenotazioni = []

    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)

    def get_prenotazione_by_index(self, index):
        return self.lista_prenotazioni[index]

    def get_prenotazione_by_posto_letto_and_cf(self, posto_letto, cf):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.servizio.posto_letto == posto_letto and prenotazione.paziente.cf == cf:
                return prenotazione

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

    def save_data(self):
        with open('listaprenotazioni/data/lista_prenotazioni_archiviate.pickle', 'wb') as handle:
            pickle.dump(self.lista_prenotazioni, handle, pickle.HIGHEST_PROTOCOL)