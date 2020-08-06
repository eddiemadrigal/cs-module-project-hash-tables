import random
from collections import defaultdict

# Read in all the words in one go
with open("/Lambda/git/cs-module-project-hash-tables/applications/markov/input.txt") as f:
    words = f.read().split()

# TODO: analyze which words can follow other words
# Your code here
word_dict = defaultdict(list)
for word, next_word in zip(words, words[1:]):    #list two words at a time: the first word and then the following word
    word_dict[word].append(next_word)   # create a dictionary and append the following word

# TODO: construct 5 random sentences
# Your code here

# a = ["this", "is", "a", "sentence"]
# print(a[1:])    # prints all words after the first one ==> ['is', 'a', 'sentence']
# print(list(zip(a, a[1:])))  # create a list of combinations

# print(word_dict["For"])

startWord = ['For', 'The', 'But', 'Dinah', 'Well']
for i in range(5):    
    word = random.choice(startWord)
    while not word.endswith("."):
        print(word, end=' ')
        word = random.choice(word_dict[word])
    print(word)