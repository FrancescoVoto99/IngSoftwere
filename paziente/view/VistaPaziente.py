from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from paziente.Controller.ControllorePaziente import ControllorePaziente
from listaricoveri.controller.ControlloreListaRicoveri import ControlloreListaPrenotazioni
from paziente.view.VistaModificaPaziente import VistaModificaPaziente
from ricovero.view.VistaRicovero import VistaRicovero


class VistaPaziente(QWidget):
    def __init__(self, paziente, archivia_paziente, elimina_callback, parent=None):
        super(VistaPaziente, self).__init__(parent)
        self.paziente = paziente
        self.controller = ControllorePaziente(paziente)
        self.archivia_paziente = archivia_paziente
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


        btn_ricovero = QPushButton("Ricovero")
        btn_ricovero.clicked.connect(self.check_ricovero)
        v_layout.addWidget(btn_ricovero)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_reparto = QPushButton("Reparto")
        btn_reparto.clicked.connect(self.check_reparto)
        v_layout.addWidget(btn_reparto)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_modifica = QPushButton("Modifica Paziente")
        btn_modifica.clicked.connect(self.modifica_paziente_click)
        v_layout.addWidget(btn_modifica)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        if self.archivia_paziente != None:
            btn_archivia = QPushButton("Archivia")
            btn_archivia.clicked.connect(self.archivia_paziente_click)
            v_layout.addWidget(btn_archivia)

        v_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_paziente() + " " + self.controller.get_cognome_paziente())

    def get_label_info(self, testo, valore):
        current_label = QLabel("{}: {}".format(testo, valore))
        current_font = current_label.font()
        current_font.setPointSize(17)
        current_label.setFont(current_font)
        return current_label

    def check_ricovero(self):
        self.vista_ricovero = VistaRicovero(self.controller.get_ricovero_paziente(), self.controller.aggiungi_nuovo_ricovero_paziente, self.controller.get_cf_paziente())
        self.vista_ricovero.show()

    def check_reparto(self):
        controller_ricoveri = ControlloreListaPrenotazioni()
        reparto=None
        for prenotazione in controller_ricoveri.get_lista_delle_prenotazioni():
            if prenotazione.paziente.cf==self.controller.get_cf_paziente():
                reparto=prenotazione.servizio.reparto
        if(reparto!=None):
             QMessageBox.about(self, "Reparto" , "Il paziente selezionato è ricoverato nel reparto di "+ reparto.upper() )


        else:
            QMessageBox.about (self, "Reparto" , "Il paziente selezionato non è ricoverato" )

    def archivia_paziente_click(self):
        self.archivia_paziente(self.controller.get_cf_paziente())
        self.archivia_callback()
        self.close()

    def modifica_paziente_click(self):
        self.vista_modifica_paziente = VistaModificaPaziente(self.paziente, self.elimina_callback)
        self.vista_modifica_paziente.show()
        self.close()