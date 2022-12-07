from EanGenerator import Ean8Generator, Ean13Generator


# ean 13
testBareCode13 = Ean13Generator("3666154117284")

print("ean8")
# ean 8
testBareCode8 = Ean8Generator("12345670")


testBareCode8.showBarcode()