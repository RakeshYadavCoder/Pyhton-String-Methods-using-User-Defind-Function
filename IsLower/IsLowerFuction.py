def Islower(InputString):
    for i in InputString:
        if ord(i) <= 90 and ord(i) >=65:
            return False
    return True
if __name__=='__main__':
    InputString = input()
    print(Islower(InputString))