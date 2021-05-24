from datetime import date


class Paziente():

    def __init__(self, nome, cognome, sesso, luogodinascita, datadinascita,
                 cf, telefono, email):
        super(Paziente, self).__init__()
        self.nome = nome
        self.cognome = cognome
        self.sesso = sesso
        self.luogodinascita = luogodinascita
        self.datadinascita = datadinascita
        self.cf = cf
        self.telefono = telefono
        self.email = email
        self.ricovero = None
        self.referto = ""

    def add_ricovero(self, ricovero):
        self.ricovero = ricovero

    def get_ricovero(self):
        if self.ricovero.is_finericovero():
            self.ricovero = None
            return None
        else:
            return self.ricovero

    def get_referto(self):
        return self.referto

    def add_referto(self, referto):
        today = date.today()
        if self.get_referto() == None:
            self.referto = '\n' + today.strftime('%d/%m/%Y') + ": " + str(referto)
        else:
            self.referto = str(self.get_referto()) +'\n' + today.strftime('%d/%m/%Y') + ": " + str(referto)

