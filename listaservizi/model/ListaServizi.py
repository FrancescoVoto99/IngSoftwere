from datetime import datetime
import json
import pickle
import os.path


class ListaServizi():

    def __init__(self):
        super(ListaServizi, self).__init__()

        self.listaservizi = []

        if os.path.isfile('listaservizi/data/lista_servizi.pickle'):
            with open('listaservizi/data/lista_servizi.pickle', 'rb') as f:
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
            if servizio.reparto.lower() == reparto.lower() and servizio.is_disponibile() and servizio.tipo != "ricovero di emergenza":
                return servizio
        return None

    def get_servizio_by_reparto_and_tipo(self, reparto, tipo, controller, datainizio, datafine):
        for servizio in self.listaservizi:
            if servizio.tipo.lower() == tipo.lower() and servizio.reparto.lower() == reparto.lower():
                if servizio.is_disponibile():
                    for prenotazione in controller.get_lista_delle_prenotazioni():
                        if prenotazione.servizio.posto_letto == servizio.posto_letto and prenotazione.servizio.tipo == servizio.tipo and prenotazione.servizio.reparto == servizio.reparto:
                            if datetime.strptime(prenotazione.datafine,'%d/%m/%Y') < datetime.strptime(datainizio,'%d/%m/%Y') or datetime.strptime(datafine,'%d/%m/%Y') < datetime.strptime(prenotazione.data,'%d/%m/%Y'):
                                return servizio
                    for prenotazione in controller.get_lista_delle_prenotazioni():
                        if prenotazione.servizio.posto_letto != servizio.posto_letto and prenotazione.servizio.tipo == servizio.tipo and prenotazione.servizio.reparto == servizio.reparto:
                            return servizio
                        else:
                            return None

    def get_lista_servizi(self):
        return self.listaservizi

    def salva_dati(self):
        with open('listaservizi/data/lista_servizi.pickle','wb') as handle:
            pickle.dump(self.listaservizi,handle,pickle.HIGHEST_PROTOCOL)

    def rimuovi_servizio_by_nome (self, nome):
        for servizio in self.listaservizi:
            if servizio.nome == nome :
                if servizio.disponibile == False:
                    return True
                else:
                    self.listaservizi.remove(servizio)
                    return False


