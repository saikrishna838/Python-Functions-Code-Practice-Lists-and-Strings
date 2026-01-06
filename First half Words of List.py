words = input().split()

words_length = len(words)

if words_length % 2 == 0:
    half_list_length = words_length // 2
else:
    half_list_length = (words_length // 2) + 1
    
new_list = words[:half_list_length]

print(new_list)