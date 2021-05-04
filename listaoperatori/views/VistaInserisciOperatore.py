from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QLineEdit, QMessageBox

from operatore.model.Operatore import Operatore


class VistaInserisciOperatore(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciOperatore, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_type("Id")
        self.get_type("Nome")
        self.get_type("Cognome")
        self.get_type("Codice fiscale")
        self.get_type("Data di nascita")
        self.get_type("Luogo di nascita")
        self.get_type("Email")
        self.get_type("Ruolo")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_Operatore)
        self.v_layout.addWidget(btn_ok)

        self.setLayout((self.v_layout))
        self.setWindowTitle("Nuovo Operatore")

    def get_type(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text = QLineEdit(self)
        self.v_layout.addWidget(current_text)
        self.info[tipo] = current_text

    def add_Operatore(self):
        id = self.info["Id"].text
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        cf = self.info["Codice fiscale"].text()
        datanascita = self.info["Data di nascita"].text()
        luogonascita = self.info["Luogo di nascita"].text()
        email = self.info["Email"].text()
        ruolo = self.info["Ruolo"].text()


        if id == "" or nome == "" or cognome == "" or luogonascita == "" or datanascita == "" or cf == "" or ruolo == "" or email == "":
            QMessageBox.critical(self, 'Errore', 'Per favore inserisci tutte le informazioni', QMessageBox.Ok,
                                 QMessageBox.Ok)
        else:
            self.controller.aggiungi_operatore(Operatore((nome + cognome).lower(), id, nome, cognome, cf, datanascita, luogonascita, email, ruolo))
            self.callback()
            self.close()