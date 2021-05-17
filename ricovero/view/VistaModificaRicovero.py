import datetime

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QMessageBox, QDateEdit

from ricovero.controller.ControlloreRicovero import ControlloreRicovero
from ricovero.model.Ricovero import Ricovero


class VistaModificaRicovero(QWidget):

    def __init__(self, ricovero, call_back_inserisci_ricovero):
        super(VistaModificaRicovero, self).__init__()

        self.controller = ControlloreRicovero(ricovero)
        self.callback_inserisci_ricovero = call_back_inserisci_ricovero

        self.h_layout = QHBoxLayout()

        self.h_layout.addWidget(QLabel("Aggiungi una nuova data di fine ricovero"))
        self.get_data_fine()
        btn_inserisci = QPushButton("Aggiungi")
        btn_inserisci.clicked.connect(self.add_ricovero_click)
        self.h_layout.addWidget(btn_inserisci)

        self.setLayout(self.h_layout)
        self.setWindowTitle("Inserire la data di fine ricovero")

    def add_ricovero_click(self):
        try:
            date = datetime.strptime(self.text_finericovero.text(), '%d/%m/%Y')
            self.callback_inserisci_ricovero(Ricovero(date.timestamp()))
            self.close()
        except:
            QMessageBox.critical(self, 'Errore', 'Inserisci correttamente la data', QMessageBox.Ok, QMessageBox.Ok)

    def get_data_fine(self):
        dateedit = QDateEdit(calendarPopup = True)
        dateedit.setDateTime(QtCore.QDateTime.currentDateTime())
        dateedit.setDisplayFormat('dd/MM/yyyy')
        self.h_layout.addWidget(dateedit)

