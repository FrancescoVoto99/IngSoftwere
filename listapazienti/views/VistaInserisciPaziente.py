from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QSpacerItem, QSizePolicy, QPushButton

from paziente.model.Paziente import Paziente


class VistaInserisciPaziente(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciPaziente, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        self.get_type("Nome")
        self.get_type("Cognome")
        self.get_type("Luogo di nascita")
        self.get_type("Data di nascita")
        self.get_type("Codice fiscale")
        self.get_type("Telefono")
        self.get_type("Email")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_paziente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout((self.v_layout))
        self.setWindowTitle("Nuovo Paziente")

    def get_type (self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text = QLineEdit(self)
        self.v_layout.addWidget(current_text)
        self.info[tipo] = current_text

    def add_paziente(self):
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        luogo_nascita = self.info["Luogo di nascita"].text()
        data_nascita = self.info["Data di nascita"].text()
        cf = self.info["Codice fiscale"].text()
        telefono = self.info["Telefono"].text()
        email = self.info["Email"].text()
        if nome == "" or cognome == "" or luogo_nascita == "" or data_nascita == "" or cf == "" or telefono == "" or email == "":
            QMessageBox.critical(self, 'Errore', 'Per favore inserisci tutte le informazioni', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_paziente(Paziente((nome+cognome).lower(), nome, cognome, luogo_nascita, data_nascita, cf, telefono, email))
            self.callback()
            self.close()