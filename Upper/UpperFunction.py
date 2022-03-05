def Upper(StringInput):
    UpperString = ''
    for i in StringInput:
        if ord(i) >= 97 and ord(i) <= 122:
            UpperString += chr(ord(i) - 32)
        else:
            UpperString += i
    return UpperString
    
if __name__=='__main__':
    StringInput = input()
    print(Upper(StringInput))