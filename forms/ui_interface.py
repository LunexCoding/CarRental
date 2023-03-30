# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceSHpnxR.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(580, 504)
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
"#leftMenuSubContainer {\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton {\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#centerMenuSubContainer, #rightMenuSubContainer {\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"#frame_4, #frame_8, #popupNotificationSubContainer {\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
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
"#saveIngredientBtn {\n"
"	"
                        "margin-top: 30px;\n"
"}\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
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
""
                        "\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
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
"	m"
                        "in-width: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{	\n"
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
"QScrollBar::add-line:horizontal:"
                        "hover {	\n"
"	background-color:#262a30;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"")
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
        self.mainBodyContent.setMinimumSize(QSize(527, 351))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.pageCars = QWidget()
        self.pageCars.setObjectName(u"pageCars")
        self.verticalLayout_18 = QVBoxLayout(self.pageCars)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_14 = QFrame(self.pageCars)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_14)
        self.formLayout.setObjectName(u"formLayout")
        self.addCarBtn = QPushButton(self.frame_14)
        self.addCarBtn.setObjectName(u"addCarBtn")
        self.addCarBtn.setMaximumSize(QSize(16777215, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addCarBtn.setIcon(icon3)
        self.addCarBtn.setIconSize(QSize(24, 24))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.addCarBtn)

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

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_12)


        self.verticalLayout_18.addWidget(self.frame_14, 0, Qt.AlignHCenter)

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
        self.scrollAreaIngredients.setGeometry(QRect(0, 0, 526, 328))
        self.horizontalLayout_13 = QHBoxLayout(self.scrollAreaIngredients)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.ingredientLayout = QVBoxLayout()
        self.ingredientLayout.setSpacing(0)
        self.ingredientLayout.setObjectName(u"ingredientLayout")

        self.horizontalLayout_13.addLayout(self.ingredientLayout)

        self.scrollArea.setWidget(self.scrollAreaIngredients)

        self.verticalLayout_18.addWidget(self.scrollArea)

        self.mainPages.addWidget(self.pageCars)
        self.pageAddCar = QWidget()
        self.pageAddCar.setObjectName(u"pageAddCar")
        self.verticalLayout_21 = QVBoxLayout(self.pageAddCar)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_11 = QFrame(self.pageAddCar)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_11)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 200))
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


        self.verticalLayout_24.addWidget(self.frame_12)

        self.frame_16 = QFrame(self.frame_11)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 250))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_16)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.labelErrorAddIngredient = QLabel(self.frame_16)
        self.labelErrorAddIngredient.setObjectName(u"labelErrorAddIngredient")
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(75)
        self.labelErrorAddIngredient.setFont(font3)
        self.labelErrorAddIngredient.setStyleSheet(u"color: red")

        self.verticalLayout_28.addWidget(self.labelErrorAddIngredient, 0, Qt.AlignHCenter)

        self.frame_13 = QFrame(self.frame_16)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setMaximumSize(QSize(16777215, 600))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_13)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_19 = QLabel(self.frame_13)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 100))
        font4 = QFont()
        font4.setPointSize(8)
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"margin-top: 10px")
        self.label_19.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_19)

        self.inputNameIngredient = QLineEdit(self.frame_13)
        self.inputNameIngredient.setObjectName(u"inputNameIngredient")
        self.inputNameIngredient.setMinimumSize(QSize(200, 0))
        self.inputNameIngredient.setMaximumSize(QSize(300, 16777215))
        self.inputNameIngredient.setStyleSheet(u"")
        self.inputNameIngredient.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.inputNameIngredient)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 100))
        self.label_20.setFont(font4)
        self.label_20.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_20)

        self.inputMeasureIngredient = QLineEdit(self.frame_13)
        self.inputMeasureIngredient.setObjectName(u"inputMeasureIngredient")
        self.inputMeasureIngredient.setMinimumSize(QSize(200, 0))
        self.inputMeasureIngredient.setMaximumSize(QSize(300, 16777215))
        self.inputMeasureIngredient.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.inputMeasureIngredient)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.saveCarBtn = QPushButton(self.frame_13)
        self.saveCarBtn.setObjectName(u"saveCarBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveCarBtn.setIcon(icon4)
        self.saveCarBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.saveCarBtn)

        self.homeBtn = QPushButton(self.frame_13)
        self.homeBtn.setObjectName(u"homeBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon5)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.homeBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_28.addWidget(self.frame_13)


        self.verticalLayout_24.addWidget(self.frame_16, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_21.addWidget(self.frame_11)

        self.mainPages.addWidget(self.pageAddCar)
        self.pageEditCar = QWidget()
        self.pageEditCar.setObjectName(u"pageEditCar")
        self.verticalLayout_2 = QVBoxLayout(self.pageEditCar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.pageEditCar)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mainPages.addWidget(self.pageEditCar)

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


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.sizeGrip)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


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
        self.addCarBtn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0438 \u0432 \u0430\u0440\u0435\u043d\u0434\u0443", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.labelErrorAddIngredient.setText(QCoreApplication.translate("MainWindow", u"All fields must be filled", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.inputNameIngredient.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Measure:", None))
        self.inputMeasureIngredient.setText("")
        self.saveCarBtn.setText("")
        self.homeBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0440\u0435\u0434\u043e\u0436\u0435\u043d\u0438\u044f \u043e\u0431 \u0430\u0440\u0435\u043d\u0434\u0435 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Copyright LunexCoding", None))
    # retranslateUi

