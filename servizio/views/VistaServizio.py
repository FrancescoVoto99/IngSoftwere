from datetime import datetime, date
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, \
    QMessageBox

from servizio.controller.ControlloreServizio import ControlloreServizio

# Classe responsabile della gestione dell'interfaccia utente:
# permette di visualizzare tutti i dati relativi ai dati
# di un pservizio

class VistaServizio(QWidget):

    def __init__(self, servizio,  elimina_servizio=False, elimina_callback=None, data=None, parent=None):
        super(VistaServizio, self).__init__(parent)
        self.controller = ControlloreServizio(servizio)
        self.data = data
        self.elimina_servizio = elimina_servizio
        self.elimina_callback = elimina_callback

        h_layout = QHBoxLayout()

        v_layout = QVBoxLayout()
        label = self.label_generate(self.controller.get_nome_servizio(), 20)
        v_layout.addWidget(label)

        label = self.label_generate("Id: {}".format(self.controller.get_id_servizio()), 17)
        v_layout.addWidget(label)

        label = self.label_generate("Tipo: {}".format(self.controller.get_tipo_servizio()), 17)
        v_layout.addWidget(label)

        label = self.label_generate("Reparto: {}".format(self.controller.get_reparto_servizio()), 17)
        v_layout.addWidget(label)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label = self.label_generate("Posto letto: {}".format(self.controller.get_posto_letto_servizio()), 17)
        v_layout.addWidget(label)

        h_layout.addLayout(v_layout)

        h_layout.addItem(QSpacerItem(50, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout2 = QVBoxLayout()
        if self.data is not None:
            newdate = datetime.strptime(self.data, '%d/%m/%Y')
            self.controller.prenota(newdate.date())
        label = self.label_generate(self.controller.get_servizio_disponibile(), 25)
        if(self.controller.get_servizio_disponibile() == "Non disponibile" ):
            label.setStyleSheet("color: red")
        else:
            label.setStyleSheet("color: green")
        if self.elimina_servizio:
            btn_elimina = QPushButton("Elimina servizio")
            btn_elimina.clicked.connect(self.conferma_eliminazione)
            v_layout.addWidget(btn_elimina)

        v_layout2.addWidget(label)

        h_layout.addLayout(v_layout2)

        self.setLayout(h_layout)
        self.setWindowTitle(servizio.nome)
        self.setStyleSheet("QWidget{background-color: plum} QPushButton{background-color: mediumorchid} ")

    def label_generate(self, etichetta, dimensione):
        label = QLabel(etichetta)
        font = label.font()
        font.setPointSize(dimensione)
        label.setFont(font)
        return label

    def conferma_eliminazione(self):
        msgbox = QMessageBox()
        msgbox.setText("Sei sicuro di voler eliminare il servizio selezionato?")
        msgbox.setWindowTitle("Conferma")
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.Yes)
        ris= msgbox.exec()
        if(ris== QMessageBox.Yes):
            self.elimina_servizio_click()

    def elimina_servizio_click(self):
        if ((self.controller.is_disponibile()) and (self.controller.prenotato() == False)):
            self.elimina_servizio(self.controller.get_nome_servizio())
        else:
            QMessageBox.critical(self, 'Errore', 'Il servizio selezionato è utilizzato in questo momento',
                                 QMessageBox.Ok, QMessageBox.Ok)
        self.elimina_callback()
        self.close()