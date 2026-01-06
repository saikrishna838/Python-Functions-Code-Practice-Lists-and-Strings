numbers = input()
numbers_list = numbers.split()
divisible_by_3_list = []

for number in numbers_list:
    number = int(number)
    
    if number % 3 == 0:
        divisible_by_3_list += [number]

print(divisible_by_3_list)