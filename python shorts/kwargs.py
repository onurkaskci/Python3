
# using kwargs
def myfunc(**kwargs):
    total = 0
    for x in kwargs.values():
        total += x
    print(total)

myfunc(a=1, b=2, c=3)