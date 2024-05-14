import os
import sys
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
import pandas as pd
import numpy as np
import Ui_interface
from Ui_color import Ui_Dialog
from PyQt5.QtWidgets import (
    QLabel, QFileDialog, QTableWidgetItem, QHeaderView, QVBoxLayout, QDialog
)
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon, QMovie
import sympy as sp
from sympy import symbols, diff, lambdify, sympify, solve, sin, cos, tan, exp, log, sinh, cosh, tanh


class MainApplication(QtWidgets.QMainWindow, Ui_interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = os.getcwd()
        self.setWindowIcon(QIcon('AniGraphix.ico'))
        self.setWindowIcon(QIcon('ico.png'))
        self.data = None
        self.setWindowTitle('AniGraphix')
        
        self.graphDataTable = GraphDataTable(self.tableWidget)    

        self.PLotWidget = pg.PlotWidget()
        self.graphicsView.setBackground((32, 29,  29))
        self.marker = 'o'
        self.color = 'b'
        self.line_style = QtCore.Qt.SolidLine
        self.graphicsView.showGrid(x=True, y=True, alpha = 1)
        self.graphicsView.addLegend()
        self.graphItems = []    
        
        self.pushButton_4.clicked.connect(lambda: self.open_new_transaction_window())
        self.pushButton.clicked.connect(lambda: self.background_color_b())
        self.pushButton_2.clicked.connect(lambda: self.background_color_w())
        self.pushButton_3.clicked.connect(lambda: self.background_anime_gif())

        self.pushButton_9.clicked.connect(lambda: self.plot_the_chart())
        self.pushButton_14.clicked.connect(lambda: self.clear())
        self.saveButton.clicked.connect(lambda: self.save())
        self.pushButton_15.clicked.connect(lambda: self.clear_all())
        self.pushButton_16.clicked.connect(lambda: self.derivatives())

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
        self.graphicsView.setBackground((187, 174, 203))

    # Код производной
    def derivatives(self):
        function_text = self.lineEdit.text()

        try:
            xmin = float(self.lineEdit_2.text())
            xmax = float(self.lineEdit_3.text())
        except ValueError:
            self.showCustomMessageBox("Ошибка", "Неверно заданы Xmin или Xmax.")
            return

        if not function_text.strip():
            self.showCustomMessageBox("Ошибка", "Поле ввода функции пусто.")
            return
    
        np_to_sympy = {
            "np.sin": "sin",
            "np.cos": "cos",
            "np.tan": "tan",
            "np.sinh": "sinh",
            "np.cosh": "cosh",
            "np.tanh": "tanh",
            "np.cot": "cot",
            "np.sec": "sec",
            "np.csc": "csc",
            "np.exp": "exp",
            "np.log": "log",
            "np.sqrt": "sqrt",
        }   
        for np_func, sympy_func in np_to_sympy.items():
            function_text = function_text.replace(np_func, sympy_func)
        
        x_symbol = symbols('x')
        try:
            local_dict = {
                "sin": sin, "cos": cos, "tan": tan, "sinh": sinh, "cosh": cosh, "tanh": tanh,
                "cot": lambda x: 1 / tan(x),
                "sec": lambda x: 1 / cos(x), "csc": lambda x: 1 / sin(x),
                "exp": exp, "log": log, "sqrt": sp.sqrt, "x": x_symbol,                
            }
            sympy_function = sympify(function_text, locals=local_dict)
            derivative = diff(sympy_function, x_symbol)
            derivative_np = lambdify(x_symbol, derivative, 'numpy')
            x = np.linspace(xmin, xmax, 1000)
            y = derivative_np(x)

            pen = pg.mkPen(color=self.selectedColor, style=self.line_style, width=2)
            graph_item = self.graphicsView.plot(x, y, pen=pen, name=f"f'(x): {function_text}")
            self.graphItems.append(graph_item)
        
        except Exception as e:
            self.showCustomMessageBox("Ошибка", f"Ошибка в вычислении производной: {e}")
            return

    #anime-gif
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
        
    def clear(self):
        if self.graphItems:
            last_graph = self.graphItems.pop() 
            self.graphicsView.removeItem(last_graph)  
   
    def clear_all(self):
        self.graphicsView.clear()

    def save(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Сохранить график", "",
                                              "SVG Files (*.svg);;All Files (*)", options=options)
        if fileName:
            if not fileName.endswith('.svg'):
                fileName += '.svg'
            exporter = pg.exporters.SVGExporter(self.graphicsView.plotItem)
            exporter.export(fileName)
    
    def set_SolidLine(self):
        self.line_style = QtCore.Qt.SolidLine
    def set_DashLine(self):
        self.line_style = QtCore.Qt.DashLine
    def set_DotLine(self):
        self.line_style = QtCore.Qt.DotLine
    def set_DashDotLine(self):
        self.line_style = QtCore.Qt.DashDotLine

    def set_crosshair(self):
            self.marker = '+' 
    def set_square(self):
            self.marker = 's'
    def set_triangle(self):
            self.marker = 't'
    def set_circle(self):
            self.marker = 'o'
   
   # построение графика без маркеров 
    def plot_the_chart(self):
        function_text = self.lineEdit.text() 

        try:
            xmin = float(self.lineEdit_2.text())
            xmax = float(self.lineEdit_3.text())
        except ValueError:
            self.showCustomMessageBox("Ошибка", "Неверно заданы Xmin или Xmax.")
            return
        
        if not function_text.strip():
            self.showCustomMessageBox("Ошибка", "Поле ввода функции пусто.")
            return

        x = np.linspace(xmin, xmax, 1000) 

        try:
            y = eval("lambda x: " + function_text, {"np": np, "__builtins__": None}, {})(x)
            pen = pg.mkPen(color=self.selectedColor, style=self.line_style, width=2)
            graph_item = self.graphicsView.plot(x, y, pen=pen, name=function_text)
            self.graphItems.append(graph_item)
            
            self.graphDataTable.add_function(function_text, xmin, xmax)
        
        except Exception as e:
            self.showCustomMessageBox("Ошибка", f"Ошибка в вычислении функции: {e}")
            return 
    
    def showCustomMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStyleSheet("""
        QMessageBox {
            background-color: rgb(7, 32, 65);
            color:rgb(33, 112, 255);
            font: italic bold 16px;
        }""")
        msgBox.exec_()
   
    def open_new_transaction_window(self):
        self.new_window = TransactionWindow()
        self.new_window.colorChanged.connect(self.apply_color_to_plot)
        self.new_window.show()
    
    def apply_color_to_plot(self, rgb_color):
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
        self.setWindowTitle('Colors')

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

class GraphDataTable:
    def __init__(self, tableWidget):
        self.tableWidget = tableWidget
        self.setup_table()

    def setup_table(self):
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Function', 'Derivative', 'Intersections', 'Range'])
        header = self.tableWidget.horizontalHeader() # Выравнивание столбиков таблицы
        for col in range(self.tableWidget.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def add_function(self, function_text, xmin, xmax):
        x = symbols('x')
        try:
            is_np_function = "np." in function_text
            function_text_sympy = function_text.replace("np.", "")
            function_sympy = sympify(function_text_sympy)

            # Вычисляем производную
            derivative = diff(function_sympy, x)
            derivative_text = str(derivative)

            # Преобразуем функцию и производную в функции lambdify
            function = lambdify(x, function_sympy, 'numpy')
            derivative_np = lambdify(x, derivative, 'numpy')

            # Находим точки пересечения с осями координат
            if not is_np_function:
                intersections = []
                roots = solve(function_sympy, x)
                for root in roots:
                    intersections.append((root, function(root)))
            else:
                intersections = None

            # Находим экстремумы функции
            extrema = solve(derivative, x)
            extrema = [float(ext) for ext in extrema if xmin <= float(ext) <= xmax]

            # Вычисляем значения функции в экстремумах и на границах интервала
            critical_points = [xmin, xmax] + extrema
            values_at_critical_points = [function(cp) for cp in critical_points]

            # Находим минимальное и максимальное значения функции
            min_value = min(values_at_critical_points)
            max_value = max(values_at_critical_points)
            function_range = f"[{min_value}, {max_value}]"

            # Вставляем данные в таблицу
            current_row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(current_row_count)
            self.tableWidget.setItem(current_row_count, 0, QTableWidgetItem(function_text_sympy))
            self.tableWidget.setItem(current_row_count, 1, QTableWidgetItem(derivative_text))
            self.tableWidget.setItem(current_row_count, 2, QTableWidgetItem(str(intersections)))
            self.tableWidget.setItem(current_row_count, 3, QTableWidgetItem(function_range))
        
        except Exception as e:
            error_message = f"Ошибка при обработке функции: {e}"
            
            print(error_message)
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QTableWidgetItem(function_text))
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QTableWidgetItem(error_message))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
     

        
        



        
        
       


    
    
        

        


