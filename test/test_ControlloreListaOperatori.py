from unittest import TestCase

from listaoperatori.model.ListaOperatori import ListaOperatori
from operatore.model.Operatore import Operatore


class TestControlloreListaOperatori(TestCase):

    # Test della funzione aggiungi_operatore()
    def test_aggiungi_operatore(self):
        self.lista_operatori = ListaOperatori()
        self.operatore = Operatore(id = "mariaferrari", nome = "Maria", cognome = "Ferrari",
                                   cf = "FRRMRA80C62F205M", datanascita = "22/03/1980",
                                   luogonascita = "Milano", email = "mariaferrari@gmail.com",
                                   ruolo = "Infermiere", password = "mary22")
        self.assertListEqual(self.lista_operatori.get_lista_operatori(), [])
        self.lista_operatori.aggiungi_operatore(self.operatore)
        self.assertIsNotNone(self.lista_operatori.get_lista_operatori())

    # Test della funzione check_cf()
    def test_check_cf(self):
        self.lista_operatori = ListaOperatori()
        self.operatore = Operatore(id="mariaferrari", nome="Maria", cognome="Ferrari",
                                   cf="FRRMRA80C62F205M", datanascita="22/03/1980",
                                   luogonascita="Milano", email="mariaferrari@gmail.com",
                                   ruolo="Infermiere", password="mary22")
        self.assertListEqual(self.lista_operatori.get_lista_operatori(), [])
        self.lista_operatori.aggiungi_operatore(self.operatore)
        self.assertTrue(self.lista_operatori.check_cf("FRRMRA80C62F205M"))

    # Test della funzione search_operatore_by_nomecognome()
    def test_search_operatore_by_nomecognome(self):
        self.lista_operatori = ListaOperatori()
        self.operatore = Operatore(id="mariaferrari", nome="Maria", cognome="Ferrari",
                                   cf="FRRMRA80C62F205M", datanascita="22/03/1980",
                                   luogonascita="Milano", email="mariaferrari@gmail.com",
                                   ruolo="Infermiere", password="mary22")
        self.assertListEqual(self.lista_operatori.get_lista_operatori(), [])
        self.lista_operatori.aggiungi_operatore(self.operatore)
        self.assertIsNone(self.lista_operatori.search_operatore_by_nomecognome("Mario", "Rossi"))

    # Test della funzione elimina_operatore_by_id()
    def test_elimina_operatore_by_id(self):
        self.lista_operatori = ListaOperatori()
        self.operatore = Operatore(id="mariaferrari", nome="Maria", cognome="Ferrari",
                                   cf="FRRMRA80C62F205M", datanascita="22/03/1980",
                                   luogonascita="Milano", email="mariaferrari@gmail.com",
                                   ruolo="Infermiere", password="mary22")
        self.assertListEqual(self.lista_operatori.get_lista_operatori(), [])
        self.lista_operatori.aggiungi_operatore(self.operatore)
        self.lista_operatori.rimuovi_operatore_by_id("mariaferrari")
        self.assertListEqual(self.lista_operatori.get_lista_operatori(), [])

