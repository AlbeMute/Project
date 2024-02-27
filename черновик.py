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