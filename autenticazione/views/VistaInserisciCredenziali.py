import json
import os
import pickle

from PyQt5.QtWidgets import QWidget, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, QLineEdit, \
    QGridLayout

from Home.views.VistaHomeAccettazione import VistaHomeAccettazione
from Home.views.VistaHomeInfermiere import VistaHomeInfermiere
from Home.views.VistaHomeMedico import VistaHomeMedico
from Home.views.VistaHomeProntoSoccorso import VistaHomeProntoSoccorso
from operatore.controller.ControlloreOperatore import ControlloreOperatore


class VistaInserisciCredenziali(QWidget):

    def __init__(self):
        super(VistaInserisciCredenziali, self).__init__()

        self.h_layout = QGridLayout()

        self.lbl_title = QLabel("Inserire le credenziali:")
        font_lbl_title = self.lbl_title.font()
        font_lbl_title.setPointSize(20)
        font_lbl_title.setBold(True)
        self.lbl_title.setFont(font_lbl_title)
        self.h_layout.addWidget((self.lbl_title), 0, 0)

        self.h_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        lbl_username = QLabel("Username")
        font_lbl_u = lbl_username.font()
        font_lbl_u.setPointSize(15)
        lbl_username.setFont(font_lbl_u)
        self.h_layout.addWidget((lbl_username),1,0)
        self.line_edit_username = QLineEdit()
        self.line_edit_username.setStyleSheet("background-color: white")
        self.h_layout.addWidget((self.line_edit_username), 1, 1)

        self.h_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        lbl_password = QLabel("Password")
        font_lbl_p = lbl_password.font()
        font_lbl_p.setPointSize(15)
        lbl_password.setFont(font_lbl_p)
        self.h_layout.addWidget((lbl_password), 2, 0)
        self.line_edit_password = QLineEdit()
        self.line_edit_password.setEchoMode(QLineEdit.Password)
        self.line_edit_password.setStyleSheet("background-color: white")
        self.h_layout.addWidget((self.line_edit_password), 2, 1)

        self.h_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("Accedi")
        btn_ok.setDefault(True)


        btn_ok.clicked.connect(self.openHome)
        self.h_layout.addWidget((btn_ok), 3, 0)

        self.setLayout(self.h_layout)
        self.setWindowTitle("HospItaly")
        self.setStyleSheet("QWidget{background-color: lightblue}QPushButton{background-color: cornflowerblue}")

    def identity_check(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()
        if os.path.isfile('listaoperatori/data/list_operatori_salvata.pickle'):
           with open('listaoperatori/data/list_operatori_salvata.pickle', 'rb') as f:
                lista_operatori = pickle.load(f)
                for operatore in lista_operatori:
                    self.controller = ControlloreOperatore(operatore)
                    if  self.controller.get_id_operatore() == username and  self.controller.get_password_operatore() == password:
                        return self.controller.get_ruolo_operatore()

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
            self.go_vista = VistaHomeInfermiere()
            self.go_vista.show()
            self.close()
        elif self.identity_check() == "Medico":
            self.go_vista = VistaHomeMedico()
            self.go_vista.show()
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'Credenziali errate', QMessageBox.Ok, QMessageBox.Ok)
