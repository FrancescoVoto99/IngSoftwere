from unittest import TestCase

from paziente.model.Paziente import Paziente
from prenotazione.model.Prenotazione import Prenotazione
from servizio.model.Servizio import Servizio


class TestControllorePrenotazione(TestCase):

    # Test della funzione libera_posto_letto()
    def test_libera_posto_letto(self):
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.servizio = Servizio(id = "a1", nome = "ricovero in Oncologia (a1)", tipo = "ricovero",
                                 reparto = "Oncologia", posto_letto = "a1", disponibile = None)
        self.prenotazione = Prenotazione(id = id, paziente = self.paziente, servizio = self.servizio,
                                         data = "28/05/2021", datafine = "02/06/2021")
        self.prenotazione.libera_posto_letto()
        self.assertIsNotNone(self.servizio.disponibile)

    # Test della funzione set_data_fine()
    def test_set_data_fine(self):
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.servizio = Servizio(id="a1", nome="ricovero in Oncologia (a1)", tipo="ricovero",
                                 reparto="Oncologia", posto_letto="a1", disponibile=None)
        self.prenotazione = Prenotazione(id=id, paziente=self.paziente, servizio=self.servizio,
                                         data="28/05/2021", datafine="02/06/2021")
        self.assertEqual(self.prenotazione.datafine, "02/06/2021")
        self.prenotazione.set_data_fine("03/06/2021")
        self.assertNotEqual(self.prenotazione.datafine, "02/06/2021")
