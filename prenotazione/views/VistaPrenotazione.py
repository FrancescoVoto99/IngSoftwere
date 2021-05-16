from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, QPushButton

from listapazienti.controller.ControlloreListaPazienti import ControlloreListaPazienti
from paziente.view.VistaPaziente import VistaPaziente
from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from servizio.views.VistaServizio import VistaServizio


class VistaPrenotazione(QWidget):

    def __init__(self, prenotazione,disdici_prenotazione, elimina_callback,  parent = None):
        super(VistaPrenotazione, self).__init__(parent)
        self.controller = ControllorePrenotazione(prenotazione)
        self.disdici_prenotazione = disdici_prenotazione
        self.elimina_callback = elimina_callback
        self.libera_posto_letto = self.controller.libera_posto_letto()
        self.controller_paziente = ControlloreListaPazienti()

        v_layout = QVBoxLayout()

        v_layout.addWidget(self.get_label_info("Id", self.controller.get_id_prenotazione()))
        v_layout.addWidget(self.get_label_info("Paziente", self.controller.get_paziente_prenotazione()))
        v_layout.addWidget(self.get_label_info("Servizio", self.controller.get_servizio_prenotazione()))
        v_layout.addWidget(self.get_label_info("Data di inizio ricovero", self.controller.get_data_prenotazione()))
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        button_disdici = QPushButton("Disdici")
        button_disdici.clicked.connect(self.disdici_prenotazione_click)
        v_layout.addWidget(button_disdici)

        self.setLayout(v_layout)

        button_libera_posto_letto = QPushButton("Libera posto letto")
        button_libera_posto_letto.clicked.connect(self.libera_posto_letto_click)
        v_layout.addWidget(button_libera_posto_letto)

        self.setLayout(v_layout)

        button_visualizza_paziente = QPushButton("Visualizza paziente")
        button_visualizza_paziente.clicked.connect(self.visualizza_paziente_click)
        v_layout.addWidget(button_visualizza_paziente)

        self.setLayout(v_layout)

        button_visualizza_servizio = QPushButton("Visualizza servizio")
        button_visualizza_servizio.clicked.connect(self.visualizza_servizio_click)
        v_layout.addWidget(button_visualizza_servizio)

        self.setLayout(v_layout)

    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(20)
        current_label.setFont(current_font)
        return current_label

    def disdici_prenotazione_click(self):
        self.disdici_prenotazione(self.controller.get_id_prenotazione())
        self.elimina_callback()
        self.close()

    def libera_posto_letto_click(self):
        self.libera_posto_letto(self.controller.get_servizio_prenotazione())
        self.elimina_callback()
        self.close()

    def visualizza_paziente_click(self):
       self.visualizza_paziente = VistaPaziente(self.controller.get_paziente_prenotazione, self.controller_paziente.archivia_paziente_by_cf , self.elimina_callback)
       self.visualizza_paziente.show()
       self.close()

    def visualizza_servizio_click(self):
       self.visualizza_servizio = VistaServizio(self.controller.get_servizio_prenotazione)
       self.visualizza_servizio.show()
       self.close()

    def get_generic_label(self, titolo):
        label = QLabel(titolo)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        return label



