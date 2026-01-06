string = input()

words = string.split()
for char in words:
    lower_case = char.lower()
    if lower_case[0] == lower_case[-1]:
        print("True")
    else:
        print("False")