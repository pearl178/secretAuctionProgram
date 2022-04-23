bids = {}
print("Welcome to the secret auction program.")

is_other = True
while is_other:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  bids[name] = bid
  answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  
  if answer == 'no':
    is_other = False
  # clear the screen

highest = 0
for bidder in bids:
  if bids[bidder] > highest:
    highest = bids[bidder]
    winner = bidder
print(f"The winner is {winner} with a bid of ${highest}")
