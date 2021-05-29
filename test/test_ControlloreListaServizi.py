from unittest import TestCase

from listaservizi.model.ListaServizi import ListaServizi
from servizio.model.Servizio import Servizio


class TestControlloreListaServizi(TestCase):

    # Test della funzione aggiungi_servizio()
    def test_aggiungi_servizio(self):
        self.lista_servizi = ListaServizi()
        self.servizio = Servizio(id="a1", nome="ricovero in Oncologia (a1)", tipo="ricovero",
                                 reparto="Oncologia", posto_letto="a1", disponibile=True)
        self.assertListEqual(self.lista_servizi.get_lista_servizi(), [])
        self.lista_servizi.aggiungi_servizio(self.servizio)
        self.assertIsNotNone(self.lista_servizi.get_lista_servizi())

    # Test della funzione elimina_servizio_by_nome()
    def test_elimina_servizio_by_nome(self):
        self.lista_servizi = ListaServizi()
        self.servizio = Servizio(id="a1", nome="ricovero in Oncologia (a1)", tipo="ricovero",
                                 reparto="Oncologia", posto_letto="a1", disponibile=True)
        self.assertListEqual(self.lista_servizi.get_lista_servizi(), [])
        self.lista_servizi.aggiungi_servizio(self.servizio)
        self.lista_servizi.rimuovi_servizio_by_nome("ricovero in Oncologia (a1)")
        self.assertListEqual(self.lista_servizi.get_lista_servizi(), [])
