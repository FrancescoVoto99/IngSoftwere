class Operatore():

    def __init__(self, id, nome, cognome, cf, datanascita, luogonascita, email, ruolo, password):
        super(Operatore, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.datanascita = datanascita
        self.luogonascita = luogonascita
        self.email = email
        self.ruolo = ruolo
        self.password = password