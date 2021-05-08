from PyQt5.QtWidgets import QGridLayout, QPushButton, QSizePolicy, QWidget

from listapazienti.views.VistaListaPazienti import VistaListaPazienti


class VistaHomeProntoSoccorso(QWidget):
    
    def __init__(self, parent = None):
        super(VistaHomeProntoSoccorso, self).__init__(parent)

        layout = QGridLayout()

        layout.addWidget(self.get_button("Lista Servizi di Emergenza", self.go_lista_servizi), 0, 0)
        layout.addWidget(self.get_button("Lista Pazienti", self.go_lista_pazienti), 0, 1)
        layout.addWidget(self.get_button("Lista Ricoveri di Emergenza", self.go_lista_ricoveri), 1, 1)

        self.setLayout(layout)
        self.resize(400, 400)
        self.setWindowTitle("Amministratore del pronto soccorso")

    def go_lista_servizi(self):
        pass

    def go_lista_pazienti(self):
        self.vista_lista_pazienti = VistaListaPazienti()
        self.vista_lista_pazienti.show()

    def go_lista_ricoveri(self):
        pass

    def get_button(self, titolo, on_click):
        bottone = QPushButton(titolo)
        bottone.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bottone.clicked.connect(on_click)
        return bottone