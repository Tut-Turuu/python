def is_number(i):
    return 48 <= ord(i) <= 57

def encode(string):
    prev = string[0]
    count = 1
    res = ''
    for i in string[1::]:
        if i == prev:
            count += 1
        else:
            if count != 1:
                res += prev + str(count)
            else:
                res += prev
            count = 1
        prev = i
    if string[-2] != string[-1]:
        res += string[-1]
    if count > 1:
        res += prev + str(count)
    return res


def decode(string):
    res = ''
    is_num = False
    flag = False # 2 letters next to each other

    letter = string[0]
    for i in range(1, len(string)):
        if is_number(string[i]):
            res += letter * int(string[i])
        else:
            if not is_number(string[i+1]):
                res += string[i]
            letter = string[i]
                
    return res


def number_to_string(n):
    if n == 1000:
        print("тысяча")

    n = str(n)
    res = ''
    digits = {0: "ноль",
              1: "один",
              2: "два",
              3: "три",
              4: "четыре",
              5: "пять",
              6: "шесть",
              7: "семь",
              8: "восемь",
              9: "девять"}
    
    for i in range(len(n)-1, -1, -1):
        if i == 2:
            if int(n[i]) == 1:
                res += "сто"
            elif int(n[i]) == 2:
                res += "двести"
            if int(n[i]) == 1:
                res += "триста"
            elif int(n[i]) == 2:
                res += "череста"
            elif 5 >= int(n[i]) >= 9:
                res += digits[int(n[i])] + "сот "
        if i == 1:
            if int(n[i]) == 1:
                if int(n[0]) == 0:
                    res += "десять"
                elif int(n[0]) == 1:
                    res += "одиннадцать"
                elif int(n[0]) == 2:
                    res += "двенадцать"
                elif int(n[0]) == 3:
                    res += "тринадцать"
                elif int(n[0]) == 4:
                    res += "четырнадцать" 
                elif int(n[0]) == 5:
                    res += "пятнадцать"
                elif int(n[0]) == 6:
                    res += "шестнадцать"
                elif int(n[0]) == 7:
                    res += "семнадцать"
                elif int(n[0]) == 8:
                    res += "восемнадцать"
                elif int(n[0]) == 9:
                    res += "девятнадцать"

                break
            elif int(n[i]) == 2:
                res += "двадцать"
            elif int(n[i]) == 3:
                res += "тридцать"
            elif int(n[i]) == 4:
                res += "сорок"
            elif 5 >= int(n[i]) >= 8:
                res += digits[int(n[i])] + "десят "
            elif int(n[i]) == 9:
                res += "девяносто"
        if i == 0 and n[i] != '0':
            res += digits[int(n[i])]
        return res
            
    '''
    if (len(str(n)) == 3):
        digit0 = str(n)[0]
        digit1 = str(n)[1]
        digit2 = str(n)[2]
    elif (len(str(n)) == 2):
        digit0 = str(n)[0]
        digit1 = str(n)[1]
    else:
        digit0 = str(n)[0]
    '''

 

while True:
    print(number_to_string(int(input("Enter string: "))))
