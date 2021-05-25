from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QMessageBox, QLabel, QLineEdit

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from listaprenotazioni.views.VistaInserisciPrenotazione import VistaInserisciPrenotazione
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
        self.resize(800, 600)
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
        contatore_posti_disponibili = 0
        contatore_posti_occupati = 0
        controller_servizi = ControlloreListaServizi()
        for servizio in controller_servizi.get_lista_servizi():
            if (servizio.is_disponibile()):
                contatore_posti_disponibili += 1
            else:
                contatore_posti_occupati += 1
        text = "I posti attualmente disponibili sono: " + str(contatore_posti_disponibili) + '\n' + "I posti attualmente occupati sono: " + str(contatore_posti_occupati)
        QMessageBox.information(self, "Visualizza posti disponibili", text, QMessageBox.Ok, QMessageBox.Ok)

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

    def closeEvent(self, event):
        self.controller.save_data()
