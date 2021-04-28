from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy

from servizio.controller.ControlloreServizio import ControlloreServizio


class VistaServizio(QWidget):

    def __init__(self, servizio, parent = None):
        super(VistaServizio, self).__init__(parent)
        self.controller = ControlloreServizio(servizio)

        h_layout = QHBoxLayout()

        v_layout = QVBoxLayout()
        label_nome = QLabel(self.controller.get_nome_servizio())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        label_tipo = QLabel("Tipo: {}".format(self.controller.get_tipo_servizio()))
        font_tipo = label_tipo.font()
        font_tipo.setPointSize(17)
        label_tipo.setFont(font_tipo)
        v_layout.addWidget(label_tipo)

        label_reparto = QLabel("Reparto: {}".format(self.controller.get_reparto_servizio()))
        font_reparto = label_reparto.font()
        font_reparto.setPointSize(17)
        label_reparto.setFont(font_reparto)
        v_layout.addWidget(label_reparto)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        label_posizione = QLabel("Posto letto: {}".format(self.controller.get_posto_letto_servizio()))
        font_posizione = label_posizione.font()
        font_posizione.setPointSize(17)
        label_posizione.setFont(font_posizione)
        v_layout.addWidget(label_posizione)

        h_layout.addLayout(v_layout)

        h_layout.addItem(QSpacerItem(50, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout2 = QVBoxLayout()

        label_disponibile = QLabel(self.controller.get_servizio_disponibile())
        font_disponibile = label_disponibile.font()
        font_disponibile.setPointSize(25)
        label_disponibile.setFont(font_disponibile)
        v_layout2.addWidget(label_disponibile)

        h_layout.addLayout((v_layout2))

        self.setLayout(h_layout)
        self.setWindowTitle(servizio.nome)
