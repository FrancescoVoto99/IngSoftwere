from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QSpacerItem, QSizePolicy, QPushButton, \
    QDateEdit, QRadioButton
from PyQt5 import QtCore
from paziente.model.Paziente import Paziente


class VistaInserisciPaziente(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciPaziente, self).__init__()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()
        self.label_sesso = QLabel()

        self.get_type("Nome")
        self.get_type("Cognome")
        self.get_sesso("Sesso")
        self.get_type("Luogo di nascita")
        self.get_datanascita("Data di nascita")
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

    def get_sesso (self, titolo):
        self.v_layout.addWidget(QLabel(titolo))
        rbtn_maschio = QRadioButton("Maschio")
        self.v_layout.addWidget(rbtn_maschio)
        rbtn_maschio.toggled.connect(self.sesso_onClicked)
        rbtn_femmina = QRadioButton("Femmina")
        self.v_layout.addWidget(rbtn_femmina)
        rbtn_femmina.toggled.connect(self.sesso_onClicked)
        self.v_layout.addWidget(self.label_sesso)
        self.info[titolo] = self.label_sesso

    def sesso_onClicked(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.label_sesso.setText(rbtn.text())

    def get_datanascita(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        dateedit = QDateEdit(calendarPopup = True)
        dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.v_layout.addWidget(dateedit)
        self.info[tipo] = dateedit

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
        elif len(telefono) < 8 or len(telefono) > 10:
            QMessageBox.critical(self, 'Errore', "Numero di telefono sbagliato", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_paziente(Paziente(nome, cognome, sesso, luogodinascita, datadinascita, cf, telefono, email))
            self.callback()
            self.close()