from PIL import Image,ImageDraw,ImageFont,ImageColor
def addcode(image):
    draw = ImageDraw.Draw(image)

    fillcolor = ImageColor.colormap.get('blcak')
    width, length = image.size
    draw.text((width - 30, 0), 'abcdefghijk', fill=fillcolor)
    image.save('no2.jpg')
    return 0

if __name__ == '__main__':
    image = Image.open('/home/dsy/git/prictise/show-me-the-code/no1.jpg')
    addcode(image)