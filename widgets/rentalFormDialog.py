from Custom_Widgets.Widgets import QDialog

from forms.ui_rentalFormDialog import Ui_rentalFormDialog

from emailSend import emailSender


class RentalFormDialog(QDialog):
    def __init__(self, parent=None):
        super(RentalFormDialog, self).__init__(parent)
        self.ui = Ui_rentalFormDialog()
        self.ui.setupUi(self)
        self.ui.errorLabel.hide()

    def __showErrorLabel(self, message):
        self.ui.errorLabel.setText(message)
        self.ui.errorLabel.show()

    def sendEmail(self, message):
        fullName = self.ui.inputFullName.text()
        email = self.ui.inputEmail.text()
        if self.validate():
            emailSender.sendEmail(
                email=email,
                subject="Заявка на аренду автомобиля",
                message=f"{fullName}, мы получили вашу заявку на аренду: {message}.\nСкоро мы свяжемся с вами."
            )

    def validate(self):
        fullName = self.ui.inputFullName.text()
        phone = self.ui.inputPhone.text()
        email = self.ui.inputEmail.text()
        if all([len(fullName), len(phone), len(email)]):
            if not emailSender.validateEmail(email):
                self.__showErrorLabel("Невалидный Email!")
                return False
            self.ui.errorLabel.hide()
            return True
        self.__showErrorLabel("Все поля должны быть заполнены!")
        return False
