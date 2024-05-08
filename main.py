from EanGenerator import Ean8Generator, Ean13Generator, _EanGeneratorProto
import sys
import argparse

cmdArgParser =  argparse.ArgumentParser(description="show ean barcode")
cmdArgParser.add_argument("-e","--ean", help="ean to show as barcode", type=str, required=True)
cmdArgParser.add_argument("-m","--mode", help="mode to render, default 'terminal'", type=str, default="terminal", choices=['terminal','png','svg'])
cmdArgParser.add_argument("-f","--file", help="file path for file render", type=str)

def showBarcode(eanGenerator:_EanGeneratorProto, mode:str, filePath:str):
    if mode == "terminal":
        eanGenerator.showBarcodeOnTerminal()

    elif mode in ["png","svg"]:
        if not filePath:
            raise Exception("No file path given")
        
        if (mode == "png" and not filePath.endswith(".png")) or (mode == "svg" and not filePath.endswith(".svg")):
            raise Exception("invalid file extention")

        if mode == "svg":
            eanGenerator.saveBarcodeAsSvg(filePath)
        else:
            eanGenerator.saveBarcodeAsPng(filePath)

if __name__ == '__main__':

    params = cmdArgParser.parse_args()
        
    try:

        if len(params.ean) == 13:
            # ean 13
            # valeur de test: 3666154117284
            testBareCode13 = Ean13Generator(params.ean)
            showBarcode(testBareCode13,params.mode,params.file)
                
        elif len(params.ean) == 8:

            # ean 8
            # valeur de test: 12345670
            testBareCode8 = Ean8Generator(params.ean)
            showBarcode(testBareCode8,params.mode,params.file)

        else:
            raise Exception("Invalid EAN size")

    except Exception as e:
        print(e)
        sys.exit(1)

        
        
