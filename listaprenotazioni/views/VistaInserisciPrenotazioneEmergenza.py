from datetime import datetime, date

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QComboBox, QDateEdit, \
    QRadioButton, QMessageBox, QLineEdit

from listapazienti.controller.ControlloreListaPazienti import ControlloreListaPazienti
from listaservizi.controller.ControlloreListaServizi import ControlloreListaServizi
from prenotazione.model.Prenotazione import Prenotazione


class VistaInserisciPrenotazioneEmergenza(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciPrenotazioneEmergenza, self).__init__()
        self.controller = controller
        self.controller_pazienti = ControlloreListaPazienti()
        self.callback = callback
        self.info = {}
        self.list_reparti = ["Oncologia", "Chirurgia", "Cardiologia", "Medicina", "Riabilitazione"]

        self.label_reparto = QLabel()
        self.label_paziente = QLabel()

        self.v_layout = QVBoxLayout()

        self.get_data("Data di inizio ricovero")
        self.get_paziente("Paziente")
        self.get_reparto("Reparto")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.setFont(QFont('Verdana', 15))
        btn_ok.clicked.connect(self.add_prenotazione)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.resize(300, 500)
        self.setWindowTitle('Nuova Prenotazione')
        self.setStyleSheet("QWidget{background-color: #ffffac} QPushButton{background-color: gold}")

    def get_paziente(self, titolo):
        lbl = QLabel(titolo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.v_layout.addWidget(lbl)
        combo_pazienti = QComboBox()
        for paziente in self.controller_pazienti.get_lista_pazienti():
            combo_pazienti.addItem(paziente.cf)
        self.v_layout.addWidget(combo_pazienti)
        combo_pazienti.activated[str].connect(self.tipo_onClicked)
        self.v_layout.addWidget(self.label_paziente)
        self.info[titolo] = self.label_paziente

    def tipo_onClicked(self, text):
        self.label_paziente.setText(text)

    def get_data(self,tipo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.v_layout.addWidget(lbl)
        today = date.today()
        date_edit = QLabel(today.strftime('%d/%m/%Y'))
        date_edit.setFont(font_lbl)
        self.v_layout.addWidget(date_edit)
        self.info[tipo] = date_edit

    def get_reparto(self, tipo):
        lbl = QLabel(tipo)
        font_lbl = lbl.font()
        font_lbl.setPointSize(17)
        font_lbl.setBold(True)
        lbl.setFont(font_lbl)
        self.v_layout.addWidget(lbl)
        for element in self.list_reparti:
            rbtn = QRadioButton(element)
            self.v_layout.addWidget(rbtn)
            rbtn.toggled.connect(self.reparto_onClicked)
        self.v_layout.addWidget(self.label_reparto)
        self.info[tipo] = self.label_reparto

    def reparto_onClicked(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.label_reparto.setText(rbtn.text())

    def add_prenotazione(self):
        controller_servizi = ControlloreListaServizi()
        data = self.info["Data di inizio ricovero"].text()
        newdate = datetime.strptime(data, '%d/%m/%Y')
        paziente = self.controller_pazienti.get_paziente_by_cf(self.info["Paziente"].text())
        servizio = controller_servizi.get_servizio_by_reparto(self.info["Reparto"].text())
        if data == "" or paziente == "" or servizio == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)
        elif servizio == None:
                QMessageBox.critical(self, 'Errore', "Tutti i servizi in questo reparto sono occupati, spostare il paziente in un'altra struttura",
                  QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_prenotazione(Prenotazione((paziente.cognome + paziente.nome).lower(), paziente, servizio, data, None))
            servizio.prenota(newdate.date())
            servizio.is_prenotato()
            controller_servizi.save_data()
            self.callback()
            self.close()