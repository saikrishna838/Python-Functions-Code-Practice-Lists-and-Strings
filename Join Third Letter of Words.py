sentence = input()

string_list = sentence.split()

result = []

for word in string_list:
    if (len(word) > 2):
        character = word[2]
        result += [character]
        
character_joined_by_comma = ",".join(result)

print(character_joined_by_comma)
        