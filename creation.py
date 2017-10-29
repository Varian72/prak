# coding=utf-8

# provides interaction with the Python interpreter
import sys

# provides core non-graphical functionality
from PyQt4 import QtCore

# provides the graphic elements
from PyQt4 import QtGui


class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # creates a 'QProgressBar'
        self.qprogressbar = QtGui.QProgressBar()

        # restarts the 'QProgressBar'
        self.qprogressbar.reset()

        # centers the text of the 'QProgressBar'
        self.qprogressbar.setAlignment(QtCore.Qt.AlignCenter)

        # connects the 'QProgressBar.valueChanged()' signal with the 'qprogressbar_value_changed()' slot
        self.qprogressbar.valueChanged.connect(self.qprogressbar_value_changed)

        # creates a 'QPushButton'
        self.qpushbutton = QtGui.QPushButton(u'&Start')

        # connects the 'QPushButton.clicked()' signal with the 'qpushbutton_clicked()' slot
        self.qpushbutton.clicked.connect(self.qpushbutton_clicked)

        # creates a 'QTimer'
        self.qtimer = QtCore.QTimer()

        # connects the 'QTimer.timeout()' signal with the 'qtimer_timeout()' slot
        self.qtimer.timeout.connect(self.qtimer_timeout)

        # creates a 'QVBoxLayout'
        vlayout = QtGui.QVBoxLayout()

        # adds the 'QProgressBar' to the 'QVBoxLayout'
        vlayout.addWidget(self.qprogressbar)

        # adds the 'QProgressBar' to the 'QVBoxLayout'
        vlayout.addWidget(self.qpushbutton)

        # inserts a stretchable space in the 'QVBoxLayout'
        vlayout.addStretch()

        # sets the 'QVBoxLayout' as the window layout
        self.setLayout(vlayout)

    # 'qtimer_timeout()' slot
    @QtCore.pyqtSlot()
    def qtimer_timeout(self):
        # gets the current value of the 'QProgressBar'
        value = self.qprogressbar.value()

        # adds 1 to the current value of the 'QProgressBar'
        self.qprogressbar.setValue(value + 1)

    # 'qpushbutton_clicked ()' slot
    @QtCore.pyqtSlot()
    def qpushbutton_clicked(self):
        # restarts the 'QProgressBar'
        self.qprogressbar.reset()

        # starts the 'QTimer' with an interval of 40 milliseconds
        self.qtimer.start(40)

    # 'qprogressbar_value_changed()' slot
    @QtCore.pyqtSlot(int)
    def qprogressbar_value_changed(self, value):
        # if the 'QProgressBar' reaches its maximum value
        if value == self.qprogressbar.maximum():
            # stops the 'QTimer'
            self.qtimer.stop()


# creates the application
application = QtGui.QApplication(sys.argv)

# creates the window
window = Window()

# sets the window title
window.setWindowTitle(u'QProgressBar - Creation')

# sets the window dimensions
window.resize(300, 80)

# shows the window
window.show()

# runs the application
sys.exit(application.exec_())
