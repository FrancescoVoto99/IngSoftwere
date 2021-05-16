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
            self.add_to_lista_ricoveri(paziente)
            v_layout.addWidget(QLabel("Attualmente il paziente è ricoverato"))
            # v_layout.addWidget(QLabel(self.controller.get_finericovero_string()))
        else:
            v_layout.addWidget(QLabel("Paziente non ricoverato"))
            v_layout.addWidget(QLabel("Aggiungi una nuova data di fine ricovero (dd/MM/yyyy)"))
            self.text_finericovero = QLineEdit()
            v_layout.addWidget(self.text_finericovero)
            btn_inserisci = QPushButton("Aggiungi")
            btn_inserisci.clicked.connect(self.add_ricovero_click)
            v_layout.addWidget(btn_inserisci)

        self.setLayout(v_layout)

   # def add_to_lista_ricoveri(self, ricovero):
    #    controller_lista = ControlloreListaRicoveri()
       # controller_lista.aggiungi_ricovero(ricovero)

    def add_ricovero_click(self):
        try:
            date = datetime.strptime(self.text_finericovero.text(), '%d/%m/%Y')
            self.callback_inserisci_ricovero(Ricovero(date.timestamp()))
            self.close()
        except:
            QMessageBox.critical(self, 'Errore', 'Inserisci la data nel formato richiesto: dd/MM/yyyy', QMessageBox.Ok, QMessageBox.Ok)