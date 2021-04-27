import sys
from PyQt5.QtWidgets import QApplication, QWidget

from Home.views.VistaHome import VistaHome

if __name__ == '__main__':
        app = QApplication(sys.argv)
        vista_home = VistaHome()
        vista_home.show()
        sys.exit(app.exec())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#provaaaa