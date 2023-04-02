# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceXxEijS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 741)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"* {\n"
"	border: None;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget {\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#headerContainer, #footerContainer {\n"
"	background-color: #2c313c;\n"
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
"	background-color: #16191d;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#inputSpecifications {\n"
"	border-top-left-radius: 0;\n"
"	border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#specificationsOptions {\n"
"	border-top-right-radius: 0;\n"
"	border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:verti"
                        "cal {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	bord"
                        "er: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color:#262a30;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR */\n"
" QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    height: 14px;\n"
"    margin: 0 15px 0 15px;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:horizontal {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-width: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:hori"
                        "zontal:hover{	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	width: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-top-left-radius: 7px;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	width: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-top-left-radius: 7px;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {	\n"
"	background-color:#262a30;\n"
"}\n"
"\n"
"QScrollBar::add-line:hor"
                        "izontal:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setAutoFillBackground(False)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        font = QFont()
        font.setPointSize(12)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(30, 25))
        self.label_5.setPixmap(QPixmap(u":/images/car-rent.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon = QIcon()
        icon.addFile(u":/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.mainBodyContent.setMinimumSize(QSize(850, 650))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, -1, 10, -1)
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.pageCars = QWidget()
        self.pageCars.setObjectName(u"pageCars")
        self.verticalLayout_18 = QVBoxLayout(self.pageCars)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_2 = QFrame(self.pageCars)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_12)

        self.addCarBtn = QPushButton(self.frame_14)
        self.addCarBtn.setObjectName(u"addCarBtn")
        self.addCarBtn.setMaximumSize(QSize(16777215, 16777215))
        self.addCarBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addCarBtn.setIcon(icon3)
        self.addCarBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.addCarBtn)


        self.horizontalLayout_6.addWidget(self.frame_14, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_2)

        self.scrollArea = QScrollArea(self.pageCars)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: rgb(56, 56, 85);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background-color: rgb(56, 56, 85);\n"
"}\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaIngredients = QWidget()
        self.scrollAreaIngredients.setObjectName(u"scrollAreaIngredients")
        self.scrollAreaIngredients.setGeometry(QRect(0, 0, 794, 530))
        self.horizontalLayout_13 = QHBoxLayout(self.scrollAreaIngredients)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.carLayout = QVBoxLayout()
        self.carLayout.setSpacing(0)
        self.carLayout.setObjectName(u"carLayout")
        self.carLayout.setContentsMargins(0, -1, -1, -1)

        self.horizontalLayout_13.addLayout(self.carLayout)

        self.scrollArea.setWidget(self.scrollAreaIngredients)

        self.verticalLayout_18.addWidget(self.scrollArea)

        self.mainPages.addWidget(self.pageCars)
        self.pageAddCar = QWidget()
        self.pageAddCar.setObjectName(u"pageAddCar")
        self.verticalLayout_21 = QVBoxLayout(self.pageAddCar)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_11 = QFrame(self.pageAddCar)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 400))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_11)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 100))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_12)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.verticalLayout_26.addWidget(self.label_16, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_4 = QFrame(self.frame_12)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 40, 0, 20)
        self.labelErrorAddCar = QLabel(self.frame_4)
        self.labelErrorAddCar.setObjectName(u"labelErrorAddCar")
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(75)
        self.labelErrorAddCar.setFont(font3)
        self.labelErrorAddCar.setStyleSheet(u"color: red")

        self.verticalLayout_5.addWidget(self.labelErrorAddCar, 0, Qt.AlignHCenter)


        self.verticalLayout_26.addWidget(self.frame_4)


        self.verticalLayout_24.addWidget(self.frame_12)

        self.frame_16 = QFrame(self.frame_11)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setMaximumSize(QSize(16777215, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_16)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_16)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_6)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(400, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 100))
        font4 = QFont()
        font4.setPointSize(8)
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"margin-top: 10px")
        self.label_19.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_19)

        self.inputModel = QLineEdit(self.frame_3)
        self.inputModel.setObjectName(u"inputModel")
        self.inputModel.setMinimumSize(QSize(200, 0))
        self.inputModel.setMaximumSize(QSize(300, 16777215))
        self.inputModel.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.inputModel)

        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 100))
        self.label_20.setFont(font4)
        self.label_20.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_20)

        self.inputModelYear = QLineEdit(self.frame_3)
        self.inputModelYear.setObjectName(u"inputModelYear")
        self.inputModelYear.setMinimumSize(QSize(200, 0))
        self.inputModelYear.setMaximumSize(QSize(300, 16777215))
        self.inputModelYear.setStyleSheet(u"")
        self.inputModelYear.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.inputModelYear)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignBottom)

        self.inputImagePath = QLineEdit(self.frame_3)
        self.inputImagePath.setObjectName(u"inputImagePath")
        self.inputImagePath.setMinimumSize(QSize(200, 0))
        self.inputImagePath.setMaximumSize(QSize(300, 16777215))
        self.inputImagePath.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.inputImagePath)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignBottom)

        self.frame_18 = QFrame(self.frame_3)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy2)
        self.frame_18.setMinimumSize(QSize(0, 170))
        self.frame_18.setMaximumSize(QSize(16777215, 170))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.specificationsOptions = QTextEdit(self.frame_18)
        self.specificationsOptions.setObjectName(u"specificationsOptions")
        self.specificationsOptions.setMaximumSize(QSize(175, 170))
        self.specificationsOptions.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.specificationsOptions)

        self.inputSpecifications = QTextEdit(self.frame_18)
        self.inputSpecifications.setObjectName(u"inputSpecifications")
        self.inputSpecifications.setMaximumSize(QSize(150, 170))
        self.inputSpecifications.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.horizontalLayout_15.addWidget(self.inputSpecifications)


        self.verticalLayout.addWidget(self.frame_18, 0, Qt.AlignLeft)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignBottom)

        self.inputCost = QLineEdit(self.frame_3)
        self.inputCost.setObjectName(u"inputCost")
        self.inputCost.setMinimumSize(QSize(200, 0))
        self.inputCost.setMaximumSize(QSize(300, 16777215))
        self.inputCost.setInputMethodHints(Qt.ImhNone)
        self.inputCost.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.inputCost)


        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.frame_3)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 20, 10, 20)
        self.imageAreaAddCarPage = QLabel(self.frame_8)
        self.imageAreaAddCarPage.setObjectName(u"imageAreaAddCarPage")
        self.imageAreaAddCarPage.setMaximumSize(QSize(16777215, 650))

        self.verticalLayout_6.addWidget(self.imageAreaAddCarPage)


        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_24.addWidget(self.frame_16)

        self.frame = QFrame(self.frame_11)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saveCarBtn = QPushButton(self.frame)
        self.saveCarBtn.setObjectName(u"saveCarBtn")
        self.saveCarBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveCarBtn.setIcon(icon4)
        self.saveCarBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.saveCarBtn, 0, Qt.AlignRight)

        self.previewImageBtn = QPushButton(self.frame)
        self.previewImageBtn.setObjectName(u"previewImageBtn")
        self.previewImageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previewImageBtn.setIcon(icon5)
        self.previewImageBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.previewImageBtn, 0, Qt.AlignHCenter)

        self.homeBtn = QPushButton(self.frame)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon6)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.homeBtn, 0, Qt.AlignLeft)


        self.verticalLayout_24.addWidget(self.frame, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.frame_11)

        self.mainPages.addWidget(self.pageAddCar)
        self.pageShell = QWidget()
        self.pageShell.setObjectName(u"pageShell")
        self.verticalLayout_2 = QVBoxLayout(self.pageShell)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_13 = QFrame(self.pageShell)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 100))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_13)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_13)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.verticalLayout_27.addWidget(self.label_17, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_9 = QFrame(self.frame_13)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 30))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 40, 0, 20)
        self.labelErrorShell = QLabel(self.frame_9)
        self.labelErrorShell.setObjectName(u"labelErrorShell")
        self.labelErrorShell.setFont(font3)
        self.labelErrorShell.setStyleSheet(u"color: red")

        self.verticalLayout_7.addWidget(self.labelErrorShell, 0, Qt.AlignHCenter)


        self.verticalLayout_27.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.inputCommand = QTextEdit(self.pageShell)
        self.inputCommand.setObjectName(u"inputCommand")

        self.verticalLayout_2.addWidget(self.inputCommand)

        self.frame_15 = QFrame(self.pageShell)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.executeBtn = QPushButton(self.frame_17)
        self.executeBtn.setObjectName(u"executeBtn")
        self.executeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/zap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.executeBtn.setIcon(icon7)
        self.executeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.executeBtn)

        self.choiceRolePage = QPushButton(self.frame_17)
        self.choiceRolePage.setObjectName(u"choiceRolePage")
        self.choiceRolePage.setCursor(QCursor(Qt.PointingHandCursor))
        self.choiceRolePage.setIcon(icon6)
        self.choiceRolePage.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.choiceRolePage)


        self.verticalLayout_4.addWidget(self.frame_17, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_15, 0, Qt.AlignVCenter)

        self.mainPages.addWidget(self.pageShell)
        self.pageChoiceRole = QWidget()
        self.pageChoiceRole.setObjectName(u"pageChoiceRole")
        self.verticalLayout_9 = QVBoxLayout(self.pageChoiceRole)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_19 = QFrame(self.pageChoiceRole)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_19)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.frame_19)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.verticalLayout_8.addWidget(self.label, 0, Qt.AlignHCenter)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.userModeBtn = QPushButton(self.frame_20)
        self.userModeBtn.setObjectName(u"userModeBtn")
        self.userModeBtn.setFont(font)
        self.userModeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userModeBtn.setIcon(icon8)
        self.userModeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.userModeBtn, 0, Qt.AlignHCenter)

        self.adminModeBtn = QPushButton(self.frame_20)
        self.adminModeBtn.setObjectName(u"adminModeBtn")
        self.adminModeBtn.setFont(font)
        self.adminModeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.adminModeBtn.setMouseTracking(False)
        icon9 = QIcon()
        icon9.addFile(u":/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.adminModeBtn.setIcon(icon9)
        self.adminModeBtn.setIconSize(QSize(24, 24))
        self.adminModeBtn.setCheckable(False)

        self.horizontalLayout_10.addWidget(self.adminModeBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_20)


        self.verticalLayout_9.addWidget(self.frame_19)

        self.mainPages.addWidget(self.pageChoiceRole)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_12.addWidget(self.label_15)

        self.sizeGrip = QFrame(self.frame_10)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.sizeGrip)


        self.horizontalLayout_11.addWidget(self.frame_10)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.headerContainer.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"RecipeBook", None))
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0438 \u0432 \u0430\u0440\u0435\u043d\u0434\u0443", None))
        self.addCarBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.labelErrorAddCar.setText(QCoreApplication.translate("MainWindow", u"All fields must be filled", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c:", None))
        self.inputModel.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430:", None))
        self.inputModelYear.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0438\u0440\u0438\u0441\u0442\u0438\u043a\u0438:", None))
        self.specificationsOptions.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041e\u0431\u044a\u0435\u043c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\""
                        ">\u0420\u0430\u0441\u0445\u043e\u0436 \u0442\u043e\u043f\u043b\u0438\u0432\u0430</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0422\u0438\u043f \u043f\u0440\u0438\u0432\u043e\u0434\u0430</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u043e\u0432</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u041a\u043e\u0440\u043e\u0431\u043a\u0430 \u043f\u0435\u0440\u0435\u0434\u0430\u0447</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\""
                        ">\u0410\u0432\u0442\u043e\u0437\u0430\u043f\u0443\u0441\u043a \u0430\u0432\u0442\u043e</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0412 \u043d\u0430\u0448\u0435\u043c \u043f\u0430\u0440\u043a\u0435</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0426\u0432\u0435\u0442</span></p></body></html>", None))
        self.inputSpecifications.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><spa"
                        "n style=\" font-size:10pt;\">\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin"
                        "-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0430\u0440\u0435\u043d\u0434\u044b \u0432 \u0441\u0443\u0442\u043a\u0438:", None))
        self.imageAreaAddCarPage.setText("")
        self.saveCarBtn.setText("")
        self.previewImageBtn.setText("")
        self.homeBtn.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0440\u043c\u0438\u043d\u0430\u043b", None))
        self.labelErrorShell.setText(QCoreApplication.translate("MainWindow", u"All fields must be filled", None))
        self.inputCommand.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Shell&gt;</span></p></body></html>", None))
        self.executeBtn.setText("")
        self.choiceRolePage.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u043e\u043b\u044c", None))
        self.userModeBtn.setText(QCoreApplication.translate("MainWindow", u" \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.adminModeBtn.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Copyright LunexCoding", None))
    # retranslateUi

