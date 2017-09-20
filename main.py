import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

qtCreatorFile = "pratyka.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        menu = QtGui.QMenu()
        menu.addAction('actionOpen',self.openDialog)
        #file = QAction("actionOpen",self)

        #file.triggered[QAction].connect(self.openDialog)
        self.setupUi(self)



    def openDialog(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        filenames = QStringList()
        print("HELLLLL")
        if dlg.exec_():
            filenames = dlg.selectedFiles()




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
