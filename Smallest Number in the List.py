numbers = input()
numbers_list = numbers.split()
smallest_number = int(numbers_list[0])

for number in numbers_list:
    number = int(number)
    
    if number < smallest_number:
        smallest_number = number
    
print(smallest_number)