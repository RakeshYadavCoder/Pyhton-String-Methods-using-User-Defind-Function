def Find(InputString, Ele_to_be_find):
    for i in range(len(InputString)):
        if InputString[i: i + len(Ele_to_be_find)] == Ele_to_be_find:
            return i
    return -1

if __name__ == '__main__':
    InputString = input()
    Ele_to_be_find = input()
    print(Find(InputString,Ele_to_be_find))