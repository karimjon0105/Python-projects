from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")
auction = {}
while True:
  name= input("What is your name? ")
  bid_price = int(input("What's your bid?: $ "))
  auction[name] = bid_price
  new_user = input("Are there any other bidders? Type Yes or No\n").lower()
  if new_user == 'yes':
    clear()
  elif new_user=='no':
    key = max(auction, key= auction.get)
    value= auction.values()
    max_value =max(value)
    print(f"The winner is {key} with a bid of {max_value}")
    break