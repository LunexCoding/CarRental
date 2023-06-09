# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elementCarxmuWik.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_elementCar(object):
    def setupUi(self, elementCar):
        if not elementCar.objectName():
            elementCar.setObjectName(u"elementCar")
        elementCar.resize(600, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementCar.sizePolicy().hasHeightForWidth())
        elementCar.setSizePolicy(sizePolicy)
        elementCar.setMinimumSize(QSize(600, 650))
        elementCar.setMaximumSize(QSize(602, 650))
        elementCar.setStyleSheet(u"* {\n"
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
"}\n"
"\n"
"QTextEdit {\n"
"	font-size: 10px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(elementCar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 20, 20)
        self.groupBox = QGroupBox(elementCar)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(650, 800))
        self.groupBox.setStyleSheet(u"border: none")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(630, 320))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.imageArea = QLabel(self.frame_3)
        self.imageArea.setObjectName(u"imageArea")
        self.imageArea.setMinimumSize(QSize(580, 315))
        self.imageArea.setMaximumSize(QSize(580, 315))

        self.verticalLayout_4.addWidget(self.imageArea)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_6)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(5)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.model = QLabel(self.frame_6)
        self.model.setObjectName(u"model")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.model.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.model)

        self.year = QLabel(self.frame_6)
        self.year.setObjectName(u"year")
        font1 = QFont()
        font1.setItalic(True)
        self.year.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.year)


        self.verticalLayout_5.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_5)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.cost = QLabel(self.frame_5)
        self.cost.setObjectName(u"cost")
        self.cost.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.cost)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_4)


        self.verticalLayout_5.addWidget(self.frame_5, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_18 = QFrame(self.frame)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setMinimumSize(QSize(0, 170))
        self.frame_18.setMaximumSize(QSize(16777215, 175))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.specificationsOptions = QTextEdit(self.frame_18)
        self.specificationsOptions.setObjectName(u"specificationsOptions")
        self.specificationsOptions.setMaximumSize(QSize(175, 175))
        self.specificationsOptions.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.specificationsOptions)

        self.specifications = QLabel(self.frame_18)
        self.specifications.setObjectName(u"specifications")
        self.specifications.setMaximumSize(QSize(175, 175))

        self.horizontalLayout_15.addWidget(self.specifications)


        self.verticalLayout_6.addWidget(self.frame_18, 0, Qt.AlignLeft)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.openRentalFormBtn = QPushButton(self.frame_7)
        self.openRentalFormBtn.setObjectName(u"openRentalFormBtn")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.openRentalFormBtn.setFont(font2)
        self.openRentalFormBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.openRentalFormBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/shopping-bag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openRentalFormBtn.setIcon(icon)
        self.openRentalFormBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.openRentalFormBtn, 0, Qt.AlignHCenter)

        self.buttonBox = QFrame(self.frame_7)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMaximumSize(QSize(70, 16777215))
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setFrameShape(QFrame.StyledPanel)
        self.buttonBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.buttonBox)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.deleteCarBtn = QPushButton(self.buttonBox)
        self.deleteCarBtn.setObjectName(u"deleteCarBtn")
        self.deleteCarBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteCarBtn.setIcon(icon1)
        self.deleteCarBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.deleteCarBtn)


        self.horizontalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout_6.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(elementCar)

        QMetaObject.connectSlotsByName(elementCar)
    # setupUi

    def retranslateUi(self, elementCar):
        elementCar.setWindowTitle(QCoreApplication.translate("elementCar", u"Form", None))
        self.groupBox.setTitle("")
        self.imageArea.setText("")
        self.model.setText(QCoreApplication.translate("elementCar", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.year.setText(QCoreApplication.translate("elementCar", u"\u0413\u043e\u0434", None))
        self.cost.setText(QCoreApplication.translate("elementCar", u"\u0426\u0435\u043d\u0430", None))
        self.label_4.setText(QCoreApplication.translate("elementCar", u"/ \u0441\u0443\u0442", None))
        self.specificationsOptions.setHtml(QCoreApplication.translate("elementCar", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041e\u0431\u044a\u0435\u043c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0420"
                        "\u0430\u0441\u0445\u043e\u0436 \u0442\u043e\u043f\u043b\u0438\u0432\u0430</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0422\u0438\u043f \u043f\u0440\u0438\u0432\u043e\u0434\u0430</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u043e\u0432</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041a\u043e\u0440\u043e\u0431\u043a\u0430 \u043f\u0435\u0440\u0435\u0434\u0430\u0447</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0410"
                        "\u0432\u0442\u043e\u0437\u0430\u043f\u0443\u0441\u043a \u0430\u0432\u0442\u043e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0412 \u043d\u0430\u0448\u0435\u043c \u043f\u0430\u0440\u043a\u0435</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0426\u0432\u0435\u0442</span></p></body></html>", None))
        self.specifications.setText(QCoreApplication.translate("elementCar", u"TextLabel", None))
        self.openRentalFormBtn.setText(QCoreApplication.translate("elementCar", u"\u0410\u0440\u0435\u043d\u0434\u0430", None))
        self.deleteCarBtn.setText("")
    # retranslateUi

