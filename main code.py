import os
import sys
from PyQt5.QtCore import Qt
import pandas as pd
import numpy as np
import Ui_interface
from Ui_color import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer




class MainApplication(QtWidgets.QMainWindow, Ui_interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = os.getcwd()
        self.setWindowIcon(QIcon('AlbeMute.ico'))
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
        self.pushButton_3.clicked.connect(lambda: self.background_anime_gif())

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

    def background_anime_gif(self):
        self.labelForGif = QLabel(self)
        # self.labelForGif.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.labelForGif)
        gifPath = "gif_black.gif"
        self.movie = QMovie(gifPath)
        self.labelForGif.setMovie(self.movie)
        self.labelForGif.resize(793, 560)  
        self.labelForGif.move(10, 10) 

        layout = QVBoxLayout()
        layout.addWidget(self.labelForGif)
        self.labelForGif.setGeometry((self.width() - 640) // 2, (self.height() - 320560) // 2, 640, 320)
        QTimer.singleShot(4100, self.labelForGif.hide)
        self.movie.start()





        
    
    # def clear(self):
        
    def clear_all(self):
        self.graphicsView.clear()
        self.lst_item_func.clear()
        self.lst_item_xlsx.clear()

    
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

    def plot_the_chart(self):
        function_text = self.lineEdit.text() 

        try:
            xmin = float(self.lineEdit_2.text())
            xmax = float(self.lineEdit_3.text())
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Неверно заданы Xmin или Xmax.")
            return

        if not function_text.strip():
            QMessageBox.warning(self, "Ошибка", "Поле ввода функции пусто.")
            return

        x = np.linspace(xmin, xmax, 500) 

        try:
            y = eval("lambda x: " + function_text, {"np": np, "__builtins__": None}, {})(x)
            pen = pg.mkPen(color=self.selectedColor, style=self.line_style, width=2)
            self.graphicsView.plot(x, y, pen=pen, name=function_text) 

        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Ошибка в вычислении функции: {e}")
            return

        

    def open_new_transaction_window(self):
        self.new_window = TransactionWindow()
        self.new_window.colorChanged.connect(self.apply_color_to_plot)
        self.new_window.show()
    
    def apply_color_to_plot(self, color):
        self.selectedColor = color


class TransactionWindow(QDialog, Ui_Dialog):
    colorChanged = pyqtSignal(tuple)  
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.pushButton_10.clicked.connect(lambda: self.emit_color("red"))
        self.pushButton_11.clicked.connect(lambda: self.emit_color("green"))
        self.pushButton_12.clicked.connect(lambda: self.emit_color("purple"))
        self.pushButton_13.clicked.connect(lambda: self.emit_color("blue"))
        self.pushButton_21.clicked.connect(lambda: self.emit_color("yellow"))
        self.pushButton_20.clicked.connect(lambda: self.emit_color('orange'))
        self.pushButton_19.clicked.connect(lambda: self.emit_color('dark_blue'))
        self.pushButton_18.clicked.connect(lambda: self.emit_color('pink'))



    def emit_color(self, color_name):
        color_map = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "purple": (128, 0, 128),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0),
            'orange':  (255, 165 ,0),
            'dark_blue' : (0, 0, 139),
            'pink' : (255, 192, 203)

        }
        self.colorChanged.emit(color_map[color_name])
    

        
def main():
  app = QtWidgets.QApplication(sys.argv)
  window = MainApplication()
  window.show()
  app.exec_()


if __name__ == '__main__':
  main()  
     

        
        



        
        
       


    
    
        

        


