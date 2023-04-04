import smtplib

from email_validator import validate_email, EmailNotValidError

from settingsConfig import settingsConfig


class _EmailSender:
    def __init__(self, __settings):
        self.__settings = __settings

    def sendEmail(self, email, subject, message):
        sender = self.__settings["email"]
        sender_password = self.__settings["password"]
        mail_lib = smtplib.SMTP_SSL(self.__settings["host"], self.__settings["port"])
        mail_lib.login(sender, sender_password)
        msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (
        sender, email, subject)
        msg += message
        mail_lib.sendmail(sender, email, msg.encode('utf8'))
        mail_lib.quit()

    def validateEmail(self, email):
        try:
            validatedEmail = validate_email(email)
            email = validatedEmail["email"]
            return True
        except EmailNotValidError as e:
            return False


emailSender = _EmailSender(settingsConfig.SMTPSettings)
