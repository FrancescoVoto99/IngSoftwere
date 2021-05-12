from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QBoxLayout, QListView, QHBoxLayout, QVBoxLayout, QPushButton

from listaservizi.controller.ControlloreListaServizi import ControlloreListaServizi
from listaservizi.views.VistaInserisciServizio import VistaInserisciServizio
from servizio.views.VistaServizio import VistaServizio


class VistaListaServizi(QWidget):
    def __init__(self,parent=None):
        super(VistaListaServizi, self).__init__(parent)

        self.controller= ControlloreListaServizi()

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

        button_layout.addStretch()

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Lista Servizi")

    def closeEvent(self, event):
        print ("ON CLOSE")
        self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        servizio_selezionato = self.controller.get_servizio_by_index(selected)
        self.vista_servizio = VistaServizio(servizio_selezionato)
        self.vista_servizio.show()

    def show_new_servizio(self):
        self.vista_inserisci_servizio = VistaInserisciServizio(self.controller, self.update_ui)
        self.vista_inserisci_servizio.show()

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for servizio in self.controller.get_lista_servizi():
            item = QStandardItem()
            item.setText(servizio.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)



