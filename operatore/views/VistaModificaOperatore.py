import datetime
from datetime import datetime, date

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QPushButton, QLabel, QLineEdit, QMessageBox, \
    QRadioButton, QDateEdit, QGridLayout
from PyQt5 import QtCore

from operatore.model.Operatore import Operatore

class VistaModificaOperatore(QWidget):
    def __init__(self, operatore, callback):
        super(VistaModificaOperatore, self).__init__()
        self.operatore = operatore
        self.callback = callback
        self.info = {}

        self.lbl_ruolo = QLabel("")
        self.lbl_date = QLabel("")
        self.grid_layout = QGridLayout()

        self.get_type("Nome",operatore.nome, 0, 0, 1, 0)
        self.get_type("Cognome", operatore.cognome, 0, 1, 1, 1)
        self.get_type("Codice fiscale",operatore.cf,  2, 0, 3, 0)
        self.get_datanascita("Data di nascita",operatore.datanascita)
        self.get_type("Luogo di nascita",operatore.luogonascita,  4, 1, 5, 1)
        self.get_type("Email",operatore.email, 2, 1, 3, 1)
        self.get_ruolo("Ruolo",operatore.ruolo)
        self.get_type("Password",operatore.password, 9, 0, 10, 0)

        self.grid_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("modifica")
        btn_ok.setFont(QFont('Verdana', 15))
        btn_ok.clicked.connect(self.modifica_operatore)
        self.grid_layout.addWidget(btn_ok,  10, 1)

        self.setLayout((self.grid_layout))
        self.resize(600, 400)
        self.setWindowTitle("Modifica Operatore")

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

    def get_ruolo(self, tipo ,ruolo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 6, 0)

        rbtn_accettazione = QRadioButton("Amministratore dell'ufficio di accettazione")
        rbtn_accettazione.toggled.connect(self.ruolo_onCliked)

        rbtn_prontosoccorso = QRadioButton("Amministratore del pronto soccorso")
        rbtn_prontosoccorso.toggled.connect(self.ruolo_onCliked)

        rbtn_infermiere = QRadioButton("Infermiere")
        rbtn_infermiere.toggled.connect(self.ruolo_onCliked)

        rbtn_medico = QRadioButton("Medico")
        rbtn_medico.toggled.connect(self.ruolo_onCliked)

        self.info[tipo] = self.lbl_ruolo
        if(ruolo=="Amministratore dell'ufficio di accettazione"):
            rbtn_accettazione.setChecked(True)
        elif (ruolo == "Amministratore del pronto soccorso"):
                rbtn_prontosoccorso.setChecked(True)
        elif (ruolo == "Infermiere"):
            rbtn_infermiere.setChecked(True)
        else:
            rbtn_medico.setChecked(True)
        self.grid_layout.addWidget(rbtn_accettazione, 7, 0)
        self.grid_layout.addWidget(rbtn_prontosoccorso,  8, 0)
        self.grid_layout.addWidget(rbtn_infermiere, 7, 1)
        self.grid_layout.addWidget(rbtn_medico,  8, 1)
        self.grid_layout.addWidget(self.lbl_ruolo, 9, 1)

    def ruolo_onCliked(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.lbl_ruolo.setText(rbtn.text())

    def get_datanascita(self,tipo,set):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 4, 0)
        dateedit = QDateEdit(calendarPopup = True)

        prova=datetime.strptime(set, '%d/%m/%Y')
        dateedit.setDateTime(prova)
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.grid_layout.addWidget(dateedit, 5, 0)
        self.info[tipo] = dateedit

    def modifica_operatore(self):
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
        if nome == "" or cognome == "" or luogonascita == "" or datanascita == "" or cf == "" or ruolo == "" or email == "" or email.find('@') == -1:
            QMessageBox.critical(self, 'Errore', 'Per favore inserisci tutte le informazioni', QMessageBox.Ok, QMessageBox.Ok)
        elif newdate.date() > today:
          QMessageBox.critical(self, 'Errore', 'Per favore inserisci correttamente la data di nascita', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.operatore.nome=nome
            self.operatore.cognome=cognome
            self.operatore.luogonascita = luogonascita
            self.operatore.datanascita = datanascita
            self.operatore.cf=cf
            self.operatore.ruolo= ruolo
            self.operatore.email=email
            self.operatore.password=password
            self.callback()
            self.close()
