# -*- coding: utf-8 -*-
from __future__ import division

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import textwrap

from collections import Counter
import numpy as np
from sklearn.neighbors.kde import KernelDensity
import matplotlib.pyplot as plt



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

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 200, 121, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(140, 110, 121, 31))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setMinimum(1)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 70, 71, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Set value", None))
        #self.pushButton.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.OK)
        self.label.setText(_translate("Form", "choose n:", None))




    def OK(self, event):
        #value = [int(item) for item in self.spinBox.value()]
        global N
        value =  self.spinBox.value()
        N = value
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
    #Global variablr
    readyText = ""
    originalText = ""

    #for tab4
    newWordsText = ""
    big_P_x = ""

    #thirPad
    NumberOfIntervalsItems = ""
    chunkedText = ""
    p_pad3 = ""
    P_pad3 = ""
    listOfAverages = ""
    sumIntervalTab3 = ""


    #third pad
    result_tap_2 = ""

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
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 411, 491))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 511, 491))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
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
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 90, 791, 401))
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        #self.tableWidget_4.setHorizontalHeaderItem(0, item)
        #item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
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
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 341, 491))
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
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

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", " ", None))
        self.pushButton.setText(_translate("MainWindow", "Build", None))
        self.pushButton.clicked.connect(self.buildTabHist1)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Symbols", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "F", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "f", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Analysis", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "N", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "p(x)", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P(x)", None))
        self.pushButton_2.setText(_translate("MainWindow", "Build", None))
        self.pushButton_2.clicked.connect(self.drawgGaf)
        self.radioButton.setText(_translate("MainWindow", "p(x)", None))
        self.radioButton_2.setText(_translate("MainWindow", "P(x)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "dTi", None))
        self.label.setText(_translate("MainWindow", "Count of interval:", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "", None))
        self.lineEdit.setText("8")
        #item = self.tableWidget_4.horizontalHeaderItem(0)
        #item.setText(_translate("MainWindow", "X", None))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "N", None))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Average", None))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "p(x)", None))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P(x)", None))
        self.pushButton_4.setText(_translate("MainWindow", "Build", None))
        self.pushButton_4.clicked.connect(self.buildGrahTab3)
        self.radioButton_3.setText(_translate("MainWindow", "p(x)", None))
        self.radioButton_4.setText(_translate("MainWindow", "P(x)", None))
        self.radioButton_5.setText(_translate("MainWindow", "intervals", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Ti", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Meaning", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value", None))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "P(x)", None))
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
            text = open(filename).read()
            self.originalText = text
            self.splitText(text)


    #This function save file ('save as' in menu bar)
    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName( self.setupUi(self), 'Save File')
        #file = open(name,'w')
        #text = self.textEdit.toPlainText()
        #file.write(text)
        #file.close()


    #This fuction open pop up where you have to choose "N"
    def open_n_Popup(self):
        self.popup = QDialog()
        self.popup.ui = Ui_Form()
        self.popup.ui.setupUi(self.popup)
        self.popup.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.popup.exec_()
        global N
        self.n = N


    #this function split text into n-gramms and run waterflow functions which
    # fill tables
    def splitText(self, text):
        self.open_n_Popup()
        splittedText = textwrap.wrap(text, self.n)
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
        for itemRow in range(0,len(valuesF)):
            item0 = QTableWidgetItem()
            item0.setText(labels[itemRow])
            item1 = QTableWidgetItem()
            item1.setText(str(valuesF[itemRow]))
            item2 = QTableWidgetItem()
            item2.setText(str(values_f[itemRow]))
            self.tableWidget.setItem(itemRow,0,item0)
            self.tableWidget.setItem(itemRow,1,item1)
            self.tableWidget.setItem(itemRow,2,item2)



    #this func is for calc f value particular/general
    def calcf(self, values_f):
        values_f = [item / len(self.readyText) for item in values_f]
        return values_f



    #this fuction is for building histogram, activated by pressing  "build"
    # button in tab 1
    def buildTabHist1(self):
        counts = Counter(self.readyText)
        labels, values = zip(*counts.items())
        # sort your values in descending order
        indSort = np.argsort(values)[::-1]
        # rearrange your data
        labels = np.array(labels)[indSort]
        values = np.array(values)[indSort]
        indexes = np.arange(len(labels))
        bar_width = 0.35
        plt.bar(indexes, values)
        # add labels
        plt.xticks(indexes + bar_width, labels)
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
        for index in range(1,len(self.readyText)):
            count = 0
            for item in range(len(readyItems)):
                if readyItems[item] == self.readyText[index]:
                    count = count + 1
            if count == 0:
                readyItems.append(self.readyText[index])
                binaryItems.append(1)
            else:
                binaryItems.append(0)
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
            item0 = QTableWidgetItem()
            item0.setText(self.readyText[itemRow])
            item1 = QTableWidgetItem()
            item1.setText(str(self.newWordsText[itemRow]))
            item2 = QTableWidgetItem()
            item2.setText(str(self.big_P_x[itemRow]))
            self.tableWidget_3.setItem(itemRow,0,item0)
            self.tableWidget_3.setItem(itemRow,1,item1)
            self.tableWidget_3.setItem(itemRow,2,item2)




    #this function build graphic for tab4 (new Symbols)
    def buildGrahTab4(self):
        iteration_x = []
        iteration_y = self.big_P_x
        for i in range(len(self.big_P_x)):
            iteration_x.append(i)
        x = iteration_x
        y = iteration_y

        plt.plot(x, y, 'k')
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
            result[item] = result[item]/sum(result)
        self.p_pad3 = result
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
            item0 = QTableWidgetItem()
            item0.setText(str(result[itemRow]))
            item1 = QTableWidgetItem()
            item1.setText(str(self.listOfAverages[itemRow]))
            item2 = QTableWidgetItem()
            item2.setText(str(self.p_pad3[itemRow]))
            item3 = QTableWidgetItem()
            item3.setText(str(self.P_pad3[itemRow]))
            self.tableWidget_4.setItem(itemRow,0,item0)
            self.tableWidget_4.setItem(itemRow,1,item1)
            self.tableWidget_4.setItem(itemRow,2,item2)
            self.tableWidget_4.setItem(itemRow,3,item3)



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
            plt.bar(resultin, result, width = bar_width)
            # add labels
            #plt.xticks(indexes + bar_width, labels)
            plt.show()
        elif self.radioButton_4.isChecked():
            iteration_x = []
            iteration_y = self.P_pad3
            for i in range(len(self.P_pad3)):
                iteration_x.append(i)
            x = iteration_x
            y = iteration_y

            plt.plot(x, y, 'k')
            plt.grid(color='b', linestyle='-', linewidth=0.5)
            plt.show()

        elif self.radioButton_3.isChecked():
            iteration_x = []
            iteration_y = self.p_pad3
            for i in range(len(self.p_pad3)):
                iteration_x.append(i)
            x = iteration_x
            y = iteration_y

            plt.plot(x, y, 'k')
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
        self.fillTableTab2()



    #this function fill qttable for tab2
    def fillTableTab2(self):
        self.tableWidget_2.setRowCount(len(self.result_tap_2)-1)
        summary = sum(self.result_tap_2)
        for itemRow in range(0,len(self.result_tap_2)):
            item0 = QTableWidgetItem()
            item0.setText(str(self.result_tap_2[itemRow]))
            item1 = QTableWidgetItem()
            item1.setText(str(self.result_tap_2[itemRow]/summary))
            item2 = QTableWidgetItem()
            item2.setText(str(1))
            self.tableWidget_2.setItem(itemRow,0,item0)
            self.tableWidget_2.setItem(itemRow,1,item1)
            self.tableWidget_2.setItem(itemRow,2,item2)



    #this function draw graphic fo tab2
    def drawgGaf(self):
        if self.radioButton.isChecked():
            iteration_x = []
            iteration_y = self.result_tap_2
            for i in range(len(self.result_tap_2)):
                iteration_x.append(i)
            x = iteration_x
            y = iteration_y

            plt.plot(x, y, 'k')
            plt.grid(color='b', linestyle='-', linewidth=0.5)
            plt.show()
        elif self.radioButton_2.isChecked():
            iteration_x = []
            iteration_y = self.result_tap_2
            for i in range(len(self.result_tap_2)):
                iteration_x.append(i)
            x = iteration_x
            y = iteration_y

            plt.plot(x, y, 'k')
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
