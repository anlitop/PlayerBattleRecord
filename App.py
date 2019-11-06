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
        self.select_type.addItems(["次留玩家","单日玩家","我全都要"])#config
        self.select_type.activated[str].connect(self.OnChooseType)
        #复制sql
        self.copy_sql_btn.clicked.connect(self.OnClickCopyBtn)
        #选择账号文件
        self.select_battle_path.connect(self.OnClickCopyBtn)
        #选择战斗记录文件
        self.select_account_btn.connect(self.OnClickCopyBtn)



    def OnChooseType(self,text):
        #测试
        msgbox=QMessageBox(QMessageBox.NoIcon,text,text)
        msgbox.exec()
    
    def OnClickCopyBtn(self):
        #获取date的时间
        #修改config
        #将config的复制到剪切板
        pass





if __name__ == "__main__":
    app=QApplication(argv)
    myapp=App()
    myapp.show()
    exit(app.exec_())

