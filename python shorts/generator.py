import sys

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

def count_up_to_list(max):
    count_list = []
    count = 1
    while count <= max:
        count_list.append(count)
        count += 1
    return count_list

print(f'Memory Used by Generator: {sys.getsizeof(count_up_to(1000000))} bytes')
print(f'Memory Used by Regular: {sys.getsizeof(count_up_to_list(1000000))} bytes')