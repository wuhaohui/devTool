import re
import os

if __name__ == '__main__':
    file = open('log.log', 'r+', encoding='UTF-8')
    content = file.read()
    # print(content)
    rule = re.compile(r'(\S+)\s+(\S+)\s+(\S+)')
    data = rule.findall(content)
    str = ''
    print(data)
    for row in data:
        str = str + "'%s' => '%s',//%s \n" % (row[0], row[1], row[2])
    print(str)
