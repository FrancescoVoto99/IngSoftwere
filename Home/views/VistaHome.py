from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listaservizi.views.VistaListaServizi import VistaListaServizi


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()

        # ricoveri_bottone.clicked.connect()

        grid_layout.addWidget(self.get_button("Lista Servizi", self.go_lista_servizi), 0, 0)
        grid_layout.addWidget(self.get_button("Lista Pazienti", self.go_lista_pazienti), 0, 1)
        grid_layout.addWidget(self.get_button("Lista Operatori", self.go_lista_operatori), 1, 0)
        grid_layout.addWidget(self.get_button("Lista Ricoveri", self.go_lista_ricoveri), 1, 1)

        self.setLayout(grid_layout)
        self.resize(400, 400)
        self.setWindowTitle("HospITALY")

    def go_lista_servizi(self):
        self.vista_lista_servizi = VistaListaServizi()
        self.vista_lista_servizi.show()

    def go_lista_pazienti(self):
        pass

    def go_lista_operatori(self):
        pass

    def go_lista_ricoveri(self):
        pass

    def get_button(self, titolo, on_click):
        bottone = QPushButton(titolo)
        bottone.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bottone.clicked.connect(on_click)
        return bottone
