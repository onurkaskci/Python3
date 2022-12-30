
def mystery_function(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    else:
        return mystery_function(n-1)

print(mystery_function(5))

# A: 4
# B: Invalid input
# C: Error
# D: 0