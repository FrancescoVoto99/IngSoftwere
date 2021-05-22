class ControlloreServizio():

    def __init__(self, servizio):
        self.model = servizio

    def get_id_servizio(self):
        return self.model.id

    def get_nome_servizio(self):
        return (self.get_tipo_servizio() + " in " + self.get_reparto_servizio() + " (" + self.get_posto_letto_servizio() + ")")

    def get_tipo_servizio(self):
        return self.model.tipo

    def get_reparto_servizio(self):
        return self.model.reparto

    def get_posto_letto_servizio(self):
        return self.model.posto_letto

    def get_servizio_disponibile(self):
        if self.model.is_disponibile():
            return "Disponibile"
        else:
            return "Non disponibile"