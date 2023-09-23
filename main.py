from EanGenerator import Ean8Generator, Ean13Generator
import sys
from MainView import InputUI
import argparse

cmdArgParser =  argparse.ArgumentParser(description="show ean barcode")
cmdArgParser.add_argument("-e","--ean", help="ean to show as barcode", type=str)

if __name__ == '__main__':

    params = cmdArgParser.parse_args()

    if params.ean:
        

        try:

            if len(params.ean) == 13:
                # ean 13
                # valeur de test: 3666154117284
                testBareCode13 = Ean13Generator(params.ean)
                testBareCode13.saveBarcodeAsSvg("./test13.svg")
                testBareCode13.saveBarcodeAsPng("./test13.png")
                testBareCode13.showBarcode()
                

            elif len(params.ean) == 8:

                # ean 8
                # valeur de test: 12345670
                testBareCode8 = Ean8Generator(params.ean)
                testBareCode8.saveBarcodeAsSvg("./test8.svg")
                testBareCode8.saveBarcodeAsPng("./test8.png")
                testBareCode8.showBarcode()

            else:
                raise Exception("Invalid EAN size")

        except Exception as e:
            print(e)
            sys.exit(1)

    else:
        print("No ean given")
        defaultApp = InputUI()
        defaultApp.mainloop()
        
