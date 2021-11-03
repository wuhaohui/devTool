from PyQt5.QtWidgets import QApplication
import re
from aip import AipOcr
from PyQt5.QtCore import Qt, QByteArray, QBuffer, QIODevice


class Tools:
    def __init__(self):
        print('init tool')

    # 转换成 '123','12'
    def transformTxtForMysql(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        if len(text) > 0:
            pattern = re.compile(r'(\S+)')
            data = pattern.findall(text)
            newText = ""
            for row in data:
                newText += '\'' + row + '\','
            result = newText.strip(',')
            self.setClipboardText(result)
        else:
            self.transImage()

    # 图片转文字
    def transImage(self):
        APP_ID = '11041712'
        API_KEY = 'oT6GbdF8QslWmEh7Amzp33Rp'
        SECRET_KEY = 'GSMpovMRvOG7AI8Kki6f1l4hS2i7annU'

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        clipboard = QApplication.clipboard()
        # print(clipboard.image())
        ba = QByteArray()
        buffer = QBuffer(ba)
        buffer.open(QIODevice.WriteOnly)
        clipboard.image().save(buffer, "jpeg")
        buffer.close()

        result = client.basicGeneral(ba)
        if result['words_result_num'] > 0:
            # 图片识别成功
            matchTxt = result['words_result'][0]['words']
            self.setClipboardText(matchTxt)
            return True
        else:
            return False

    # 读取mysql字段
    def readMysqlTableFiled(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        rule = re.compile(r'`(\w+)`')
        data = rule.findall(text)
        newText = ""
        for row in data:
            newText += '\'' + row + '\','
        self.setClipboardText(newText.strip(','))

    def setClipboardText(self, content):
        clipboard = QApplication.clipboard()
        clipboard.setText(content)
        print('粘贴板内容:' + content)
