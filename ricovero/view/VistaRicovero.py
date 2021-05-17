from datetime import datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

#from listaricoveri.controller.ControlloreListaRicoveri import ControlloreListaRicoveri
from ricovero.controller.ControlloreRicovero import ControlloreRicovero
from ricovero.model.Ricovero import Ricovero

class VistaRicovero(QWidget):

    def __init__(self, ricovero, callback_inserici_ricovero, paziente):
        super(VistaRicovero, self).__init__()
        self.controller = ControlloreRicovero(ricovero)
        self.callback_inserisci_ricovero = callback_inserici_ricovero

        v_layout = QVBoxLayout()
        if self.controller.is_ricoverato(paziente):
            v_layout.addWidget(QLabel("Attualmente il paziente è ricoverato"))
        else:
            v_layout.addWidget(QLabel("Paziente non ricoverato"))

        self.setLayout(v_layout)
