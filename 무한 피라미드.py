import time

icons = ['!', '@', '#', '$', '%', '^']
iconNum = 0
layerOutput = ''

def newLayer():
    global icons, iconNum, layerOutput

    if iconNum == len(icons)-1: iconNum = 0
    layerOutput += icons[iconNum]
    iconNum += 1

while True:
    newLayer()
    print(layerOutput)
    time.sleep(1)