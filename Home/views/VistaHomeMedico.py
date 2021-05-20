from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QGridLayout, QPushButton, QSizePolicy, QWidget, QListView, QVBoxLayout, QHBoxLayout

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from listaprenotazioni.views.VistaListaPrenotazioniReparto import VistaListaPrenotazioniReparto


class VistaHomeMedico(QWidget):

    def __init__(self):
        super(VistaHomeMedico, self).__init__()

        layout = QGridLayout()

        layout.addWidget(self.get_button("Lista dei ricoveri", self.go_lista_prenotazioni), 0, 0)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Cardiologia", self.go_prenotazioni_reparto_cardiologia), 0, 1)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Chirurgia", self.go_prenotazioni_reparto_chirurgia), 1, 0)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Oncologia", self.go_prenotazioni_reparto_oncologia), 1, 1)

        self.setLayout(layout)
        self.resize(600, 200)
        self.setWindowTitle("Medico")

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()

    def go_prenotazioni_reparto_cardiologia(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Cardiologia")
        self.vista_lista_prenotazioni_reparti.show()

    def go_prenotazioni_reparto_chirurgia(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Chirurgia")
        self.vista_lista_prenotazioni_reparti.show()

    def go_prenotazioni_reparto_oncologia(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Oncologia")
        self.vista_lista_prenotazioni_reparti.show()

    def get_button(self, titolo, on_click):
        bottone = QPushButton(titolo)
        bottone.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bottone.clicked.connect(on_click)
        return bottone

