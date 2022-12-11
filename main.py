from EanGenerator import Ean8Generator, Ean13Generator


# ean 13
testBareCode13 = Ean13Generator("3666154117284")

testBareCode13.saveBarcodeAsSvg("./test13.svg")

# ean 8
testBareCode8 = Ean8Generator("12345670")

testBareCode8.saveBarcodeAsSvg("./test8.svg")

testBareCode8.showBarcode()
