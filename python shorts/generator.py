import memory_profiler

@memory_profiler.profile
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

@memory_profiler.profile
def count_up_to_list(max):
    count_list = []
    count = 1
    while count <= max:
        count_list.append(count)
        count += 1
    return count_list

# Generate values using the generator
for number in count_up_to(1000000):
    pass

# Generate values using the traditional function
for number in count_up_to_list(1000000):
    pass
