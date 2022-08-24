from EanGenerator import Ean8Generator, Ean13Generator

# ean 13
testBareCode = Ean13Generator("3666154117284")

# ean 8
#testBareCode = Ean8Generator("12345670")


testBareCode.showBarcode()