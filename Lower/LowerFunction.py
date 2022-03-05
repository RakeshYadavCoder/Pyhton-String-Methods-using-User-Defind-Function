def Lower(StringInput):
    OutputString = ''
    for i in StringInput:
        if ord(i)<= 90 and ord(i) >= 65:
            OutputString += chr(ord(i) + 32)
        else:
            OutputString += i
    return OutputString

if __name__=='__main__':
    StringInput = input()
    print(Lower(StringInput))