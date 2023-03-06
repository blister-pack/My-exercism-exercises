class Luhn:
    def __init__(self, card_num):
        self.cred_card = card_num

    def valid(self):
        card_noSpaces = self.cred_card.replace(" ", "")

        #  checking for length
        if len(card_noSpaces) <= 1:
            return "Card invalid - too short"

        #  checking if we have a number
        try:
            int(card_noSpaces)
        except Exception:
            return "Card isn't a number"

        #  checking if it's Luhn


# ---------------------------------------------------------------------------------
num1Valid = Luhn("4539 3195 0343 6467")
num2Invalid = Luhn("8273 1232 7352 0569")
num3Invalid = Luhn("abab abab")
print(num3Invalid.valid())
print(num1Valid.valid())
print(num2Invalid.valid())
