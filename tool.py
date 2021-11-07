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
        print(clipboard.image().byteCount())

        if clipboard.image().byteCount() == 0:
            return False

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
    def readMysqlTableFiled(self, text):
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

    def transArr(self, content, type):
        if type == 3:
            rule = re.compile(r'(\S+)\s+(\S+)\s+(\S+).*')
            temp = "'%s' => '%s',//%s \n"
        else:
            rule = re.compile(r'(\S+)\s+(\S+).*')
            temp = "'%s' => '%s',\n"
        data = rule.findall(content)
        str = ''
        for row in data:
            if type == 3:
                str = str + temp % (row[0], row[1], row[2])
            else:
                str = str + temp % (row[0], row[1])
        self.setClipboardText(str)

    def smartTrans(self):
        clipboard = QApplication.clipboard()
        content = clipboard.text()
        # 图片转文字
        if content == '':
            self.transImage()
            return True
        print('获取粘贴板内容：' + content)
        # 清空情面的空格
        content = re.sub('^\s+', '', content)
        # 判断是否创建表sql
        if len(re.compile(r'^CREATE TABLE').findall(content)) > 0:
            self.readMysqlTableFiled(content)
        else:
            rule = re.compile(r'.*')
            data = rule.findall(content)
            print(data)
            if data is None:
                return '格式异常-无法转换'
            firstRow = data[0]
            res = re.compile(r'\w+').findall(firstRow)
            print(res)
            if len(res) == 1:
                self.transformTxtForMysql()
                return True
            elif len(res) in [2, 3]:
                self.transArr(content, len(res))
                return True
            else:
                return '异常'
