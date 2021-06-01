from PyQt5.QtWidgets import QLabel, QPushButton, QSpacerItem, QSizePolicy, QVBoxLayout, QWidget

from listapazienti.controller.ControlloreListaPazienti import ControlloreListaPazienti
from paziente.view.VistaPaziente import VistaPaziente
from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from servizio.views.VistaServizio import VistaServizio


class VistaPrenotazioneArchiviata(QWidget):

    def __init__(self, prenotazione, elimina_callback,  bool, parent = None):
        super(VistaPrenotazioneArchiviata, self).__init__(parent)
        self.prenotazione=prenotazione
        self.controller = ControllorePrenotazione(prenotazione)
        self.elimina_callback = elimina_callback
        self.controller_paziente = ControlloreListaPazienti()
        self.bool = bool

        v_layout = QVBoxLayout()


        v_layout.addWidget(self.get_label_info("Id", self.controller.get_id_prenotazione()))
        v_layout.addWidget(self.get_label_info("Paziente", self.controller.get_paziente_prenotazione().nome+" "+self.controller.get_paziente_prenotazione().cognome))
        v_layout.addWidget(self.get_label_info("Servizio", self.controller.get_servizio_prenotazione().nome))
        v_layout.addWidget(self.get_label_info("Data di inizio ricovero", self.controller.get_data_prenotazione()))
        v_layout.addWidget(self.get_label_info("Data di fine ricovero", self.controller.get_datafine_prenotazione()))
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(v_layout)
        self.setStyleSheet("QWidget{background-color: #ffffac} QPushButton{background-color: gold}")

        button_visualizza_paziente = QPushButton("Visualizza paziente")
        button_visualizza_paziente.clicked.connect(self.visualizza_paziente_click)
        v_layout.addWidget(button_visualizza_paziente)

        self.setLayout(v_layout)

        if self.bool == True:
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


    def visualizza_paziente_click(self):
       self.visualizza_paziente = VistaPaziente(self.controller.get_paziente_prenotazione(), False)
       self.visualizza_paziente.show()
       self.close()

    def visualizza_servizio_click(self):
       self.visualizza_servizio = VistaServizio(self.controller.get_servizio_prenotazione(), False, None, self.prenotazione.data)
       self.visualizza_servizio.show()
       self.close()

    def get_generic_label(self, titolo):
        label = QLabel(titolo)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        return label



