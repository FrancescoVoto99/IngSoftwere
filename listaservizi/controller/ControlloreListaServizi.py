from listaservizi.model.ListaServizi import ListaServizi


class ControlloreListaServizi():

    def __init__(self):
        super(ControlloreListaServizi, self).__init__()
        self.model = ListaServizi()

    def get_lista_servizi(self):
        return self.model.get_lista_servizi()

    def get_servizio_by_index(self,index):
        return self.model.get_servizio_by_index(index)

    def get_servizio_by_id(self, id):
        return self.model.get_servizio_by_id(id)

    def get_servizio_by_nome(self, posto_letto):
        return self.model.get_servizio_by_nome(posto_letto)

    def get_servizio_by_reparto(self, reparto):
        return self.model.get_servizio_by_reparto(reparto)

    def get_servizio_by_tipo(self, tipo):
        return self.model.get_servizio_by_tipo(tipo)

    def get_servizio_by_reparto_and_tipo(self, reparto, tipo, controller, datainizio, datafine):
        return self.model.get_servizio_by_reparto_and_tipo(reparto, tipo, controller, datainizio, datafine)

    def save_data(self):
        self.model.salva_dati()

    def aggiungi_servizio(self, servizio):
        self.model.aggiungi_servizio(servizio)

    def all_disponible(self):
        self.model.all_disponibile()

    def elimina_servizio_by_nome(self, nome):
        self.model.rimuovi_servizio_by_nome(nome)

