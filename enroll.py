# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:17:05 2019

@author: TEEE
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import serial
Ui_MainWindow, QtBaseClass = uic.loadUiType("uiux.ui")

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.confirm.clicked.connect(self.send)
        self.ui.connect.clicked.connect(self.Connect)

    def send(self):
        name = (self.ui.namebox.toPlainText())
        sernum = self.ui.no_box.toPlainText()
        self.__ser.write(str.encode(name + ""+ sernum))
        git= self.__ser.readline()
        print(git.decode())
        self.ui.output.setText(git.decode())
        
    def Connect(self):
        try:
            self.__ser = serial.Serial('COM28', 115200, timeout=1)
        except:
            self.ui.output.setText("error Opening port")
            print("error connecting to port")
        else:
            self.ui.output.setText("Successfully connected")

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

