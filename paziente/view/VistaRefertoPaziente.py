from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit

from listapazienti.controller.ControlloreListaPazienti import ControlloreListaPazienti
from paziente.Controller.ControllorePaziente import ControllorePaziente


class VistaRefertoPaziente(QWidget):

    def __init__(self, paziente, callback, parent = None):
        super(VistaRefertoPaziente, self).__init__(parent)

        self.controller = ControllorePaziente(paziente)
        self.callback = callback

        v_layout = QVBoxLayout()

        label_inserisci = QLabel("Inserire un nuovo referto: ")
        font_inserisci = label_inserisci.font()
        font_inserisci.setPointSize(30)
        label_inserisci.setFont(font_inserisci)
        v_layout.addWidget(label_inserisci)

        self.referto_edit = QLineEdit()
        v_layout.addWidget(self.referto_edit)

        btn_ok = QPushButton("Conferma")
        btn_ok.setFont(QFont('Verdana', 15))
        btn_ok.clicked.connect(self.add_referto)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_paziente() + " " + self.controller.get_cognome_paziente())

    def add_referto(self):
        controller_pazienti = ControlloreListaPazienti()
        self.controller.aggiungi_nuovo_referto_paziente = self.controller.aggiungi_nuovo_referto_paziente(self.referto_edit.text())
        controller_pazienti.save_data()
        if self.callback() != None:
            self.callback()
        self.close()



