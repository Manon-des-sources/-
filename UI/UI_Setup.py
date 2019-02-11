#!/user/bin/env python3
# -*- coding: utf-8 -*-

from UI import Ui_MainWindow

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
# 弹出窗口需要用到QWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtPrintSupport import QPrinter

# from PyQt5.QtCore import QTextCodec
# QTextCodec.setCodecForLocale(QTextCodec.codecForName("utf-8"))

class WindowSetup(Ui_MainWindow, QWidget):
    def __init__(self, MainWindow):
        print("init start")
        super().__init__()
        self.setupWindow(MainWindow)
        self.setupKeys()
    def setupWindow(self, MainWindow):
        # 用UI初始化后这个主窗体
        self.setupUi(MainWindow)
        # 不主动显示历史记录窗口
        self.dockWidget_history.hide()

        # 主窗体窗体设置补充
        MainWindow.setWindowTitle("协议解析工具(V1.0)")
        MainWindow.setWindowIcon(QIcon("../image/小娜.png"))

        # 主窗体显示
        MainWindow.show()
        print("show")

    def setupKeys(self):
        print("setupKeys")
        self.KeyDecode.clicked.connect(self.decodeProtocal)
        self.KeyOpen.clicked.connect(self.openFile)
        self.KeySave.clicked.connect(self.saveFile)
        self.KeyClear.clicked.connect(self.clearText)
        self.actionClear.triggered.connect(self.clearText)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionopenFiles.triggered.connect(self.openFiles)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSaveAs.triggered.connect(self.saveAsFile)
        self.actionPrint.triggered.connect(self.printFile)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionaddProtocal.triggered.connect(self.addProtocal)
        self.actionhelp.triggered.connect(self.helpInfo)
        self.actionHistory.triggered.connect(self.openHistoryWindow)
        self.actionabout.triggered.connect(self.aboutInfo)

    def decodeProtocal(self):
        print("decode Protocal")
        
    def clearText(self):
        self.Text_dataFrame.clear()
        self.Text_ProtocalView.clear()
        print("clearText")
        
    def openFile(self):
        print("openFile")
        # .getOpenFileName(窗口标题, 默认路径, 文件类型)
        # 返回文件路径(字符串)
        fname = QFileDialog.getOpenFileName(self, "打开文件", './', '*')
        print(fname)
        if fname[0]:
            # 使用with语句打开文件后、它会自动关闭文件
            with open(fname[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.Text_dataFrame.setText(f.read())

    def openFiles(self):
        print("openFiles")
        # 返回文件路径(字符串)列表
        fnames = QFileDialog.getOpenFileNames(self, "打开多个文件", './', '*')
        print(fnames)
        self.clearText()
        if fnames[0]:
            for fname in fnames[0]:
                with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
                    self.Text_dataFrame.append(f.read())

    def saveFile(self):
        print("saveFile")
        fname = QFileDialog.getSaveFileName(self, "保存文件", './', "Text file (*.txt)")
        if fname[0]:
            with open(fname[0], 'w', encoding='utf-8', errors='ignore') as f:
                # .toPlainText()用于获取QTextEdit的内容
                f.write(self.Text_dataFrame.toPlainText())
        
    def saveAsFile(self):
        print("saveAsFile")
        fname = QFileDialog.getSaveFileName(self, "保存文件", './', "Text file (*.txt)")
        if fname[0]:
            with open(fname[0], 'w', encoding='utf-8', errors='ignore') as f:
                # .toPlainText()用于获取QTextEdit的内容
                f.write(self.Text_dataFrame.toPlainText())
        
    def printFile(self):
        print("printFile")
        printer = QPrinter()
        printDialog = QPrintDialog(printer, self)
        if QDialog.Accepted == printDialog.exec_():
            # 打印机选择完成后、调用QTextEdit的打印方法进行打印
            self.Text_dataFrame.print(printer)
        
    def exitApp(self):
        print("exitApp")
        qApp.quit()
        # self.close()

    def addProtocal(self):
        print("addProtocal")

    def helpInfo(self):
        print("helpInfo")

    def aboutInfo(self):
        print("aboutInfo")
        aboutInfoWindow = 0
        # aboutInfoText = QTextEdit(self.centralwidget)
        # aboutInfoText.setObjectName("支持的协议：")
        # aboutInfoText.show()
        
    def openHistoryWindow(self):
        print("openHistoryWindow")
        self.dockWidget_history.show()
        

if __name__ == '__main__':
    # 启动一个应用程序
    app = QApplication(sys.argv)
    # 创建一个主窗体
    MainWindow = QMainWindow()
    exe = WindowSetup(MainWindow)
    # 应用程序进入主循环
    sys.exit(app.exec_())
