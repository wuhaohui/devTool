import re
import os

if __name__ == '__main__':
    file = open('log.log', 'r+', encoding='UTF-8')
    content = file.read()
    # print(content)
    rule = re.compile(r'^(\S+)\s+(\S+)\s*\n')
    data = rule.findall(content)
    str = ''
    headRow = re.search('^(\S+)\s+(\S+)\s*\n',content)

    headRow = rule.search(content)
    if headRow is None:
        headRow = re.search('^(\S+)\s+(\S+)\s*\n',content)
    exit()
    print(data)
    for row in data:
        if row.length == 2:
            str = str + "'%s' => '%s',\n" % (row[0], row[1])
        else:
            str = str + "'%s' => '%s',//%s \n" % (row[0], row[1], row[2])
    print(str)
