import os
import sys
from PyQt5.QtCore import Qt
import pandas as pd
import numpy as np
import Ui_interface
from Ui_color import Ui_Dialog
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtCore import QUrl








class MainApplication(QtWidgets.QMainWindow, Ui_interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.initVideoPlayer()
        self.directory = os.getcwd()
        self.setWindowIcon(QIcon('AniGraphix.ico'))
        self.setWindowIcon(QIcon('ico.png'))
        self.data = None
        self.setWindowTitle('AniGraphix')
        
        self.userFunction = None
        self.currentXRange = (0, 10)

        self.PLotWidget = pg.PlotWidget()
        self.graphicsView.setBackground((255, 255,  255))
        self.marker = 'o'
        self.color = 'b'
        self.line_style = QtCore.Qt.SolidLine
        self.graphicsView.showGrid(x=True, y=True, alpha = 1)
        self.graphicsView.addLegend()
        # self.plot_item_func = []
        self.graphItems = []    
        
        self.pushButton_4.clicked.connect(lambda: self.open_new_transaction_window())
        self.pushButton.clicked.connect(lambda: self.background_color_b())
        self.pushButton_2.clicked.connect(lambda: self.background_color_w())
        self.pushButton_3.clicked.connect(lambda: self.background_anime_gif())

        self.pushButton_9.clicked.connect(lambda: self.plot_the_chart())
        self.horizontalSlider.valueChanged.connect(self.updateGraph)
        self.pushButton_14.clicked.connect(lambda: self.clear())
        # self.pushButton_14.clicked.connect(lambda: self.playVideo())
        self.pushButton_15.clicked.connect(lambda: self.clear_all())

        self.pushButton_10.clicked.connect(lambda: self.set_crosshair())
        self.pushButton_11.clicked.connect(lambda: self.set_square())
        self.pushButton_12.clicked.connect(lambda: self.set_triangle())
        self.pushButton_13.clicked.connect(lambda: self.set_circle())

        self.pushButton_8.clicked.connect(lambda: self.set_SolidLine())
        self.pushButton_7.clicked.connect(lambda: self.set_DashLine())
        self.pushButton_6.clicked.connect(lambda: self.set_DotLine())
        self.pushButton_5.clicked.connect(lambda: self.set_DashDotLine())

   
#------------------------------- Functions --------------------------
        self.horizontalSlider.valueChanged.connect(self.updateGraph)

        self.x = np.linspace(0, 10, 10)
        self.y = np.sin(self.x)
        self.updateGraph()

       


    def background_color_b(self):
        self.graphicsView.setBackground((32, 29,  29))
        
    def background_color_w(self):
        self.graphicsView.setBackground((255, 255,  255))

    def background_anime_gif(self):
        self.labelForGif = QLabel(self)
        self.labelForGif.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.labelForGif)
        gifPath = "gif_black.gif"
        self.movie = QMovie(gifPath)
        self.labelForGif.setMovie(self.movie)
        self.labelForGif.resize(640, 320)  
        self.labelForGif.move(10, 10) 

        layout = QVBoxLayout()
        layout.addWidget(self.labelForGif)
        self.labelForGif.setGeometry((self.width() - 640) // 2, (self.height() - 320) // 2, 640, 320)
        QTimer.singleShot(4000, self.labelForGif.hide)
        self.movie.start()

        
    #     self.playVideoButton = QPushButton("Play Video", self)
    #     self.playVideoButton.setGeometry(750, 100, 100, 30)
    #     self.playVideoButton.clicked.connect(self.playVideo)
        
    # def initVideoPlayer(self):
    #     self.videoWidget = QVideoWidget(self)
    #     self.videoWidget.setGeometry(100, 100, 720, 720)
    #     self.videoWidget.hide()

    #     self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
    #     self.mediaPlayer.setVideoOutput(self.videoWidget)

    #     videoPath = "anime_jumpscare.mp4"  
    #     self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(videoPath)))

    # def playVideo(self):
    #     if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
    #         self.mediaPlayer.pause()
    #         self.videoWidget.hide()
    #     else:
    #         self.videoWidget.show()
    #         self.mediaPlayer.play()
        


        
    def clear(self):
        if self.graphItems:
            last_graph = self.graphItems.pop() 
            self.graphicsView.removeItem(last_graph)  


    
    def clear_all(self):
        self.graphicsView.clear()
        # self.lst_item_func.clear()




    def set_SolidLine(self):
        self.line_style = QtCore.Qt.SolidLine
        self.updateGraph()
    def set_DashLine(self):
        self.line_style = QtCore.Qt.DashLine
        self.updateGraph()
    def set_DotLine(self):
        self.line_style = QtCore.Qt.DotLine
        self.updateGraph()
    def set_DashDotLine(self):
        self.line_style = QtCore.Qt.DashDotLine
        self.updateGraph()

    # def plot_the_chart(self):
    #     function_text = self.lineEdit.text() 

    #     try:
    #         xmin = float(self.lineEdit_2.text())
    #         xmax = float(self.lineEdit_3.text())
    #     except ValueError:
    #         QMessageBox.warning(self, "Ошибка", "Неверно заданы Xmin или Xmax.")
    #         return

    #     if not function_text.strip():
    #         QMessageBox.warning(self, "Ошибка", "Поле ввода функции пусто.")
    #         return

    #     x = np.linspace(xmin, xmax, 500) 

    #     try:
    #         y = eval("lambda x: " + function_text, {"np": np, "__builtins__": None}, {})(x)
    #         pen = pg.mkPen(color=self.selectedColor, style=self.line_style, width=2)
    #         # self.graphicsView.plot(x, y, pen=pen, name=function_text) 
    #         graph_item = self.graphicsView.plot(x, y, pen=pen, name=function_text)
    #         self.graphItems.append(graph_item)


    #     except Exception as e:
    #         QMessageBox.warning(self, "Ошибка", f"Ошибка в вычислении функции: {e}")
    #         return 

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
        try:
            self.userFunction = eval(f"lambda x: {function_text}", {"np": np})
            self.currentXRange = (float(self.lineEdit_2.text()), float(self.lineEdit_3.text()))
            self.updateGraph()  
        except Exception as e:
            print(f"Ошибка: {e}")

    def updateGraph(self):
        if self.userFunction:
            xmin, xmax = self.currentXRange
            x = np.linspace(xmin, xmax, 1000) 
            y = self.userFunction(x)

            for item in self.graphItems:
                self.graphicsView.removeItem(item)
            self.graphItems.clear()

            pen = pg.mkPen(color=self.selectedColor, style=self.line_style, width=2)
            lineItem = self.graphicsView.plot(x, y, pen=pen)
            self.graphItems.append(lineItem)

            marker_count = self.horizontalSlider.value()
            if marker_count > 0:
                marker_interval = max(1, len(x) // marker_count)
                x_markers = x[::marker_interval]
                y_markers = y[::marker_interval]
                markersItem = self.graphicsView.plot(x_markers, y_markers, pen=None, symbol=self.marker, symbolSize=5, symbolBrush='b')
                self.graphItems.append(markersItem)


    
    def set_crosshair(self):
        self.marker = '+' 
        self.updateGraph()

    def set_square(self):
        self.marker = 's'
        self.updateGraph()

    def set_triangle(self):
        self.marker = 't'
        self.updateGraph()

    def set_circle(self):
        self.marker = 'o'
        self.updateGraph()


    def open_new_transaction_window(self):
        self.new_window = TransactionWindow()
        self.new_window.colorChanged.connect(self.apply_color_to_plot)
        self.new_window.show()
    
    def apply_color_to_plot(self, rgb_color):
        self.updateGraph()
        self.selectedColor = pg.mkColor(rgb_color)


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
     

        
        



        
        
       


    
    
        

        


