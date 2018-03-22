from PIL import Image
import os
def change():
    list = ospath()
    print('ok')
    for i in list:
        img = Image.open('./picture/%s' % i)
        if max(img.size) > 1136:
            value = max(img.size) / 1136.0
            newsize_min = min(img.size) / value
            newthing = img.resize((1136, int(newsize_min)), Image.ANTIALIAS)
            newthing.save('new' + i)

        else:
            print("this picture %s is ok" % i)


def ospath():
    list = []
    dirpath = './picture'
    alldata = os.listdir(dirpath)
    for i in alldata:
        list.append(i)
    return list
if __name__ == '__main__':
    change()