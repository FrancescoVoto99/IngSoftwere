class Paziente():

    def __init__(self, nome, cognome, luogo_nascita, data_nascita,
                 cf, telefono, email):
        super(Paziente, self).__init__()
        self.nome = nome
        self.cognome = cognome
        self.luogo_nascita = luogo_nascita
        self.data_nascita = data_nascita
        self.cf = cf
        self.telefono = telefono
        self.email = email

