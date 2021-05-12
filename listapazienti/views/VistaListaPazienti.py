from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listapazienti.controller.ControlloreListaPazienti import ControlloreListaPazienti
from listapazienti.views.VistaInserisciPaziente import VistaInserisciPaziente
from paziente.view.VistaPaziente import VistaPaziente


class VistaListaPazienti(QWidget):

    def __init__(self, parent=None):
        super(VistaListaPazienti, self).__init__(parent)

        self.controller = ControlloreListaPazienti()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        button_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self .show_selected_info)
        button_layout.addWidget(open_button)

        button_new = QPushButton("Nuovo")
        button_new.clicked.connect(self.show_new_paziente)
        button_layout.addWidget(button_new)

        button_layout.addStretch()

        h_layout.addLayout(button_layout)

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Lista Pazienti")

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for paziente in self.controller.get_lista_pazienti():
            item = QStandardItem()
            item.setText(paziente.nome + " " + paziente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        paziente_selezionato = self.controller.get_paziente_by_index(selected)
        self.vista_paziente = VistaPaziente(paziente_selezionato, self.controller.archivia_paziente_by_cf, self.update_ui)
        self.vista_paziente.show()

    def show_new_paziente(self):
        self.vista_inserisci_paziente = VistaInserisciPaziente(self.controller, self.update_ui)
        self.vista_inserisci_paziente.show()

    def closeEvent(self, event):
        self.controller.save_data()