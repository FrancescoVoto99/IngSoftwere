from PyQt5.QtWidgets import QGridLayout, QPushButton, QSizePolicy, QWidget

from listapazienti.views.VistaListaPazienti import VistaListaPazienti
from listaprenotazioni.views.VistaListaPrenotazioniEmergenza import VistaListaPrenotazioniEmergenza
from listaservizi.views.VistaListaServiziEmergenza import VistaListaServiziEmergenza


class VistaHomeProntoSoccorso(QWidget):
    
    def __init__(self, parent = None):
        super(VistaHomeProntoSoccorso, self).__init__(parent)

        layout = QGridLayout()

        layout.addWidget(self.get_button("Lista Servizi di Emergenza", self.go_lista_servizi, "background-color: #cfc7e5"), 0, 0)
        layout.addWidget(self.get_button("Lista Pazienti", self.go_lista_pazienti, "background-color: #bad9ac"), 0, 1)
        layout.addWidget(self.get_button("Lista Prenotazioni di Emergenza", self.go_lista_prenotazioni, "background-color: #cfc7e5"), 0, 2)

        self.setLayout(layout)
        self.resize(600, 200)
        self.setWindowTitle("Amministratore del pronto soccorso")

    def go_lista_servizi(self):
        self.vista_lista_servizi = VistaListaServiziEmergenza()
        self.vista_lista_servizi.show()

    def go_lista_pazienti(self):
        self.vista_lista_pazienti = VistaListaPazienti()
        self.vista_lista_pazienti.show()

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni_emergenza = VistaListaPrenotazioniEmergenza(True)
        self.vista_lista_prenotazioni_emergenza.show()

    def get_button(self, titolo, on_click, colore):
        bottone = QPushButton(titolo)
        bottone.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = bottone.font()
        font.setPointSize(9)
        font.setBold(True)
        bottone.setFont(font)
        bottone.clicked.connect(on_click)
        bottone.setStyleSheet(colore)
        return bottone