# raise the even numbers to their second power 
# and odd numbers to their 3rd power
numbers = [2, 3, 4, 5]

result = []
for number in numbers:
    if number % 2 != 0:
        result.append(number**3)
    else:
        result.append(number**2)
print('Result WITHOUT list comprehension: ')
print(result)

comprehension_result = [x**3 if x % 2 != 0 else x**2 for x in numbers]
print('Result WITH list comprehension: ')
print(comprehension_result)
