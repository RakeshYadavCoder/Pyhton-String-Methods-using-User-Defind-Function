def Isalnum(InputString):
    for i in InputString:
        if (ord(i) <= 57 and ord(i) >= 48) or (ord(i) <= 90 and ord(i) >=65) or (ord(i) <= 122 and ord(i) >= 97):
            continue
        else:
            return False
    return True
if __name__ == '__main__':
    InputString = input()
    print(Isalnum(InputString))