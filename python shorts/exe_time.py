import time

def my_function():
    # code to be measured
    time.sleep(2)

# measure the execution time
start_time = time.perf_counter()
my_function()
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time*1000:.6f} milliseconds")
