list_with_sublists = ['a', 'b', ['a', 'a', 'c'], 'a']

#Solution 1
count = list_with_sublists.count('a')
print(f'Count Function Output: {count}')  # Output: 2

#Solution 2
count = 0
for element in list_with_sublists:
    if element == 'a':
        count += 1
    elif isinstance(element, list):
        count += element.count('a')
print(f'For Loop Output: {count}')  # Output: 4
