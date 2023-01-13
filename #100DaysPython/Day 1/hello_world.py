#print("HEllo world")



#from art import logo

def calculator_program(number1, number2, operation):
  #function to work the calc program
  if operation == "+":
    total = num1 + num2
  elif operation == "-":
    total = num1 - num2
  elif operation == "*":
    total = num1 * num2
  elif operation == "/":
    total = num1 / num2
  else:
    print("Wrong input. Try again")
  return total


while True:
  #print(logo)
  #loop to continuously ask user for inputs
  num1 = int(input("what's the first number?: "))
  print("\n+\n-\n*\n/")
  op = input("Pick an operation: ")
  num2 = int(input("Enter the second number?: "))
  
  total = calculator_program(num1, num2, op)

  print(f"{num1} {op} {num2} = {total}")

  
  another_try = input(f"Type 'y' to continue calculating using {total}, or type 'n' to start new calculation:  ").lower()

  if another_try == "quit":
    break
  elif another_try == "y":
    num1 = total
  elif another_try == 'n':
    pass





