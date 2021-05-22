from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QPushButton, QListView, QVBoxLayout, QMessageBox

from listapazienti.controller.ControlloreListaPazienti import ControlloreListaPazienti
from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from paziente.view.VistaPaziente import VistaPaziente
from prenotazione.views.VistaPrenotazione import VistaPrenotazione


class VistaListaPrenotazioniReparto(QWidget):

    def __init__(self, reparto):
        super(VistaListaPrenotazioniReparto, self).__init__()

        self.reparto = reparto
        self.controller = ControlloreListaPrenotazioni()

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
        if (len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].data()
            stringa = selected.split()
            prenotazione_selezionata = self.controller.get_prenotazione_by_posto_letto(
                stringa[len(stringa) - 1].replace('(', '').replace(')', ''))
            self.vista_prenotazione = VistaPrenotazione(prenotazione_selezionata,
                                                        self.controller.elimina_prenotazione_by_id, self.update_ui)
            self.vista_prenotazione.show()
        else:
            QMessageBox.critical(self, 'Errore', "Selezionare una prenotazione", QMessageBox.Ok, QMessageBox.Ok)
