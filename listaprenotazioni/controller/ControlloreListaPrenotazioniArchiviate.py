import os
import pickle

from listaprenotazioni.model.ListaPrenotazioniArchiviate import ListaPrenotazioniArchiviate

# Classe responsabile della gestione delle relazioni tra
# il model ListaPrenotazioniArchiviate e la view
# VistaListaPrenotazioniArchiviate

class ControlloreListaPrenotazioniArchiviate():
    def __init__(self):
        super(ControlloreListaPrenotazioniArchiviate, self).__init__()
        self.model = ListaPrenotazioniArchiviate()
        if os.path.isfile('listaprenotazioni/data/lista_prenotazioni_archiviate.pickle'):
            with open('listaprenotazioni/data/lista_prenotazioni_archiviate.pickle', 'rb') as f:
                lista_prenotazioni_salvata = pickle.load(f)
            self.model.lista_prenotazioni = lista_prenotazioni_salvata

    def aggiungi_prenotazione(self, prenotazione):
        self.model.aggiungi_prenotazione(prenotazione)

    def get_prenotazione_by_index(self, index):
        return self.model.get_prenotazione_by_index(index)

    def get_lista_delle_prenotazioni(self):
        return self.model.get_lista_prenotazioni()

    def get_prenotazione_by_posto_letto_and_cf(self, posto_letto, cf):
        return self.model.get_prenotazione_by_posto_letto_and_cf(posto_letto, cf)

    def save_data(self):
        self.model.save_data()
