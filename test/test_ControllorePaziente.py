from unittest import TestCase

from paziente.model.Paziente import Paziente

class TestControllorePaziente(TestCase):

    # Test della funzione get_ricovero_paziente()
    def test_get_ricovero_paziente(self):
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.assertIsNone(self.paziente.ricovero)

    # Test della funzione aggiungi_ricovero_paziente()
    def test_aggiungi_nuovo_ricovero_paziente(self):
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.assertIsNone(self.paziente.ricovero)
        self.paziente.add_ricovero(ricovero = True)
        self.assertIsNotNone(self.paziente.ricovero)

    # Test della funzione get_referto_paziente()
    def test_get_referto_paziente(self):
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.paziente.get_referto()
        self.assertEqual(self.paziente.referto, "")

    # Test della funzione aggiungi_nuovo_referto_paziente()
    def test_aggiungi_nuovo_referto_paziente(self):
        self.paziente = Paziente(nome="Mario", cognome="Rossi", sesso="Maschio",
                                 luogodinascita="Ancona", datadinascita="12/07/1980",
                                 cf="RSSMRA80L12A271V", telefono="3345609712",
                                 email="mariorossi@gmail.com")
        self.assertEqual(self.paziente.referto, "")
        self.paziente.add_referto(self.paziente.referto == "Il paziente accusa dolori")
        self.assertNotEqual(self.paziente.referto, "")

