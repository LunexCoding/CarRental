from pathlib import Path

from Custom_Widgets.Widgets import *
from PySide2.examples.widgets.layouts.flowlayout import FlowLayout

from forms.ui_interface import Ui_MainWindow
from widgets.flowLayout import FlowLayout
from widgets.elementCar import ElementCar

from helpers.emailSend import emailSender
from helpers.fileSystem import fileSystem
from helpers.database import databaseSession
from helpers.sqlQueries import SqlQueries
from helpers.server import ftpServer
from settingsConfig import settingsConfig


IMAGE_CARS = Path("imageCars")
ADMIN_TOKEN = settingsConfig.AdminSettings["token"]


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
        self.ui.labelRentalForm.hide()

        if self.userRole != 'admin':
            self.__hideAdminElements()

        self.flowCarLayout = FlowLayout()
        self.ui.carLayout.addLayout(self.flowCarLayout)

        self.ui.userModeBtn.clicked.connect(lambda: self.__activateUserRole())
        self.ui.saveCarBtn.clicked.connect(lambda: self.addCar())
        self.ui.previewImageBtn.clicked.connect(lambda: self.showImageAddCarPage())
        self.ui.executeBtn.clicked.connect(lambda: self.__executeCommand())
        self.ui.sendRentaFormBtn.clicked.connect(lambda: self.__sendRentalForm())
        self.ui.closeRentalFormBtn.clicked.connect(lambda: self.__clearRentalForm())

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

    def __showLabelRentalForm(self, message, errorMode=True):
        if errorMode:
            self.ui.labelRentalForm.setStyleSheet("color: red;")
        else:
            self.ui.labelRentalForm.setStyleSheet("color: green;")
        self.ui.labelRentalForm.setText(message)
        self.ui.labelRentalForm.show()


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
                    if token == ADMIN_TOKEN:
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
        itemCar._openRentalForm.connect(self.__openRentalForm)

    # Rental form
    def __openRentalForm(self, model, modelYear, cost):
        if self.ui.labelRentalForm.isVisible():
            self.ui.labelRentalForm.hide()
        self.ui.mainPages.setCurrentIndex(1)
        self.ui.labelCarData.setText(f"Модель: {model}\nГод производства: {modelYear}\nЦена аренды в сутки: {cost}")

    def __sendRentalForm(self):
        carData = self.ui.labelCarData.text()
        if self.__validateRentalForm():
            fullName = self.ui.inputFullName.text()
            email = self.ui.inputEmail.text()
            emailSender.sendEmail(
                email=email,
                subject="Заявка на аренду автомобиля",
                message=f"{fullName}, мы получили вашу заявку на аренду:\n{carData}.\nСкоро мы свяжемся с вами."
            )

    def __validateRentalForm(self):
        fullName = self.ui.inputFullName.text()
        phone = self.ui.inputPhone.text()
        email = self.ui.inputEmail.text()
        if all([len(fullName), len(phone), len(email)]):
            if not emailSender.validateEmail(email):
                self.__showLabelRentalForm("Невалидный Email!")
                return False
            self.ui.labelRentalForm.hide()
            self.__showLabelRentalForm("Заявка отправлена!", False)
            return True
        self.__showLabelRentalForm("Все поля должны быть заполнены!")
        return False

    def __clearRentalForm(self):
        self.ui.labelRentalForm.hide()
        self.ui.inputFullName.clear()
        self.ui.inputPhone.clear()
        self.ui.inputEmail.clear()

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
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())
