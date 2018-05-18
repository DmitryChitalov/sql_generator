# -*- coding: utf-8 -*-
# Modules import
from PyQt5 import QtCore
from PyQt5 import QtSql
from PyQt5.QtWidgets import QWidget, QLabel, QRadioButton, QGridLayout, \
    QLineEdit, QPushButton, QHBoxLayout, QFrame, QVBoxLayout, QFormLayout, \
    QFileDialog, QListWidgetItem, QTableView

# Structure of the database choosing form


class DBChooseClass(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        global par
        par = parent
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint)
        self.setWindowModality(QtCore.Qt.WindowModal)

        # Choosing of database format - block
        self.db_format_label = QLabel('Выберите формат БД')
        self.sqlite_radio = QRadioButton('SQLite')
        self.sqlite_radio.setChecked(True)
        self.mysql_radio = QRadioButton('MySQL')
        self.msaccess_radio = QRadioButton('MSAccess')
        self.db_format_hbox = QGridLayout()
        self.db_format_hbox.addWidget(self.sqlite_radio, 0, 0)
        self.db_format_hbox.addWidget(self.mysql_radio, 0, 1)
        self.db_format_hbox.addWidget(self.msaccess_radio, 0, 2)
        self.sqlite_radio.toggled.connect(self.on_sqlite_radio_clicked)
        self.mysql_radio.toggled.connect(self.on_mysql_radio_clicked)
        self.msaccess_radio.toggled.connect(self.on_msaccess_radio_clicked)

        # SQLite and MSAccess database parameters - block
        self.db_path_lbl = QLabel('Путь:')
        self.db_path_edit = QLineEdit()
        self.db_path_edit.setEnabled(False)
        self.db_path_edit.setFixedSize(224, 25)
        self.db_path_button = QPushButton("...")
        self.db_path_button.clicked.connect(self.on_db_path_choose)
        self.db_path_button.setFixedSize(25, 25)
        self.db_path_hbox = QHBoxLayout()
        self.db_path_hbox.addWidget(self.db_path_lbl)
        self.db_path_hbox.addWidget(self.db_path_edit)
        self.db_path_hbox.addWidget(self.db_path_button)
        self.db_path_hbox_frame = QFrame()
        self.db_path_hbox_frame.setLayout(self.db_path_hbox)

        # MySQL database parameters - block
        self.host_lbl = QLabel('Хост:')
        self.host_name = QLineEdit()
        self.database_lbl = QLabel('Имя БД:')
        self.database_name = QLineEdit()
        self.user_lbl = QLabel('Пользователь:')
        self.user_name = QLineEdit()
        self.passwrd_lbl = QLabel('Пароль:')
        self.passwrd_txt = QLineEdit()
        self.db_prs_grid = QGridLayout()
        self.db_prs_grid.addWidget(self.host_lbl, 0, 0)
        self.db_prs_grid.addWidget(self.host_name, 0, 1)
        self.db_prs_grid.addWidget(self.database_lbl, 1, 0)
        self.db_prs_grid.addWidget(self.database_name, 1, 1)
        self.db_prs_grid.addWidget(self.user_lbl, 2, 0)
        self.db_prs_grid.addWidget(self.user_name, 2, 1)
        self.db_prs_grid.addWidget(self.passwrd_lbl, 3, 0)
        self.db_prs_grid.addWidget(self.passwrd_txt, 3, 1)
        self.db_prs_grid_frame = QFrame()
        self.db_prs_grid_frame.setLayout(self.db_prs_grid)
        self.db_prs_grid_frame.setVisible(False)

        # Put db_path_hbox_frame and db_prs_grid_frame into layout
        self.db_prs_grid_vbox = QVBoxLayout()
        self.db_prs_grid_vbox.addWidget(self.db_path_hbox_frame)
        self.db_prs_grid_vbox.addWidget(self.db_prs_grid_frame)

        # HBox and frame for all parameters
        self.db_format_grid = QGridLayout()
        self.db_format_grid.addWidget(self.db_format_label, 0, 0,
                                      alignment=QtCore.Qt.AlignCenter)
        self.db_format_grid.addLayout(self.db_format_hbox, 1, 0)
        self.db_format_grid.addLayout(self.db_prs_grid_vbox, 2, 0,
                                      alignment=QtCore.Qt.AlignCenter)
        self.db_format_grid_frame = QFrame()
        self.db_format_grid_frame.setLayout(self.db_format_grid)
        self.db_format_grid_hbox = QHBoxLayout()
        self.db_format_grid_hbox.addWidget(self.db_format_grid_frame)

        # Main buttons of the form
        self.save_button = QPushButton('Сохранить')
        self.save_button.setFixedSize(80, 25)
        self.save_button.clicked.connect(self.on_save_clicked)
        self.save_button.setEnabled(False)
        self.cancel_button = QPushButton('Отмена')
        self.cancel_button.setFixedSize(80, 25)
        self.cancel_button.clicked.connect(self.on_cancel_clicked)
        self.buttons_hbox = QHBoxLayout()
        self.buttons_hbox.addWidget(self.save_button)
        self.buttons_hbox.addWidget(self.cancel_button)

        # layout of form elements
        self.form_grid = QGridLayout()
        self.form_grid.addLayout(self.db_format_grid_hbox, 0, 0,
                                 alignment=QtCore.Qt.AlignCenter)
        self.form_grid.addLayout(self.buttons_hbox, 1, 0,
                                 alignment=QtCore.Qt.AlignCenter)
        self.form_frame = QFrame()
        self.form_frame.setStyleSheet(
            open(
                "./styles/properties_form_style.qss",
                "r").read())
        self.form_frame.setLayout(self.form_grid)
        self.form = QFormLayout()
        self.form.addRow(self.form_frame)
        self.setLayout(self.form)

    # Function of sqlite_radio press
    def on_sqlite_radio_clicked(self):
        self.setFixedHeight(180)
        self.db_path_hbox_frame.setVisible(True)
        self.db_prs_grid_frame.setVisible(False)

    # Function of msaccess_radio press
    def on_msaccess_radio_clicked(self):
        self.setFixedHeight(180)
        self.db_path_hbox_frame.setVisible(True)
        self.db_prs_grid_frame.setVisible(False)

    # Function of mysql_radio press
    def on_mysql_radio_clicked(self):
        self.setFixedHeight(250)
        self.db_path_hbox_frame.setVisible(False)
        self.db_prs_grid_frame.setVisible(True)

    # Function of btn_path press
    def on_db_path_choose(self):
        global db_path
        db_path, _filter = QFileDialog.getOpenFileName(
            None, "Open Data File", '.', "(*.sqlite *db)")
        self.db_path_edit.setText(db_path)
        self.save_button.setEnabled(True)

    # Save function
    def on_save_clicked(self):
        # Set connection with SQLite
        if self.sqlite_radio.isChecked():
            self.con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            self.con.setDatabaseName(db_path)
            self.con.open()

        # Set connection with MySQL
        if self.mysql_radio.isChecked():
            self.con = QtSql.QSqlDatabase.addDatabase('QMYSQL')
            self.con.setHostName(self.host_name.text)
            self.con.setDatabaseName(self.database_name.text())
            self.con.setUserName(self.user_name.text())
            self.con.setPassword(self.passwrd_txt.text())
            self.con.open()

        # Set connection with Microsoft Access through ODBC
        if self.msaccess_radio.isChecked():
            self.con = QtSql.QSqlDatabase.addDatabase("QODBC")
            self.con.setDatabaseName("DRIVER={Microsoft Access Driver \
            (*.mdb)};FIL={MS Access};DBQ=" + db_path + '"')
            self.con.open()

        if self.con.isOpen():
            self.msg_lbl = QLabel(
                '<span style="color:#008000;">БД успешно открыта</span>')
        else:
            self.msg_lbl = QLabel(
                '<span style="color:#ff0000;">Не удалось открыть БД</span>')

        # Out service message
        par.addDockWidget(QtCore.Qt.TopDockWidgetArea, par.tdw)
        par.addDockWidget(QtCore.Qt.BottomDockWidgetArea, par.serv_mes)
        par.serv_mes.setWidget(par.listWidget)
        par.serv_mes.setWindowTitle("Служебные сообщения")
        par.item = QListWidgetItem()
        par.listWidget.addItem(par.item)
        par.listWidget.setItemWidget(par.item, self.msg_lbl)

        # Title out
        self.tdw_lbl = QLabel('База данных:')
        self.tdw_lbl.setStyleSheet("border-style: none;" "font-size: 10pt;")
        self.tdw_path_lbl = QLineEdit()
        self.tdw_path_lbl.setStyleSheet("background-color: white;"
                                        "font-size: 10pt;" "color: green;")
        self.tdw_path_lbl.setFixedSize(500, 25)
        self.tdw_path_lbl.setText(db_path)
        self.tdw_path_lbl.setEnabled(False)
        par.tdw_grid.addWidget(self.tdw_lbl, 0, 0,
                               alignment=QtCore.Qt.AlignCenter)
        par.tdw_grid.addWidget(self.tdw_path_lbl, 0, 1,
                               alignment=QtCore.Qt.AlignCenter)

        # Making table-window
        self.database_window = QWidget()
        self.database_window.setWindowTitle("Модель-таблица")

        # Making box for table
        self.database_window_vbox = QVBoxLayout()

        # Making field for query enter
        self.query_lbl = QLabel('Введите запрос:')
        self.query_edit = QLineEdit()
        self.query_grid = QGridLayout()
        self.query_grid.addWidget(self.query_lbl, 0, 0)
        self.query_grid.addWidget(self.query_edit, 0, 1)
        self.query_grid_frame = QFrame()
        self.query_grid_frame.setLayout(self.query_grid)

        # Place frame with query_lbl and query_edit in database_window_vbox
        self.database_window_vbox.addWidget(self.query_grid_frame)

        # Making button for query run
        self.query_run_btn = QPushButton("Выполнить запрос")
        self.query_run_btn.clicked.connect(self.on_query_run)
        self.database_window_vbox.addWidget(self.query_run_btn)

        # Making controls for out of query results
        self.query_run_lbl = QLabel('Результат выполнения запроса:')
        self.database_window_vbox.addWidget(self.query_run_lbl)
        self.db_data_table = QTableView()
        self.database_window_vbox.addWidget(self.db_data_table)

        # Place container in the window
        self.database_window.setLayout(self.database_window_vbox)
        self.database_window.resize(300, 250)
        par.setCentralWidget(self.database_window)
        self.close()

    # Query run
    def on_query_run(self):
        self.sqm = QtSql.QSqlQueryModel(parent=self.db_data_table)
        self.sqm.setQuery(self.query_edit.text())
        self.db_data_table.setModel(self.sqm)

    # Cancel function
    def on_cancel_clicked(self):
        self.close()
