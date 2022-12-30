def greet(func):
  def wrapper(*args, **kwargs):
    print("Hello!")
    func(*args, **kwargs)
  return wrapper

@greet
def say_hi():
  print("Hi there!")

say_hi()
