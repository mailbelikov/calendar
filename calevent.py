#!/usr/bin/python3

from PyQt5 import QtWidgets as QW
from cal import Ui_cal
import sys, sqlite3

class calEvent(QW.QMainWindow):
    def __init__(self):   #, parent=None):
        super().__init__()
        self.ui = Ui_cal()
        self.ui.setupUi(self)

        self.base = sqlite3.connect('caldb.db')
        self.calbase = self.base.cursor()
        self.SelectDate()

        self.ui.btnSave.clicked.connect(self.SaveEvent)
        self.ui.calWidget.selectionChanged.connect(self.SelectDate)

    def closeEvent(self, event):
        print('close ...')
        self.calbase.close()
        self.base.close()
        event.accept()

    def SelectDate(self):
        seldate = self.ui.calWidget.selectedDate().toPyDate()
        sql = 'SELECT * FROM cal_event WHERE date = ?;'
        res = self.calbase.execute(sql, (seldate,)).fetchall()
        if len(res) > 0:
            self.ui.txtEventList.setText(res[0][1])
        else:
            self.ui.txtEventList.setText('')

    def SaveEvent(self):
        seldate = self.ui.calWidget.selectedDate().toPyDate()
        sql = 'SELECT * FROM cal_event WHERE date = ?;'
        res = self.calbase.execute(sql, (seldate,)).fetchall()
        if len(res) > 0:
            sql = 'UPDATE cal_event set event = ? WHERE date = ?;'
            self.calbase.execute(sql, (self.ui.txtEventList.toPlainText(), seldate))
        else:
            sql = 'INSERT INTO cal_event VALUES (?, ?);'
            self.calbase.execute(sql, (self.ui.calWidget.selectedDate().toPyDate(), self.ui.txtEventList.toPlainText()))
        self.base.commit()

app = QW.QApplication(sys.argv)
window = calEvent()
window.show()
app.exec_()
