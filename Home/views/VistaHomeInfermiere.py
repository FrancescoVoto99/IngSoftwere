from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from listaprenotazioni.views.VistaListaPrenotazioniReparto import VistaListaPrenotazioniReparto

# Classe responsabile della gestione dell'interfaccia utente
# principale dell'infermiere

class VistaHomeInfermiere(QWidget):

    def __init__(self, parent = None):
        super(VistaHomeInfermiere, self).__init__(parent)

        layout = QGridLayout()

        layout.addWidget(self.get_button("Lista dei ricoveri", self.go_lista_prenotazioni), 0, 0)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Cardiologia", self.go_prenotazioni_reparto_cardiologia),0, 1)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Chirurgia", self.go_prenotazioni_reparto_chirurgia), 1,0)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Oncologia", self.go_prenotazioni_reparto_oncologia),  1,1)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Medicina", self.go_prenotazioni_reparto_medicina), 2,0)
        layout.addWidget(self.get_button("Visualizza pazienti ricoverati in Riabilitazione", self.go_prenotazioni_reparto_riabilitazione), 2,1)

        self.setLayout(layout)
        self.resize(800, 400)
        self.setWindowTitle("Infermiere")
        self.setStyleSheet("QWidget{background-color: lightgreen} QPushButton{background-color: mediumseagreen; color: black}")

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni(False, False)
        self.vista_lista_prenotazioni.showMaximized()

    def go_prenotazioni_reparto_cardiologia(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Cardiologia", False)
        self.vista_lista_prenotazioni_reparti.showMaximized()

    def go_prenotazioni_reparto_chirurgia(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Chirurgia", False)
        self.vista_lista_prenotazioni_reparti.showMaximized()

    def go_prenotazioni_reparto_oncologia(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Oncologia", False)
        self.vista_lista_prenotazioni_reparti.showMaximized()

    def go_prenotazioni_reparto_medicina(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Medicina", False)
        self.vista_lista_prenotazioni_reparti.showMaximized()

    def go_prenotazioni_reparto_riabilitazione(self):
        self.vista_lista_prenotazioni_reparti = VistaListaPrenotazioniReparto("Riabilitazione", False)
        self.vista_lista_prenotazioni_reparti.showMaximized()

    def get_button(self, titolo, on_click):
        bottone = QPushButton(titolo)
        bottone.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = bottone.font()
        font.setPointSize(15)
        font.setBold(True)
        bottone.setFont(font)
        bottone.clicked.connect(on_click)

        return bottone


