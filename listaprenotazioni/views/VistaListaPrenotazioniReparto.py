from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QPushButton, QListView, QVBoxLayout, QMessageBox

from listapazienti.controller.ControlloreListaPazienti import ControlloreListaPazienti
from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from paziente.view.VistaPaziente import VistaPaziente
from paziente.view.VistaRefertoPaziente import VistaRefertoPaziente

# Classe responsabile della gestione dell'interfaccia utente:
# permette all'utente di visualizzare la lista delle
# prenotazioni in corso per ogni reparto presente nella struttura

class VistaListaPrenotazioniReparto(QWidget):

    def __init__(self, reparto, bool1):
        super(VistaListaPrenotazioniReparto, self).__init__()

        self.reparto = reparto
        self.controller = ControlloreListaPazienti()
        self.bool1 = bool1

        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        self.h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.get_info_paziente)
        buttons_layout.addWidget(open_button)

        if self.bool1 == True:
            referto_button = QPushButton("Nuovo referto")
            referto_button.clicked.connect(self.get_referto_paziente)
            buttons_layout.addWidget(referto_button)

        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        self.setLayout(self.h_layout)
        self.resize(1200, 600)
        self.setWindowTitle('Lista pazienti ricoverati nel reparto di ' + self.reparto)
        self.setStyleSheet("QWidget{background-color: #ffffac} QPushButton{background-color: gold}")
        self.list_view.setStyleSheet("background-color: white")


    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        controller_prenotazione = ControlloreListaPrenotazioni()
        for prenotazione in controller_prenotazione.get_lista_delle_prenotazioni():
            if prenotazione.servizio.disponibile == False and prenotazione.servizio.reparto == self.reparto:
                item = QStandardItem()
                item.setText(prenotazione.paziente.nome + ' '+ prenotazione.paziente.cognome +  " (" + prenotazione.paziente.cf.upper() + ")")
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
            paziente_selezionato = self.controller.get_paziente_by_cf(stringa[len(stringa) - 1].replace('(', '').replace(')', ''))
            self.vista_paziente = VistaPaziente(paziente_selezionato, True, self.update_ui)
            self.vista_paziente.show()
        else:
            QMessageBox.critical(self, 'Errore', "Selezionare una paziente", QMessageBox.Ok, QMessageBox.Ok)

    def get_referto_paziente(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].data()
            stringa = selected.split()
            paziente_selezionato = self.controller.get_paziente_by_cf(stringa[len(stringa) - 1].replace('(', '').replace(')', ''))
            self.vista_paziente = VistaRefertoPaziente(paziente_selezionato, self.update_ui)
            self.vista_paziente.show()
        else:
            QMessageBox.critical(self, 'Errore', "Selezionare un paziente", QMessageBox.Ok, QMessageBox.Ok)

    def closeEvent(self, event):
        self.controller.save_data()