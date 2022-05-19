import re
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsView, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, \
    QLabel, QTextEdit
from PyQt5.QtCore import Qt, QByteArray, QBuffer, QIODevice, QTimer
from PyQt5.QtGui import QClipboard
from tool import Tools
from notice import NotificationWindow


class App(QWidget):
    def __init__(self):
        self.tools = Tools()
        app = QApplication(sys.argv)
        super().__init__()
        self.ui()
        sys.exit(app.exec_())

    def ui(self):
        self.setWindowTitle('开发小助手')
        self.resize(350, 200)

        label = QLabel(self)
        label.setText(
            "<a href='https://union-click.jd.com/jdc?e=618%7Cpc%7C&p=JF8BAKcJK1olXDYDZBoCUBVIMzZNXhpXVhgcEhgbFxBCHD1WR2tXJw5VSlc9byloACxWZSNvWmV7EwY9BEcnBm8JGlwRVAUGV25dCUoWAmsPE10dbTYCVW4WZkonAW4JHlgVWgAFV25dD08XC28IHVkTWQQBZFldAXsVAGoAGlMQVQ8eXFpYDEIXM184GGsSXQ8WUiwcWl8RcV84G1slXTZdEAMAOEkWAmsBKw'>支持</a>")
        label.setOpenExternalLinks(True)
        label.setAlignment(Qt.AlignCenter)

        self.ruleText = QTextEdit(self)
        oneButton = QPushButton("智能转换")
        oneButton.clicked.connect(self.samrtTrans)

        twoButton = QPushButton("去除引号")
        twoButton.clicked.connect(self.filterQuotation)

        threeButton = QPushButton("测试")
        threeButton.clicked.connect(lambda: self.aboutqt())

        # 布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.ruleText)
        vbox.addWidget(oneButton)
        vbox.addWidget(twoButton)
        vbox.addWidget(label)
        # vbox.addWidget(threeButton)

        self.setLayout(vbox)
        self.show()

    def samrtTrans(self):
        result = False
        rule = self.ruleText.toPlainText()
        if len(rule) > 0:
            result = self.transInput(rule)
        if result == False:
            sender = self.sender()
            sender.setDisabled(True)
            result = self.tools.smartTrans()
            sender.setDisabled(False)
        if result == True:
            NotificationWindow.success('提示', '转换成功')
        else:
            NotificationWindow.error('提示', '转换失败')

    # 去除引号
    def filterQuotation(self):
        clipboard = QApplication.clipboard()
        content = clipboard.text()
        content = content.replace('\"', '').replace('\'', '')
        clipboard.setText(content)

    def aboutqt(self):
        msgBox = QMessageBox()
        msgBox.information(self, "提示", "转换成功！")
        # # msgBox = QMessageBox().information()
        # # msgBox.setText('转换成功')
        # msgBox.setStandardButtons(QMessageBox.Ok )
        # msgBox.button(QMessageBox.Ok).animateClick(3000)

    def transInput(self, rule):
        clipboard = QApplication.clipboard()
        content = clipboard.text()

        result = re.compile(r'(\$\d+)').findall(rule)
        if len(result) > 0:
            regexpRule = ""
            for num in range(len(result)):
                regexpRule = regexpRule + "(\S+)"
                if num != len(result) - 1:
                    regexpRule = regexpRule + "\s+"

            rule = rule.replace('$', '\\')
            newContent = re.sub(regexpRule, rule, content)
            clipboard.setText(newContent)
            return True

        return False
