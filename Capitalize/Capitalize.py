def Capitalize(InputString):
    OutputString = ''
    for i in range(len(InputString)):
        if i == 0 and (ord(InputString[i]) <= 122 and ord(InputString[i])  >= 97):
            OutputString += chr(ord(InputString[i]) - 32)
        elif i != 0 and (ord(InputString[i])  <= 90 and ord(InputString[i])  >= 65):
            OutputString += chr(ord(InputString[i]) + 32)
        else:
            OutputString += InputString[i]
    return OutputString  
if __name__=='__main__':
    InputString = input()
    print(Capitalize(InputString))