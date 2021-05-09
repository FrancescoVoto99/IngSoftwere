class Paziente():

    def __init__(self, nome, cognome, luogodinascita, datadinascita,
                 cf, telefono, email):
        super(Paziente, self).__init__()
        self.nome = nome
        self.cognome = cognome
        self.luogodinascita = luogodinascita
        self.datadinascita = datadinascita
        self.cf = cf
        self.telefono = telefono
        self.email = email

