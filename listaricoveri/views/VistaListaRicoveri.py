import datetime

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QMessageBox

from listaricoveri.controller.ControlloreListaRicoveri import ControlloreListaRicoveri
from ricovero.controller.ControlloreRicovero import ControlloreRicovero
from ricovero.model.Ricovero import Ricovero
from ricovero.view.VistaModificaRicovero import VistaModificaRicovero
from ricovero.view.VistaRicovero import VistaRicovero


class VistaListaRicoveri(QWidget):

    def __init__(self):
        super(VistaListaRicoveri, self).__init__()

        h_layout = QHBoxLayout()
        self.controller = ControlloreListaRicoveri()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista pazienti attualmente ricoverati')

    def show_selected_info(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].row()
            ricovero_selezionato = self.controller.get_ricovero_by_index(selected)
            self.vista_ricovero = VistaModificaRicovero(ricovero_selezionato, self.update_ui)
            self.vista_ricovero.show()
        else:
            QMessageBox.critical(self, 'Errore', "Selezionare un paziente", QMessageBox.Ok, QMessageBox.Ok)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        self.controller.aggiungi_ricovero()
        for paziente_ricoverato in self.controller.get_lista_dei_ricoveri():
            item = QStandardItem()
            item.setText(paziente_ricoverato.nome + ' ' + paziente_ricoverato.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    def closeEvent(self, event):
        self.controller.save_data()