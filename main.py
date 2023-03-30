from Custom_Widgets.Widgets import *

from forms.ui_interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())
