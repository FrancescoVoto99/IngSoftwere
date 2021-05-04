from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, QPushButton

from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione


class VistaPrenotazione(QWidget):

    def __init__(self, prenotazione,disdici_prenotazione, elimina_callback, libera_posto_letto, parent = None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controller = ControllorePrenotazione(prenotazione)
        self.disdici_prenotazione = disdici_prenotazione
        self.elimina_callback = elimina_callback
        self.libera_posto_letto = libera_posto_letto

        v_layout = QVBoxLayout()

        v_layout.addWidget(self.get_generic_label("Id {}".format(self.controller.get_id_prenotazione())))
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(self.get_generic_label("Paziente {}".format(self.controller.get_paziente_prenotazione())))
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(self.get_generic_label("Servizio {}".format(self.controller.get_servizio_prenotazione())))
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        v_layout.addWidget(self.get_generic_label("Data {}".format(self.controller.get_data_prenotazione())))
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        button_disdici = QPushButton("Disdici")
        button_disdici.clicked.connect(self.disdici_prenotazione_click)
        v_layout.addWidget(button_disdici)

        self.setLayout(v_layout)

        button_libera_posto_letto = QPushButton("Libera posto letto")
        button_libera_posto_letto.clicked.connect(self.libera_posto_letto_click)
        v_layout.addWidget(button_libera_posto_letto)

        self.setLayout(v_layout)

    def disdici_prenotazione_click(self):
        self.disdici_prenotazione(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()

    def libera_posto_letto_click(self):
        self.libera_posto_letto(self.controller.get_servizio_prenotazione())
        self.elimina_callback()
        self.close()

    def get_generic_label(self, titolo):
        label = QLabel(titolo)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        return label



