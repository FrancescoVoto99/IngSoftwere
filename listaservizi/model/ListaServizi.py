import json
import pickle
import os.path

from servizio.model.Servizio import Servizio


class ListaServizi():

    def __init__(self):
        super(ListaServizi, self).__init__()

        self.listaservizi = []

        if os.path.isfile('listaservizi/data/lista_servizi_salvata.pickle'):
            with open('listaservizi/data/lista_servizi_salvata.pickle', 'rb') as f:
                self.listaservizi = pickle.load(f)

    def aggiungi_servizio(self,servizio1):
        self.listaservizi.append(servizio1)

    def get_servizio_by_index(self,index):
        return self.listaservizi[index]

    def get_servizio_by_id(self,id):
        for servizio in self.listaservizi:
            if servizio.id == id:
                return servizio

    def get_servizio_by_nome(self, posto_letto):
        for servizio in self.listaservizi:
            if servizio.posto_letto == posto_letto:
                return servizio

    def get_servizio_by_tipo(self):
        for servizio in self.listaservizi:
            return servizio.__getattribute__("tipo")

    def get_servizio_by_reparto(self, reparto):
        for servizio in self.listaservizi:
            if servizio.reparto.lower() == reparto.lower():
                return servizio

    def get_lista_servizi(self):
        return self.listaservizi

    def salva_dati(self):
        with open('listaservizi/data/lista_servizi_salvata.pickle','wb') as handle:
            pickle.dump(self.listaservizi,handle,pickle.HIGHEST_PROTOCOL)