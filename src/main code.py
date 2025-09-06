class NumberStringConvert:
    def __init__(self):
        self.ignore_words = ["and"]

    def word_to_num(self, word):

        word = word.lower()

        if word == "one":
            return 1
        elif word == "two":
            return 2
        elif word == "three":
            return 3
        elif word == "four":
            return 4
        elif word == "five":
            return 5
        elif word == "six":
            return 6
        elif word == "seven":
            return 7
        elif word == "eight":
            return 8
        elif word == "nine":
            return 9
        elif word == "ten":
            return 10
        elif word == "eleven":
            return 11
        elif word == "twelve":
            return 12
        elif word == "thirteen":
            return 13
        elif word == "fourteen":
            return 14
        elif word == "fifteen":
            return 15
        elif word == "sixteen":
            return 16
        elif word == "seventeen":
            return 17
        elif word == "eighteen":
            return 18
        elif word == "nineteen":
            return 19

        # Tens
        elif word == "twenty":
            return 20
        elif word == "thirty":
            return 30
        elif word == "forty":
            return 40
        elif word == "fifty":
            return 50
        elif word == "sixty":
            return 60
        elif word == "seventy":
            return 70
        elif word == "eighty":
            return 80
        elif word == "ninety":
            return 90

        elif word == "hundred" or word == "thousand" or word == "lakh":
            return None

        elif word == "and":
            return None

        else:
            raise ValueError("Invalid word in input: " + word)

    def convert(self, text):
        """
        Main function to convert full sentence like
        'two lakh ten thousand five' into a number.
        """

        words = text.lower().strip().split()

        total = 0

        current = 0

        for word in words:
            num = self.word_to_num(word)

            if num is not None:  
                current += num

            elif word == "hundred":
                if current == 0:
                    current = 1
                current *= 100

            elif word == "thousand":
                if current == 0:
                    current = 1
                total += current * 1000
                current = 0 

            elif word == "lakh":
                if current == 0:
                    current = 1
                total += current * 100000
                current = 0  # reset

            elif word in self.ignore_words:
                # Just skip "and"
                continue

            else:
                raise ValueError("Invalid word is in input: " + word)

        return total + current


converter = NumberStringConvert()

print("Enter a number in words (up to lakhs): ")
user_input = input().strip()

try:
    result = converter.convert(user_input)
    print("The number is:", result)
except ValueError as e:
    print("Error:", e)
