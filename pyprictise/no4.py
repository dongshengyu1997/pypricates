import re
from collections import defaultdict
def replace(string):
    if string.group(1) == 'n\'t':
        return string.group(1)
    return ''
def search(filename):
    dic = defaultdict(int)
    with open(filename,'r') as w:
        data = w.read()
    data = data.lower()
    data = re.sub(r'(n[\']t]) | ([\W\d]])', replace, data)
    datalist = re.split(r'[\s\n]+', data)
    for i in datalist:
        dic[i] += 1
    del dic['']
    return dic

if __name__ == '__main__':
    diction = search('no4')
    for k, v in diction.items():
        print("%s -> %d" % (k, v))