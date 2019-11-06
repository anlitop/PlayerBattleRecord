from sys import exit,argv
from Ui_BattleRecord import Ui_Battle
from os import path,startfile
from json import dumps,load
from webbrowser import open_new_tab,get
from PyQt5.QtCore import pyqtSignal,QThread
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog,QMessageBox



class App(QMainWindow,Ui_Battle):
    def __init__(self):
        super(App,self).__init__()
        self.setupUi(self)
        #绑定事件






if __name__ == "__main__":
    app=QApplication(argv)
    myapp=App()
    myapp.show()
    exit(app.exec_())

