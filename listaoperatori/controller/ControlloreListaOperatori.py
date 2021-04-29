from listaoperatori.model.ListaOperatori import ListaOperatori


class ControlloreListaOperatori():

    def __init__(self):
        super(ControlloreListaOperatori, self).__init__()
        self.model = ListaOperatori()

    def aggiungi_operatore(self, operatore):
        self.model.aggiungi_operatore(operatore)

    def get_lista_operatori(self):
        return self.model.get_lista_operatori()

    def get_operatore_by_index(self, index):
        self.model.get_operatore_by_index(index)

    def elimina_operatore_by_id(self, id):
        self.model.rimuovi_operatore_by_id(id)

    def save_data(self):
        self.model.save_data()