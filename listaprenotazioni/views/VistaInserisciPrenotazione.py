import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QPushButton, QWidget, \
    QDateEdit, QRadioButton, QMessageBox
from PyQt5 import QtCore

from listapazienti.controller.ControlloreListaPazienti import ControlloreListaPazienti
from listapazienti.views.VistaInserisciPaziente import VistaInserisciPaziente
from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from listaservizi.controller.ControlloreListaServizi import ControlloreListaServizi
from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__()
        self.controller = controller
        self.controller_pazienti = ControlloreListaPazienti()
        self.callback = callback
        self.info = {}
        #self.lista_pazienti = []
        #if os.path.isfile('listapazienti/data/lista_pazienti.pickle'):
        #    with open('listapazienti/data/lista_pazienti.pickle', 'rb') as f:
         #        self.lista_pazienti = pickle.load(f)

        self.label_reparto = QLabel()
        self.label_paziente = QLabel()

        self.v_layout = QVBoxLayout()

        self.get_data("Data di inizio ricovero")
        self.get_paziente("Paziente")
        self.get_reparto("Reparto")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prenotazione)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle('Nuova Prenotazione')

    def get_paziente(self, titolo):
        self.v_layout.addWidget(QLabel(titolo))
        combo_pazienti = QComboBox()
        for paziente in self.controller_pazienti.get_lista_pazienti():
            combo_pazienti.addItem(paziente.cf)
        self.v_layout.addWidget(combo_pazienti)
        combo_pazienti.activated[str].connect(self.tipo_onClicked)
        self.v_layout.addWidget(self.label_paziente)
        self.info[titolo] = self.label_paziente

    def tipo_onClicked(self, text):
        self.label_paziente.setText(text)

    def get_data(self,tipo):
        self.v_layout.addWidget(QLabel(tipo))
        dateedit = QDateEdit(calendarPopup=True)
        dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.v_layout.addWidget(dateedit)
        self.info[tipo] = dateedit

    def get_reparto(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        rbtn_oncologia = QRadioButton("Reparto di oncologia")
        self.v_layout.addWidget(rbtn_oncologia)
        rbtn_oncologia.toggled.connect(self.reparto_onClicked)
        rbtn_chirurgia = QRadioButton("Reparto di chirurgia")
        self.v_layout.addWidget(rbtn_chirurgia)
        rbtn_chirurgia.toggled.connect(self.reparto_onClicked)
        rbtn_cardiologia = QRadioButton("Reparto di cardiologia")
        self.v_layout.addWidget(rbtn_cardiologia)
        rbtn_cardiologia.toggled.connect(self.reparto_onClicked)
        self.v_layout.addWidget(self.label_reparto)
        self.info[tipo] = self.label_reparto

    def reparto_onClicked(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.label_reparto.setText(rbtn.text())

    def add_prenotazione(self):

        controller_servizi=ControlloreListaServizi()
        data = self.info["Data di inizio ricovero"].text()
        paziente = self.controller_pazienti.get_paziente_by_cf(self.info["Paziente"].text())
        stringa_servizio=self.info["Reparto"].text().split()
        servizio = controller_servizi.get_servizio_by_reparto(stringa_servizio[len(stringa_servizio)-1])
        if data == "" or paziente == "" or servizio == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(Prenotazione((paziente.cognome+paziente.nome).lower(), paziente, servizio, data))
            servizio.prenota()
            controller_servizi.save_data()
            self.callback()
            self.close()
