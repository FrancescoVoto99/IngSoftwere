from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, \
    QRadioButton, QMessageBox, QCheckBox

from servizio.model.Servizio import Servizio


class VistaInserisciServizio(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciServizio, self).__init__()

        self.v_layout = QVBoxLayout()
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.lbl_reparto = QLabel()
        self.lbl_disponibile = QLabel()
        self.lbl_tipo = QLabel()

        self.get_type("Id")
        self.get_type("Nome")
        self.get_tipo("Tipo")
        self.get_reparto("Reparto")
        self.get_type("Posto letto")
        self.get_disponibile("Disponibile")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_servizio)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Servizio")

    def get_type(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        current_text = QLineEdit(self)
        self.v_layout.addWidget(current_text)
        self.info[tipo] = current_text

    def get_tipo(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        radioButton_ricovero = QRadioButton("ricovero")
        self.v_layout.addWidget(radioButton_ricovero)
        radioButton_ricovero.toggled.connect(self.tipo_onCliked)
        radioButton_ricoveroem = QRadioButton("ricovero di emergenza")
        self.v_layout.addWidget(radioButton_ricoveroem)
        radioButton_ricoveroem.toggled.connect(self.tipo_onCliked)
        self.v_layout.addWidget(self.lbl_tipo)
        self.info[tipo] = self.lbl_tipo

    def tipo_onCliked (self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.lbl_tipo.setText(rbtn.text())

    def get_reparto(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        rbtn_onco = QRadioButton("Oncologia")
        self.v_layout.addWidget(rbtn_onco)
        rbtn_onco.toggled.connect(self.reparto_onCliked)
        rbtn_chirurgia = QRadioButton("Chirurgia")
        self.v_layout.addWidget(rbtn_chirurgia)
        rbtn_chirurgia.toggled.connect(self.reparto_onCliked)
        rbtn_cardio = QRadioButton("Oncologia")
        self.v_layout.addWidget(rbtn_cardio)
        rbtn_cardio.toggled.connect(self.reparto_onCliked)
        self.v_layout.addWidget(self.lbl_reparto)
        self.info[tipo] = self.lbl_reparto

    def reparto_onCliked (self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.lbl_reparto.setText(rbtn.text())

    def get_disponibile(self, tipo):
        checkBoxDisponibile = QCheckBox()
        self.v_layout.addWidget(QLabel(tipo))
        checkBoxDisponibile.stateChanged.connect(self.disponibile_onClicked)
        self.v_layout.addWidget(checkBoxDisponibile)
        self.v_layout.addWidget(self.lbl_disponibile)
        self.info[tipo] = self.lbl_disponibile

    def disponibile_onClicked(self):
        checkBox = self.sender()
        if checkBox.isChecked() == True:
            self.lbl_disponibile.setText(str(checkBox.isChecked()))
        else:
            self.lbl_disponibile.setText("")

    def add_servizio(self):
        id = self.info["Id"].text()
        nome = self.info["Nome"].text()
        tipo = self.info["Tipo"].text()
        reparto = self.info["Reparto"].text()
        posto_letto = self.info["Posto letto"].text()
        disponibile = self.info["Disponibile"].text()
        if id == "" or nome == "" or tipo == "" or reparto == "" or posto_letto == "" or disponibile == "":
            QMessageBox.critical(self, 'Errore', 'Per favore inserisci tutte le informazioni', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_servizio(Servizio(id, nome, tipo, reparto, posto_letto, disponibile))
            self.callback()
            self.close()