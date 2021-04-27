class Servizio():
    def __init__(self,id,nome,tipo,reparto,posto_letto,disponibile):
        super(Servizio,self).__init__()
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.reparto= reparto
        self.posto_letto=posto_letto
        self.disponibile = True

    def is_disponibile(self):
        return self.disponibile

    def prenota(self):
        self.disponibile= False
