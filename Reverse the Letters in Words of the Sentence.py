sentence = input()
words_list = sentence.split()

modified_sentence = []
for word in words_list:
    modified_sentence += [word[::-1]]
    
reversed_letters_sentence = " ".join(modified_sentence)
print(reversed_letters_sentence)