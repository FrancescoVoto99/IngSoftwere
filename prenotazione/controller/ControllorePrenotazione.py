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
    def libera_posto_letto(self):
        return  self.model.libera_posto_letto

    def get_data_prenotazione(self):
        return self.model.data






