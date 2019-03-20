from katas.py.expand_number import expanded_number

roman = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, "XX": 20,
         "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90, "C": 100, "CC": 200, "CCC": 300,
         "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900, "M": 1000}

arabigo = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 20: "XX",
           30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC", 100: "C", 200: "CC", 300: "CCC",
           400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM", 1000: "M", 2000: "MM", 3000: "MMM"}


def to_roman(num):
    if (num == None or num < 1): return "None"
    result = ""
    numbers = expanded_number(num)
    for i in range(len(numbers)):
        result = arabigo[numbers[i]] + result
    return result


def from_roman(string):
    if (string == None): return "None"
    result = 0
    digit = ""
    for i in range(len(string)):
        if ((digit + string[i]) not in roman):
            result = roman[digit] + result
            digit = string[i]
        else:
            digit += string[i]
        if (i == (len(string) - 1)):
            result = roman[digit] + result
    return result
