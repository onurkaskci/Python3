f = lambda x: x + 1
g = lambda x: x * 2
h = lambda x: x ** 2

x = 10
print(f(g(h(x))))

# A: 21
# B: 201
# C: 11


f = lambda x: x + 1
g = lambda x: x * 2
h = lambda x: x ** 2

x = 10
print((f(g(h(x)))) + (g(f(h(x)))))

# A: 403
# B: 211
# C: 102
