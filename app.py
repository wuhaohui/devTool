import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsView, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QLabel
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

        label = QLabel(self)
        label.setText("<a href='https://u.jd.com/yLpjXpZ'>支持</a>")
        label.setOpenExternalLinks(True)
        label.setAlignment(Qt.AlignCenter)

        oneButton = QPushButton("智能转换")
        oneButton.clicked.connect(self.samrtTrans)

        # 布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(oneButton)
        vbox.addWidget(label)

        self.setLayout(vbox)
        self.show()

    def samrtTrans(self):
        sender = self.sender()
        sender.setDisabled(True)
        self.tools.smartTrans()
        sender.setDisabled(False)

    def aboutqt(self):
        msgBox = QMessageBox().information(self, "提示", "转换成功！")
        # # msgBox = QMessageBox().information()
        # # msgBox.setText('转换成功')
        # msgBox.setStandardButtons(QMessageBox.Ok )
        # msgBox.button(QMessageBox.Ok).animateClick(3000)
