import unittest
from EanCheckHelper import isCorrectEan,calculateDigitCheck, EanType
from EanException import InvalidEanCharacter, InvalidCheckDigit

class TestEanCheckHelper(unittest.TestCase):

    def test_isCorrectEan_noerror(self):
        self.assertEqual(isCorrectEan("3666154117284"),True)
        self.assertEqual(isCorrectEan("3666154117284", EanType.EAN13),True)
        

    def test_isCorrectEan_error(self):
        self.assertEqual(isCorrectEan("3666154117284", EanType.EAN8),False)
        with self.assertRaises(InvalidCheckDigit) as InvCDE:
            isCorrectEan("3666154117285")
            self.assertEqual(InvCDE.exception.wrongDigit,"5")
        with self.assertRaises(InvalidEanCharacter) as InvECE:
            isCorrectEan("36661541172n4")
 
        self.assertEqual(isCorrectEan(None),False)

    def test_calculDigitCheck_noerror(self):
        self.assertEqual(calculateDigitCheck("366615411728"),"4")

    def test_calculDigitCheck_error(self):
        self.assertRaises(TypeError,calculateDigitCheck, None)



if __name__ == "__main__":
    unittest.main(verbosity=2)