def first_function(func):
  def wrapper(*args):
    value = func(*args)
    if value <= 3:
      print('3')
    elif value <= 2:
      print('2')
  return wrapper

@first_function
def second_function(*args):
  return sum(list(args))

second_function(1,2)

# A: 3
# B: 2
# C: SyntaxError