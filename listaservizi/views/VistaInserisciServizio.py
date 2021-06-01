from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, \
    QRadioButton, QMessageBox, QCheckBox, QGridLayout, QComboBox

from servizio.model.Servizio import Servizio


class VistaInserisciServizio(QWidget):

    def __init__(self, controller, callback):
        super(VistaInserisciServizio, self).__init__()

        self.v_layout = QVBoxLayout()
        self.controller = controller
        self.callback = callback
        self.info = {}
        self.list_reparti = ["Oncologia", "Chirurgia", "Cardiologia", "Medicina", "Riabilitazione"]
        self.list_tipi = ["ricovero", "ricovero di emergenza"]

        self.lbl_reparto = QLabel()
        self.lbl_disponibile = QLabel()
        self.lbl_tipo = QLabel()
        self.lbl_nome = QLabel()

        self.get_type("Id")
        self.get_tipo("Tipo")
        self.get_reparto("Reparto")
        self.get_type("Posto letto")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.setFont(QFont('Verdana', 15))
        btn_ok.clicked.connect(self.add_servizio)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(300, 500)
        self.setWindowTitle("Nuovo Servizio")
        self.setStyleSheet("background-color: #FF7377")

    def get_type(self, tipo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.v_layout.addWidget(lbl)
        current_text = QLineEdit(self)
        current_text.setStyleSheet("background-color: white")
        self.v_layout.addWidget(current_text)
        self.info[tipo] = current_text

    def get_tipo(self, tipo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.v_layout.addWidget(lbl)
        comboBox_tipo = QComboBox()
        comboBox_tipo.setStyleSheet("background-color: white")
        for element in self.list_tipi:
            comboBox_tipo.addItem(element)
        self.v_layout.addWidget(comboBox_tipo)
        comboBox_tipo.activated[str].connect(self.tipo_onClicked)
        self.v_layout.addWidget(self.lbl_tipo)
        self.info[tipo] = self.lbl_tipo

    def tipo_onClicked (self, text):
        self.lbl_tipo.setText(text)

    def get_reparto(self, tipo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.v_layout.addWidget(lbl)
        for reparto in self.list_reparti:
            rbtn = QRadioButton(reparto)
            self.v_layout.addWidget(rbtn)
            rbtn.toggled.connect(self.reparto_onClicked)
        self.v_layout.addWidget(self.lbl_reparto)
        self.info[tipo] = self.lbl_reparto

    def reparto_onClicked (self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.lbl_reparto.setText(rbtn.text())

    def add_servizio(self):
        id = self.info["Id"].text()
        tipo = self.info["Tipo"].text()
        reparto = self.info["Reparto"].text()
        posto_letto = self.info["Posto letto"].text()
        disponibile = True
        if id == "" or tipo == "" or reparto == "" or posto_letto == "" :
            QMessageBox.critical(self, 'Errore', 'Per favore inserisci tutte le informazioni', QMessageBox.Ok, QMessageBox.Ok)
        else:
            nome = (tipo + " in " + reparto + " (" + posto_letto + ")")
            self.controller.aggiungi_servizio(Servizio(id, nome, tipo, reparto, posto_letto, disponibile))
            self.callback()
            self.close()