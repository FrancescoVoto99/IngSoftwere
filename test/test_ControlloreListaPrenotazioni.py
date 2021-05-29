from unittest import TestCase

from listapazienti.model.ListaPazienti import ListaPazienti
from listaprenotazioni.model.ListaPrenotazioni import ListaPrenotazioni
from listaservizi.model.ListaServizi import ListaServizi
from paziente.model.Paziente import Paziente
from prenotazione.model.Prenotazione import Prenotazione
from servizio.model.Servizio import Servizio


class TestControlloreListaPrenotazioni(TestCase):

    # Test della funzione aggiungi_prenotazione()
    def test_aggiungi_prenotazione(self):
        self.lista_prenotazioni = ListaPrenotazioni()
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.servizio = Servizio(id="a1", nome="ricovero in Oncologia (a1)", tipo="ricovero",
                                 reparto="Oncologia", posto_letto="a1", disponibile=None)
        self.prenotazione = Prenotazione(id="id", paziente=self.paziente, servizio=self.servizio,
                                         data="28/05/2021", datafine="02/06/2021")
        self.assertListEqual(self.lista_prenotazioni.get_lista_prenotazioni(), [])
        self.lista_prenotazioni.aggiungi_prenotazione(self.prenotazione)
        self.assertIsNotNone(self.lista_prenotazioni.get_lista_prenotazioni())

    # Test della funzione elimina_prenotazione_by_id()
    def test_elimina_prenotazione_by_id(self):
        self.lista_prenotazioni = ListaPrenotazioni()
        self.lista_servizi = ListaServizi()
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.servizio = Servizio(id="a1", nome="ricovero in Oncologia (a1)", tipo="ricovero",
                                 reparto="Oncologia", posto_letto="a1", disponibile = True)
        self.prenotazione = Prenotazione(id="rossimario", paziente=self.paziente, servizio=self.servizio,
                                         data="30/05/2021", datafine="02/06/2021")
        self.assertListEqual(self.lista_prenotazioni.get_lista_prenotazioni(), [])
        self.assertListEqual(self.lista_servizi.get_lista_servizi(), [])
        self.lista_servizi.aggiungi_servizio(self.servizio)
        self.lista_prenotazioni.aggiungi_prenotazione(self.prenotazione)
        #self.assertTrueself.lista_prenotazioni.rimuovi_prenotazione_by_id("bianchigiovanni"))
        self.lista_prenotazioni.rimuovi_prenotazione_by_id("bianchigiovanni")
        self.assertIsNotNone(self.lista_prenotazioni.get_lista_prenotazioni())
        #self.lista_prenotazioni.rimuovi_prenotazione_by_id("rossimario")
        #self.assertEquals(self.lista_prenotazioni.get_lista_prenotazioni(), [])
