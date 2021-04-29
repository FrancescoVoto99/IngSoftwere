from listapazienti.model.ListaPazienti import ListaPazienti


class ControlloreListaPazienti():

    def __init__(self):
        super(ControlloreListaPazienti, self).__init__()
        self.model = ListaPazienti()

    def aggiungi_paziente(self, paziente):
        self.model.aggiungi_paziente(paziente)

    def get_lista_pazienti(self):
        return self.model.get_lista_pazienti()

    def get_paziente_by_index(self, index):
        self.model.get_paziente_by_index(index)

    def elimina_paziente_by_cf(self, cf):
        self.model.rimuovi_paziente_by_cf(cf)

    def save_data(self):
        self.model.save_data()