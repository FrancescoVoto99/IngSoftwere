import json

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QSpacerItem, QSizePolicy, \
    QPushButton, QVBoxLayout

from autenticazione.views.VistaInserisciCredenziali import VistaInserisciCredenziali


class VistaAutenticazione(QWidget):

    def __init__(self, parent = None):
        super(VistaAutenticazione, self).__init__(parent)

        self.v_layout = QVBoxLayout()
        self.lbl = QLabel("Benvenuto a HospItaly")
        font_lbl = self.lbl.font()
        font_lbl.setPointSize(50)
        self.lbl.setFont(font_lbl)
        self.v_layout.addWidget(self.lbl)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.lbl_foto = QLabel()
        foto = QPixmap('immagine.jpg')
        self.lbl_foto.setPixmap(foto)
        self.v_layout.addWidget(self.lbl_foto)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_accedi = QPushButton("Accedi")
        btn_accedi.setFont(QFont('Verdana',30))
        btn_accedi.clicked.connect(self.go_vista_inserisci_credenziali)
        self.v_layout.addWidget(btn_accedi)

        self.setLayout(self.v_layout)
        self.resize(200, 200)
        self.setWindowTitle("Benvenuto")

    def go_vista_inserisci_credenziali(self):
        self.vista_inserisci_credenziali = VistaInserisciCredenziali()
        self.vista_inserisci_credenziali.show()
        self.close()
