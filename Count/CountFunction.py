def Count(InputString, Ele_to_be_count):
    count = 0
    
    for i in range(len(InputString)):
        if InputString[i: i+len(Ele_to_be_count)] == Ele_to_be_count:
            count += 1
    return count
    

if __name__ == '__main__':
    InputString = input()
    Ele_to_be_count = input()
    print(Count(InputString, Ele_to_be_count))