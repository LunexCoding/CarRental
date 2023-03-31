from PySide2 import QtGui
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal

from forms.ui_elementCar import Ui_elementCar


class ElementCar(QWidget):
    _delete = Signal()
    _edit = Signal(str, str, str, str, str)

    def __init__(self, model, year, specifications, imagePath, cost, parent=None):
        super(ElementCar, self).__init__(parent)
        self.ui = Ui_elementCar()
        self.ui.setupUi(self)

        font = QFont('MS Shell Dql 2', 10)

        self._model = model
        self._year = year
        self._specifications = specifications
        self._imagePath = imagePath
        self._cost = cost

        self.ui.model.setText(self._model)
        self.ui.year.setText(self._year)
        self.ui.specifications.setText(self._specifications)
        self.ui.specifications.setFont(font)
        self.ui.cost.setText(self._cost)

        size = self.ui.imageArea.size()
        img = QtGui.QImage(self._imagePath)
        pixmap = QtGui.QPixmap(img.scaled(size))
        self.ui.imageArea.setPixmap(pixmap)

        self.ui.deleteCarBtn.clicked.connect(self.delete)
        self.ui.editCarBtn.clicked.connect(self.edit)
        self.ui.editCarBtn.clicked.connect(self._showButtonBox)

        # self._hideButtonBox()

    def delete(self):
        self._delete.emit()

    def edit(self):
        self._edit.emit(self._model, self._year, self._specifications, self._imagePath, self._cost)

    def _showButtonBox(self):
        self.ui.buttonBox.show()

    def _hideButtonBox(self):
        self.ui.buttonBox.hide()
