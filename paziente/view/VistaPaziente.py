from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from paziente.Controller.ControllorePaziente import ControllorePaziente


class VistaPaziente(QWidget):
    def __init__(self, paziente, elimina_paziente, elimina_callback, parent=None):
        super(VistaPaziente, self).__init__(parent)
        self.controller = ControllorePaziente(paziente)
        self.elimina_paziente = elimina_paziente
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_paziente() + " " + self.controller.get_cognome_paziente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_label_info("Luogo di nascita", self.controller.get_luogodinascita_paziente()))
        v_layout.addWidget(self.get_label_info("Data di nascita", self.controller.get_datadinascita_paziente()))
        v_layout.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_paziente()))
        v_layout.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_paziente()))
        v_layout.addWidget(self.get_label_info("Email", self.controller.get_email_paziente()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ricovero = QPushButton("Ricovero")
        btn_ricovero.clicked.connect(self.check_ricovero)
        v_layout.addWidget(btn_ricovero)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_reparto = QPushButton("Reparto")
        btn_reparto.clicked.connect(self.check_reparto)
        v_layout.addWidget(btn_reparto)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_archivia = QPushButton("Archivia")
        btn_archivia.clicked.connect(self.archivia_paziente_click)
        v_layout.addWidget(btn_archivia)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_paziente() + " " + self.controller.get_cognome_paziente())

    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    #def check_abbonamento(self):
        #self.vista_abbonamento = VistaAbbonamento(self.controller.get_abbonamento_cliente(), self.controller.aggiungi_nuovo_abbonamento_cliente)
        #self.vista_abbonamento.show()

    def archivia_paziente_click(self):
        self.archivia_paziente(self.controller.get_cf_paziente())
        self.archivia_callback()
        self.close()