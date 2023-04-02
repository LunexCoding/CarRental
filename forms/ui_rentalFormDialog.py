# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rentalFormDialoggNNuLV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_rentalFormDialog(object):
    def setupUi(self, rentalFormDialog):
        if not rentalFormDialog.objectName():
            rentalFormDialog.setObjectName(u"rentalFormDialog")
        rentalFormDialog.setWindowModality(Qt.WindowModal)
        rentalFormDialog.resize(315, 355)
        rentalFormDialog.setMinimumSize(QSize(315, 355))
        rentalFormDialog.setMaximumSize(QSize(315, 355))
        rentalFormDialog.setStyleSheet(u"* {\n"
"	color: #fff;\n"
"	background-color: #2a2f38;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #16191d;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}")
        rentalFormDialog.setSizeGripEnabled(False)
        rentalFormDialog.setModal(False)
        self.verticalLayout_2 = QVBoxLayout(rentalFormDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(rentalFormDialog)
        self.frame_5.setObjectName(u"frame_5")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_6.addWidget(self.label_4)

        self.errorLabel = QLabel(self.frame_5)
        self.errorLabel.setObjectName(u"errorLabel")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.errorLabel.setFont(font1)
        self.errorLabel.setStyleSheet(u"color: red;")

        self.verticalLayout_6.addWidget(self.errorLabel, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame = QFrame(rentalFormDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setMaximumSize(QSize(400, 400))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 20)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.inputFullName = QLineEdit(self.frame_4)
        self.inputFullName.setObjectName(u"inputFullName")
        self.inputFullName.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_4.addWidget(self.inputFullName)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.inputPhone = QLineEdit(self.frame_2)
        self.inputPhone.setObjectName(u"inputPhone")
        self.inputPhone.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout.addWidget(self.inputPhone)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.inputEmail = QLineEdit(self.frame_3)
        self.inputEmail.setObjectName(u"inputEmail")
        self.inputEmail.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_3.addWidget(self.inputEmail)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonBox = QDialogButtonBox(self.frame_6)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Yes)
        self.buttonBox.setCenterButtons(True)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(rentalFormDialog)

        QMetaObject.connectSlotsByName(rentalFormDialog)
        self.buttonBox.accepted.connect(rentalFormDialog.accept)
        self.buttonBox.rejected.connect(rentalFormDialog.reject)
    # setupUi

    def retranslateUi(self, rentalFormDialog):
        rentalFormDialog.setWindowTitle(QCoreApplication.translate("rentalFormDialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("rentalFormDialog", u"\u0424\u043e\u0440\u043c\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438 \u0437\u0430\u044f\u0432\u043a\u0438 \u043d\u0430 \u0430\u0440\u0435\u043d\u0434\u0443", None))
        self.errorLabel.setText(QCoreApplication.translate("rentalFormDialog", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("rentalFormDialog", u"\u0424\u0418\u041e:", None))
        self.label_2.setText(QCoreApplication.translate("rentalFormDialog", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d:", None))
        self.label_3.setText(QCoreApplication.translate("rentalFormDialog", u"Email:", None))
    # retranslateUi

