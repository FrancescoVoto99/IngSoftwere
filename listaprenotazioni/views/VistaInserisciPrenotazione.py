import os
import pickle
from datetime import datetime, date, timedelta

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QPushButton, QWidget, \
    QDateEdit, QRadioButton, QMessageBox, QGridLayout
from PyQt5 import QtCore

from listapazienti.controller.ControlloreListaPazienti import ControlloreListaPazienti
from listapazienti.views.VistaInserisciPaziente import VistaInserisciPaziente
from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
#from listaricoveri.controller.ControlloreListaRicoveri import ControlloreListaRicoveri
from listaservizi.controller.ControlloreListaServizi import ControlloreListaServizi
from prenotazione.model.Prenotazione import Prenotazione
from servizio.controller.ControlloreServizio import ControlloreServizio


class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__()
        self.controller = controller
        self.controller_pazienti = ControlloreListaPazienti()
        self.callback = callback
        self.info = {}

        self.grid_layout = QGridLayout()

        self.lista_tipi = ["ricovero", "ricovero di emergenza"]
        self.label_reparto = QLabel()
        self.label_paziente = QLabel()
        self.label_tipo = QLabel()

        self.get_data("Data di inizio ricovero")
        self.get_data_fine("Data di fine ricovero")
        self.get_paziente("Paziente")
        self.get_reparto("Reparto")
        self.get_tipo_ricovero("Tipo di ricovero")

        self.grid_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.setFont(QFont('Verdana', 15))
        btn_ok.clicked.connect(self.add_prenotazione)
        self.grid_layout.addWidget(btn_ok, 9, 1)

        self.setLayout(self.grid_layout)
        self.resize(600, 400)
        self.setWindowTitle('Nuova Prenotazione')
        self.setStyleSheet("QWidget{background-color: #ffffac} QPushButton{background-color: gold}")

    def get_paziente(self, titolo):
        lbl = QLabel(titolo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 2, 0)
        combo_pazienti = QComboBox()
        combo_pazienti.setStyleSheet("background-color: white")
        for paziente in self.controller_pazienti.get_lista_pazienti():
            combo_pazienti.addItem(paziente.cf)
        self.grid_layout.addWidget(combo_pazienti, 3, 0)
        combo_pazienti.activated[str].connect(self.paziente_onClicked)
        self.grid_layout.addWidget(self.label_paziente, 4, 0)
        self.info[titolo] = self.label_paziente

    def paziente_onClicked(self, text):
        self.label_paziente.setText(text)

    def get_data_fine(self,tipo):
        lbl = QLabel(tipo+" (opzionale)")
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 0, 1)
        dateedit = QDateEdit(calendarPopup=True)
        dateedit.setStyleSheet("background-color: white")
        dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.grid_layout.addWidget(dateedit, 1, 1)
        self.info[tipo] = dateedit

    def get_data(self,tipo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 0, 0)
        dateedit = QDateEdit(calendarPopup=True)
        dateedit.setStyleSheet("background-color: white")
        dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.grid_layout.addWidget(dateedit, 1, 0)
        self.info[tipo] = dateedit

    def get_reparto(self, tipo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 5, 0)
        rbtn_oncologia = QRadioButton("Reparto di oncologia")
        self.grid_layout.addWidget(rbtn_oncologia, 6, 0)
        rbtn_oncologia.toggled.connect(self.reparto_onClicked)
        rbtn_chirurgia = QRadioButton("Reparto di chirurgia")
        self.grid_layout.addWidget(rbtn_chirurgia, 7, 0)
        rbtn_chirurgia.toggled.connect(self.reparto_onClicked)
        rbtn_cardiologia = QRadioButton("Reparto di cardiologia")
        self.grid_layout.addWidget(rbtn_cardiologia, 8, 0)
        rbtn_cardiologia.toggled.connect(self.reparto_onClicked)
        rbtn_medicina = QRadioButton("Reparto di medicina")
        self.grid_layout.addWidget(rbtn_medicina, 6, 1)
        rbtn_medicina.toggled.connect(self.reparto_onClicked)
        rbtn_riabilitazione = QRadioButton("Reparto di riabilitazione")
        self.grid_layout.addWidget(rbtn_riabilitazione, 7, 1)
        rbtn_riabilitazione.toggled.connect(self.reparto_onClicked)
        self.grid_layout.addWidget(self.label_reparto, 9, 0)
        self.info[tipo] = self.label_reparto

    def reparto_onClicked(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.label_reparto.setText(rbtn.text())

    def get_tipo_ricovero(self, tipo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.grid_layout.addWidget(lbl, 2, 1)
        combo_ricoveri = QComboBox()
        combo_ricoveri.setStyleSheet("background-color: white")
        for ricovero in self.lista_tipi:
            combo_ricoveri.addItem(ricovero)
        self.grid_layout.addWidget(combo_ricoveri, 3, 1)
        combo_ricoveri.activated[str].connect(self.tipo_onClicked)
        self.grid_layout.addWidget(self.label_tipo, 4, 1)
        self.info[tipo] = self.label_tipo

    def tipo_onClicked(self, text):
        self.label_tipo.setText(text)

    def check_prenotazione(self, cf, datainizio, datafine):
        for element in self.controller.get_lista_delle_prenotazioni():
            if element.paziente.cf == cf and (datetime.strptime(element.datafine,'%d/%m/%Y') > datetime.strptime(datainizio,'%d/%m/%Y') or datetime.strptime(datafine,'%d/%m/%Y') < datetime.strptime(element.data,'%d/%m/%Y')):
                return True

    def add_prenotazione(self):
        controller_servizi = ControlloreListaServizi()
        datainizio = self.info["Data di inizio ricovero"].text()
        datafine = self.info["Data di fine ricovero"].text()
        date_required = date.today() + timedelta(days=7)
        newdate = datetime.strptime(datainizio, '%d/%m/%Y')
        finedata = datetime.strptime(datafine, '%d/%m/%Y')
        paziente = self.controller_pazienti.get_paziente_by_cf(self.info["Paziente"].text())
        stringa_servizio = self.info["Reparto"].text().split()
        tipo_ricovero = self.info["Tipo di ricovero"].text()
        servizio = controller_servizi.get_servizio_by_reparto_and_tipo(stringa_servizio[len(stringa_servizio)-1], tipo_ricovero, self.controller, datainizio, datafine)
        if self.check_prenotazione(paziente.cf, datainizio, datafine) == True:
                QMessageBox.critical(self, 'Errore', 'Il paziente ' + paziente.nome + ' ' + paziente.cognome + ' è già ricoverato in quel periodo in un altro reparto', QMessageBox.Ok, QMessageBox.Ok)
        elif datainizio == "" or paziente == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        elif servizio == None:
                QMessageBox.critical(self, 'Errore', 'Tutti i servizi in questo reparto sono occupati nelle date inserite, selezionare un posto di emergenza o modificare le date',
                  QMessageBox.Ok, QMessageBox.Ok)
        elif newdate.date() <= date_required and tipo_ricovero != "ricovero di emergenza":
                QMessageBox.critical(self, 'Errore', "Bisogna prenotare almeno una settimana prima", QMessageBox.Ok, QMessageBox.Ok)
        elif newdate.date() > finedata.date():
                QMessageBox.critical(self, 'Errore', "Inserire correttamente le date", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(Prenotazione((paziente.cognome + paziente.nome).lower(), paziente, servizio, datainizio, datafine))
            servizio.prenota(newdate.date())
            servizio.is_prenotato()
            controller_servizi.save_data()
            self.callback()
            self.close()


