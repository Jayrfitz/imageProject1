from PIL import Image

pixels = []
folder = ""
image1 = Image.open(folder +"1.png")
pic1 = image1.load()
pixels.append(pic1)

image2 = Image.open(folder +"2.png")
pic2 = image2.load()
pixels.append(pic2)

image3 = Image.open(folder +"3.png")
pic3 = image3.load()
pixels.append(pic3)

image4 = Image.open(folder +"4.png")
pic4 = image4.load()
pixels.append(pic4)

image5 = Image.open(folder +"5.png")
pic5 = image5.load()
pixels.append(pic5)

image6 = Image.open(folder +"6.png")
pic6 = image6.load()
pixels.append(pic6)

image7 = Image.open(folder +"7.png")
pic7 = image7.load()
pixels.append(pic7)

image8 = Image.open(folder +"8.png")
pic8 = image8.load()
pixels.append(pic8)

image9 = Image.open(folder +"9.png")
pic9 = image9.load()
pixels.append(pic9)

pixelsFinal = Image.new(image1.mode , image1.size)
finalData = pixelsFinal.load()
width = 495
height = 557

def medianOdd(pixlist):
    listlenth = len(pixlist)
    sortedValues = sorted(pixlist)
    middleIndex = (listlenth + 1) / 2
    middleIndex = int(middleIndex)
    return sortedValues[middleIndex]

for x in range(0 , width):
    for y in range(0 , height):
        redlist = []
        greenlist = []
        bluelist = []
        for picCount in range(0 , 8):
            pix = pixels[picCount][x,y]
            redlist.append(pix[0])
            greenlist.append(pix[1])
            bluelist.append(pix[2])
        finalData[x,y] = (medianOdd(redlist),medianOdd(greenlist),medianOdd(bluelist))
pixelsFinal.show()
