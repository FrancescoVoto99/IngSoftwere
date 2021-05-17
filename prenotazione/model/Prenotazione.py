from paziente.model.Paziente import Paziente
from servizio.model.Servizio import Servizio


class Prenotazione():
    def __init__(self, id, paziente, servizio, data):
        super(Prenotazione, self).__init__()
        self.id = id
        self.paziente = paziente
        self.servizio = servizio
        self.data = data

    def libera_posto_letto(self):
        self.servizio.disponibile = True