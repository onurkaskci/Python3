f = lambda x: x + 1 # 200 -> 201
g = lambda x: x * 2 # 100 -> 200
h = lambda x: x ** 2 # 10 -> 100

x = 10
print(f(g(h(x))))

# A: 21
# B: 201
# C: 11