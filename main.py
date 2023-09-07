# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image,ImageChops,ImageFilter
import numpy


def switchpixel(img):
    image = Image.open(img)
    w,h = image.size
    new_image = Image.new("RGB",(w,h))
    for x in range(1, w):
        for y in range(h):
            pixel = image.getpixel((x, y))
            new_image.putpixel((x -5 , y-5), pixel)
    new_image.save("modified_image_3.png")

    image.close()
    new_image.close()

def transparent(img1,img2,img3,img4,alpha_val):
    image1 = Image.open(img1)
    image2 = Image.open(img2)
    image3 = Image.open(img3)
    image4 = Image.open(img4)

    # 确保图像有一个透明通道（Alpha通道）
    if image1.mode != "RGBA":
        image1 = image1.convert("RGBA")
    if image2.mode != "RGBA":
        image2 = image2.convert("RGBA")
    if image3.mode != "RGBA":
        image3 = image3.convert("RGBA")
    if image4.mode != "RGBA":
        image4 = image4.convert("RGBA")
    image1 = image1.filter(ImageFilter.BLUR)
    image2 = image2.filter(ImageFilter.BLUR)
    image3 = image3.filter(ImageFilter.BLUR)
    image4 = image4.filter(ImageFilter.BLUR)
    result_1 = ImageChops.blend(image1, image2, alpha_val / 255.0)
    result_2 = ImageChops.blend(image3, image4, alpha_val / 255.0)
    result = ImageChops.blend(result_1, result_2, alpha_val / 255.0)
    result.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # switchpixel('Images/Potholes/31.png')
    img1 = 'modified_image_1.png'
    img2 = 'Images/Potholes/31.png'
    img3 = 'modified_image_2.png'
    img4 = 'modified_image_3.png'
    transparent(img1,img2,img3,img4,100)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
