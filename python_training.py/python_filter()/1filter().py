def is_even(num):
    return num%2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(is_even, numbers))

print(even_numbers)