from unittest import TestCase

from listapazienti.model.ListaPazienti import ListaPazienti
from paziente.model.Paziente import Paziente


class TestControlloreListaPazienti(TestCase):

    # Test della funzione aggiungi_paziente()
    def test_aggiungi_paziente(self):
        self.lista_pazienti = ListaPazienti()
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.assertListEqual(self.lista_pazienti.get_lista_pazienti(), [])
        self.lista_pazienti.aggiungi_paziente(self.paziente)
        self.assertIsNotNone(self.lista_pazienti.get_lista_pazienti())

    # Test della funzione check_cf()
    def test_check_cf(self):
        self.lista_pazienti = ListaPazienti()
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.assertListEqual(self.lista_pazienti.get_lista_pazienti(), [])
        self.lista_pazienti.aggiungi_paziente(self.paziente)
        self.assertFalse(self.lista_pazienti.check_cf("FRRMRA80C62F205M"))
