
from math import trunc
import tkinter as tk
from tkinter import Canvas

from xml.etree import ElementTree as ET
import zlib
import struct

import numberRenderer

class PngChunkBuilder:

	def __init__(self,chunkName:str,data:bytes):
		self.__chunkType = chunkName.encode("ascii")
		if chunkName != "IEND":
			self.__chunkData = data
			self.__chunkDataLen = struct.pack('>I', len(data))
			if chunkName =="PLTE" and len(data)%3 !=0:
				raise Exception("invalid palette data")
		else:
			self.__chunkData= "".encode()
			self.__chunkDataLen =struct.pack('>I', 0)
		self.__chunkCRC = struct.pack('>I', zlib.crc32(self.__chunkData, zlib.crc32(struct.pack('>4s', self.__chunkType))))

	def getBytesContent(self):
		return b"".join([self.__chunkDataLen,self.__chunkType, self.__chunkData, self.__chunkCRC])


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

    
    def saveAsSvg(self,filePath:str, barcodeValue:str):
        '''
        save barcode to svg file
        filePath: path to saved svg file
        '''
        initialStr = '''
        <svg version='1.1' baseProfile='full' width='700' height='200' xmlns='http://www.w3.org/2000/svg'>
        </svg>'''
        root = ET.XML(initialStr)
        barcodeZone = ET.SubElement(root,"g")
        barcodeZone.set("stroke", self.color)
        index = 10
        for el in barcodeValue:
            if el == "1":
                line = ET.SubElement(barcodeZone,"line")
                line.set("stroke-width",str(self.width))
                line.set("y1",str(10))
                line.set("x1",str(index))
                line.set("y2",str(10 + self.height))
                line.set("x2",str(index))
            index = index + self.width

        tree = ET.ElementTree(root)
        ET.register_namespace("","http://www.w3.org/2000/svg")

        tree.write(filePath, encoding="utf-8",xml_declaration=True)

    def saveAsPng(self,filepath:str,barcodeValue:str):
        # magic number
        magicNumber = struct.pack('>BBBBBBBB', 137, 80, 78, 71, 13, 10, 26,10)
        # grayscale
        colorType =0
        IDHRChunk = PngChunkBuilder("IHDR",struct.pack('>IIBBBBB', self.width*len(barcodeValue) + 20, self.height+20, 8, colorType, 0, 0, 0))



        dataPng = []
        for i in range(0,5):
            datarow = []
            datarow.extend((self.width*len(barcodeValue) + 20)*[255])
            dataPng.append(datarow)

        for i in range(0,self.height):
            datarow = []
            datarow.extend(10*[255])
            for value in barcodeValue:
                 if value =="1":
                      datarow.extend(self.width*[0])
                 else:
                      datarow.extend(self.width*[255])

            datarow.extend(10*[255])
            dataPng.append(datarow)

        for i in range(0,15):
            datarow = []
            datarow.extend((self.width*len(barcodeValue) + 20)*[255])
            dataPng.append(datarow)

        numberRenderer.drawNumber(dataPng,(self.height+12,5),"0")
        numberRenderer.drawNumber(dataPng,(self.height+12,10),"1")
        numberRenderer.drawNumber(dataPng,(self.height+12,15),"2")
        numberRenderer.drawNumber(dataPng,(self.height+12,20),"3")
        numberRenderer.drawNumber(dataPng,(self.height+12,25),"4")
        numberRenderer.drawNumber(dataPng,(self.height+12,30),"5")
        numberRenderer.drawNumber(dataPng,(self.height+12,35),"6")
        numberRenderer.drawNumber(dataPng,(self.height+12,40),"7")
        numberRenderer.drawNumber(dataPng,(self.height+12,45),"8")
        numberRenderer.drawNumber(dataPng,(self.height+12,50),"9")

        

        # ecriture des pixels
        
        image = []
        for ligne in dataPng:
            image.append(struct.pack('>B', 0))
            ligneInt = []
            for pixel in ligne:
                ligneInt.append(struct.pack('>B', pixel))
            image.extend(ligneInt)

        image_compressee = zlib.compress(b"".join(image))

        IDATChunk = PngChunkBuilder("IDAT",image_compressee)

        IENDChunk=PngChunkBuilder("IEND",b"")

        byteContentList: list[bytes] = []
        byteContentList.append(magicNumber)
        byteContentList.append(IDHRChunk.getBytesContent())
        byteContentList.append(IDATChunk.getBytesContent())
        byteContentList.append(IENDChunk.getBytesContent())

        fileContent = b"".join(byteContentList)
        with open(filepath,"wb") as pngFile:
            pngFile.write(fileContent)


    
    def renderInWindow(self, eanValue:str, barcodeValue:str):
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

