import traceback

def exception_handling():
  #numbers = int(input("Please enter a number: "))
  try:
    numbers = int(input("Please enter a number: "))
  except ValueError:
    traceback.print_exc()
    print("oops")
  