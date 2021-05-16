from PyQt5.QtWidgets import QGridLayout, QPushButton, QSizePolicy, QWidget

from listapazienti.views.VistaListaPazienti import VistaListaPazienti
from listaricoveri.views.VistaListaRicoveri import VistaListaRicoveri


class VistaHomeMedico(QWidget):

    def __init__(self):
        super(VistaHomeMedico, self).__init__()

        layout = QGridLayout()

        layout.addWidget(self.get_button("Lista Pazienti", self.go_lista_pazienti), 0, 0)
        layout.addWidget(self.get_button("Lista Ricoveri", self.go_lista_ricoveri), 0, 1)

        self.setLayout(layout)
        self.resize(600, 200)
        self.setWindowTitle("Medico")

    def go_lista_pazienti(self):
        self.vista_lista_pazienti = VistaListaPazienti()
        self.vista_lista_pazienti.show()

    def go_lista_ricoveri(self):
        self.vista_lista_ricoveri = VistaListaRicoveri()
        self.vista_lista_ricoveri.show()

    def get_button(self, titolo, on_click):
        bottone = QPushButton(titolo)
        bottone.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bottone.clicked.connect(on_click)
        return bottone