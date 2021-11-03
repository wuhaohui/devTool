import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsView, QPushButton, QHBoxLayout, QVBoxLayout
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

        oneButton = QPushButton("转 in 字符串")
        oneButton.clicked.connect(self.transTxt)

        twoButton = QPushButton("DDL 转字段")
        twoButton.clicked.connect(self.transMysqlField)

        threeButton = QPushButton("图片转文字")
        threeButton.clicked.connect(self.transImage)

        # 布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(oneButton)
        vbox.addWidget(twoButton)
        vbox.addWidget(threeButton)

        self.setLayout(vbox)
        self.show()

    def transTxt(self):
        self.tools.transformTxtForMysql()
        print('click  transTxt')

    def transMysqlField(self):
        self.tools.readMysqlTableFiled()
        print('click  transMysqlField')

    # 图片转文字
    def transImage(self):
        self.tools.transImage()
