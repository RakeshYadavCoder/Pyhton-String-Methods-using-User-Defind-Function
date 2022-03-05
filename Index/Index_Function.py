def Index(InputString, Element):
    for i in range(len(InputString)):
        if InputString[i: i+ len(Element)] == Element:
             return i
    return 'ValueError: substring not found'
if __name__ == '__main__':
    InputString  = input()
    Ele_to_be_search = input()
    print(Index(InputString, Ele_to_be_search))