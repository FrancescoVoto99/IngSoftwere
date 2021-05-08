import datetime
from datetime import datetime, date

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QPushButton, QLabel, QLineEdit, QMessageBox, \
    QRadioButton, QDateEdit
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
        self.v_layout = QVBoxLayout()

        self.get_type("Nome")
        self.get_type("Cognome")
        self.get_type("Codice fiscale")
        self.get_datanascita("Data di nascita")
        self.get_type("Luogo di nascita")
        self.get_type("Email")
        self.get_ruolo("Ruolo")
        self.get_type("Password")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_operatore)
        self.v_layout.addWidget(btn_ok)

        self.setLayout((self.v_layout))
        self.setWindowTitle("Nuovo Operatore")

    def get_type(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text = QLineEdit(self)
        self.v_layout.addWidget(current_text)
        self.info[tipo] = current_text

    def get_ruolo(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        rbtn_accettazione = QRadioButton("Amministratore dell'ufficio di accettazione")
        self.v_layout.addWidget(rbtn_accettazione)
        rbtn_accettazione.toggled.connect(self.ruolo_onCliked)
        rbtn_prontosoccorso = QRadioButton("Amministratore del pronto soccorso")
        self.v_layout.addWidget(rbtn_prontosoccorso)
        rbtn_prontosoccorso.toggled.connect(self.ruolo_onCliked)
        rbtn_infermiere = QRadioButton("Infermiere")
        self.v_layout.addWidget(rbtn_infermiere)
        rbtn_infermiere.toggled.connect(self.ruolo_onCliked)
        rbtn_medico = QRadioButton("Medico")
        self.v_layout.addWidget(rbtn_medico)
        rbtn_medico.toggled.connect(self.ruolo_onCliked)
        self.v_layout.addWidget(self.lbl_ruolo)
        self.info[tipo] = self.lbl_ruolo

    def ruolo_onCliked(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.lbl_ruolo.setText(rbtn.text())

    def get_datanascita(self,tipo):
        self.v_layout.addWidget(QLabel(tipo))
        dateedit = QDateEdit(calendarPopup = True)
        dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.v_layout.addWidget(dateedit)
        self.info[tipo] = dateedit

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
        if nome == "" or cognome == "" or luogonascita == "" or datanascita == "" or cf == "" or ruolo == "" or email == "":
            QMessageBox.critical(self, 'Errore', 'Per favore inserisci tutte le informazioni', QMessageBox.Ok, QMessageBox.Ok)
        elif newdate.date() > today:
            QMessageBox.critical(self, 'Errore', 'Per favore inserisci correttamente la data di nascita', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_operatore(Operatore((nome+cognome).lower(), nome, cognome, cf, datanascita, luogonascita, email, ruolo, password))
            self.callback()
            self.close()

   