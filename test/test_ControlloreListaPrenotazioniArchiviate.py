from unittest import TestCase

from listaprenotazioni.model.ListaPrenotazioniArchiviate import ListaPrenotazioniArchiviate
from paziente.model.Paziente import Paziente
from prenotazione.model.Prenotazione import Prenotazione
from servizio.model.Servizio import Servizio


class TestControlloreListaPrenotazioniArchiviate(TestCase):

    # Test della funzione aggiungi_prenotazione()
    def test_aggiungi_prenotazione(self):
        self.lista_prenotazioni_archiviate = ListaPrenotazioniArchiviate()
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.servizio = Servizio(id="a1", nome="ricovero in Oncologia (a1)", tipo="ricovero",
                                 reparto="Oncologia", posto_letto="a1", disponibile=None)
        self.prenotazione = Prenotazione(id="a1", paziente=self.paziente, servizio=self.servizio,
                                         data="30/05/2021", datafine="02/06/2021")
        self.assertListEqual(self.lista_prenotazioni_archiviate.get_lista_prenotazioni(), [])
        self.lista_prenotazioni_archiviate.aggiungi_prenotazione(self.prenotazione)
        self.assertIsNotNone(self.lista_prenotazioni_archiviate.get_lista_prenotazioni())
