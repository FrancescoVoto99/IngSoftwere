import json

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QSpacerItem, QSizePolicy, \
    QPushButton, QGridLayout
from PyQt5.QtCore import Qt

from autenticazione.views.VistaInserisciCredenziali import VistaInserisciCredenziali


class VistaAutenticazione(QWidget):

    def __init__(self, parent = None):
        super(VistaAutenticazione, self).__init__(parent)


        self.v_layout = QGridLayout()
        self.lbl = QLabel("Benvenuto a HospItaly")
        font_lbl = self.lbl.font()
        font_lbl.setPointSize(50)
        font_lbl.setBold(True)
        self.lbl.setFont(font_lbl)
        self.v_layout.addWidget(self.lbl, 0, 1)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.lbl_foto = QLabel()
        foto = QPixmap('immagine.jpg')
        self.lbl_foto.setAlignment(Qt.AlignCenter)
        self.lbl_foto.setPixmap(foto)
        self.v_layout.addWidget(self.lbl_foto, 1, 1)

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_accedi = QPushButton("Accedi")
        btn_accedi.setFont(QFont('Verdana',30))
        btn_accedi.clicked.connect(self.go_vista_inserisci_credenziali)
        self.v_layout.addWidget(btn_accedi, 2, 1)

        btn_chiudi = QPushButton("Esci")
        btn_chiudi.setFont(QFont('Verdana', 30))
        btn_chiudi.clicked.connect(self.close)
        self.v_layout.addWidget(btn_chiudi, 3, 1)

        self.setLayout(self.v_layout)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWindowTitle("Benvenuto")


        self.showFullScreen()
        self.setStyleSheet("QWidget{background-color: lightblue}QPushButton{background-color: cornflowerblue}")



    def go_vista_inserisci_credenziali(self):
        self.vista_inserisci_credenziali = VistaInserisciCredenziali()
        self.vista_inserisci_credenziali.show()
        self.close()
