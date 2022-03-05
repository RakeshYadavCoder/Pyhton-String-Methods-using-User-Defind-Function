#ascii 0 to 9 value start from 48 to 57
def Isdigit(InputString):
    for i in InputString:
        if ord(i) >= 48 and ord(i) <= 57:
            continue
        else:
            return False
    return True
if __name__ == '__main__':
    InputString = input()
    print(Isdigit(InputString))