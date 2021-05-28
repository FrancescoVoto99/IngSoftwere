from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QSpacerItem, QSizePolicy, QPushButton, \
    QDateEdit, QRadioButton, QGridLayout
from PyQt5 import QtCore
from paziente.model.Paziente import Paziente


class VistaInserisciPaziente(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciPaziente, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.grid_layout = QGridLayout()
        self.label_sesso = QLabel()

        self.get_type("Nome", 0, 0, 1, 0)
        self.get_type("Cognome", 0, 1, 1, 1)
        self.get_sesso("Sesso")
        self.get_type("Luogo di nascita", 5, 0, 6, 0)
        self.get_datanascita("Data di nascita")
        self.get_type("Codice fiscale", 2, 1, 3, 1)
        self.get_type("Telefono", 7, 0, 8, 0)
        self.get_type("Email", 7, 1, 8, 1)

        self.grid_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.setFont(QFont('Verdana', 15))
        btn_ok.clicked.connect(self.add_paziente)
        self.grid_layout.addWidget(btn_ok, 9, 0)

        self.setLayout((self.grid_layout))
        self.resize(600, 400)
        self.setWindowTitle("Nuovo Paziente")

    def get_type (self, tipo, rl, cl, re, ce):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, rl, cl)
        current_text = QLineEdit(self)
        self.grid_layout.addWidget(current_text, re, ce)
        self.info[tipo] = current_text

    def get_sesso (self, titolo):
        lbl = QLabel(titolo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 2, 0)
        rbtn_maschio = QRadioButton("Maschio")
        self.grid_layout.addWidget(rbtn_maschio,3, 0)
        rbtn_maschio.toggled.connect(self.sesso_onClicked)
        rbtn_femmina = QRadioButton("Femmina")
        self.grid_layout.addWidget(rbtn_femmina, 4, 0)
        rbtn_femmina.toggled.connect(self.sesso_onClicked)
        self.grid_layout.addWidget(self.label_sesso)
        self.info[titolo] = self.label_sesso

    def sesso_onClicked(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.label_sesso.setText(rbtn.text())

    def get_datanascita(self, tipo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 5, 1)
        dateedit = QDateEdit(calendarPopup = True)
        dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.grid_layout.addWidget(dateedit, 6, 1)
        self.info[tipo] = dateedit

    def check_email(self, text):
        if text.find('@') == -1:
            return True
        else:
            return False

    def add_paziente(self):
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        sesso = self.info["Sesso"]. text()
        luogodinascita = self.info["Luogo di nascita"].text()
        datadinascita = self.info["Data di nascita"].text()
        cf = self.info["Codice fiscale"].text()
        telefono = self.info["Telefono"].text()
        email = self.info["Email"].text()
        if nome == "" or cognome == "" or sesso == "" or luogodinascita == "" or datadinascita == "" or cf == "" or telefono == "" or email == "":
            QMessageBox.critical(self, 'Errore', 'Per favore inserisci tutte le informazioni', QMessageBox.Ok, QMessageBox.Ok)
        elif self.controller.check_cf(cf):
            QMessageBox.critical(self, 'Errore', "Il paziente è già stato inserito nella lista", QMessageBox.Ok, QMessageBox.Ok)
        elif self.check_email(email):
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci correttamente l'email", QMessageBox.Ok,QMessageBox.Ok)
        elif len(telefono) < 8 or len(telefono) > 10:
            QMessageBox.critical(self, 'Errore', "Numero di telefono sbagliato", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_paziente(Paziente(nome, cognome, sesso, luogodinascita, datadinascita, cf, telefono, email))
            self.callback()
            self.close()