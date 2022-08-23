
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

    def __init__(self, width:int=4, height:int = 40, color:str="black"):
        self.width = width
        self.color = color

    
    def renderInWindow(self, eanValue:str, barcodeValue:str,listIndexMeta:list):
        '''
        Render barcode on tkinter window
        '''
        app = tk.Tk()
        app.title(eanValue)

        dimWindow = str(len(barcodeValue)*self.width + self.emptyInit*2) + "x" + str(50 + self.height)
        app.geometry(dimWindow)
        canvas = Canvas(app,width=len(barcodeValue)*self.width+ self.emptyInit*2, background="white")
        canvas.pack()

        
        for i,el in enumerate(barcodeValue):
            if el == "1":
                if i in listIndexMeta:
                    canvas.create_line(self.emptyInit+ i*self.width, 10, self.emptyInit +i*self.width, 10 + self.height + 20, width=self.width, fill=self.color)
                else:
                    canvas.create_line(self.emptyInit+ i*self.width, 10, self.emptyInit +i*self.width, 10 + self.height, width=self.width, fill=self.color)
            #index = index + self.width

        app.mainloop()

