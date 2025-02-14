# EXERCICE 1

items=[x for x in input().split(',')]
items.sort()
print (','.join(items))

#EXERCICE 2

sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word =""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)
