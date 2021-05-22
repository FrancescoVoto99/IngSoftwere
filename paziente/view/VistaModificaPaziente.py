import datetime
from datetime import datetime, date

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QLabel, QPushButton, QLineEdit, \
    QRadioButton, QDateEdit, QMessageBox
from PyQt5 import QtCore

from operatore.model.Operatore import Operatore

class VistaModificaPaziente(QWidget):
    def __init__(self, paziente, callback):
        super(VistaModificaPaziente, self).__init__()
        self.paziente = paziente
        self.callback = callback
        self.info = {}

        self.label_sesso = QLabel("")
        self.lbl_date = QLabel("")
        self.v_layout = QVBoxLayout()

        self.get_type("Nome", paziente.nome)
        self.get_type("Cognome", paziente.cognome)
        self.get_sesso("Sesso", paziente.sesso)
        self.get_type("Luogo di nascita", paziente.luogodinascita)
        self.get_datanascita("Data di nascita", paziente.datadinascita)
        self.get_type("Codice fiscale", paziente.cf)
        self.get_type("Telefono", paziente.telefono)
        self.get_type("Email", paziente.email)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("modifica")
        btn_ok.clicked.connect(self.modifica_paziente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout((self.v_layout))
        self.setWindowTitle("Modifica Paziente")

    def get_type(self, tipo, set):
        self.v_layout.addWidget(QLabel(tipo))
        current_text = QLineEdit(self)
        current_text.setText(set)
        self.v_layout.addWidget(current_text)
        self.info[tipo] = current_text

    def get_sesso(self, tipo1, tipo2):
        self.v_layout.addWidget(QLabel(tipo1))
        rbtn_maschio = QRadioButton("Maschio")
        rbtn_maschio.toggled.connect(self.sesso_onClicked)
        rbtn_femmina = QRadioButton("Femmina")
        rbtn_femmina.toggled.connect(self.sesso_onClicked)
        self.info[tipo1] = self.label_sesso
        if (tipo2 == "Maschio"):
            rbtn_maschio.setChecked(True)
        else:
            rbtn_femmina.setChecked(True)
        self.v_layout.addWidget(rbtn_maschio)
        self.v_layout.addWidget(rbtn_femmina)
        self.v_layout.addWidget(self.label_sesso)

    def sesso_onClicked(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.label_sesso.setText(rbtn.text())

    def get_datanascita(self,tipo,set):
        self.v_layout.addWidget(QLabel(tipo))
        dateedit = QDateEdit(calendarPopup = True)
        prova=datetime.strptime(set, '%d/%m/%Y')
        dateedit.setDateTime(prova)
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.v_layout.addWidget(dateedit)
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
