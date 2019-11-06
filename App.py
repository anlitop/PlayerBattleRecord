from sys import exit,argv
from Ui_BattleRecord import Ui_Battle
from os import path,startfile
from json import dumps,load
from webbrowser import open_new_tab,get
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog,QMessageBox
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt,pyqtSignal,QThread
from Script.config import *

class App(QMainWindow,Ui_Battle):
    def __init__(self):
        super(App,self).__init__()
        self.setupUi(self)
        #读取config
        self.config=get_config("config.json")
        
        
        #绑定事件
        types=["次留玩家","单日玩家","我全都要"]
        self.select_type.addItems(types)#config
        #需要的类型
        self.analy_type=types[0]
        self.select_type.activated[str].connect(self.OnChooseType)
        #复制sql
        self.copy_sql_btn.clicked.connect(self.OnClickCopyBtn)
        #选择账号文件
        self.select_battle_path.clicked.connect(self.OnClickSelect_battle_path)
        self.account_lineEdit.setText(self.config["次留玩家文件路径"])
        #选择战斗记录文件
        self.select_account_btn.clicked.connect(self.OnClickSelect_account_btn)
        self.battle_lineEdit.setText(self.config["战斗记录文件路径"])
        #设置时间
        analy_date=QDate.currentDate()
        self.select_date.setDate(analy_date)
        self.analy_date=''

        #需要控制的按钮组
        self.control_btns=[self.copy_sql_btn,self.select_battle_path,self.select_account_btn]

        #剪切板
        self.cb=QApplication.clipboard()




    def OnChooseType(self,text):
        self.analy_type=text
    def OnClickCopyBtn(self):
        #获取date的时间
        _time = self.select_date.date()
        self.analy_date=_time.toString(Qt.ISODate)
        #修改config
        self.config["sql_date"]=self.analy_date
        save_config(self.config)
        #将config的复制到剪切板
        self.cb.clear()
        self.cb.setText(self.config["sql_date"])
        #弹出提示，是否直接去网站
        reply=QMessageBox.information(self,"复制成功","复制成功是否前往网站进行查询",QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        #确认则前往
        if reply==QMessageBox.Ok:
            try:
                get("chrome").open_new_tab(self.config["tga_url"])
            except Exception as e:
                open_new_tab(self.config["tga_url"])

    def OnClickSelect_battle_path(self):
        #config中默认文件夹
        #检查路径合法
        path=self.check_file_path(self.battle_lineEdit,"战斗记录文件路径")
        fname,ok=QFileDialog.getOpenFileName(self,"选择文件",path,'csv files(*.csv)')
        if ok:
            self.battle_lineEdit.setText(str(fname))
            self.config["战斗记录文件路径"]=str(fname)
            save_config(self.config)
            print('ok')
        

    def OnClickSelect_account_btn(self):
        path=self.check_file_path(self.account_lineEdit,"次留玩家文件路径")
        fname,ok=QFileDialog.getOpenFileName(self,"选择文件",path,'csv files(*.csv)')
        if ok:
            self.account_lineEdit.setText(str(fname))
            self.config["次留玩家文件路径"]=str(fname)
            save_config(self.config)
            print('ok')
    

    def check_file_path(self,l_edit,key_name):
        '''如果lineedit中有文件路径，就返回路径'''
        if path.isfile(l_edit.text()):
            return l_edit.text()
        else:
            print("wrong path"+l_edit.text())
            return self.config[key_name] 





if __name__ == "__main__":
    app=QApplication(argv)
    myapp=App()
    myapp.show()
    exit(app.exec_())

