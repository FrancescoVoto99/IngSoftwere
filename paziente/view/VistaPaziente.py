from datetime import date, datetime

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni
from paziente.Controller.ControllorePaziente import ControllorePaziente
from paziente.view.VistaModificaPaziente import VistaModificaPaziente

# Classe responsabile della gestione dell'interfaccia utente:
# permette di visualizzare tutti i dati relativi ai dati
# di un paziente

class VistaPaziente(QWidget):
    def __init__(self, paziente, bool, elimina_callback = None, parent=None):
        super(VistaPaziente, self).__init__(parent)
        self.paziente = paziente
        self.bool = bool
        self.controller = ControllorePaziente(paziente)
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_paziente() + " " + self.controller.get_cognome_paziente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_label_info("Sesso", self.controller.get_sesso_paziente()))
        v_layout.addWidget(self.get_label_info("Luogo di nascita", self.controller.get_luogodinascita_paziente()))
        v_layout.addWidget(self.get_label_info("Data di nascita", self.controller.get_datadinascita_paziente()))
        v_layout.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_paziente()))
        v_layout.addWidget(self.get_label_info("Telefono", self.controller.get_telefono_paziente()))
        v_layout.addWidget(self.get_label_info("Email", self.controller.get_email_paziente()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_reparto = QPushButton("Ricovero")
        btn_reparto.clicked.connect(self.check_reparto)
        v_layout.addWidget(btn_reparto)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        if self.bool == True:
          btn_referto = QPushButton("Referto")
          btn_referto.clicked.connect(self.check_referto)
          v_layout.addWidget(btn_referto)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_modifica = QPushButton("Modifica Paziente")
        btn_modifica.clicked.connect(self.modifica_paziente_click)
        v_layout.addWidget(btn_modifica)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_paziente() + " " + self.controller.get_cognome_paziente())
        self.setStyleSheet("QWidget{background-color: lightpink} QPushButton{background-color: palevioletred} ")

    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    def check_reparto(self):
        controller_ricoveri = ControlloreListaPrenotazioni()
        reparto = None
        for prenotazione in controller_ricoveri.get_lista_delle_prenotazioni():
            if prenotazione.paziente.cf == self.controller.get_cf_paziente():
               newdate = datetime.strptime(prenotazione.data, "%d/%m/%Y")
               reparto = prenotazione.servizio.reparto
        if(reparto != None) and newdate.date() <= date.today():
             QMessageBox.about(self, "Reparto" , "Il paziente selezionato ?? ricoverato nel reparto di "+ reparto.upper())
        else:
            if (reparto != None) and newdate.date() > date.today():
                QMessageBox.about(self, "Reparto", "Il paziente selezionato verr?? ricoverato nel reparto di " + reparto.upper() + " il giorno " + newdate.strftime('%d/%m/%Y'))
            else:
                QMessageBox.about (self, "Reparto" , "Il paziente selezionato non ?? ricoverato" )

    def check_referto(self):
        if self.controller.get_referto_paziente() == "":
            QMessageBox.about(self, "Referto", "Non ?? stato inserito alcun referto per il paziente selezionato")
        else:
            QMessageBox.about(self, "Referto", "Il referto inserito dal medico ?? :" + str(self.controller.get_referto_paziente()))

    def modifica_paziente_click(self):
        self.vista_modifica_paziente = VistaModificaPaziente(self.paziente, self.elimina_callback)
        self.vista_modifica_paziente.show()
        self.close()

