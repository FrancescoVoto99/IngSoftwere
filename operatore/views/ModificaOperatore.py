import datetime
from datetime import datetime, date

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QPushButton, QLabel, QLineEdit, QMessageBox, \
    QRadioButton, QDateEdit
from PyQt5 import QtCore

from operatore.model.Operatore import Operatore

class ModificaOperatore(QWidget):

    def __init__(self, operatore, callback):
        super(ModificaOperatore, self).__init__()
        self.operatore = operatore
        self.callback = callback
        self.info = {}

        self.lbl_ruolo = QLabel("")
        self.lbl_date = QLabel("")
        self.v_layout = QVBoxLayout()

        self.get_type("Nome",operatore.nome)
        self.get_type("Cognome", operatore.cognome)
        self.get_type("Codice fiscale",operatore.cf)
        self.get_datanascita("Data di nascita",operatore.datanascita)
        self.get_type("Luogo di nascita",operatore.luogonascita)
        self.get_type("Email",operatore.email)
        self.get_ruolo("Ruolo",operatore.ruolo)
        self.get_type("Password",operatore.password)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("modifica")
        btn_ok.clicked.connect(self.modifica_operatore)
        self.v_layout.addWidget(btn_ok)

        self.setLayout((self.v_layout))
        self.setWindowTitle("Modifica Operatore")

    def get_type(self, tipo, set ):
        self.v_layout.addWidget(QLabel(tipo))
        current_text = QLineEdit(self)
        current_text.setText(set)
        self.v_layout.addWidget(current_text)
        self.info[tipo] = current_text

    def get_ruolo(self, tipo ,ruolo):
        self.v_layout.addWidget(QLabel(tipo))
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
        self.v_layout.addWidget(rbtn_accettazione)
        self.v_layout.addWidget(rbtn_prontosoccorso)
        self.v_layout.addWidget(rbtn_infermiere)
        self.v_layout.addWidget(rbtn_medico)
        self.v_layout.addWidget(self.lbl_ruolo)

    def ruolo_onCliked(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.lbl_ruolo.setText(rbtn.text())

    def get_datanascita(self,tipo,set):
        self.v_layout.addWidget(QLabel(tipo))
        dateedit = QDateEdit(calendarPopup = True)

        prova=datetime.strptime(set, '%d/%m/%Y')
        dateedit.setDateTime(prova)
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.v_layout.addWidget(dateedit)
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
        if nome == "" or cognome == "" or luogonascita == "" or datanascita == "" or cf == "" or ruolo == "" or email == "":
            QMessageBox.critical(self, 'Errore', 'Per favore inserisci tutte le informazioni', QMessageBox.Ok, QMessageBox.Ok)
   #     elif newdate.date() > today:
    #        QMessageBox.critical(self, 'Errore', 'Per favore inserisci correttamente la data di nascita', QMessageBox.Ok, QMessageBox.Ok)
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
