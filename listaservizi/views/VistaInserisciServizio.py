from PyQt5 import QtCore
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
        self.list_nomi = ["Ricovero in oncologia", "Ricovero di emergenza in oncologia", "Ricovero in chirurgia",
                          "Ricovero di emergenza in chirurgia", "Ricovero in cardiologia",
                          "Ricovero di emergenza in cardiologia"]
        self.list_reparti = ["Oncologia", "Chirurgia", "Cardiologia"]
        self.list_tipi = ["ricovero", "ricovero di emergenza"]

        self.lbl_reparto = QLabel()
        self.lbl_disponibile = QLabel()
        self.lbl_tipo = QLabel()
        self.lbl_nome = QLabel()

        self.get_type("Id")
        self.get_nome("Nome")
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

    def get_nome(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        comboBox_nome = QComboBox()
        for nome in self.list_nomi:
            comboBox_nome.addItem(nome)
        self.v_layout.addWidget(comboBox_nome)
        comboBox_nome.activated[str].connect(self.nome_onClicked)
        self.v_layout.addWidget(self.lbl_nome)
        self.info[tipo] = self.lbl_nome

    def nome_onClicked(self, text):
        self.lbl_nome.setText(text)

    def get_tipo(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
        comboBox_tipo = QComboBox()
        for element in self.list_tipi:
            comboBox_tipo.addItem(element)
        self.v_layout.addWidget(comboBox_tipo)
        comboBox_tipo.activated[str].connect(self.tipo_onClicked)
        self.v_layout.addWidget(self.lbl_tipo)
        self.info[tipo] = self.lbl_tipo

    def tipo_onClicked (self, text):
        self.lbl_tipo.setText(text)

    def get_reparto(self, tipo):
        self.v_layout.addWidget(QLabel(tipo))
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