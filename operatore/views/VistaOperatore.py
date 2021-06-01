from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from operatore.controller.ControlloreOperatore import ControlloreOperatore
from operatore.views.VistaModificaOperatore import VistaModificaOperatore


class VistaOperatore(QWidget):

    def __init__(self, operatore, elimina_operatore, elimina_callback, parent = None):
        super(VistaOperatore, self).__init__(parent)
        self.operatore = operatore
        self.controller = ControlloreOperatore(operatore)
        self.elimina_operatore = elimina_operatore
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        lbl_nome_cognome = QLabel (self.controller.get_nome_operatore() + " " + self.controller.get_cognome_operatore())
        font_nome_cognome = lbl_nome_cognome.font()
        font_nome_cognome.setPointSize(30)
        lbl_nome_cognome.setFont(font_nome_cognome)
        v_layout.addWidget(lbl_nome_cognome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_label_info("Id", self.controller.get_id_operatore()))
        v_layout.addWidget(self.get_label_info("Codice Fiscale", self.controller.get_cf_operatore()))
        v_layout.addWidget(self.get_label_info("Data di nascita", self.controller.get_data_nascita_operatore()))
        v_layout.addWidget(self.get_label_info("Luogo di nascita", self.controller.get_luogo_nascita_operatore()))
        v_layout.addWidget(self.get_label_info("Email", self.controller.get_email_operatore()))
        v_layout.addWidget(self.get_label_info("Ruolo", self.controller.get_ruolo_operatore()))
        v_layout.addWidget(self.get_label_info("Password", self.controller.get_password_operatore()))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina operatore")
        btn_elimina.clicked.connect(self.conferma_eliminazione)
        v_layout.addWidget(btn_elimina)

        btn_modifica = QPushButton("Modifica Operatore")
        btn_modifica.clicked.connect(self.modifica_operatore_click)
        v_layout.addWidget(btn_modifica)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_operatore() + ' ' + self.controller.get_cognome_operatore())
        self.setStyleSheet("background-color: #ffd597")

    def get_label_info(self, txt, val):
        lbl = QLabel("{}: {}".format(txt, val))
        lbl_font = lbl.font()
        lbl_font.setPointSize(18)
        lbl.setFont(lbl_font)
        return lbl

    def conferma_eliminazione(self):
        msgbox = QMessageBox()
        msgbox.setText("sei sicuro di voler eliminare l'operatore selezionato?")
        msgbox.setWindowTitle("Conferma")
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.Yes)
        ris= msgbox.exec()
        if(ris== QMessageBox.Yes):
            self.elimina_operatore_click()

    def elimina_operatore_click(self):
        self.elimina_operatore(self.controller.get_id_operatore())
        self.elimina_callback()
        self.close()

    def modifica_operatore_click(self):
        self.vista_modifica_operatore= VistaModificaOperatore(self.operatore, self.elimina_callback)
        self.vista_modifica_operatore.show()
        self.close()