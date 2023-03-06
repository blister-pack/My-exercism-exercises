class Luhn:
    def __init__(self, card_num):
        self.cred_card = card_num

    def valid(self):
        card_noSpaces = self.cred_card.replace(" ", "")

        #  checking for length
        if len(card_noSpaces) <= 1:
            return False

        #  checking if we have a number
        try:
            int(card_noSpaces)
        except Exception:
            return False

        #  checking if it's Luhn
        listforLuhn = []
        for count, number in enumerate(
            card_noSpaces[len(card_noSpaces) - 1 :: -1], start=1
        ):
            if count % 2 == 0:
                new_num = int(number) * 2
                if new_num > 9:
                    new_num = new_num - 9
                    listforLuhn.append(new_num)
                else:
                    listforLuhn.append(new_num)
            else:
                listforLuhn.append(int(number))

        if sum(listforLuhn) % 10 == 0:
            return True
        else:
            return False


# ---------------------------------------------------------------------------------
num1Valid = Luhn("4539 3195 0343 6467")
num2Invalid = Luhn("8273 1232 7352 0569")
num3Invalid = Luhn("abab abab")
print(num1Valid.valid())
print(num2Invalid.valid())
print(num3Invalid.valid())
