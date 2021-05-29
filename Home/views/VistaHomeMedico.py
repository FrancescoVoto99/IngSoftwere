from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QPalette
from PyQt5.QtWidgets import QGridLayout, QPushButton, QSizePolicy, QWidget, QListView, QVBoxLayout, QHBoxLayout

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from listaprenotazioni.views.VistaListaPrenotazioniReparto import VistaListaPrenotazioniReparto


class VistaHomeMedico(QWidget):

    def __init__(self):
        super(VistaHomeMedico, self).__init__()

        layout = QGridLayout()

        layout.addWidget(self.get_button("Lista dei ricoveri", self.go_lista_prenotazioni, "background-color: #cfc7e5"), 0, 0)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Cardiologia", self.go_prenotazioni_reparto_cardiologia, "background-color: #cfc7e5"), 0, 1)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Chirurgia", self.go_prenotazioni_reparto_chirurgia, "background-color: #cfc7e5"), 1, 0)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Oncologia", self.go_prenotazioni_reparto_oncologia, "background-color: #cfc7e5"), 1, 1)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Medicina", self.go_prenotazioni_reparto_medicina, "background-color: #cfc7e5"), 2,0)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Riabilitazione", self.go_prenotazioni_reparto_riabilitazione, "background-color: #cfc7e5"), 2,1)

        self.setLayout(layout)
        self.resize(800, 400)
        self.setWindowTitle("Medico")

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni(False, True)
        self.vista_lista_prenotazioni.show()

    def go_prenotazioni_reparto_cardiologia(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Cardiologia", True)
        self.vista_lista_prenotazioni_reparti.show()

    def go_prenotazioni_reparto_chirurgia(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Chirurgia", True)
        self.vista_lista_prenotazioni_reparti.show()

    def go_prenotazioni_reparto_oncologia(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Oncologia", True)
        self.vista_lista_prenotazioni_reparti.show()

    def go_prenotazioni_reparto_medicina(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Medicina", True)
        self.vista_lista_prenotazioni_reparti.show()

    def go_prenotazioni_reparto_riabilitazione(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Riabilitazione", True)
        self.vista_lista_prenotazioni_reparti.show()

    def get_button(self, titolo, on_click, colore):
        palette = QPalette()
        palette.setColor(QPalette.ButtonText, Qt.black)
        bottone = QPushButton(titolo)
        bottone.setPalette(palette)
        bottone.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = bottone.font()
        font.setPointSize(15)
        font.setBold(True)
        bottone.setFont(font)
        bottone.clicked.connect(on_click)
        bottone.setStyleSheet(colore)
        return bottone

