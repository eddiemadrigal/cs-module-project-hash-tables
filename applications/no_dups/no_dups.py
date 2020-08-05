def no_dups(s):
    # Your code here
    words = s.split(" ")    # s is assigned an array of words from 
    myList = []

    for word in words:
        if (words.count(word) > 1 and (word not in myList) or words.count(word) == 1):
            myList.append(word)
    return(' '.join(myList))



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))