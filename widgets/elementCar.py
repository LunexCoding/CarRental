from pathlib import Path

from PySide2 import QtGui
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal

from forms.ui_elementCar import Ui_elementCar


IMAGE_CARS = "imageCars"


class ElementCar(QWidget):
    _delete = Signal(str, str, str, str, str)
    _edit = Signal(str, str, str, str, str)

    def __init__(self, userRole, model, year, imagePath, specifications, cost, parent=None):
        super(ElementCar, self).__init__(parent)
        self.ui = Ui_elementCar()
        self.ui.setupUi(self)

        font = QFont('MS Shell Dql 2', 10)

        self.userRole = userRole

        self._model = model
        self._year = year
        self._imagePath = f"{IMAGE_CARS}/{imagePath}"
        self._specifications = specifications
        self._cost = cost

        self.ui.model.setText(self._model)
        self.ui.year.setText(self._year)
        self.ui.specifications.setText(self._specifications)
        self.ui.specifications.setFont(font)
        self.ui.cost.setText(self._cost)

        if self.userRole != 'admin':
            self.hideAdminElements()

        size = self.ui.imageArea.size()
        img = QtGui.QImage(self._imagePath)
        pixmap = QtGui.QPixmap(img.scaled(size))
        self.ui.imageArea.setPixmap(pixmap)

        self.ui.deleteCarBtn.clicked.connect(self.delete)
        self.ui.editCarBtn.clicked.connect(self.edit)

    def hideAdminElements(self):
        self.ui.buttonBox.hide()

    def delete(self):
        self._delete.emit(self._model, self._year, self._imagePath, self._specifications, self._cost)

    def edit(self):
        self._edit.emit(self._model, self._year, self._imagePath, self._specifications, self._cost)

    def _showButtonBox(self):
        self.ui.buttonBox.show()

    def _hideButtonBox(self):
        self.ui.buttonBox.hide()
