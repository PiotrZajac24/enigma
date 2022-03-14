# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(955, 726)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setToolTipDuration(0)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.loadTextButton = QPushButton(self.centralwidget)
        self.loadTextButton.setObjectName(u"loadTextButton")
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.loadTextButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.loadTextButton)

        self.loadTextAndSettingsButton = QPushButton(self.centralwidget)
        self.loadTextAndSettingsButton.setObjectName(u"loadTextAndSettingsButton")
        self.loadTextAndSettingsButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.loadTextAndSettingsButton)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setFont(font1)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.clearText = QPushButton(self.centralwidget)
        self.clearText.setObjectName(u"clearText")
        self.clearText.setFont(font1)

        self.verticalLayout_3.addWidget(self.clearText)

        self.encryptButton = QPushButton(self.centralwidget)
        self.encryptButton.setObjectName(u"encryptButton")
        self.encryptButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.encryptButton)

        self.textShow = QTextBrowser(self.centralwidget)
        self.textShow.setObjectName(u"textShow")
        self.textShow.setFont(font1)

        self.verticalLayout_3.addWidget(self.textShow)

        self.saveTextAndSettingsButton = QPushButton(self.centralwidget)
        self.saveTextAndSettingsButton.setObjectName(u"saveTextAndSettingsButton")
        self.saveTextAndSettingsButton.setFont(font1)

        self.verticalLayout_3.addWidget(self.saveTextAndSettingsButton)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.widget_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 2, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.autoSave = QCheckBox(self.centralwidget)
        self.autoSave.setObjectName(u"autoSave")
        self.autoSave.setFont(font1)

        self.verticalLayout_2.addWidget(self.autoSave)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_12.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_12)

        self.randomSettings = QPushButton(self.centralwidget)
        self.randomSettings.setObjectName(u"randomSettings")

        self.verticalLayout_2.addWidget(self.randomSettings)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.widget)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.rotorsNumber = QSpinBox(self.centralwidget)
        self.rotorsNumber.setObjectName(u"rotorsNumber")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.rotorsNumber.sizePolicy().hasHeightForWidth())
        self.rotorsNumber.setSizePolicy(sizePolicy4)
        self.rotorsNumber.setMinimum(3)
        self.rotorsNumber.setMaximum(100)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.rotorsNumber)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rotorsList = QListWidget(self.centralwidget)
        self.rotorsList.setObjectName(u"rotorsList")

        self.gridLayout_2.addWidget(self.rotorsList, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rotationEdit = QLineEdit(self.page_3)
        self.rotationEdit.setObjectName(u"rotationEdit")
        self.rotationEdit.setFont(font1)

        self.horizontalLayout_4.addWidget(self.rotationEdit)

        self.drawAdditionalRotation = QPushButton(self.page_3)
        self.drawAdditionalRotation.setObjectName(u"drawAdditionalRotation")
        self.drawAdditionalRotation.setFont(font1)

        self.horizontalLayout_4.addWidget(self.drawAdditionalRotation)

        self.saveRotationButton = QPushButton(self.page_3)
        self.saveRotationButton.setObjectName(u"saveRotationButton")
        self.saveRotationButton.setEnabled(True)
        self.saveRotationButton.setFont(font1)
        self.saveRotationButton.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.saveRotationButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.rotorSettings = QTextBrowser(self.page_3)
        self.rotorSettings.setObjectName(u"rotorSettings")
        self.rotorSettings.setFont(font1)

        self.gridLayout_3.addWidget(self.rotorSettings, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.letterOrder = QLineEdit(self.page_3)
        self.letterOrder.setObjectName(u"letterOrder")
        self.letterOrder.setFont(font1)

        self.horizontalLayout_2.addWidget(self.letterOrder)

        self.drawLetterOrder = QPushButton(self.page_3)
        self.drawLetterOrder.setObjectName(u"drawLetterOrder")
        sizePolicy4.setHeightForWidth(self.drawLetterOrder.sizePolicy().hasHeightForWidth())
        self.drawLetterOrder.setSizePolicy(sizePolicy4)
        self.drawLetterOrder.setFont(font1)

        self.horizontalLayout_2.addWidget(self.drawLetterOrder)

        self.saveLetterOrderButton = QPushButton(self.page_3)
        self.saveLetterOrderButton.setObjectName(u"saveLetterOrderButton")
        self.saveLetterOrderButton.setEnabled(True)
        self.saveLetterOrderButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.saveLetterOrderButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.formLayout.setLayout(2, QFormLayout.SpanningRole, self.gridLayout_2)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_9.setFont(font3)

        self.horizontalLayout.addWidget(self.label_9)

        self.entranceSwapsText = QLineEdit(self.centralwidget)
        self.entranceSwapsText.setObjectName(u"entranceSwapsText")
        self.entranceSwapsText.setFont(font1)

        self.horizontalLayout.addWidget(self.entranceSwapsText)

        self.entranceSwaps = QSpinBox(self.centralwidget)
        self.entranceSwaps.setObjectName(u"entranceSwaps")
        self.entranceSwaps.setToolTipDuration(-2)
        self.entranceSwaps.setMaximum(12)
        self.entranceSwaps.setValue(8)

        self.horizontalLayout.addWidget(self.entranceSwaps)

        self.randomEntranceSwaps = QPushButton(self.centralwidget)
        self.randomEntranceSwaps.setObjectName(u"randomEntranceSwaps")
        self.randomEntranceSwaps.setFont(font1)

        self.horizontalLayout.addWidget(self.randomEntranceSwaps)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.reverseSwapsText = QLineEdit(self.centralwidget)
        self.reverseSwapsText.setObjectName(u"reverseSwapsText")
        self.reverseSwapsText.setFont(font1)

        self.horizontalLayout_10.addWidget(self.reverseSwapsText)

        self.randomReverseSwaps = QPushButton(self.centralwidget)
        self.randomReverseSwaps.setObjectName(u"randomReverseSwaps")
        self.randomReverseSwaps.setFont(font1)

        self.horizontalLayout_10.addWidget(self.randomReverseSwaps)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy5)
        self.label_19.setFont(font3)

        self.horizontalLayout_43.addWidget(self.label_19)

        self.textCode = QLineEdit(self.centralwidget)
        self.textCode.setObjectName(u"textCode")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.textCode.sizePolicy().hasHeightForWidth())
        self.textCode.setSizePolicy(sizePolicy6)
        self.textCode.setFont(font1)

        self.horizontalLayout_43.addWidget(self.textCode)

        self.randomCode = QPushButton(self.centralwidget)
        self.randomCode.setObjectName(u"randomCode")
        self.randomCode.setFont(font1)

        self.horizontalLayout_43.addWidget(self.randomCode)


        self.verticalLayout.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.textRotorOrder = QLineEdit(self.centralwidget)
        self.textRotorOrder.setObjectName(u"textRotorOrder")
        sizePolicy6.setHeightForWidth(self.textRotorOrder.sizePolicy().hasHeightForWidth())
        self.textRotorOrder.setSizePolicy(sizePolicy6)
        self.textRotorOrder.setFont(font1)

        self.horizontalLayout_12.addWidget(self.textRotorOrder)

        self.randomOrder = QPushButton(self.centralwidget)
        self.randomOrder.setObjectName(u"randomOrder")
        self.randomOrder.setFont(font1)

        self.horizontalLayout_12.addWidget(self.randomOrder)


        self.verticalLayout.addLayout(self.horizontalLayout_12)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.saveSettings = QPushButton(self.centralwidget)
        self.saveSettings.setObjectName(u"saveSettings")
        self.saveSettings.setFont(font1)

        self.horizontalLayout_14.addWidget(self.saveSettings)

        self.loadFileButton = QPushButton(self.centralwidget)
        self.loadFileButton.setObjectName(u"loadFileButton")
        self.loadFileButton.setFont(font1)

        self.horizontalLayout_14.addWidget(self.loadFileButton)

        self.clearSettings = QPushButton(self.centralwidget)
        self.clearSettings.setObjectName(u"clearSettings")
        self.clearSettings.setFont(font1)

        self.horizontalLayout_14.addWidget(self.clearSettings)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_14)

        self.textSettings = QTextBrowser(self.centralwidget)
        self.textSettings.setObjectName(u"textSettings")
        sizePolicy.setHeightForWidth(self.textSettings.sizePolicy().hasHeightForWidth())
        self.textSettings.setSizePolicy(sizePolicy)
        self.textSettings.setFont(font1)

        self.verticalLayout_4.addWidget(self.textSettings)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.writeFileButton = QPushButton(self.centralwidget)
        self.writeFileButton.setObjectName(u"writeFileButton")
        self.writeFileButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.writeFileButton)

        self.resetCurrentSettings = QPushButton(self.centralwidget)
        self.resetCurrentSettings.setObjectName(u"resetCurrentSettings")
        self.resetCurrentSettings.setFont(font1)

        self.horizontalLayout_3.addWidget(self.resetCurrentSettings)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.widget_2, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 955, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Maszyna szyfruj\u0105ca Enigma", None))
        self.loadTextButton.setText(QCoreApplication.translate("MainWindow", u"Wczytaj tekst", None))
        self.loadTextAndSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Wczytaj tekst i ustawienia maszyny", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wpisz tekst do zaszyfrowania/odszyfrowania", None))
        self.clearText.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 tekst", None))
        self.encryptButton.setText(QCoreApplication.translate("MainWindow", u"Zaszyfruj/odszyfruj", None))
        self.textShow.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Zaszyfrowany/odszyfrowany tekst pojawi si\u0119 tutaj", None))
        self.saveTextAndSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Zapisz zaszyfrowany tekst z ustawieniami do pliku", None))
        self.autoSave.setText(QCoreApplication.translate("MainWindow", u"Automatycznie zapisuj ustawienia maszyny po wczytaniu z pliku", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Zmie\u0144 ustawienia", None))
        self.randomSettings.setText(QCoreApplication.translate("MainWindow", u"Losuj wszystko", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 wirnik\u00f3w", None))
        self.rotationEdit.setText("")
        self.rotationEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wpisz liter\u0119", None))
        self.drawAdditionalRotation.setText(QCoreApplication.translate("MainWindow", u"Losuj", None))
        self.saveRotationButton.setText(QCoreApplication.translate("MainWindow", u"Zmie\u0144", None))
        self.letterOrder.setText("")
        self.letterOrder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wpisz kolejno\u015b\u0107 liter", None))
        self.drawLetterOrder.setText(QCoreApplication.translate("MainWindow", u"Losuj", None))
        self.saveLetterOrderButton.setText(QCoreApplication.translate("MainWindow", u"Zmie\u0144", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Entrance swaps", None))
        self.entranceSwapsText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wpisz po\u0142\u0105czenia na \u0142\u0105cznicy (e.g. AC HN PD)", None))
        self.randomEntranceSwaps.setText(QCoreApplication.translate("MainWindow", u"Losuj", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Reverse swaps", None))
        self.reverseSwapsText.setText("")
        self.reverseSwapsText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wpisz po\u0142\u0105czenia na wirniku odwracaj\u0105cym (u\u017cyj wszystkich liter)", None))
        self.randomReverseSwaps.setText(QCoreApplication.translate("MainWindow", u"Losuj", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Initial code", None))
        self.textCode.setText("")
        self.textCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"np. AZE", None))
        self.randomCode.setText(QCoreApplication.translate("MainWindow", u"Losuj", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Rotor order", None))
        self.textRotorOrder.setText("")
        self.textRotorOrder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"np. 3 1 2", None))
        self.randomOrder.setText(QCoreApplication.translate("MainWindow", u"Losuj", None))
        self.saveSettings.setText(QCoreApplication.translate("MainWindow", u"Zapisz ustawienia", None))
        self.loadFileButton.setText(QCoreApplication.translate("MainWindow", u"Wczytaj z pliku", None))
        self.clearSettings.setText(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Aktualne ustawienia", None))
        self.writeFileButton.setText(QCoreApplication.translate("MainWindow", u"Zapisz aktualne ustawienia do pliku", None))
        self.resetCurrentSettings.setText(QCoreApplication.translate("MainWindow", u"Resetuj ustawienia", None))
    # retranslateUi

