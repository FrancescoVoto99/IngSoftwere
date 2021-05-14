from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy

from servizio.controller.ControlloreServizio import ControlloreServizio


class VistaServizio(QWidget):

    def __init__(self, servizio, parent=None):
        super(VistaServizio, self).__init__(parent)
        self.controller = ControlloreServizio(servizio)

        h_layout = QHBoxLayout()

        v_layout = QVBoxLayout()
        label = self.label_generate(self.controller.get_nome_servizio(), 20)
        v_layout.addWidget(label)

        label = self.label_generate("Id: {}".format(self.controller.get_id_servizio()), 17)
        v_layout.addWidget(label)

        label = self.label_generate("Tipo: {}".format(self.controller.get_tipo_servizio()), 17)
        v_layout.addWidget(label)

        label = self.label_generate("Reparto: {}".format(self.controller.get_reparto_servizio()), 17)
        v_layout.addWidget(label)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label = self.label_generate("Posto letto: {}".format(self.controller.get_posto_letto_servizio()), 17)
        v_layout.addWidget(label)

        h_layout.addLayout(v_layout)

        h_layout.addItem(QSpacerItem(50, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout2 = QVBoxLayout()
        label = self.label_generate(self.controller.get_servizio_disponibile(), 25)
        if(self.controller.get_servizio_disponibile()=="Non disponibile"):
            label.setStyleSheet("background-color: red")
        else:
            label.setStyleSheet("background-color: green")


        v_layout2.addWidget(label)

        h_layout.addLayout(v_layout2)

        self.setLayout(h_layout)
        self.setWindowTitle(servizio.nome)

    def label_generate(self, etichetta, dimensione):
        label = QLabel(etichetta)
        font = label.font()
        font.setPointSize(dimensione)
        label.setFont(font)
        return label
