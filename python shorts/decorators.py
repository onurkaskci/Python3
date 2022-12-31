def first_function(func):
  def wrapper(*args):
    value = func(*args)
    if value <= 3:
      print('value is 3')
    elif value <= 2:
      print('value is 2')
    else: 
      print('Invalid Input')
  return wrapper

@first_function
def second_function(*args):
  return sum(list(args))

second_function(1,2)

# A: 
# B:
# C: