from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from operatore.controller.ControlloreOperatore import ControlloreOperatore


class VistaOperatore(QWidget):

    def __init__(self, operatore, elimina_operatore, elimina_callback, parent = None):
        super(VistaOperatore, self).__init__(parent)
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

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina operatore")
        btn_elimina.clicked.connect(self.elimina_operatore_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_operatore() + ' ' + self.controller.get_cognome_operatore())

    def get_label_info(self, txt, val):
        lbl = QLabel("{}: {}".format(txt, val))
        lbl_font = lbl.font()
        lbl_font.setPointSize(18)
        lbl.setFont(lbl_font)
        return lbl

    def elimina_operatore_click(self):
        self.elimina_operatore(self.controller.get_id_operatore())
        self.elimina_callback()
        self.close()