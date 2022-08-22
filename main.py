from EanCheckHelper import isCorrectEan, EanType, calculateDigitCheck



from EanGenerator import Ean8Generator, Ean13Generator

testBareCode = Ean13Generator("3666154117284")

testBareCode.showBarcode()