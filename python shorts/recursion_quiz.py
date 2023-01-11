
val = []

def count_down(x):
    if x % 2 == 0:
        val.append(x)
    if x > 0:
        count_down(x-1)

count_down(10)
print(val)

# A: [10, 8, 6, 4, 2, 0]
# B: [9, 7, 5, 3, 1]
# C: [10]
# D: RecursionError
