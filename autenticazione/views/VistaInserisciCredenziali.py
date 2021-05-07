import json

from PyQt5.QtWidgets import QWidget, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, QLineEdit, \
    QGridLayout

from Home.views.VistaHomeAccettazione import VistaHomeAccettazione
from Home.views.VistaHomeInfermiere import VistaHomeInfermiere
from Home.views.VistaHomeMedico import VistaHomeMedico
from Home.views.VistaHomeProntoSoccorso import VistaHomeProntoSoccorso


class VistaInserisciCredenziali(QWidget):

    def __init__(self):
        super(VistaInserisciCredenziali, self).__init__()

        self.h_layout = QGridLayout()

        self.lbl_title = QLabel("Inserire le credenziali:")
        self.h_layout.addWidget((self.lbl_title), 0, 0)

        self.h_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        lbl_username = QLabel("Username")
        self.h_layout.addWidget((lbl_username),1,0)
        self.line_edit_username = QLineEdit()
        self.h_layout.addWidget((self.line_edit_username), 1, 1)

        self.h_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        lbl_password = QLabel("Password")
        self.h_layout.addWidget((lbl_password), 2, 0)
        self.line_edit_password = QLineEdit()
        self.h_layout.addWidget((self.line_edit_password), 2, 1)

        self.h_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("Ok")
        btn_ok.clicked.connect(self.openHome)
        self.h_layout.addWidget((btn_ok), 3, 0)

        self.setLayout(self.h_layout)
        self.setWindowTitle("HospItaly")

    def identity_check(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()
        with open('autenticazione/data/data_info.json') as f:
            lista_autenticazioni = json.load(f)
            for autenticazioni in lista_autenticazioni:
                if autenticazioni["Username"] == username and autenticazioni["Password"] == password:
                    return autenticazioni["Professione"]

    def openHome(self):
        if self.identity_check() == "Amministratore dell'ufficio di accettazione":
            self.go_vista = VistaHomeAccettazione()
            self.go_vista.show()
            self.close()
        elif self.identity_check() == "Amministratore del pronto soccorso":
            self.go_vista = VistaHomeProntoSoccorso()
            self.go_vista.show()
            self.close()
        elif self.identity_check() == "Infermiere":
            self.go_vista == VistaHomeInfermiere()
            self.go_vista.show()
            self.close()
        elif self.identity_check() == "Medico":
            self.go_vista == VistaHomeMedico()
            self.go_vista.show()
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Credenziali errate', QMessageBox.Ok, QMessageBox.Ok)
