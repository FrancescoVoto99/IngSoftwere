from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox

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

        button_new = QPushButton("Cerca")
        lbl_nome = QLabel("Nome")
        lbl_cognome = QLabel("Cognome")
        self.lineedit_nome = QLineEdit(self)
        self.lineedit_cognome = QLineEdit(self)
        button_new.clicked.connect(self.search_operatore)
        button_layout.addWidget(lbl_nome)
        button_layout.addWidget(self.lineedit_nome)
        button_layout.addWidget(lbl_cognome)
        button_layout.addWidget(self.lineedit_cognome)
        button_layout.addWidget(button_new)

        button_layout.addStretch()

        h_layout.addLayout(button_layout)

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Lista Pazienti")

    def update_ui(self, nome_search = "", cognome_search = ""):
        self.listview_model = QStandardItemModel(self.list_view)
        for paziente in self.controller.get_lista_pazienti():
            if nome_search == "" or paziente.nome.lower() == nome_search.lower():
                if cognome_search == "" or paziente.cognome.lower() == cognome_search.lower():
                    item = QStandardItem()
                    item.setText(paziente.nome + " " + paziente.cognome)
                    item.setEditable(False)
                    font = item.font()
                    font.setPointSize(18)
                    item.setFont(font)
                    item.__setattr__("cf", paziente.cf)
                    self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_selected_info(self):
        if (len(self.list_view.selectedIndexes()) > 0):
            selected = self.list_view.selectedIndexes()[0].data()
            paziente_selezionato = self.controller.get_paziente_by_cf(selected.replace(" ", ""))
            self.vista_paziente = VistaPaziente(paziente_selezionato, self.controller.archivia_paziente_by_cf, self.update_ui)
            self.vista_paziente.show()
        else:
            QMessageBox.critical(self, 'Errore', "Selezionare un paziente", QMessageBox.Ok, QMessageBox.Ok)

    def show_new_paziente(self):
        self.vista_inserisci_paziente = VistaInserisciPaziente(self.controller, self.update_ui)
        self.vista_inserisci_paziente.show()

    def search_operatore (self):
        self.update_ui(self.lineedit_nome.text(),self.lineedit_cognome.text())

    def closeEvent(self, event):
        self.controller.save_data()
