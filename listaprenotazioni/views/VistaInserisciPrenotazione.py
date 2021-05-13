import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox, QTextEdit, QWidget

from listapazienti.views.VistaInserisciPaziente import VistaInserisciPaziente
from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazione(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazione, self).__init__()
        self.controller = controller
        self.callback = callback

        #self.controller = ControlloreListaPrenotazioni()

        v_layout = QVBoxLayout()

        v_layout.addWidget(QLabel("Data (dd/MM/yyyy)"))
        self.text_data = QLineEdit(self)
        v_layout.addWidget(self.text_data)

        v_layout.addWidget(QLabel("paziente"))
        self.text_paziente = QLineEdit(self)
        v_layout.addWidget(self.text_paziente)


        self.combo_servizi = QComboBox()
        self.comboservizi_model = QStandardItemModel(self.combo_servizi)
        if os.path.isfile('listaservizi/data/lista_servizi_salvata.pickle'):
            with open('listaservizi/data/lista_servizi_salvata.pickle', 'rb') as f:
                self.lista_servizi = pickle.load(f)
            self.lista_servizi_disponibili = [s for s in self.lista_servizi.get_lista_servizi() if s.is_disponibile()]
            for servizio in self.lista_servizi_disponibili:
                item = QStandardItem()
                item.setText(servizio.nome)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboservizi_model.appendRow(item)
            self.combo_servizi.setModel(self.comboservizi_model)
        v_layout.addWidget(QLabel("Servizio"))
        v_layout.addWidget(self.combo_servizi)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prenotazione)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuova Prenotazione')

    def add_prenotazione(self):
        data = self.text_data.text()
        paziente = self.text_paziente.text()
        servizio = self.lista_servizi_disponibili[self.combo_servizi.currentIndex()]
        if data == "" or paziente == "" or not servizio:
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(Prenotazione((servizio.nome).lower(), paziente, servizio, data))
            servizio.prenota()
            with open('listaservizi/data/lista_servizi_salvata.pickle', 'wb') as handle:
                pickle.dump(self.lista_servizi, handle, pickle.HIGHEST_PROTOCOL)
            self.callback()
            self.close()
