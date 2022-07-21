def romanToInteger(s):
    counter = 0
    romanToInteger = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000,
                      "IV": 4,
                      "IX": 9,
                      "XL": 40,
                      "XC": 90,
                      "CD": 400,
                      "CM": 900}
    j = 0
    while j in range(len(s)):
        if j+1 in range(len(s)):
            if s[j] + s[j + 1] in romanToInteger:
                counter = romanToInteger[s[j] + s[j + 1]] + counter
                j = j + 2
            elif s[j] in romanToInteger:
                counter = romanToInteger[s[j]] + counter
                j = j + 1
        else:
            counter = romanToInteger[s[j]] + counter
            break
    return counter
if __name__ == '__main__':
    print(romanToInteger("LVIII"))

