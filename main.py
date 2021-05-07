import sys
from PyQt5.QtWidgets import QApplication, QWidget

from autenticazione.views.VistaAutenticazione import VistaAutenticazione

if __name__ == '__main__':
        app = QApplication(sys.argv)
        vista_autenticazione = VistaAutenticazione()
        vista_autenticazione.show()
        sys.exit(app.exec())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
