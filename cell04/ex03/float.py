user_input=input("Please enter a number: ")
try:number+float(user_input)
if number.is_integer():print("The number is not a decimal(it's an integer).") else:print("The number is a decimal.")
except Valueerror:print("Invalid input.That is not a number.")