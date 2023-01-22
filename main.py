from EanGenerator import Ean8Generator, Ean13Generator
import sys



if __name__ == '__main__':

    params = sys.argv

    if len(params) > 1:
        
        possibleEan = params[1]

        try:

            if len(possibleEan) == 13:
                # ean 13
                testBareCode13 = Ean13Generator("3666154117284")
                testBareCode13.saveBarcodeAsSvg("./test13.svg")
                testBareCode13.showBarcode()

            else:

                # ean 8
                testBareCode8 = Ean8Generator("12345670")
                testBareCode8.saveBarcodeAsSvg("./test8.svg")
                testBareCode8.showBarcode()

        except:
            sys.exit(1)
