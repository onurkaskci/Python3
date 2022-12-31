
def first_function(func):
  def wrapper(*args):
    received_value = func(*args)
    if received_value > 2:
      print('received value > 2')
    else:
      print('received value < 2')
  return wrapper

@first_function
def second_function(*args):
  return sum(list(args))

second_function(1,2)

# A: received value > 2
# B: received value < 2
# C: SyntaxError