
from math import trunc
import tkinter as tk
from tkinter import Canvas

class BarcodeRendering:
    '''
    Class to render barcode in different ways
    '''
    width:str = 4
    height:str = 40
    color:str = "black"
    emptyInit:int =  30
    listIndexMeta = []

    def __init__(self, listIndex:list, width:int=4, height:int = 40, color:str="black"):
        self.width = width
        self.color = color
        self.height = height
        self.listIndexMeta =listIndex

    
    def renderInWindow(self, eanValue:str, barcodeValue:str, indexFirstPart:int, indexSecondPart:int):
        '''
        Render barcode on tkinter window
        '''
        app = tk.Tk()
        app.title(eanValue)

        dimWindow = str(len(barcodeValue)*self.width + self.emptyInit*2) + "x" + str(50 + self.height)
        app.geometry(dimWindow)
        canvas = Canvas(app,width=len(barcodeValue)*self.width+ self.emptyInit*2, background="white")
        canvas.pack()

        if len(eanValue) ==13:
            decalagePart1 = 1
            decalagePart2 = 7

            canvas.create_text(self.emptyInit/2, 20 + self.height, text=eanValue[0])
        else:
            decalagePart1 = 0
            decalagePart2 = 4
        
        for i,el in enumerate(barcodeValue):
            if el == "1":
                if i in self.listIndexMeta:
                    canvas.create_line(self.emptyInit+ i*self.width, 10, self.emptyInit +i*self.width, 10 + self.height + 20, width=self.width, fill=self.color)
                else:
                    canvas.create_line(self.emptyInit+ i*self.width, 10, self.emptyInit +i*self.width, 10 + self.height, width=self.width, fill=self.color)

            if i > 2 and i < self.listIndexMeta[3]:
                iref = i - 2
                if iref%7 == 3:
                    textValue=trunc(iref/7)
                    canvas.create_text(self.emptyInit+ (i+1)*self.width, 20 + self.height, text=eanValue[textValue + decalagePart1])
            elif i > self.listIndexMeta[7] and i< self.listIndexMeta[8]:
                iref = i - self.listIndexMeta[7]
                if iref%7 == 3:
                    textValue=trunc(iref/7)
                    canvas.create_text(self.emptyInit+ (i+1)*self.width, 20 + self.height, text=eanValue[textValue + decalagePart2])

        app.mainloop()

