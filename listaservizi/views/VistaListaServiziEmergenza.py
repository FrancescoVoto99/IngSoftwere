from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLabel, QLineEdit

from listaservizi.controller.ControlloreListaServizi import ControlloreListaServizi
from servizio.views.VistaServizio import VistaServizio


class VistaListaServiziEmergenza(QWidget):

    def __init__(self, parent = None):
        super(VistaListaServiziEmergenza, self).__init__(parent)

        self.controller = ControlloreListaServizi()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)

        for servizio in self.controller.get_lista_servizi():
            if servizio.tipo == "ricovero di emergenza":
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

        h_layout.addLayout(button_layout)

        self.setLayout(h_layout)
        self.resize(800, 500)
        self.setWindowTitle("Lista Servizi di Emergenza")

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].data()
        stringa = selected.split()
        servizio_selezionato = self.controller.get_servizio_by_nome(stringa[len(stringa) - 1].replace('(', '').replace(')', ''))
        self.vista_servizio = VistaServizio(servizio_selezionato, self.controller.elimina_servizio_by_nome, self.update_ui)
        self.vista_servizio.show()

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()

    def update_ui(self, reparto_search = "", posto_letto_search = ""):
        self.listview_model = QStandardItemModel(self.list_view)
        for servizio in self.controller.get_lista_servizi():
                if servizio.tipo == "ricovero di emergenza":
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