def intToRoman(num):
    integerToRoman = {1: "I",
                      2: "II",
                      3: "III",
                      4: "IV",
                      5: "V",
                      9: "IX",
                      10: "X",
                      40: "XL",
                      50: "L",
                      90: "XC",
                      100: "C",
                      400: "CD",
                      500: "D",
                      900: "CM",
                      1000: "M"}
    num1 = str(num)
    roman = ""
    num3 = []
    for i in range(len(num1)):

        num2 = int(num1[i])*10**(len(num1)-(i+1))
        if num2 == 4 * 10 ** (len(num1) - (i + 1)):
            num3.append(4 * 10 ** (len(num1) - (i + 1)))
        elif num2 == 9 * 10 ** (len(num1) - (i + 1)):
            num3.append(9 * 10 ** (len(num1) - (i + 1)))
        elif num2 > 5*10**(len(num1)-(i+1)):
            num3.append(5*10**(len(num1)-(i+1)))
            num2 = num2 - 5*10**(len(num1)-(i+1))
            for j in range(int(num2/(10**(len(num1)-(i+1))))):
                num3.append(1*10**(len(num1)-(i+1)))
        elif num2 < 5*10**(len(num1)-(i+1)):
            for j in range(int(num2/(10**(len(num1)-(i+1))))):
                num3.append(1*10**(len(num1)-(i+1)))
        else:
            num3.append(5 * 10 ** (len(num1)-(i+1)))
    for i in range(len(num3)):
        roman = roman + integerToRoman[num3[i]]
    return roman


if __name__ == '__main__':
    print(intToRoman(1994))