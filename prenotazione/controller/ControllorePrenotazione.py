from prenotazione.model.Prenotazione import Prenotazione


class ControllorePrenotazione():
    def __init__(self, prenotazione):
        self.model = prenotazione

    def get_id_prenotazione(self):
        return self.model.id

    def get_paziente_prenotazione(self):
        return self.model.paziente

    def get_servizio_prenotazione(self):
        return self.model.servizio

    def set_servizio_prenotazione(self, servizio):
        self.model = servizio

    def get_data_prenotazione(self):
        return self.model.data

    def set_data_prenotazione(self, data):
        self.model = data






