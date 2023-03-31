from Custom_Widgets.Widgets import *
from PySide2.examples.widgets.layouts.flowlayout import FlowLayout

from forms.ui_interface import Ui_MainWindow
from widgets.flowLayout import FlowLayout
from widgets.elementCar import ElementCar


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()

        font = QFont('MS Shell Dql 2', 10)
        self.ui.inputSpecifications.setFont(font)

        self.ui.labelErrorAddCar.hide()

        self.flowCarLayout = FlowLayout()
        self.ui.carLayout.addLayout(self.flowCarLayout)

        self.ui.saveCarBtn.clicked.connect(lambda: self.addCar())
        self.ui.previewImageBtn.clicked.connect(lambda: self.showImage())

    def showErrorLabelAddCar(self, message):
        self.ui.labelErrorAddCar.setText(message)
        self.ui.labelErrorAddCar.show()

    def addCar(self):
        if self._validateAddCarForm():
            self.ui.labelErrorAddCar.hide()
            self.__carAdded()
        else:
            ...

    def _validateAddCarForm(self):
        model = self.ui.inputModel.text()
        year = self.ui.inputModelYear.text()
        image = self.ui.inputImagePath.text()
        specifications = self.ui.inputSpecifications.toPlainText()
        cost = self.ui.inputCost.text()
        if (all([len(model), len(year), len(image), len(specifications), len(cost)])):
            if not year.isdecimal() or not cost.isdecimal():
                self.showErrorLabelAddCar("Поля <Год> и <Стоимость аренды в сутки> принимает только числовой тип!")
                return False
            if "характеристика" in specifications:
                self.showErrorLabelAddCar("Все характеристики должны быть указаны!")
                return False
            return True
        self.showErrorLabelAddCar("Все поля должны быть заполнены!")
        return False

    def showImage(self):
        if len(self.ui.inputImagePath.text()):
            size = self.ui.imageArea.size()
            img = QtGui.QImage(self.ui.inputImagePath.text())
            pixmap = QtGui.QPixmap(img.scaled(size))
            self.ui.imageArea.setPixmap(pixmap)
        else:
            self.showErrorLabelAddCar("Не указан путь к изображению!")

    def __carAdded(self):
        itemCar = ElementCar(
            self.ui.inputModel.text(),
            self.ui.inputModelYear.text(),
            self.ui.inputSpecifications.toPlainText(),
            self.ui.inputImagePath.text(),
            self.ui.inputCost.text()
        )
        self.flowCarLayout.addWidget(itemCar)
        itemCar._delete.connect(self.__deleteCar)
        itemCar._edit.connect(self.__editCar)

        self.ui.inputModel.clear()
        self.ui.inputModelYear.clear()
        self.ui.inputSpecifications.setText("характеристика\n" * 8 + "характеристика")
        self.ui.inputImagePath.clear()
        self.ui.inputCost.clear()

    def __deleteCar(self):
        widget = self.sender()
        self.flowCarLayout.removeWidget(widget)
        widget.deleteLater()

    def __editCar(self, model, year, specifications, imagePath, cost):
        self.ui.mainPages.setCurrentIndex(1)
        self.ui.inputModel.setText(model)
        self.ui.inputModelYear.setText(year)
        self.ui.inputSpecifications.setText(specifications)
        self.ui.inputImagePath.setText(imagePath)
        self.ui.inputCost.setText(cost)
        self.showImage()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())
