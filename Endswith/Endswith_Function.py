def Endswith(InputString, Ele_to_be_check):
    if InputString[len(InputString) - len(Ele_to_be_check): len(InputString)] == Ele_to_be_check:
        return True
    else:
        return False

if __name__ == '__main__':
    InputString = input()
    Ele_to_be_check = input()
    print(Endswith(InputString, Ele_to_be_check))