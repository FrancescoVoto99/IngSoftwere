import json
import pickle
import os.path

from servizio.model.Servizio import Servizio


class ListaServizi():

    def __init__(self):
        super(ListaServizi, self).__init__()

        self.listaservizi = []

        if os.path.isfile('listaservizi/data/dati_lista_servizi.pickle'):
            with open('listaservizi/data/dati_lista_servizi.pickle', 'rb') as f:
                self.listaservizi = pickle.load(f)
        else:
            with open('listaservizi/data/lista_servizi_iniziali.json') as f:
                lista_servizi_iniziali = json.load(f)
            for servizio in lista_servizi_iniziali:
                self.aggiungi_servizio(Servizio(servizio["id"], servizio["nome"], servizio["tipo"],
                                                servizio["reparto"], servizio["posto_letto"],
                                                servizio["disponibile"]))




    def aggiungi_servizio(self,servizio1):
        self.listaservizi.append(servizio1)

    def get_servizio_by_index(self,index):
        return self.listaservizi[index]

    def get_lista_servizi(self):
        return self.listaservizi

    def salva_dati(self):
        with open('listaservizi/data/dati_lista_servizi.pickle','wb') as handle:
            pickle.dump(self.listaservizi,handle,pickle.HIGHEST_PROTOCOL)