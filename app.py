import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsView, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QByteArray, QBuffer, QIODevice
from PyQt5.QtGui import QClipboard
from tool import Tools


class App(QWidget):
    def __init__(self):
        self.tools = Tools()
        app = QApplication(sys.argv)
        super().__init__()
        self.ui()
        sys.exit(app.exec_())

    def ui(self):
        self.setWindowTitle('开发小助手')
        self.resize(350,200)
        oneButton = QPushButton("转 in 字符串")
        oneButton.clicked.connect(self.transTxt)

        twoButton = QPushButton("DDL 转字段")
        twoButton.clicked.connect(self.transMysqlField)

        threeButton = QPushButton("图片转文字")
        threeButton.clicked.connect(self.transImage)

        tourButton = QPushButton("转数组")
        tourButton.clicked.connect(self.transArr)

        abouttButton = QPushButton("关于")
        abouttButton.clicked.connect(self.aboutqt)

        # 布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(oneButton)
        vbox.addWidget(twoButton)
        vbox.addWidget(threeButton)
        vbox.addWidget(tourButton)
        vbox.addWidget(abouttButton)

        self.setLayout(vbox)
        self.show()

    def transTxt(self):
        self.tools.transformTxtForMysql()

    def transMysqlField(self):
        self.tools.readMysqlTableFiled()

    # 图片转文字
    def transImage(self):
        sender = self.sender()
        sender.setDisabled(True)
        self.tools.transImage()
        sender.setDisabled(False)


    def transArr(self):
        self.tools.transArr()

    def aboutqt(self):
        msgBox = QMessageBox().information(self, "提示", "转换成功！")
        # # msgBox = QMessageBox().information()
        # # msgBox.setText('转换成功')
        # msgBox.setStandardButtons(QMessageBox.Ok )
        # msgBox.button(QMessageBox.Ok).animateClick(3000)
