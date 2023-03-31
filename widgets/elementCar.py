from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal

from forms.ui_elementCar import Ui_elementCar


class ElementCar(QWidget):
    _delete = Signal()
    _edit = Signal(str)
    _update = Signal(str, float)

    def __init__(self, model, year, imagePath, cost, parent=None):
        super(ElementCar, self).__init__(parent)
        # g_storage.onProductUpdated.register(self._onProductAdded)
        self.ui = Ui_elementCar()
        self.ui.setupUi(self)
        # self._widgetID = widgetID
        self.ui.model.setText(model)
        self.ui.year.setText(year)
        self._imagePath = imagePath
        self.ui.cost.setText(str(cost))

        self.ui.deleteCarBtn.clicked.connect(self.delete)
        self.ui.editCarBtn.clicked.connect(self._showButtonBox)

        # self._hideButtonBox()

    def delete(self):
        self._delete.emit()

    def _showButtonBox(self):
        self.ui.buttonBox.show()

    def _hideButtonBox(self):
        self.ui.buttonBox.hide()
