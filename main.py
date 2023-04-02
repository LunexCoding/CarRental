from decouple import config
from pathlib import Path

from Custom_Widgets.Widgets import *
from PySide2.examples.widgets.layouts.flowlayout import FlowLayout

from forms.ui_interface import Ui_MainWindow
from widgets.flowLayout import FlowLayout
from widgets.elementCar import ElementCar
from widgets.rentalFormDialog import RentalFormDialog, emailSender

from helpers.fileSystem import fileSystem
from helpers.database import databaseSession
from helpers.sqlQueries import SqlQueries
from helpers.server import ftpServer
from settingsConfig import settingsConfig


IMAGE_CARS = Path("imageCars")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()

        self.userRole = "user"

        font = QFont('MS Shell Dql 2', 10)
        self.ui.inputSpecifications.setFont(font)
        self.ui.inputCommand.setFont(font)

        self.ui.labelErrorAddCar.hide()
        self.ui.labelErrorShell.hide()
        if self.userRole != 'admin':
            self.__hideAdminElements()

        self.flowCarLayout = FlowLayout()
        self.ui.carLayout.addLayout(self.flowCarLayout)

        self.ui.userModeBtn.clicked.connect(lambda: self.__activateUserRole())
        self.ui.saveCarBtn.clicked.connect(lambda: self.addCar())
        self.ui.previewImageBtn.clicked.connect(lambda: self.showImageAddCarPage())
        self.ui.executeBtn.clicked.connect(lambda: self.__executeCommand())

    def __loadData(self):
        fileSystem.makeDir(IMAGE_CARS, recreate=True)
        for image in ftpServer.listDir():
            ftpServer.downloadFile(image)
        with databaseSession as db:
            data = db.getRows(SqlQueries.selectAllCars())
            if data:
                for car in data:
                    self.ui.inputModel.setText(car["model"])
                    self.ui.inputModelYear.setText(str(car["modelYear"]))
                    self.ui.inputImagePath.setText(f'{IMAGE_CARS}/{car["image"]}')
                    self.ui.inputSpecifications.setText(car["specifications"])
                    self.ui.inputCost.setText(str(car["cost"]))
                    self.__carWidgetAdded()
                    self.__clearAddCarForm()

    def __activateUserRole(self):
        self.userRole = "user"
        self.ui.mainPages.setCurrentIndex(0)
        self.__loadData()

    def __activateAdminRole(self):
        self.userRole = "admin"
        self.__showAdminElements()
        self.ui.mainPages.setCurrentIndex(0)
        self.__loadData()

    def __hideAdminElements(self):
        self.ui.addCarBtn.hide()

    def __showAdminElements(self):
        self.ui.addCarBtn.show()

    def __showErrorLabelShell(self, message):
        self.ui.labelErrorShell.setText(message)
        self.ui.labelErrorShell.show()

    def __showErrorLabelAddCar(self, message):
        self.ui.labelErrorAddCar.setText(message)
        self.ui.labelErrorAddCar.show()

    # shell -> command processing
    def __executeCommand(self):
        if self.__validateCommand():
            self.__activateAdminRole()

    def __validateCommand(self):
        commandLine = self.ui.inputCommand.toPlainText().replace("Shell>", "")
        if len(commandLine):
            commandArgs = commandLine.split()
            command = commandArgs.pop(0)
            if command == "admin":
                if len(commandArgs):
                    token = commandArgs.pop(0)
                    if token == config("ADMIN_TOKEN", default=""):
                        self.ui.labelErrorShell.hide()
                        self.ui.inputCommand.setText("Введен верный токен! Ожидайте загрузки")
                        return True
                    else:
                        self.__showErrorLabelShell("Неверный токен!")
                else:
                    self.__showErrorLabelShell("Пропущен аргумент!")
            else:
                self.__showErrorLabelShell("Неверная команда!")
        else:
            self.__showErrorLabelShell("Введите команду!")

    # process of adding a car
    def addCar(self):
        if self.__validateAddCarForm():
            self.__carWidgetAdded()
            self.__addCarToDB()
            self.__clearAddCarForm()

    def __validateAddCarForm(self):
        model = self.ui.inputModel.text()
        modelYear = self.ui.inputModelYear.text()
        image = self.ui.inputImagePath.text()
        specifications = self.ui.inputSpecifications.toPlainText()
        cost = self.ui.inputCost.text()
        if (all([len(model), len(modelYear), len(image), len(specifications), len(cost)])):
            if not modelYear.isdecimal() or not cost.isdecimal():
                self.__showErrorLabelAddCar("Поля <Год> и <Стоимость аренды в сутки> принимает только числовой тип!")
                return False
            if "характеристика" in specifications:
                self.__showErrorLabelAddCar("Все характеристики должны быть указаны!")
                return False
            self.ui.labelErrorAddCar.hide()
            return True
        self.__showErrorLabelAddCar("Все поля должны быть заполнены!")
        return False

    def __carWidgetAdded(self):
        itemCar = ElementCar(
            self.userRole,
            self.ui.inputModel.text(),
            self.ui.inputModelYear.text(),
            self.ui.inputImagePath.text(),
            self.ui.inputSpecifications.toPlainText(),
            self.ui.inputCost.text()
        )
        self.flowCarLayout.addWidget(itemCar)
        itemCar._delete.connect(self.deleteCar)
        itemCar._openRentalForm.connect(self.openRentalForm)

    def openRentalForm(self, model, modelYear, cost):
        dialog = RentalFormDialog()
        responce = dialog.exec_()
        while not dialog.validate():
            dialog.show()
            if responce == QtWidgets.QDialog.Rejected:
                break
        else:
            dialog.sendEmail(f"\nМодуль: {model}\nГод выпуска: {modelYear}\nЦена аренды в сутки: {cost}р\n")

    def __addCarToDB(self):
        model = self.ui.inputModel.text()
        modelYear = self.ui.inputModelYear.text()
        image = self.ui.inputImagePath.text()
        relativeImagePath = Path(image).name
        specifications = self.ui.inputSpecifications.toPlainText()
        cost = self.ui.inputCost.text()
        with databaseSession as db:
            db.execute(
                SqlQueries.insertCar(model, modelYear, image, specifications, cost),
                dict(
                    model=model,
                    modelYear=modelYear,
                    image=relativeImagePath,
                    specifications=specifications,
                    cost=cost
                )
            )
        ftpServer.uploadFile(image)
        filename = fileSystem.getFilename(image, suffix=True)
        if not fileSystem.exists(IMAGE_CARS / filename):
            fileSystem.copyFile(image, IMAGE_CARS / filename)

    def __clearAddCarForm(self):
        self.ui.inputModel.clear()
        self.ui.inputModelYear.clear()
        self.ui.inputImagePath.clear()
        self.ui.inputSpecifications.setText("характеристика\n" * 8 + "характеристика")
        self.ui.inputCost.clear()

    # process of deleting a car
    def deleteCar(self, model, modelYear, image, specifications, cost):
        self.__deleteCarWidget()
        self.__deleteCarFromDB(model, modelYear, image, specifications, cost)

    def __deleteCarWidget(self):
        widget = self.sender()
        self.flowCarLayout.removeWidget(widget)
        widget.deleteLater()

    def __deleteCarFromDB(self, model, modelYear, image, specifications, cost):
        image = Path(image).name
        with databaseSession as db:
            db.execute(
                SqlQueries.deleteCar(model, modelYear, image, specifications, cost),
                dict(
                    model=model,
                    modelYear=modelYear,
                    image=image,
                    specifications=specifications,
                    cost=cost
                )
            )
        ftpServer.deleteFile(image)
        if not fileSystem.exists(IMAGE_CARS / image):
            ftpServer.downloadFile(image)
        fileSystem.remove(IMAGE_CARS / image)

    def showImageAddCarPage(self):
        if len(self.ui.inputImagePath.text()):
            size = self.ui.imageAreaAddCarPage.size()
            img = QtGui.QImage(self.ui.inputImagePath.text())
            pixmap = QtGui.QPixmap(img.scaled(size))
            self.ui.imageAreaAddCarPage.setPixmap(pixmap)
        else:
            self.__showErrorLabelAddCar("Не указан путь к изображению!")


if __name__ == "__main__":
    IMAGE_CARS.mkdir(exist_ok=True)
    emailSender.loadSettings(settingsConfig.settings)
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())
