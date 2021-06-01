from datetime import datetime, date
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QBoxLayout, QListView, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit, \
    QMessageBox

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from listaservizi.controller.ControlloreListaServizi import ControlloreListaServizi
from listaservizi.views.VistaInserisciServizio import VistaInserisciServizio
from servizio.views.VistaServizio import VistaServizio


class VistaListaServizi(QWidget):
    def __init__(self,parent=None):
        super(VistaListaServizi, self).__init__(parent)

        self.controller= ControlloreListaServizi()
        self.controller_prenotazioni = ControlloreListaPrenotazioni()

        h_layout = QHBoxLayout()
        self.list_view= QListView()
        self.listview_model= QStandardItemModel(self.list_view)
        for servizio in self.controller.get_lista_servizi():
            item = QStandardItem()
            item.setText(servizio.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        h_layout.addWidget(self.list_view)

        button_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        button_layout.addWidget(open_button)

        h_layout.addLayout(button_layout)

        button_new = QPushButton("Nuovo")
        button_new.clicked.connect(self.show_new_servizio)
        button_layout.addWidget(button_new)

        button_new = QPushButton("Cerca")
        lbl_reparto = QLabel("Reparto")
        lbl_posto_letto = QLabel("Posto letto")
        self.lineedit_reparto = QLineEdit(self)
        self.lineedit_posto_letto = QLineEdit(self)
        button_new.clicked.connect(self.search_servizio)
        button_layout.addWidget(lbl_reparto)
        button_layout.addWidget(self.lineedit_reparto)
        button_layout.addWidget(lbl_posto_letto)
        button_layout.addWidget(self.lineedit_posto_letto)
        button_layout.addWidget(button_new)

        button_layout.addStretch()

        self.setLayout(h_layout)
        self.resize(800,500)
        self.setWindowTitle("Lista Servizi")

    def lista_prenotazioni(self, nome):
        for prenotazione in self.controller_prenotazioni.get_lista_delle_prenotazioni():
            if prenotazione.servizio.nome.lower() == nome.lower():
                newdate = datetime.strptime(prenotazione.data, '%d/%m/%Y')
                if newdate.date() <= date.today():
                    return prenotazione.data
        return None

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        if (len(self.list_view.selectedIndexes())>0):
            selected = self.list_view.selectedIndexes()[0].data()
            stringa = selected.split()
            servizio_selezionato = self.controller.get_servizio_by_nome(stringa[len(stringa)-1].replace('(', '').replace(')', ''))
            self.vista_servizio = VistaServizio(servizio_selezionato, self.controller.elimina_servizio_by_nome, self.update_ui, self.lista_prenotazioni(servizio_selezionato.nome))
            self.vista_servizio.show()
        else:
            QMessageBox.critical(self, 'Errore', "Selezionare un servizio", QMessageBox.Ok, QMessageBox.Ok)

    def show_new_servizio(self):
        self.vista_inserisci_servizio = VistaInserisciServizio(self.controller, self.update_ui)
        self.vista_inserisci_servizio.show()

    def update_ui(self, reparto_search = "", posto_letto_search = ""):
        self.listview_model = QStandardItemModel(self.list_view)
        self.controller.get_lista_servizi().sort(key=lambda x: x.nome.lower(), reverse=False)
        for servizio in self.controller.get_lista_servizi():
            if reparto_search == "" or ((servizio.reparto.lower()).find(reparto_search.lower())) == 0:
                if posto_letto_search == "" or ((servizio.posto_letto.lower()).find(posto_letto_search.lower())) == 0:
                    item = QStandardItem()
                    item.setText(servizio.nome)
                    item.setEditable(False)
                    font = item.font()
                    font.setPointSize(18)
                    item.setFont(font)
                    item.__setattr__("nome", servizio.nome)
                    self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def search_servizio (self):
        self.update_ui(self.lineedit_reparto.text(),self.lineedit_posto_letto.text())



