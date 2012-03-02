"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

def letters_of(n):
    if n in numbers:
        return len(numbers[n])
        pass

    letters = []
    if n >= 1000:
        letters.append(numbers[n//1000])
        letters.append("thousand")
        n %= 1000
        # TODO implement further construction if neccessary
    if n >= 100:
        letters.append(numbers[n//100])
        letters.append("hundred")
        if n % 100 != 0:
            letters.append("and")
            pass
        n %= 100
        pass
    if n >= 20:
        letters.append(numbers[(n//10)*10])
        n %= 10
        pass
    if n > 0:
        letters.append(numbers[n])
        pass
    return sum(map(len, letters))
    pass

print sum(map(letters_of, range(1, 1001)))
