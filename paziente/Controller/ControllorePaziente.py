class ControllorePaziente():
   def __init__(self, paziente):
    self.model = paziente

   def get_nome_paziente(self):
       return self.model.nome

   def get_cognome_paziente(self):
       return self.model.cognome

   def get_sesso_paziente(self):
       return self.model.sesso

   def get_luogodinascita_paziente(self):
       return self.model.luogodinascita

   def get_datadinascita_paziente(self):
        return self.model.datadinascita

   def get_cf_paziente(self):
        return self.model.cf

   def get_telefono_paziente(self):
        return self.model.telefono

   def get_email_paziente(self):
        return self.model.email

   def get_ricovero_paziente(self):
        return self.model.ricovero

   def aggiungi_nuovo_ricovero_paziente(self, ricovero):
        self.model.add_ricovero(ricovero)

