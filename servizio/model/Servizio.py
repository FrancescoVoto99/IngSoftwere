from datetime import date

# Classe responsabile della gestione dei dati
# dell'entità Servizio

class Servizio():

    def __init__(self, id, nome, tipo, reparto, posto_letto, disponibile):
        super(Servizio, self).__init__()
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.reparto = reparto
        self.posto_letto = posto_letto
        self.disponibile = disponibile
        self.prenotato = False

    def is_disponibile(self):
        return self.disponibile

    def is_prenotato(self):
        self.prenotato = True

    def prenotato(self):
        return self.prenotato

    def set_prenotato(self):
        self.prenotato = False

    def prenota(self, data):
        if data <= date.today():
            self.disponibile = False
        else:
            self.disponibile = True

    def set_disponibile(self):
        self.disponibile = True


