def no_dups(s):
    # Your code here
    s = s.split(" ")
    myList = []

    for i in s:
        if (s.count(i) > 1 and (i not in myList) or s.count(i) == 1):
            myList.append(i)
    return(' '.join(myList))



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))