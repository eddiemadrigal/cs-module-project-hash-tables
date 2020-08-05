def word_count(s):
    # Your code here
    word_collection = {}

    # replace individual characters in the first argument with corresponding characters of the second argument
    # based on the translation table (.makestrans(x, y=None, z=None))
    lower_s = s.translate(str.maketrans('str', 'str', '":;,.-+=/\|[]{}()*^&')).lower().split()
    for i in lower_s:
        if i in word_collection:
            word_collection[i] += 1
        else:
            word_collection[i] = 1
    return word_collection



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))