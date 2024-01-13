"""!  QT GUI Interface


  - sys 
  - .. 
  - gs 
  - helpers 
  - gs 
  
Author(s):
  - Created by Davidka on 09.11.2023 .
"""

# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python


import sys
#####from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QDesktopWidget
from src.suppliers import Supplier
from src.settings import gs
from src.helpers import  logger,  logs_and_errors_decorator
from src.io_interface import j_loads as j_loads
# --------------------------------


class MainWindow(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()

        # Настройка окна

        # Задаем размер окна
        width = 1200
        height = 800

        # Получаем размер экрана
        screen_size = QDesktopWidget().screenGeometry(-1)

        # Вычисляем координаты верхнего левого угла окна
        x = (screen_size.width() - width) // 2
        y = (screen_size.height() - height) // 2

        # Устанавливаем размер и положение окна
        self.setGeometry(x, y, width, height)

        # Title
        self.setWindowTitle('hypotez')
        # Создание раскрывающегося списка
        self.combobox = QComboBox(self)
        self.combobox.setGeometry(50, 50, 300, 60)
        # self.combobox.addItems(['Вариант 1', 'Вариант 2', 'Вариант 3'])

        # Создание кнопки
        self.button = QPushButton('Start parcing', self)
        self.button.setGeometry(400, 50, 300, 60)
        # self.button.move(50, 100)
        self.button.clicked.connect(self.on_button_click)

    def run(self, supplier_prefix):
        self.window = MainWindow()
        self.window.combobox.addItems(supplier_prefix)
        self.window.show()
        sys.exit(self.app.exec_())

    def on_button_click(self):
        # Обработчик события нажатия кнопки
        supplier_prefix = self.combobox.currentText()
        logger.info(
            f''' Старт {supplier_prefix} в {gs.GET_NOW}''')

        s = Supplier(supplier_prefix=supplier_prefix, lang='EN')
        s.run()
