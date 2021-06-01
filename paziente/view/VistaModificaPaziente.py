import datetime
from datetime import datetime, date

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QLabel, QPushButton, QLineEdit, \
    QRadioButton, QDateEdit, QMessageBox, QGridLayout
from PyQt5 import QtCore

from operatore.model.Operatore import Operatore
from paziente.Controller.ControllorePaziente import ControllorePaziente


class VistaModificaPaziente(QWidget):
    def __init__(self, paziente, callback):
        super(VistaModificaPaziente, self).__init__()
        self.paziente = paziente
        self.controller = ControllorePaziente(paziente)
        self.callback = callback
        self.info = {}

        self.label_sesso = QLabel("")
        self.lbl_date = QLabel("")
        self.grid_layout = QGridLayout()

        self.get_type("Nome", self.controller.get_nome_paziente() , 0, 0, 1, 0)
        self.get_type("Cognome", self.controller.get_cognome_paziente(), 0, 1, 1, 1)
        self.get_sesso("Sesso", self.controller.get_sesso_paziente())
        self.get_type("Luogo di nascita", self.controller.get_luogodinascita_paziente(), 5, 0, 6, 0)
        self.get_datanascita("Data di nascita", self.controller.get_datadinascita_paziente())
        self.get_type("Codice fiscale", self.controller.get_cf_paziente(), 2, 1, 3, 1)
        self.get_type("Telefono", self.controller.get_telefono_paziente(), 7, 0, 8, 0)
        self.get_type("Email", self.controller.get_email_paziente(), 7, 1, 8, 1)

        self.grid_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("modifica")
        btn_ok.setFont(QFont('Verdana', 15))
        btn_ok.clicked.connect(self.modifica_paziente)
        self.grid_layout.addWidget(btn_ok, 9, 0)

        self.setLayout(self.grid_layout)
        self.resize(600, 400)
        self.setWindowTitle("Modifica Paziente")

    def get_type(self, tipo, set, rl, cl, re, ce):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, rl, cl)
        current_text = QLineEdit(self)
        current_text.setText(set)
        self.grid_layout.addWidget(current_text, re, ce)
        self.info[tipo] = current_text

    def get_sesso(self, tipo1, tipo2):
        lbl = QLabel(tipo1)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 2, 0)
        rbtn_maschio = QRadioButton("Maschio")
        rbtn_maschio.toggled.connect(self.sesso_onClicked)
        rbtn_femmina = QRadioButton("Femmina")
        rbtn_femmina.toggled.connect(self.sesso_onClicked)
        self.info[tipo1] = self.label_sesso
        if (tipo2 == "Maschio"):
            rbtn_maschio.setChecked(True)
        else:
            rbtn_femmina.setChecked(True)
        self.grid_layout.addWidget(rbtn_maschio,3, 0)
        self.grid_layout.addWidget(rbtn_femmina, 4, 0)
        self.grid_layout.addWidget(self.label_sesso)

    def sesso_onClicked(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.label_sesso.setText(rbtn.text())

    def get_datanascita(self,tipo,set):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 5, 1)
        dateedit = QDateEdit(calendarPopup = True)
        prova=datetime.strptime(set, '%d/%m/%Y')
        dateedit.setDateTime(prova)
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.grid_layout.addWidget(dateedit, 6, 1)
        self.info[tipo] = dateedit

    def modifica_paziente(self):
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        sesso = self.info["Sesso"].text()
        luogodinascita = self.info["Luogo di nascita"].text()
        datadinascita = self.info["Data di nascita"].text()
        cf = self.info["Codice fiscale"].text()
        telefono = self.info["Telefono"].text()
        email = self.info["Email"].text()
        today = date.today()
        newdate = datetime.strptime(datadinascita, '%d/%m/%Y')
        if nome == "" or cognome == "" or sesso == "" or luogodinascita == "" or datadinascita == "" or cf == "" or telefono == "" or email == "":
            QMessageBox.critical(self, 'Errore', 'Per favore inserisci tutte le informazioni', QMessageBox.Ok, QMessageBox.Ok)
        elif newdate.date() > today:
          QMessageBox.critical(self, 'Errore', 'Per favore inserisci correttamente la data di nascita', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.paziente.nome = nome
            self.paziente.cognome = cognome
            self.paziente.sesso = sesso
            self.paziente.luogodinascita = luogodinascita
            self.paziente.datadinascita = datadinascita
            self.paziente.cf = cf
            self.paziente.telefono = telefono
            self.paziente.email = email
            if self.callback!=None:
                self.callback()
            self.close()
