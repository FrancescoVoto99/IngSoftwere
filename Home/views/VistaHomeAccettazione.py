from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listaoperatori.views.VistaListaOperatori import VistaListaOperatori
from listapazienti.views.VistaListaPazienti import VistaListaPazienti
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from listaservizi.views.VistaListaServizi import VistaListaServizi

# Classe responsabile della gestione dell'interfaccia utente
# principale dell'amministratore dell'ufficio di
# accettazione

class VistaHomeAccettazione(QWidget):
    def __init__(self, parent=None):
        super(VistaHomeAccettazione, self).__init__(parent)
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_button("Lista Servizi", self.go_lista_servizi, "background-color: plum"), 0, 0)
        grid_layout.addWidget(self.get_button("Lista Pazienti", self.go_lista_pazienti, "background-color: lightpink"), 0, 1)
        grid_layout.addWidget(self.get_button("Lista Operatori", self.go_lista_operatori, "background-color: lightgreen"), 1, 0)
        grid_layout.addWidget(self.get_button("Lista Prenotazioni", self.go_lista_prenotazioni, "background-color: #ffffac"), 1, 1)

        self.setLayout(grid_layout)
        self.resize(400, 400)
        self.setWindowTitle("Amministratore dell'ufficio di accettazione")
        self.setStyleSheet("background-color: lightblue")

    def go_lista_servizi(self):
        self.vista_lista_servizi = VistaListaServizi()
        self.vista_lista_servizi.showMaximized()

    def go_lista_pazienti(self):
        self.vista_lista_pazienti = VistaListaPazienti(False)
        self.vista_lista_pazienti.showMaximized()

    def go_lista_operatori(self):
        self.vista_lista_operatori = VistaListaOperatori()
        self.vista_lista_operatori.showMaximized()

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni(True, True)
        self.vista_lista_prenotazioni.showMaximized()

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
