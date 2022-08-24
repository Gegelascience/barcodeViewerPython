

class InvalidCheckDigit(Exception):
    """Exception when checkDigit is invalid"""


    def __init__(self,wrongDigit:str, message="invalid check digit") -> None:
        self.message = message
        self.wrongDigit = wrongDigit
        super().__init__(self.message)

    def __str__(self):
        return f'{self.wrongDigit} -> {self.message}'


class InvalidEanCharacter(Exception):
    """Exception when ean character is invalid"""


    def __init__(self) -> None:
        super().__init__("invalid character on ean")