from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QPushButton, QListView, QVBoxLayout

from listapazienti.controller.ControlloreListaPazienti import ControlloreListaPazienti
from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from paziente.view.VistaPaziente import VistaPaziente


class VistaListaPrenotazioniReparto(QWidget):

    def __init__(self, reparto):
        super(VistaListaPrenotazioniReparto, self).__init__()

        self.reparto = reparto

        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.get_info_paziente)
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        self.setLayout(self.h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista pazienti ricoverati nel reparto di ' + self.reparto)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        controller_prenotazione = ControlloreListaPrenotazioni()
        for prenotazione in controller_prenotazione.get_lista_delle_prenotazioni():
            if prenotazione.servizio.disponibile == False and prenotazione.servizio.reparto == self.reparto:
                item = QStandardItem()
                item.setText(prenotazione.paziente.nome + ' '+ prenotazione.paziente.cognome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def get_info_paziente(self):
        controller = ControlloreListaPazienti()
        selected = self.list_view.selectedIndexes()[0].row()
        paziente_selezionato = controller.get_paziente_by_index(selected)
        self.vista_paziente = VistaPaziente(paziente_selezionato, None, self.update_ui)
        self.vista_paziente.show()
