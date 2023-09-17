from replit import clear
import art
print(art.logo)

bids ={}

def greater_bid():
  result= 0
  winner = ''
  for i in bids:
    if result < int(bids[i]):
      result= int(bids[i])
      winner = i
    
  print(f"The winner is {winner} with a bid of ${result}")

condition=True
while(condition == True):
  name= input("Enter your name: ")
  price= input("Enter your bid price:$")
  bids[name] = price
  other_user = input("Is any other bidder want? type 'yes' or 'no'")
  if(other_user == "yes"):
    condition= True
    clear()
  elif (other_user == "no"):
    condition= False
    greater_bid()

