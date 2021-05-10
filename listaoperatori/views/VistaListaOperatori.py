from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QLabel, QLineEdit

from listaoperatori.controller.ControlloreListaOperatori import ControlloreListaOperatori
from listaoperatori.views.VistaInserisciOperatore import VistaInserisciOperatore
from operatore.views.VistaOperatore import VistaOperatore


class VistaListaOperatori(QWidget):

    def __init__(self):
        super(VistaListaOperatori, self).__init__()
        self.controller = ControlloreListaOperatori()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        button_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        button_layout.addWidget(open_button)

        button_new = QPushButton("Nuovo")
        button_new.clicked.connect(self.show_new_operatore)
        button_layout.addWidget(button_new)

        button_new = QPushButton("Cerca")
        lbl_nome = QLabel("Nome")
        lbl_cognome = QLabel("Cognome")
        lineedit_nome = QLineEdit(self)
        lineedit_cognome = QLineEdit(self)
        #button_new.clicked.connect(self.search_operatore(lineedit_nome, lineedit_cognome))
        button_layout.addWidget(lbl_nome)
        button_layout.addWidget(lineedit_nome)
        button_layout.addWidget(lbl_cognome)
        button_layout.addWidget(lineedit_cognome)
        button_layout.addWidget(button_new)

        button_layout.addStretch()

        h_layout.addLayout(button_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Lista Operatori")

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for operatore in self.controller.get_lista_operatori():
            item = QStandardItem()
            item.setText(operatore.nome + " " + operatore.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        operatore_selezionato = self.controller.get_operatore_by_index(selected)
        self.vista_operatore = VistaOperatore(operatore_selezionato, self.controller.elimina_operatore_by_id, self.update_ui)
        self.vista_operatore.show()

    def show_new_operatore(self):
        self.vista_inserisci_operatore = VistaInserisciOperatore(self.controller, self.update_ui)
        self.vista_inserisci_operatore.show()

    def search_operatore (self, nome, cognome):
        operatore_cercato = self.controller.search_operatore_by_nomecognome(nome, cognome)
        self.cerca_operatore = VistaOperatore(operatore_cercato, self.controller.search_operatore_by_nomecognome, self.update_ui)
        self.cerca_operatore.show()

    def closeEvent(self, event):
        self.controller.save_data()