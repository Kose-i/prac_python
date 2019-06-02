#! /usr/bin/env python3

import sys

#from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QPushButton

if __name__=='__main__':
  app = QApplication(sys.argv)
  
  widget = QWidget()
  widget.resize(200, 200)
  widget.setWindowTitle("window-Title")
  button = QPushButton('Change title', widget)

  def change_title():
    widget.setWindowTitle('Hello Qt')

  button.setGeometry(50, 25, 100, 50)

  button.clicked.connect(change_title)

  widget.show()
  
  app.exec_()
