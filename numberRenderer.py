def drawNumber(originalData:list, upperLeftPointer:tuple, numberValue:str):
    numberPixels = []
    if numberValue == "0":
        numberPixels = [(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,2),(3,0),(3,2),(4,0),(4,1),(4,2)]

    elif numberValue == "1":
        numberPixels = [(0,2),(1,2),(2,2),(3,2),(4,2)]

    elif numberValue == "2":
        numberPixels = [(0,0),(0,1),(0,2),(1,2),(2,0),(2,1),(2,2),(3,0),(4,0),(4,1),(4,2)]

    elif numberValue == "3":
        numberPixels = [(0,0),(0,1),(0,2),(1,2),(2,0),(2,1),(2,2),(3,2),(4,0),(4,1),(4,2)]

    elif numberValue == "4":
        numberPixels = [(0,0),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2),(3,2),(4,2)]

    elif numberValue == "5":
        numberPixels = [(0,0),(0,1),(0,2),(1,0),(2,0),(2,1),(2,2),(3,2),(4,0),(4,1),(4,2)]

    elif numberValue == "6":
        numberPixels = [(0,0),(0,1),(0,2),(1,0),(2,0),(2,1),(2,2),(3,0),(3,2),(4,0),(4,1),(4,2)]

    elif numberValue == "7":
        numberPixels = [(0,0),(0,1),(0,2),(1,2),(2,2),(3,2),(4,2)]

    elif numberValue == "8":
        numberPixels = [(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2),(3,0),(3,2),(4,0),(4,1),(4,2)]

    elif numberValue == "9":
        numberPixels = [(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2),(3,2),(4,0),(4,1),(4,2)]
    else:
        raise Exception("Invalid number")
    
    for pix in numberPixels:
            #greySclale
            originalData[upperLeftPointer[0] + pix[0]][upperLeftPointer[1] + pix[1]] = 0