class ControlloreOperatore():

    def __init__(self, operatore):
        self.model = operatore

    def get_id_operatore(self):
        return self.model.id

    def get_nome_operatore(self):
        return self.model.nome

    def get_cognome_operatore(self):
        return self.model.cognome

    def get_cf_operatore(self):
        return self.model.cf

    def get_data_nascita_operatore(self):
        return self.model.datanascita

    def get_luogo_nascita_operatore(self):
        return self.model.luogonascita

    def get_email_operatore(self):
        return self.model.email

    def get_ruolo_operatore(self):
        return self.model.ruolo

    def get_password_operatore(self):
        return self.model.password
