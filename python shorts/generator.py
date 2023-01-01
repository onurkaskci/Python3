import time

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

start_time_gen = time.perf_counter()
# Generate values using the generator
for number in count_up_to(1000000):
    pass
end_time_gen = time.perf_counter()
elapsed_time_gen = end_time_gen - start_time_gen

start_time_normal = time.perf_counter()
# Generate values using the traditional function
for number in count_up_to_list(1000000):
    pass
end_time_normal = time.perf_counter()
elapsed_time_normal = end_time_normal - start_time_normal

# Multiple the seconds by 1000 to get milliseconds
print(f"Elapsed time for Generator: {elapsed_time_gen:.6f} seconds") 
print(f"Elapsed time for Return: {elapsed_time_normal:.6f} seconds")
print(f'Generator was {(elapsed_time_normal-elapsed_time_gen)*1000:.0f} (milli)seconds faster!')
