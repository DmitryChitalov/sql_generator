#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Modules import
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QDockWidget, \
    QGridLayout, QFrame, QListWidget, QDesktopWidget, QApplication, QStyle

from forms.db_choose_form import DBChooseClass

# The main window of the program


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        # Main Window Toolbar
        self.tool_bar = QToolBar()
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.tool_bar)
        self.database_open = QAction(self)
        database_open_ico = self.style().standardIcon(QStyle.SP_DirOpenIcon)
        self.database_open.setIcon(database_open_ico)
        self.database_open.setToolTip('Выбрать базу данных')
        self.database_open.triggered.connect(self.on_database_open)
        self.tool_bar.addAction(self.database_open)

        # Central widget - query table
        self.tdw = QDockWidget()
        self.tdw.setFeatures(self.tdw.NoDockWidgetFeatures)
        self.tdw_grid = QGridLayout()
        self.tdw_grid.setColumnStretch(2, 1)
        self.tdw_frame = QFrame()
        self.tdw_frame.setStyleSheet(
            "background-color: ghostwhite;"
            "border-width: 0.5px;"
            "border-style: solid;"
            "border-color: silver;")
        self.tdw_frame.setLayout(self.tdw_grid)
        self.tdw.setWidget(self.tdw_frame)

        # Bottom widget
        self.serv_mes = QDockWidget()
        self.serv_mes.setFixedSize(1400, 80)
        self.serv_mes.setFeatures(self.serv_mes.NoDockWidgetFeatures)
        self.listWidget = QListWidget()

    # Function of form opening
    def on_database_open(self):
        db_choose_win = DBChooseClass(self)
        db_choose_win.setWindowTitle('Форма выбора режима работы с программой')
        db_choose_win.show()
        screen = QDesktopWidget().screenGeometry()
        x = int((screen.width() - db_choose_win.width()) / 2)
        y = int((screen.height() - db_choose_win.height()) / 2)
        db_choose_win.move(x, y)


# Display the main window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MW = MainWindow()
    MW.setWindowTitle('Программа для выполнения SQL запросов')
    MW.setFixedSize(700, 500)
    MW.show()
    sys.exit(app.exec_())
