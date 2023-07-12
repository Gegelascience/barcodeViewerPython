from EanGenerator import Ean8Generator, Ean13Generator
import sys



if __name__ == '__main__':

    params = sys.argv

    if len(params) > 1:
        
        possibleEan = params[1]

        try:

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

        except Exception as e:
            print(e)
            sys.exit(1)

    else:
        print("No ean given")
