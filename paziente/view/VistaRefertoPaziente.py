from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit

from paziente.Controller.ControllorePaziente import ControllorePaziente


class VistaRefertoPaziente(QWidget):

    def __init__(self, paziente, parent = None):
        super(VistaRefertoPaziente, self).__init__(parent)

        self.controller = ControllorePaziente(paziente)

        v_layout = QVBoxLayout()

        label_inserisci = QLabel("Inserire un nuovo referto: ")
        font_inserisci = label_inserisci.font()
        font_inserisci.setPointSize(30)
        label_inserisci.setFont(font_inserisci)
        v_layout.addWidget(label_inserisci)

        self.referto_edit = QTextEdit(self)
        v_layout.addWidget(self.referto_edit)

        btn_ok = QPushButton("Conferma")
        btn_ok.clicked.connect(self.add_referto)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_paziente() + " " + self.controller.get_cognome_paziente())

    def add_referto(self):
        if self.controller.get_referto_paziente() == None:
            self.controller.aggiungi_nuovo_referto_paziente(self.referto_edit.text())
        else:
            QMessageBox.critical(self, 'Errore', "Non è possibile inserire un nuovo referto", QMessageBox.Ok, QMessageBox.Ok)



