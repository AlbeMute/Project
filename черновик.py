# pen = pg.mkPen(color=(np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)), style=self.line_style, width=2)
# pen = pg.mkPen(color=self.selectedColor, style=self.line_style, width=2)

        # self.graphicsView.plot(x, y, pen=pen, name=function_text) 
        
        # symbol_map = {
        #     'crosshair': '+',
        #     's': 's',  
        #     't': 't',  
        #     'o': 'o',  
        # }
        # symbol = symbol_map.get(self.marker, None)

        # self.graphicsView.plot(x, y, pen=pen, symbol=symbol, name=function_text)


    # def open_new_transaction_window(self):
    #     self.new_window = QtWidgets.QDialog()
    #     self.new_window.colorChanged.connect(self.apply_color_to_plot)  
    #     self.ui_window = Ui_Dialog()
    #     self.ui_window.setupUi(self.new_window)
    #     self.new_window.show()


# class  TransactionWindow(QDialog, Ui_Dialog, Ui_interface.Ui_MainWindow):
#       def __init__(self):
#             super().__init__()
#             self.pushButton_10.clicked.connect(lambda: self.set_red())
#       def set_red(self):
#             self.pushButton_10.setStyleSheet("background-color: red;")



    # def emit_color(self, color):
    #     self.colorChanged.emit(color)  

    # def set_red(self):
    #     self.pushButton_10.setStyleSheet("background-color: r;")
    #     self.emit_color("r")

    # def set_red(self):
    #     self.pushButton_10.setStyleSheet("background-color: r;")
    # def set_green(self):
    #     self.pushButton_11.setStyleSheet('background-color: green;')
    # def set_purple(self):
    #     self.pushButton_12.setStyleSheet('background-color: purple;')
    # def set_blue(self):
    #     self.pushButton_13.setStyleSheet('background-color: blue;')
    # def set_yellow(self):
    #     self.pushButton_21.setStyleSheet('background-color: yellow;')
    # def set_orange   


# построение 1 графика с маркерами
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

# построение графика без маркеров
    def plot_the_chart(self):
        functions_text = self.lineEdit.text().split(',')  
        
        try:
            xmin = float(self.lineEdit_2.text())
            xmax = float(self.lineEdit_3.text())
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Неверно заданы Xmin или Xmax.")
            return

        if not functions_text:
            QMessageBox.warning(self, "Ошибка", "Поле ввода функции пусто.")
            return

        x = np.linspace(xmin, xmax, 1000) 
        for func_text in functions_text: 
            func_text = func_text.strip()  
            if not func_text:
                continue

        try:
            userFunction = eval(f"lambda x: {func_text}", {"np": np})
            self.updateGraph()
            y = userFunction(x)

            pen = pg.mkPen(color=self.selectedColor, style=self.line_style, width=2)
            graph_item = self.graphicsView.plot(x, y, pen=pen, name=func_text)
            self.graphItems.append(graph_item)

        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Ошибка в вычислении функции: {e}")
# маркеры для графика
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


#------------------------------- Functions --------------------------

        # self.x = np.linspace(0, 10, 10)
        # self.y = np.sin(self.x)
        # self.updateGraph()
                

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

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QUrl
        self.initVideoPlayer()

        self.userFunction = None
        self.currentXRange = (0, 10)


        self.playVideoButton = QPushButton("Play Video", self)
        self.playVideoButton.setGeometry(750, 100, 100, 30)
        self.playVideoButton.clicked.connect(self.playVideo)
        
    def initVideoPlayer(self):
        self.videoWidget = QVideoWidget(self)
        self.videoWidget.setGeometry(100, 100, 720, 720)
        self.videoWidget.hide()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        videoPath = "anime_jumpscare.mp4"  
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(videoPath)))

    def playVideo(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            self.videoWidget.hide()
        else:
            self.videoWidget.show()
            self.mediaPlayer.play()




   # построение графика без маркеров
    @staticmethod
    def check(den):
        try:
            x = float(den)
        except:
            return False
        # if type(den) == float:
        #     return True 
        # else:
        #     return False
    
    def plot_the_chart(self):
        function_text = self.lineEdit.text() 
        if self.check(self.lineEdit_2.text()) and self.check(self.lineEdit_3.text()):
            xmin = float(self.lineEdit_2.text())
            xmax = float(self.lineEdit_3.text())
        else:
            QMessageBox.warning(self, "Ошибка", "Неверно заданы Xmin или Xmax.")