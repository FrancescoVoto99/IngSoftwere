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

    def add_ricovero(self, ricovero):
        self.ricovero = ricovero

    def get_ricovero(self):
        if self.ricovero.is_finericovero():
            self.ricovero = None
            return None
        else:
            return self.ricovero



