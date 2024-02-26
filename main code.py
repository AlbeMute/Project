import os
import sys
from PyQt5.QtCore import Qt
import pandas as pd
import Ui_interface
from Ui_color import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore

class MainApplication(QtWidgets.QMainWindow, Ui_interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = os.getcwd()
        self.data = None
        self.setWindowTitle('AlbeMute')
        
        self.PLotWidget = pg.PlotWidget()
        self.graphicsView.setBackground((255, 255,  255))
        self.marker = 'o'
        self.color = 'b'
        self.lst_item_func = []
        self.lst_item_xlsx = []
        self.line_style = QtCore.Qt.SolidLine
        self.graphicsView.showGrid(x=True, y=True, alpha = 1)
        self.graphicsView.addLegend()
        
        self.pushButton_4.clicked.connect(lambda: self.open_new_transaction_window())
        self.pushButton.clicked.connect(lambda: self.background_color_b())
        self.pushButton_2.clicked.connect(lambda: self.background_color_w())

        self.pushButton_9.clicked.connect(lambda: self.plot_the_chart())
        self.pushButton_14.clicked.connect(lambda: self.clear())
        self.pushButton_15.clicked.connect(lambda: self.clear_all())

        self.pushButton_10.clicked.connect(lambda: self.set_crosshair())
        self.pushButton_11.clicked.connect(lambda: self.set_square())
        self.pushButton_12.clicked.connect(lambda: self.set_triangle())
        self.pushButton_13.clicked.connect(lambda: self.set_circle())

        self.pushButton_8.clicked.connect(lambda: self.set_SolidLine())
        self.pushButton_7.clicked.connect(lambda: self.set_DashLine())
        self.pushButton_6.clicked.connect(lambda: self.set_DotLine())
        self.pushButton_5.clicked.connect(lambda: self.set_DashDotLine())
    
    def background_color_b(self):
        self.graphicsView.setBackground((32, 29,  29))
        
    def background_color_w(self):
        self.graphicsView.setBackground((255, 255,  255))
    
    def clear(self):
        self.graphicsView.removeItem(self.lst_item_xlsx[0])
        self.lst_item_xlsx.pop(0)
    def clear_all(self):
        self.graphicsView.clear()
        self.lst_item_func.clear()
    
    def set_crosshair(self):
        self.marker = 'crosshair'
    def set_square(self):
        self.marker = 's'
    def set_triangle(self):
        self.marker = 't'   
    def set_circle(self):
        self.marker = 'o'  
    
    def set_SolidLine(self):
        self.line_style = QtCore.Qt.SolidLine
    def set_DashLine(self):
        self.line_style = QtCore.Qt.DashLine
    def set_DotLine(self):
        self.line_style = QtCore.Qt.DotLine
    def set_DashDotLine(self):
        self.line_style = QtCore.Qt.DashDotLine

    

    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

class  TransactionWindow(QDialog, Ui_Dialog, Ui_interface.Ui_MainWindow):
      def __init__(self):
            super().__init__()
            self.pushButton_10.clicked.connect(lambda: self.set_red())
      def set_red(self):
            self.pushButton_10.setStyleSheet("background-color: red;")

        
        
       


    
    
        

        


def main():
  app = QtWidgets.QApplication(sys.argv)
  window = MainApplication()
  window.show()
  app.exec_()


if __name__ == '__main__':
  main()