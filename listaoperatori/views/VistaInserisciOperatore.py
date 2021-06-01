import datetime
from datetime import datetime, date

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QPushButton, QLabel, QLineEdit, QMessageBox, \
    QRadioButton, QDateEdit, QGridLayout
from PyQt5 import QtCore

from operatore.model.Operatore import Operatore

class VistaInserisciOperatore(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciOperatore, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.lbl_ruolo = QLabel("")
        self.lbl_date = QLabel("")
        self.grid_layout = QGridLayout()

        self.get_type("Nome", 0, 0, 1, 0)
        self.get_type("Cognome", 0, 1, 1, 1)
        self.grid_layout.addItem(QSpacerItem(10, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.get_type("Codice fiscale", 2, 0, 3, 0)
        self.get_type("Email", 2, 1, 3, 1)
        self.grid_layout.addItem(QSpacerItem(10, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.get_datanascita("Data di nascita")
        self.get_type("Luogo di nascita", 4, 1, 5, 1)
        self.grid_layout.addItem(QSpacerItem(10, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.get_ruolo("Ruolo")
        self.grid_layout.addItem(QSpacerItem(10, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.get_type("Password", 9, 0, 10, 0)
        self.grid_layout.addItem(QSpacerItem(10, 30, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.setFont(QFont('Verdana', 15))
        btn_ok.clicked.connect(self.add_operatore)
        self.grid_layout.addWidget(btn_ok, 10, 1)

        self.setLayout(self.grid_layout)
        self.resize(600, 400)
        self.setWindowTitle("Nuovo Operatore")
        self.setStyleSheet("background-color: #caffca")

    def get_type(self, tipo, rl, cl, re, ce):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, rl, cl)
        current_text = QLineEdit(self)
        current_text.setStyleSheet("background-color: white")
        self.grid_layout.addWidget(current_text, re, ce)
        self.info[tipo] = current_text

    def get_ruolo(self, tipo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 6, 0)
        rbtn_accettazione = QRadioButton("Amministratore dell'ufficio di accettazione")
        self.grid_layout.addWidget(rbtn_accettazione, 7, 0)
        rbtn_accettazione.toggled.connect(self.ruolo_onClicked)
        rbtn_prontosoccorso = QRadioButton("Amministratore del pronto soccorso")
        self.grid_layout.addWidget(rbtn_prontosoccorso, 8, 0)
        rbtn_prontosoccorso.toggled.connect(self.ruolo_onClicked)
        rbtn_infermiere = QRadioButton("Infermiere")
        self.grid_layout.addWidget(rbtn_infermiere, 7, 1)
        rbtn_infermiere.toggled.connect(self.ruolo_onClicked)
        rbtn_medico = QRadioButton("Medico")
        self.grid_layout.addWidget(rbtn_medico, 8, 1)
        rbtn_medico.toggled.connect(self.ruolo_onClicked)
        self.grid_layout.addWidget(self.lbl_ruolo, 9, 1)
        self.info[tipo] = self.lbl_ruolo

    def ruolo_onClicked(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.lbl_ruolo.setText(rbtn.text())

    def get_datanascita(self,tipo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 4, 0)
        dateedit = QDateEdit(calendarPopup = True)
        dateedit.setStyleSheet("background-color: white")
        dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.grid_layout.addWidget(dateedit, 5, 0)
        self.info[tipo] = dateedit

    def check_email(self, text):
        if text.find('@') == -1:
            return True
        else:
            return False

    def add_operatore(self):
        nome = self.info["Nome"].text()
        cognome = self.info["Cognome"].text()
        cf = self.info["Codice fiscale"].text()
        datanascita = self.info["Data di nascita"].text()
        luogonascita = self.info["Luogo di nascita"].text()
        email = self.info["Email"].text()
        ruolo = self.info["Ruolo"].text()
        password = self.info["Password"].text()
        today = date.today()
        newdate = datetime.strptime(datanascita, '%d/%m/%Y')
        if nome == "" or cognome == "" or luogonascita == "" or datanascita == "" or cf == "" or ruolo == "" or email == "" :
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni', QMessageBox.Ok, QMessageBox.Ok)
        elif self.check_email(email):
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci correttamente l'email", QMessageBox.Ok, QMessageBox.Ok)
        elif newdate.date() > today:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci correttamente la data di nascita', QMessageBox.Ok, QMessageBox.Ok)
        elif self.controller.check_cf(cf):
            QMessageBox.critical(self, 'Errore', "L'operatore è già presente nella lista", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_operatore(Operatore((nome+cognome).lower(), nome, cognome, cf, datanascita, luogonascita, email, ruolo, password))
            self.callback()
            self.close()

   