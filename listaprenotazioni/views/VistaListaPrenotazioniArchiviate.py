from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QMessageBox

from listaprenotazioni.controller.ControlloreListaPrenotazioniArchiviate import ControlloreListaPrenotazioniArchiviate
from prenotazione.views.VistaPrenotazione import VistaPrenotazione
from prenotazione.views.VistaPrenotazioneArchiviata import VistaPrenotazioneArchiviata


class VistaListaPrenotazioniArchiviate(QWidget):

    def __init__(self, bool):
        super(VistaListaPrenotazioniArchiviate, self).__init__()
        h_layout = QHBoxLayout()
        self.controller = ControlloreListaPrenotazioniArchiviate()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)
        self.bool = bool

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.get_info_prenotazioni)
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()

        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(1200, 600)
        self.setWindowTitle('Lista Prenotazioni Archiviate')
        self.setStyleSheet("QWidget{background-color: #ffffac} QPushButton{background-color: gold}")
        self.list_view.setStyleSheet("background-color: white")

    def update_ui(self, reparto_search = "", nome_search = "", cognome_search = ""):
        self.listview_model = QStandardItemModel(self.list_view)
        for prenotazione in self.controller.get_lista_delle_prenotazioni():
            if reparto_search == "" or ((prenotazione.servizio.reparto.lower()).find(reparto_search.lower())) == 0:
                if nome_search == "" or ((prenotazione.paziente.nome.lower()).find(nome_search.lower())) == 0:
                    if cognome_search == "" or ((prenotazione.paziente.cognome.lower()).find(cognome_search.lower())) == 0:
                        item = QStandardItem()
                        item.setText("(" + prenotazione.paziente.cf + ") " + prenotazione.servizio.nome)
                        item.setEditable(False)
                        font = item.font()
                        font.setPointSize(18)
                        item.setFont(font)
                        self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def get_info_prenotazioni(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].data()
            stringa = selected.split()
            prenotazione_selezionata = self.controller.get_prenotazione_by_posto_letto_and_cf(stringa[len(stringa) - 1].replace('(', '').replace(')', ''), stringa[0].replace('(', '').replace(')', ''))
            self.vista_prenotazione_archiviata = VistaPrenotazioneArchiviata(prenotazione_selezionata, self.update_ui, self.bool)
            self.vista_prenotazione_archiviata.show()
        else:
            QMessageBox.critical(self, 'Errore', "Selezionare una prenotazione", QMessageBox.Ok, QMessageBox.Ok)

    def closeEvent(self, event):
        self.controller.save_data()