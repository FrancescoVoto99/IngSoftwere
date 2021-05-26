from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QMessageBox, QLabel, QLineEdit, \
    QTableWidget, QTableWidgetItem, QHeaderView

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from listaprenotazioni.views.VistaInserisciPrenotazione import VistaInserisciPrenotazione
from listaprenotazioni.views.VistaListaPrenotazioniArchiviate import VistaListaPrenotazioniArchiviate
from listaservizi.controller.ControlloreListaServizi import ControlloreListaServizi
from prenotazione.views.VistaPrenotazione import VistaPrenotazione



class VistaListaPrenotazioni(QWidget):
    def __init__(self):
        super(VistaListaPrenotazioni, self).__init__()

        h_layout = QHBoxLayout()
        self.controller = ControlloreListaPrenotazioni()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.get_info_prenotazioni)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Nuova")
        new_button.clicked.connect(self.show_new_prenotazione)
        buttons_layout.addWidget(new_button)

        button_disponibilita = QPushButton("Visualizza posti disponibili")
        button_disponibilita.clicked.connect(self.show_disponibilita)
        buttons_layout.addWidget(button_disponibilita)

        button_archiviate = QPushButton("Visualizza prenotazioni archiviate")
        button_archiviate.clicked.connect(self.show_archiviate)
        buttons_layout.addWidget(button_archiviate)

        buttons_layout.addStretch()

        button_new = QPushButton("Cerca")
        lbl_reparto = QLabel("Reparto")
        lbl_nome = QLabel("Nome Paziente")
        lbl_cognome = QLabel("Cognome Paziente")
        self.lineedit_reparto = QLineEdit(self)
        self.lineedit_nome = QLineEdit(self)
        self.lineedit_cognome = QLineEdit(self)
        button_new.clicked.connect(self.search_prenotazione)
        buttons_layout.addWidget(lbl_reparto)
        buttons_layout.addWidget(self.lineedit_reparto)
        buttons_layout.addWidget(lbl_nome)
        buttons_layout.addWidget(self.lineedit_nome)
        buttons_layout.addWidget(lbl_cognome)
        buttons_layout.addWidget(self.lineedit_cognome)
        buttons_layout.addWidget(button_new)

        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(1200, 600)
        self.setWindowTitle('Lista Prenotazioni')

    def get_info_prenotazioni(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].data()
            stringa = selected.split()
            prenotazione_selezionata = self.controller.get_prenotazione_by_posto_letto_and_cf(stringa[len(stringa) - 1].replace('(','').replace(')',''), stringa[0].replace('(','').replace(')',''))
            self.vista_prenotazione = VistaPrenotazione(prenotazione_selezionata, self.controller.elimina_prenotazione_by_id, self.update_ui)
            self.vista_prenotazione.show()
        else:
            QMessageBox.critical(self, 'Errore', "Selezionare una prenotazione", QMessageBox.Ok, QMessageBox.Ok)

    def show_new_prenotazione(self):
        self.vista_inserisci_prenotazione = VistaInserisciPrenotazione(self.controller, self.update_ui)
        self.vista_inserisci_prenotazione.show()

    def show_disponibilita(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Reparto"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Posti Disponibili"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Posti Occupati"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Oncologia"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(str(self.posti_disponibili("oncologia"))))
        self.tableWidget.setItem(1, 2, QTableWidgetItem(str(self.posti_occupati("oncologia"))))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Chirurgia"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem(str(self.posti_disponibili("chirurgia"))))
        self.tableWidget.setItem(2, 2, QTableWidgetItem(str(self.posti_occupati("chirurgia"))))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cardiologia"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem(str(self.posti_disponibili("cardiologia"))))
        self.tableWidget.setItem(3, 2, QTableWidgetItem(str(self.posti_occupati("cardiologia"))))
        self.tableWidget.setItem(4, 0, QTableWidgetItem("Medicina"))
        self.tableWidget.setItem(4, 1, QTableWidgetItem(str(self.posti_disponibili("medicina"))))
        self.tableWidget.setItem(4, 2, QTableWidgetItem(str(self.posti_occupati("medicina"))))
        self.tableWidget.setItem(5, 0, QTableWidgetItem("Riabilitazione"))
        self.tableWidget.setItem(5, 1, QTableWidgetItem(str(self.posti_disponibili("riabilitazione"))))
        self.tableWidget.setItem(5, 2, QTableWidgetItem(str(self.posti_occupati("riabilitazione"))))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setWindowTitle("Posti disponibili in ogni reparto")
        self.tableWidget.show()

    def posti_disponibili(self, reparto):
        contatore_posti_disponibili = 0
        controller_servizi = ControlloreListaServizi()
        for servizio in controller_servizi.get_lista_servizi():
            if servizio.reparto.lower() == reparto.lower():
               if (servizio.is_disponibile()):
                   contatore_posti_disponibili += 1
        return contatore_posti_disponibili

    def posti_occupati(self, reparto):
        contatore_posti_occupati = 0
        controller_servizi = ControlloreListaServizi()
        for servizio in controller_servizi.get_lista_servizi():
            if servizio.reparto.lower() == reparto.lower():
               if servizio.is_disponibile() == False:
                   contatore_posti_occupati += 1
        return contatore_posti_occupati

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

    def search_prenotazione (self):
        self.update_ui(self.lineedit_reparto.text(),self.lineedit_nome.text(), self.lineedit_cognome.text())

    def show_archiviate(self):
        self.vista_archiviate = VistaListaPrenotazioniArchiviate()
        self.vista_archiviate.show()

    def closeEvent(self, event):
        self.controller.save_data()
