def sum_numbers(a, b):
    return a+b

print('Function with limited arguments: ')
print(sum_numbers(1, 2))

def sum_multiple_numbers(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total

print('Function with unlimited arguments: ')
print(sum_multiple_numbers(1, 2, 3, 4, 5)) 


