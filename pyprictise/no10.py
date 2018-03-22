from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
def rechar():
    return chr(random.randint(65, 90))
def recolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
def recolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def ranpic():
    height = 60
    width = 60 * 4
    image = Image.new('RGB', (240, 60), (255,255,255))
    font = ImageFont.truetype('/usr/share/fonts/truetype/tlwg/Sawasdee-Bold.ttf', 36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=recolor())
    for t in range(4):
        m = rechar()
        print(m)
        draw.text((60 * t + 10, 10), m, font=font, fill=recolor2())
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')
if __name__ == '__main__':
    ranpic()