from listaoperatori.model.ListaOperatori import ListaOperatori


class ControlloreListaOperatori():

    def __init__(self):
        super(ControlloreListaOperatori, self).__init__()
        self.model = ListaOperatori()

    def aggiungi_operatore(self, operatore):
        self.model.aggiungi_operatore(operatore)

    def check_cf (self, text):
        for element in self.get_lista_operatori():
            if element.cf == text:
                return True
        return False

    def get_lista_operatori(self):
        return self.model.get_lista_operatori()

    def get_operatore_by_index(self, index):
        return self.model.get_operatore_by_index (index)

    def get_operatore_numeber(self, index):
        return self.model.get_operatore_number

    def get_operatore_by_id(self, id):
        return self.model.get_operatore_by_id (id)

    def search_operatore_by_nomecognome(self, nome, cognome):
        return self.model.search_operatore_by_nomecognome(nome, cognome)

    def elimina_operatore_by_id(self, id):
        self.model.rimuovi_operatore_by_id(id)

    def save_data(self):
        self.model.save_data()