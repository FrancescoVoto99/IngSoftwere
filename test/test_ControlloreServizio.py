from datetime import date, datetime
from unittest import TestCase

from paziente.model.Paziente import Paziente
from prenotazione.model.Prenotazione import Prenotazione
from servizio.model.Servizio import Servizio


class TestControlloreServizio(TestCase):

    # Test della funzione is_disponibile()
    def test_is_disponibile(self):
        self.servizio = Servizio(id="a1", nome="ricovero in Oncologia (a1)", tipo="ricovero",
                                reparto="Oncologia", posto_letto="a1", disponibile=None)
        self.assertIsNone(self.servizio.disponibile)

    # Test della funzione is_prenotato()
    def test_is_prenotato(self):
        self.servizio = Servizio(id="a1", nome="ricovero in Oncologia (a1)", tipo="ricovero",
                                 reparto="Oncologia", posto_letto="a1", disponibile=None)
        self.assertIsNotNone(self.servizio.prenotato)

    # Test della funzione set_prenotato()
    def test_set_prenotato(self):
        self.servizio = Servizio(id="a1", nome="ricovero in Oncologia (a1)", tipo="ricovero",
                                 reparto="Oncologia", posto_letto="a1", disponibile=None)
        self.assertIsNotNone(self.servizio.prenotato)
        self.servizio.set_prenotato()
        self.assertIsNotNone(self.servizio.prenotato)

    # Test della funzione prenota()
    def test_prenota(self):
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.servizio = Servizio(id="a1", nome="ricovero in Oncologia (a1)", tipo="ricovero",
                                 reparto="Oncologia", posto_letto="a1", disponibile=None)
        self.prenotazione = Prenotazione(id=id, paziente=self.paziente, servizio=self.servizio,
                                         data="28/05/2021", datafine="02/06/2021")
        self.servizio.prenota(datetime.strptime(self.prenotazione.data, '%d/%m/%Y').date())
        self.assertIsNotNone(self.servizio.prenotato)

    # Test della funzione set_disponibile()
    def test_set_disponibile(self):
        self.servizio = Servizio(id="a1", nome="ricovero in Oncologia (a1)", tipo="ricovero",
                                 reparto="Oncologia", posto_letto="a1", disponibile=None)
        self.servizio.set_disponibile()
        self.assertIsNotNone(self.servizio.disponibile)
