from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from AXEl_UI import Ui_MainWindow
import Main
import sys


class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        Main.run_axel()


start_function = MainThread()


class GuiStart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.axel_ui = Ui_MainWindow()
        self.axel_ui.setupUi(self)
        self.axel_ui.start_botton.clicked.connect(self.startFunc)
        self.axel_ui.exit_botton.clicked.connect(self.close)
    
    def startFunc(self):
        self.axel_ui.movies = QtGui.QMovie('Database\\GUI\\Code.gif')
        self.axel_ui.scifi_terminal.setMovie(self.axel_ui.movies)
        self.axel_ui.movies.start()

        self.axel_ui.movies = QtGui.QMovie('Database\\GUI\\earth.gif')
        self.axel_ui.gif1.setMovie(self.axel_ui.movies)
        self.axel_ui.movies.start()

        self.axel_ui.movies = QtGui.QMovie('Database\\GUI\\initial.gif')
        self.axel_ui.initiating.setMovie(self.axel_ui.movies)
        self.axel_ui.movies.start()

        self.axel_ui.movies = QtGui.QMovie('Database\\GUI\\reactor.gif')
        self.axel_ui.reactor.setMovie(self.axel_ui.movies)
        self.axel_ui.movies.start()

        self.axel_ui.movies = QtGui.QMovie('Database\\GUI\\reactor2.gif')
        self.axel_ui.reactor_3.setMovie(self.axel_ui.movies)
        self.axel_ui.movies.start()

        self.axel_ui.movies = QtGui.QMovie('Database\\GUI\\scifi.gif')
        self.axel_ui.reactor_2.setMovie(self.axel_ui.movies)
        self.axel_ui.movies.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)

        timer.start(1000)

        start_function.start()

    def showtime(self):

        current_time = QTime.currentTime()

        label_time = current_time.toString("hh:mm:ss")
        label = "Time : " + label_time

        self.axel_ui.textBrowser.setText(label) 

Gui_App = QApplication(sys.argv)

Gui_Axel = GuiStart()

Gui_Axel.show()

exit(Gui_App.exec_())
