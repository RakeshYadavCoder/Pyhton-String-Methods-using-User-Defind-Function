def Startswith(InputString, Ele_to_be_check):
    if InputString[0: len(Ele_to_be_check)] == Ele_to_be_check:
        return True
    else:
        return False
if __name__ == '__main__':
    InputString = input()
    Ele_to_be_check = input()
    print(Startswith(InputString, Ele_to_be_check))