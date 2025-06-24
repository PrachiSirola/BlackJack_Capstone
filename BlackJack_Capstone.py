print("WELCOME TO THE GAME BLACKJACK CAPSTONE")
import random
def deal_card():
  """Return a random card from the deck"""
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return (card)

def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0

  if cards==11 and sum(cards)>21: 
    cards.remove(11) 
    cards.append(1) 
  return sum(cards)

def compare(u_score, c_score):
  if u_score==c_score:
    return "DRAW"
  elif c_score==0:
    return "Computer has blackjack. YOU LOSE..."
  elif u_score==0:
    return "You have blackjack. YOU WIN..."
  elif u_score> 21:
    return "Your score is above 21. YOU LOSE..."
  elif c_score> 21:
    return "Computer score is above 21. YOU WIN..."
  elif u_score> c_score:
    return"Your score is more closer to 21. YOU WIN..."
  else:
    return"Computer score is more closer to 21. YOU LOSE..."


user_card=[] 
computer_card=[]
computer_score= -1
user_score= -1
is_game_over= False

for n in range(2): 
   user_card.append(deal_card())
   computer_card.append(deal_card()) 
while not is_game_over:
  user_score=calculate_score(user_card)   
  computer_score=calculate_score(computer_card) 

  print(f"Your sum of two numbers is {user_card} = {user_score}")
  print(f"Computer first card : {computer_card[0]}")

  if user_score==0 or computer_score==0 or user_score > 21:
    is_game_over = True
  else:
    ask=input("You want to get another card? 'yes' or 'no': ").lower()
    if ask=="yes":
      user_card.append(deal_card())
    else:
      is_game_over = True

#Working on computer side now    
while computer_score!=0 and computer_score<17:
  computer_card.append(deal_card())
  computer_score=calculate_score(computer_card)
print(f"Your final hand: {user_card}, final score: {user_score}")
print(f"Computer final hand: {computer_card}, computer final hand {computer_score}")
print(compare(user_score, computer_score))  

