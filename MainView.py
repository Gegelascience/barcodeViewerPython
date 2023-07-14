import tkinter as tk
from tkinter import ttk, StringVar
from EanGenerator import Ean8Generator, Ean13Generator


class InputUI(tk.Tk):

    def __init__(self):
        super().__init__()
    
        self.title("BarcodeViewer")
        self.geometry("300x200")

        ttk.Label(self,text="Write EAN code").pack(pady=(5,0))
        
        # ajout du champ formulaire
        self.barcode = StringVar()
        package_entry = ttk.Entry(self, width=20, textvariable=self.barcode)
        package_entry.pack(pady=(10,0))
        
        btnSearch = ttk.Button(self, text="Show", command=self.showBarcode)
        btnSearch.bind('<Return>', self.showBarcode)
        btnSearch.pack(pady=(10,0))


    def showBarcode(self, event=None):
        possibleEan = self.barcode.get()
        if len(possibleEan) == 13:
            # ean 13
            # valeur de test: 3666154117284
            testBareCode13 = Ean13Generator(possibleEan)
            testBareCode13.saveBarcodeAsSvg("./test13.svg")
            testBareCode13.saveBarcodeAsPng("./test13.png")
            testBareCode13.showBarcode()
                

        elif len(possibleEan) == 8:

            # ean 8
            # valeur de test: 12345670
            testBareCode8 = Ean8Generator(possibleEan)
            testBareCode8.saveBarcodeAsSvg("./test8.svg")
            testBareCode8.saveBarcodeAsPng("./test8.png")
            testBareCode8.showBarcode()

        else:
            raise("Invalid EAN size")