def Isupper(InputString):
    for i in InputString:
        if ord(i) <= 122 and ord(i) >= 97:
            return False
    return True
if __name__=='__main__':
    InputString = input()
    print(Isupper(InputString))