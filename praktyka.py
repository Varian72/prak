#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals

import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from itertools import izip, islice, tee

import textwrap

import os
import math
from operator import itemgetter
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

global N
N = 1

global L
global startIn
global finishIn
global isSliced

startIn = 0
finishIn = 100
isSliced = False

class Ui_Form(object):

    global L

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(600, 300)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 200, 121, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #self.pushButton_2 = QtGui.QPushButton(Form)
        #self.pushButton_2.setGeometry(QtCore.QRect(70, 200, 121, 41))
        #self.pushButton_2.setObjectName(_fromUtf8("pushButton"))
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(400, 120, 71, 22))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(400, 150, 91, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))


        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(140, 20, 121, 31))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setMinimum(1)

        self.spinBox_2 = QtGui.QSpinBox(Form)
        self.spinBox_2.setGeometry(QtCore.QRect(140, 80, 121, 31))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_2.setMaximum(L)



        self.spinBox_3 = QtGui.QSpinBox(Form)
        self.spinBox_3.setGeometry(QtCore.QRect(140, 120, 121, 31))
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_3.setMinimum(finishIn)
        self.spinBox_3.setMaximum(L)




        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(85, 31, 66, 11))
        self.label.setObjectName(_fromUtf8("label"))


        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 73, 71, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))



        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 46, 330, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))



        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 113, 71, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Set value", None))
        #self.pushButton_2.setText(_translate("Form","Exit", None))
        #self.pushButton.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.OK)

        self.label.setText(_translate("Form", "choose n:", None))
        self.label_2.setText(_translate("Form", "Lo:", None))
        self.label_3.setText(_translate("Form", str("You can choose an area("+ "1-"+ str(L)+")to discover, below:"), None))
        self.label_4.setText(_translate("Form", "deltaL:", None))
        self.radioButton.setText(_translate("Form", "Whole", None))
        self.radioButton_2.setText(_translate("Form", "Slice", None))
        self.spinBox_2.setEnabled(False)
        self.spinBox_3.setEnabled(False)
        self.radioButton_2.clicked.connect(self.enableOrDisable)
        self.radioButton.clicked.connect(self.enableOrDisable)


    def enableOrDisable(self):
        if self.radioButton.isChecked():
            self.spinBox_2.setEnabled(False)
            self.spinBox_3.setEnabled(False)
        elif self.radioButton_2.isChecked():
            self.spinBox_2.setEnabled(True)
            self.spinBox_3.setEnabled(True)






    def OK(self, event):
        #value = [int(item) for item in self.spinBox.value()]
        global N, startIn, finishIn , isSliced
        value =  self.spinBox.value()
        value1 = self.spinBox_2.value()
        value2  = self.spinBox_3.value()
        N = value
        startIn = value1
        finishIn = value2
        if self.radioButton_2.isChecked():
            isSliced = True
        else:
            isSliced = False
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        stringer= str("You succesfully choose N=" + str(N))
        msg.setText(stringer)
        msg.setInformativeText("This value set how much items will be in interval")
        msg.setWindowTitle("Changed  N !!!!")
        msg.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        msg.setStandardButtons(QMessageBox.Ok )
        msg.exec_()
        #msg.buttonClicked.connect(msgbtn)



        #popup = QDialog()
        #popup.ui = Ui_Form()

 #


class Ui_MainWindow(object):
    #Global variable
    readyText = ""
    originalText = ""
    setTab1 = False
    setTab2 = False
    setTab3 = False
    setTab4 = False

    file1 = None
    file2 = None
    file3 = None
    file4 = None




    #firstpad
    table1Array = []
    tab1Flag =  False
    generalOne = []

    #for tab4
    newWordsText = ""
    big_P_x = ""

    #third Pad
    NumberOfIntervalsItems = ""
    chunkedText = ""
    p_pad3 = ""
    P_pad3 = ""
    listOfAverages = ""
    sumIntervalTab3 = ""


    #second pad
    result_tap_2 = ""
    result_P_tap_2 = ""

    #general
    filename = ""
    global N
    n = N
    popup = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 791, 521))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.pushButton = QtGui.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(560, 200, 151, 71))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tableWidget = QtGui.QTableWidget(self.tab_3)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 431, 491))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSortingEnabled(True)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 511, 491))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.pushButton_2 = QtGui.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 200, 121, 71))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.radioButton = QtGui.QRadioButton(self.tab_4)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(560, 150, 71, 22))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.tab_4)
        self.radioButton_2.setGeometry(QtCore.QRect(670, 150, 91, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.label = QtGui.QLabel(self.tab_5)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.tab_5)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 141, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.tableWidget_4 = QtGui.QTableWidget(self.tab_5)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 90, 791, 401))
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        #self.tableWidget_4.setHorizontalHeaderItem(0, item)
        #item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        self.pushButton_4 = QtGui.QPushButton(self.tab_5)
        self.pushButton_4.setGeometry(QtCore.QRect(648, 16, 111, 61))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.radioButton_3 = QtGui.QRadioButton(self.tab_5)
        self.radioButton_3.setGeometry(QtCore.QRect(480, 0, 117, 22))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.tab_5)
        self.radioButton_4.setGeometry(QtCore.QRect(480, 30, 117, 22))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(self.tab_5)
        self.radioButton_5.setGeometry(QtCore.QRect(480, 60, 117, 22))
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.tabWidget_2.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tableWidget_3 = QtGui.QTableWidget(self.tab_6)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 421, 491))
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.verticalHeader().setVisible(False)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        self.pushButton_3 = QtGui.QPushButton(self.tab_6)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 200, 161, 71))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tabWidget_2.addTab(self.tab_6, _fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        #self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionChange = QtGui.QAction(MainWindow)
        self.actionChange.setObjectName(_fromUtf8("actionChange"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionChange)
        self.menubar.addAction(self.menuFile.menuAction())
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_4.setSortingEnabled(True)
        self.tableWidget_3.setSortingEnabled(True)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", " ", None))
        self.pushButton.setText(_translate("MainWindow", "Build", None))
        self.pushButton.clicked.connect(self.buildTabHist1)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Rang", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Symbols", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "F", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "f", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Analysis", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "dT", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "N", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "p(x)", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P(x)", None))
        self.pushButton_2.setText(_translate("MainWindow", "Build", None))
        self.pushButton_2.clicked.connect(self.drawgGaf)
        self.radioButton.setText(_translate("MainWindow", "p(x)", None))
        self.radioButton_2.setText(_translate("MainWindow", "P(x)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "dTi", None))
        self.label.setText(_translate("MainWindow", "Count of interval:", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "", None))
        self.lineEdit.setText("8")
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ti bin", None))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "N", None))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Average", None))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "p(x)", None))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "P(x)", None))
        self.pushButton_4.setText(_translate("MainWindow", "Build", None))
        self.pushButton_4.clicked.connect(self.buildGrahTab3)
        self.radioButton_3.setText(_translate("MainWindow", "p(x)", None))
        self.radioButton_4.setText(_translate("MainWindow", "P(x)", None))
        self.radioButton_5.setText(_translate("MainWindow", "intervals", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Ti", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Position", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Meaning", None))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Value", None))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P'(x)", None))
        self.pushButton_3.setText(_translate("MainWindow", "Build", None))
        self.pushButton_3.clicked.connect(self.buildGrahTab4)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "New Symbols", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "New Symbols", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "F=", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.triggered.connect(self.openDialog)
        self.actionChange.setShortcut("Ctrl+S")
        self.actionChange.triggered.connect(self.file_save)
        self.actionChange.setText(_translate("MainWindow", "Save as", None))


    #This function opendialog in which data is loaded
    def openDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName()
        if filename:
            filename = unicode(filename, "utf-8")
            text = open(filename).read()
            self.originalText = text.decode("utf-8")
            global L
            L = len(self.originalText)
            self.splitText(self.originalText)
            #print(self.originalText)


    #This function save file ('save as' in menu bar)
    def file_save(self):
        #name = QtGui.QFileDialog.getSaveFileName( self.setupUi(self), 'Save File')
        name = QtGui.QFileDialog.getSaveFileName()
        name = unicode(name, "utf-8")
        self.file1 = open(name + ":AnalysisSymbol", 'w' )
        self.file2 = open(name + ":dti", 'w' )
        self.file3 = open(name + ":Ti", 'w' )
        self.file4 = open(name + ":NewSymbols", 'w' )
        self.setTab1 = True
        self.setTab2 = True
        self.setTab3 = True
        self.setTab4 = True


        self.table1()
        self.fillTableTab2()
        self.fillTableTab3()
        self.buildTable4()
        #file1.write()
        #file2.write(self.getTab2())
        #file3.write(self.getTab3())
        #file4.write(self.getTab4())

        #file1.close()
        #file2.close()
        #file3.close()
        #file4.close()



    #This fuction open pop up where you have to choose "N"
    def open_n_Popup(self):
        self.popup = QDialog()
        self.popup.ui = Ui_Form()
        self.popup.ui.setupUi(self.popup)
        self.popup.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.popup.exec_()
        global N, startIn, finishIn ,isSliced
        self.n = N
        self.startIn = startIn
        self.finishIn = finishIn
        self.isSliced = isSliced


    #this function split text into n-gramms and run waterflow functions which
    # fill tables
    def splitText(self, text):
        self.open_n_Popup()
        if self.isSliced:
            slicedtext = text[self.startIn:self.startIn + self.finishIn]
        else:
            slicedtext = text
        slicedtext = slicedtext.decode('utf8')
        splittedText = []
        for item in range(len(slicedtext)- self.n):
            splittedText.append(slicedtext[item:item+self.n])
        self.readyText = splittedText
        #here caled waterflow functions for tab1
        self.table1()
        #here called waterflow functions for tab4
        self.calcNewSymbols()
        #here called watetflow functions for tab3
        self.chunksIntervals()
        #here calle wateeflow functions for tab2
        self.calcSecTab()




    #first tab (Analysis tab)

    #this fuction fill table1 (tap1), get frquecy so len(values )not full len
    def table1(self):
        counts = Counter(self.readyText)
        labels, valuesF = zip(*counts.items())
        indexes = np.arange(len(labels))
        values_f = self.calcf( valuesF)
        self.tableWidget.setRowCount(len(valuesF))
        output = [0] * len(valuesF)
        for i, x in enumerate(sorted(range(len(valuesF)), key=lambda y: valuesF[y], reverse = True)):
            output[x] = i+1

        if self.setTab1 == False:
            temporaryGeneral = []
        for itemRow in range(0,len(valuesF)):
            if self.setTab1 == False:
                item0 = QTableWidgetItem()
                item0.setData(Qt.DisplayRole, output[itemRow])
                item1 = QTableWidgetItem()
                item1.setText(labels[itemRow])
                item2 = QTableWidgetItem()
                item2.setData(Qt.DisplayRole, valuesF[itemRow])
                item3 = QTableWidgetItem()
                item3.setText(str(values_f[itemRow]))
                self.tableWidget.setItem(itemRow, 0, item0)
                self.tableWidget.setItem(itemRow, 1, item1)
                self.tableWidget.setItem(itemRow, 2, item2)
                self.tableWidget.setItem(itemRow, 3, item3)
                temporaryGeneral.append([output[itemRow],labels[itemRow],valuesF[itemRow],values_f[itemRow]])
            else:
                self.file1.write(str(str(self.generalOne[itemRow][0]) + '\t' + str(self.generalOne[itemRow][1])+ '\t' + str(self.generalOne[itemRow][2])+'\t' + str(self.generalOne[itemRow][3]))+'\n')
            #compose into list of list in order to sort in func below
            #if len(self.table1Array) != len(valuesF):
            #    self.table1Array.append([itemRow, labels[itemRow], valuesF[itemRow], values_f[itemRow]])
        #self.table1Array = sorted(self.table1Array, key = lambda x: int(x[2]), reverse = True )
        #for itemRow in range(0,len(valuesF)):
        #    item0 = QTableWidgetItem()
            #item0.setData(Qt.DisplayRole, )
        if self.setTab1 == False:
            self.generalOne = sorted(temporaryGeneral, key=itemgetter(0))
        else:
            self.file1.close()
        self.setTab1 = False
        self.tab1Flag = True



    #this func sort array not usedt !!!
    def sortHist1(self):
        if self.tab1Flag == True:
            for itemRow in range(0,len(self.table1Array)):
                item1 = QTableWidgetItem()
                item1.setText(str(self.table1Array[itemRow][1]))
                item2 = QTableWidgetItem()
                item2.setData(self.table1Array[itemRow][2])
                item3 = QTableWidgetItem()
                item3.setData(str(self.table1Array[itemRow][3]))
                self.tableWidget.setItem(itemRow,1,item1)
                self.tableWidget.setItem(itemRow,2,item2)
                self.tableWidget.setItem(itemRow,3,item3)
            self.tab1Flag = False
        else:
            self.table1()




    #this func is for calc f value particular/general
    def calcf(self, valuesF):
        values_f = []
        for item in range(len(valuesF)):
            values_f.append(valuesF[item]/len(self.originalText))
        #values_f = [item / len(valuesF) for item in valuesF]
        return values_f



    #this fuction is for building histogram, activated by pressing  "build"
    # button in tab 1
    def buildTabHist1(self):
        prepeare_counts = self.readyText
        result = None
        #if len(self.readyText) > 30:
        #    prepeare_counts = self.readyText[0::int(len(self.readyText)*10/100)]
        #    print(int(len(self.readyText)*10/len(self.readyText)))
        #    print(len(prepeare_counts))
        #    print(len(self.readyText))
        counts = Counter(prepeare_counts)
        labels, values = zip(*counts.items())
        # sort your values in descending order
        indSort = np.argsort(values)[::-1]
        # rearrange your data
        labels = np.array(labels)[indSort]
        values = np.array(values)[indSort]
        seen = set()
        seen_add = seen.add
        result= [x for x in values if not (x in seen or seen_add(x))]
        #values = zip(*[iter(values)] * int(len(values)/10))
        #for item in values:
        #    result.append(sum(item)/len(item))
        #    print(sum(item)/len(item) , sum(item), len(item) , item)
        #print len(values)
        indexes = np.arange(len(result))
        bar_width = 0.35
        #here1
        for i in range(1,len(result)):
            result[i] = math.log10(result[i])
        plt.bar(indexes[1::], result[1::])
        #histogram, bin_edges = np.histogram(values, bins = 10)
        #plt.bar(histogram,bin_edges[:-1], width = 0.35)
        #print(bin_edges)
        #print(histogram)

        plt.xlim(min(indexes), max(indexes))
        # add labels
        #plt.xticks(indexes + bar_width, labels)
        plt.show()






    #NEW SYMBOLS TAB(4th tab)

    #this function run into text and match all first time userd symbols or
    #ngramms as 1 and already seen as 0
    def calcNewSymbols(self):
        #In this loop, finally all matched indexes is set to 1 other is 0
        #check whether firs tTimeM atchedItems index = index of readyText and set 1
        #or 0
        readyItems = []
        binaryItems = []
        binaryItems.append(1)
        item = 1
        #for item in range(1, len( self.readyText)):
        while item < len(self.readyText):
            try:
                result = self.readyText[:item].index(self.readyText[item])
                item+=1
                binaryItems.append(0)
            except ValueError:
                item+=1
                binaryItems.append(1)
            """
            count = 0
            for item in range(len(readyItems)):
                if readyItems[item] == self.readyText[index]:
                    count = count + 1
            if count == 0:
                readyItems.append(self.readyText[index])
                binaryItems.append(1)
            else:
                binaryItems.append(0)
        binaryItems = defaultdict(list)
        for i,item in enumerate(self.readyText):
            binaryItems[item].append(i)
        binaryItems = {k:v for k,v in binaryItems.items() if len(v)>1}
        print(binaryItems)
        """
        self.newWordsText = binaryItems
        self.buildTable4()



#this function is copy pasted from parent projecs as it is
#it shoul count P(x) in interval from [1;0], so be attentive
    def calculate_P_tab4(self):
        result = []
        summary = 0
        for item in self.newWordsText:
            if item:
                summary += 1
        value = 1 / summary
        current = 0
        for item in self.newWordsText:
            if item:
                current += value
            result.append(current)
        return result



    #this fuction fill tab4 table with values get in fun above
    def buildTable4(self):
        #call function which calculate P(x)
        self.big_P_x = self.calculate_P_tab4()
        self.tableWidget_3.setRowCount(len(self.newWordsText))
        for itemRow in range(0,len(self.newWordsText)):
            if self.setTab4 == False:
                item0 = QTableWidgetItem()
                item0.setData(Qt.DisplayRole,itemRow)
                item1 = QTableWidgetItem()
                item1.setText(self.readyText[itemRow])
                item2 = QTableWidgetItem()
                item2.setText(str(self.newWordsText[itemRow]))
                item3 = QTableWidgetItem()
                item3.setText(str(self.big_P_x[itemRow]))
                #self.setTab4.append(,self.readyText[itemRow], self.newWordsText[itemRow], self.big_P_x[itemRow])
                self.tableWidget_3.setItem(itemRow,0,item0)
                self.tableWidget_3.setItem(itemRow,1,item1)
                self.tableWidget_3.setItem(itemRow,2,item2)
                self.tableWidget_3.setItem(itemRow,3,item3)
            else:
                self.file4.write(str(str(itemRow) + '\t' + str(self.readyText[itemRow])+ '\t' + str(self.newWordsText[itemRow])+'\t' + str( self.big_P_x[itemRow]))+'\n')
        if self.setTab4 == True:
            self.file4.close()
        self.setTab4 = False



    #this function build graphic for tab4 (new Symbols)
    def buildGrahTab4(self):
        iteration_x = []
        iteration_y = self.big_P_x
        newArrayY = []
        for i in range(1,len(self.big_P_x)):
            if iteration_y[i] != 0:
                iteration_x.append(math.log10(i))
                newArrayY.append(math.log10(iteration_y[i]))
        x = iteration_x
        y = newArrayY

        plt.plot(x, y, 'k', marker = 'o')
        plt.grid(color='b', linestyle='-', linewidth=0.5)
        plt.show()







    #thirdTap(the hardest)

    #this function gets value from line edit and convert to int
    def getFromLineEdit(self):
        new_value = ""
        value = [str(item) for item in self.lineEdit.text()]
        for item in value:
            new_value = new_value + item
        self.NumberOfIntervalsItems = int( len(self.readyText)/int(new_value) )




    #this function chunks readyText for intervals(which value we get from  input)
    def chunksIntervals(self):
        self.getFromLineEdit()
        self.chunkedText = zip(*[iter(self.newWordsText)] * self.NumberOfIntervalsItems)
        self.get_p_tab3()




    #this function is copied from c# parent. No matter how it works
    def get_p_tab3(self):
        result = []
        for index in range(len(self.chunkedText)):
            summary = 0
            for item in self.chunkedText[index]:
                if item:
                    summary+=1
            result.append(summary)
        for item in range(len(result)):
            result[item] = result[item]/sum(self.newWordsText)
        self.p_pad3 = sorted(result, reverse = True)
        self.get_P_tab3()



    #this function is copied from c# parent. No metter how it works(on previous interval get value)
    #takes sum of new words from previous intervals and get 1 - sum  new words on  prev intervals / general_summary
    def get_P_tab3(self):
        result = []
        current_p = 1.0
        for index in range(len(self.chunkedText)):
            summary = 0
            for item in self.chunkedText[index]:
                if item:
                    summary+=1
            result.append(summary)
        new_result = []
        new_result.append(current_p)
        general_summary = sum(result)
        for item in range(1, len(result)):
            new_result.append( current_p - (sum(result[0:item])/general_summary))
        self.P_pad3 = new_result
        self.calcAverage()



    #this function calculate average items
    def calcAverage(self):
        self.listOfAverages = []
        average = int(self.NumberOfIntervalsItems)
        for item in range(len(self.chunkedText)):
            self.listOfAverages.append(average)
            average += self.NumberOfIntervalsItems
        self.fillTableTab3()



    #this function fill qttable for tab3
    def fillTableTab3(self):
        #calc sum of new symbols/ngrams again
        result = []
        for index in range(len(self.chunkedText)):
            summary = 0
            for item in self.chunkedText[index]:
                if item:
                    summary+=1
            result.append(summary)
        self.tableWidget_4.setRowCount(len(self.chunkedText))
        for itemRow in range(0,len(self.chunkedText)):
            if self.setTab3 == False:
                item0 = QTableWidgetItem()
                item0.setData(Qt.DisplayRole, itemRow + 1)
                item1 = QTableWidgetItem()
                item1.setText(str(result[itemRow]))
                item2 = QTableWidgetItem()
                item2.setData(Qt.DisplayRole, self.listOfAverages[itemRow])
                item3 = QTableWidgetItem()
                item3.setText(str(self.p_pad3[itemRow]))
                item4 = QTableWidgetItem()
                item4.setText(str(self.P_pad3[itemRow]))
                self.tableWidget_4.setItem(itemRow,0,item0)
                self.tableWidget_4.setItem(itemRow,1,item1)
                self.tableWidget_4.setItem(itemRow,2,item2)
                self.tableWidget_4.setItem(itemRow,3,item3)
                self.tableWidget_4.setItem(itemRow,4,item4)
            else:
                self.file3.write(str(str(itemRow + 1) + '\t' + str(result[itemRow]) + '\t' + str(self.listOfAverages[itemRow])+ '\t' + str(self.p_pad3[itemRow])+'\t' + str( self.P_pad3[itemRow]))+'\n')

        if self.setTab3 == True:
            self.file3.close()
        self.setTab3 = False



    #this function build graphic via mat plot lib , here it build one which is
    #checked
    def buildGrahTab3(self):
        self.chunksIntervals()
        if self.radioButton_5.isChecked():
            #calc sum of new symbols/ngrams again
            result = []
            resultin = []
            for index in range(len(self.chunkedText)):
                summary = 0
                for item in self.chunkedText[index]:
                    if item:
                        summary+=1
                result.append(summary)
                resultin.append(index)
            counts = Counter(result)
            #labels, values = zip(*counts.items())

            #indexes = np.arange(len(labels))
            bar_width = 0.35
            #   here2
            newRes = []
            newInd = []
            for i in range(len(result)):
                if result[i] != 0:
                    newRes.append(math.log10(result[i]))
                    newInd.append(i)

            plt.bar(newInd, newRes, width = bar_width)
            # add labels
            #plt.xticks(indexes + bar_width, labels)
            plt.show()
        elif self.radioButton_4.isChecked():
            iteration_x = []
            iteration_y = self.P_pad3
            newRes = []
            newInd = []
            for i in range(len(self.P_pad3)):
                if iteration_y[i] != 0:
                    newInd.append(math.log10(i+1))
                    newRes.append(math.log10(iteration_y[i]))
            x = newInd
            #x = [math.log10(item) for item in iteration_x]

            y =  newRes

            plt.plot(x, y, 'k',  marker='o')
            plt.grid(color='b', linestyle='-', linewidth=0.5)
            plt.show()

        elif self.radioButton_3.isChecked():
            iteration_x = []
            iteration_y = self.p_pad3
            newArrayY = []
            for i in range(len(self.p_pad3)):
                if iteration_y[i] != 0:
                    iteration_x.append(math.log10(i+1))
                    newArrayY.append(math.log10(iteration_y[i]))
            x = iteration_x
            y = newArrayY

            plt.plot(x, y, 'k',  marker='o')
            plt.grid(color='b', linestyle='-', linewidth=0.5)
            plt.show()





    #LAst tab(2, second Dti)
    #this function make chunks depent on smth
    def calcSecTab (self):
        fn = 1
        st = 0
        dti = {}
        #calc dti
        for item in range(1, len(self.newWordsText)):
            fn = item
            if self.newWordsText[item]:
                dti[item]= (fn - st - 1)
                st = item
        autoChunk = []
    #set intervals
        for item in dti:
            if item in autoChunk:
                autoChunk[item] += 1
            else:
                autoChunk.append(item)
        self.result_tap_2 = sorted(autoChunk, reverse = True)
        self.calc_Big_P_tab2()
        self.fillTableTab2()



    #this func calc P(x) for tab2
    def calc_Big_P_tab2(self):
        current = 1
        summary = sum(self.result_tap_2)
        result = []
        for item in self.result_tap_2:
            result.append(current)
            current = current - (item / summary)
        #self.result_P_tap_2 = result[::1]
        self.result_P_tap_2 = result



    #this function fill qttable for tab2
    def fillTableTab2(self):
        self.tableWidget_2.setRowCount(len(self.result_tap_2)-1)
        summary = sum(self.result_tap_2)
        for itemRow in range(0,len(self.result_tap_2)):
            if self.setTab2 == False:
                item0 = QTableWidgetItem()
                item0.setData(Qt.DisplayRole, itemRow)
                item1 = QTableWidgetItem()
                #item1.setText(str(self.result_tap_2[itemRow]))
                item1.setData(Qt.DisplayRole, self.result_tap_2[itemRow])
                item2 = QTableWidgetItem()
                item2.setText(str(self.result_tap_2[itemRow]/summary))
                self.result_tap_2[itemRow] = self.result_tap_2[itemRow]/summary
                item3 = QTableWidgetItem()
                item3.setText(str(self.result_P_tap_2[itemRow]))
                #self.setTab2.append(str(str(itemRow + 1) + '\t' + str(self.result_tap_2[itemRow]) + '\t' + str(self.result_tap_2[itemRow]/summary)+ '\t' + str(self.result_P_tap_2[itemRow])+ '\n'))
                self.tableWidget_2.setItem(itemRow,0,item0)
                self.tableWidget_2.setItem(itemRow,1,item1)
                self.tableWidget_2.setItem(itemRow,2,item2)
                self.tableWidget_2.setItem(itemRow,3,item3)
            else:
                self.file2.write(str(str(itemRow + 1) + '\t' + str(self.result_tap_2[itemRow]) + '\t' + str(self.result_tap_2[itemRow]/summary)+ '\t' + str(self.result_P_tap_2[itemRow]))+'\n')

        if self.setTab2 == True:
            self.file2.close()
        self.setTab2 = False



    #this function draw graphic fo tab2
    def drawgGaf(self):
        if self.radioButton.isChecked():
            iteration_x = []
            iteration_y = self.result_tap_2
            newArrayX = []
            newArrayY = []
            for i in range(1, len(self.result_tap_2)):
            #    x = [math.log10(item) for item in iteration_x]
                newArrayX.append(math.log10(i))
                newArrayY.append(math.log10(iteration_y[i]))
            y = newArrayY
            x = newArrayX

            plt.plot(x, y, 'k', marker='o')
            plt.grid(color='b', linestyle='-', linewidth=0.5)
            plt.show()
        elif self.radioButton_2.isChecked():
            iteration_x = []
            iteration_y = self.result_P_tap_2
            newArrayY = []
            newArrayX = []
            for i in range(1,len(self.result_P_tap_2)):
                newArrayX.append(math.log10(i))
                newArrayY.append(math.log10(iteration_y[i]))
            x = newArrayX
            y = newArrayY

            plt.plot(x, y, 'k', marker='o')
            plt.grid(color='b', linestyle='-', linewidth=0.5)
            plt.show()







if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
