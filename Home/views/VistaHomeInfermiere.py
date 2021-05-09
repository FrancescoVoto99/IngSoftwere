from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listapazienti.views.VistaListaPazienti import VistaListaPazienti
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from listaservizi.views.VistaListaServizi import VistaListaServizi


class VistaHomeInfermiere(QWidget):

    def __init__(self, parent = None):
        super(VistaHomeInfermiere, self).__init__(parent)

        layout = QGridLayout()

        layout.addWidget(self.get_button("Lista Servizi", self.go_lista_servizi), 0, 0)
        layout.addWidget(self.get_button("Lista Pazienti", self.go_lista_pazienti), 1, 0)
        layout.addWidget(self.get_button("Lista Ricoveri", self.go_lista_ricoveri), 0, 1)

        self.setLayout(layout)
        self.resize(400, 400)
        self.setWindowTitle("Infermiere")

    def go_lista_servizi(self):
        self.vista_lista_servizi = VistaListaServizi()
        self.vista_lista_servizi.show()

    def go_lista_pazienti(self):
        self.vista_lista_pazienti = VistaListaPazienti()
        self.vista_lista_pazienti.show()

    def go_lista_ricoveri(self):
        self.vista_lista_ricoveri = VistaListaPrenotazioni()
        self.vista_lista_ricoveri.show()

    def get_button(self, titolo, on_click):
        bottone = QPushButton(titolo)
        bottone.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bottone.clicked.connect(on_click)
        return bottone


