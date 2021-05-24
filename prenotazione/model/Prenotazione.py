
class Prenotazione():
    def __init__(self, id, paziente, servizio, data, datafine=None):
        super(Prenotazione, self).__init__()
        self.id = id
        self.paziente = paziente
        self.servizio = servizio
        self.data = data
        self.datafine= datafine

    def libera_posto_letto(self):
        self.servizio.disponibile = True

    def set_data_fine(self,datafine):
        self.datafine=datafine
