def Index(InputString, Element):
    IndexList = []
    for i in range(len(InputString)):
        if InputString[i: i+ len(Element)] == Element:
             IndexList.append(i)
    if len(IndexList) == 0:
        return 'ValueError: substring not found'
    else: 
        return IndexList[-1]
if __name__ == '__main__':
    InputString  = input()
    Ele_to_be_search = input()
    print(Index(InputString, Ele_to_be_search))