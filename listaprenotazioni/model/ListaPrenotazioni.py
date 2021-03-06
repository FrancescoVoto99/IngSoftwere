import pickle

from listaservizi.controller.ControlloreListaServizi import ControlloreListaServizi

# Classe responsabile della gestione dei dati della
# lista delle prenotazioni

class ListaPrenotazioni():
    def __init__(self):
        super(ListaPrenotazioni, self).__init__()
        self.lista_prenotazioni = []

    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)

    def rimuovi_prenotazione_by_id(self, id):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.id == id:
                prenotazione.servizio.set_disponibile()
                prenotazione.servizio.set_prenotato()
                self.lista_prenotazioni.remove(prenotazione)
                controller=ControlloreListaServizi()
                disp=controller.get_servizio_by_id(prenotazione.servizio.id)
                disp.set_disponibile()
                disp.set_prenotato()
                controller.save_data()
                return True
        return False

    def get_prenotazione_by_index(self, index):
        return self.lista_prenotazioni[index]

    def get_prenotazione_by_posto_letto_and_cf(self,posto_letto, cf):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.servizio.posto_letto == posto_letto and prenotazione.paziente.cf == cf:
                return prenotazione

    def get_prenotazione_by_id(self, id):
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.id == id:
                return prenotazione

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

    def save_data(self):
        with open('listaprenotazioni/data/lista_prenotazioni_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_prenotazioni, handle, pickle.HIGHEST_PROTOCOL)