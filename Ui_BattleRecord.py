# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\DDMS_Daily\BattleRecord.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Battle(object):
    def setupUi(self, Battle):
        Battle.setObjectName("Battle")
        Battle.resize(472, 204)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Battle.sizePolicy().hasHeightForWidth())
        Battle.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Battle)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 135))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.select_date = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.select_date.setObjectName("select_date")
        self.gridLayout.addWidget(self.select_date, 3, 2, 1, 1)
        self.select_battle_path = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.select_battle_path.setObjectName("select_battle_path")
        self.gridLayout.addWidget(self.select_battle_path, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.select_account_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.select_account_btn.setObjectName("select_account_btn")
        self.gridLayout.addWidget(self.select_account_btn, 5, 3, 1, 1)
        self.select_type = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.select_type.setAcceptDrops(False)
        self.select_type.setObjectName("select_type")
        self.gridLayout.addWidget(self.select_type, 2, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 5, 2, 1, 1)
        self.copy_sql_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.copy_sql_btn.setObjectName("copy_sql_btn")
        self.gridLayout.addWidget(self.copy_sql_btn, 3, 3, 1, 1)
        self.work_progress_bar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.work_progress_bar.setProperty("value", 0)
        self.work_progress_bar.setObjectName("work_progress_bar")
        self.gridLayout.addWidget(self.work_progress_bar, 6, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.open_link_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_link_btn.setGeometry(QtCore.QRect(180, 160, 111, 41))
        self.open_link_btn.setObjectName("open_link_btn")
        Battle.setCentralWidget(self.centralwidget)

        self.retranslateUi(Battle)
        QtCore.QMetaObject.connectSlotsByName(Battle)

    def retranslateUi(self, Battle):
        _translate = QtCore.QCoreApplication.translate
        Battle.setWindowTitle(_translate("Battle", "战斗数据提取"))
        self.select_battle_path.setText(_translate("Battle", "选择"))
        self.label.setText(_translate("Battle", "提取哪种玩家战斗记录"))
        self.select_account_btn.setText(_translate("Battle", "选择"))
        self.label_2.setText(_translate("Battle", "玩家注册日期"))
        self.label_3.setText(_translate("Battle", "战斗玩家路径(battle)"))
        self.label_4.setText(_translate("Battle", "次留玩家名单(account)"))
        self.copy_sql_btn.setText(_translate("Battle", "复制语句"))
        self.label_5.setText(_translate("Battle", "处理进度"))
        self.open_link_btn.setText(_translate("Battle", "开始"))

