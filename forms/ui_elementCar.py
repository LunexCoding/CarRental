# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elementCareiSAlo.ui'
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
        elementCar.resize(484, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementCar.sizePolicy().hasHeightForWidth())
        elementCar.setSizePolicy(sizePolicy)
        elementCar.setMinimumSize(QSize(0, 0))
        elementCar.setMaximumSize(QSize(485, 500))
        elementCar.setStyleSheet(u"* {\n"
"	color: #fff;\n"
"	background-color: red;\n"
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
        self.verticalLayout_2 = QVBoxLayout(elementCar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(elementCar)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setStyleSheet(u"border: none")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 15, 0, 0)
        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(405, 405))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(400, 400))
        self.label.setMaximumSize(QSize(400, 400))

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
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

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.model)

        self.year = QLabel(self.frame_6)
        self.year.setObjectName(u"year")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.year)


        self.verticalLayout_5.addWidget(self.frame_6)

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

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.cost)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_4)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_2)

        self.buttonBox = QFrame(self.groupBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFrameShape(QFrame.StyledPanel)
        self.buttonBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.buttonBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.deleteCarBtn = QPushButton(self.buttonBox)
        self.deleteCarBtn.setObjectName(u"deleteCarBtn")
        icon = QIcon()
        icon.addFile(u":/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteCarBtn.setIcon(icon)
        self.deleteCarBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.deleteCarBtn)

        self.editCarBtn = QPushButton(self.buttonBox)
        self.editCarBtn.setObjectName(u"editCarBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editCarBtn.setIcon(icon1)
        self.editCarBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.editCarBtn)


        self.horizontalLayout.addWidget(self.buttonBox, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(elementCar)

        QMetaObject.connectSlotsByName(elementCar)
    # setupUi

    def retranslateUi(self, elementCar):
        elementCar.setWindowTitle(QCoreApplication.translate("elementCar", u"Form", None))
        self.groupBox.setTitle("")
        self.label.setText("")
        self.model.setText(QCoreApplication.translate("elementCar", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.year.setText(QCoreApplication.translate("elementCar", u"\u0413\u043e\u0434", None))
        self.cost.setText(QCoreApplication.translate("elementCar", u"\u0426\u0435\u043d\u0430", None))
        self.label_4.setText(QCoreApplication.translate("elementCar", u"/ \u0441\u0443\u0442", None))
        self.deleteCarBtn.setText("")
        self.editCarBtn.setText("")
    # retranslateUi

