import random

#The card deck
cards = ["Ace", "Ace", "Ace", "Ace", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "K"]

#This will create an array of 52 randomly shuffled cards (53 is not included).
x = random.sample(cards, 53)
#This will create an array of 4 randomly shuffled suits (5 is not included).

print("Welcome to Blackjack!")
print()
print("Rules: \n\nIf you get 21 points you automatically win\nIf you go over 21 then you are bust\nThe closet to 21 points will win")
print()
print("What is your name?")
playerName = input()
print("----------------------------------------------")

#Now that the deck is shuffled the first 1st and 2nd in the array will be given to the player and the 3rd and 4th cards will be given to the dealer.
player_card1, player_card2 = x[0], x[1]
dealer_card1, dealer_card2 = x[2], x[3]
player_cards_string = "Player: " + str(x[0]) + ", " + str(x[1])
dealer_cards_string = "Player: " + str(x[2]) + ", " + str(x[3])

#This will display the players and the dealers cards. I displayed it as a string just in case the player is given an Ace, Jack, Queen or King.
display_player = playerName + ": your cards are " + str(x[0]) + ", " + str(x[1])
print (display_player) #This shows the players first 2 cards.

#Becuase all face cards are equal to 10 I have used an if loop to convert that into an interger, the interger being 10.
if player_card1 == "J" or player_card1 == "Q" or player_card1 == "K":
  player_card1 = 10
elif player_card2 == "J" or player_card2 == "Q" or player_card2 == "K":
  player_card2 = 10
elif player_card1 == "Ace":
  player_card = 1 or 11
elif player_card2 == "Ace":
  player_card2 = 1 or 11

player_total_score = player_card1 + player_card2
print(playerName + ": your current total is: " + str(player_total_score))

#I will repeat the same code for the dealer
if dealer_card1 == "J" or dealer_card1 == "Q" or dealer_card1 == "K":
  dealer_card1 = 10
elif dealer_card2 == "J" or dealer_card2 == "Q" or dealer_card2 == "K":
  dealer_card2 = 10
elif dealer_card1 == "Ace":
  dealer_card = 1 or 11
elif dealer_card2 == "Ace":
  dealer_card2 = 1 or 11
print()
display_dealer = "Dealer: your cards are: " + str(x[2]) + ", " + str(x[3])
print (display_dealer)

if dealer_card1 == "J" or dealer_card1 == "Q" or dealer_card1 == "K":
  dealer_card1 = 10
elif dealer_card2 == "J" or dealer_card2 == "Q" or dealer_card2 == "K":
  dealer_card2 = 10
elif dealer_card1 == "Ace":
  dealer_card = 1 or 11
elif dealer_card2 == "Ace":
  dealer_card2 = 1 or 11

dealer_total_score = dealer_card1 + dealer_card2
print("Dealer: your current total is: " + str(dealer_total_score))
print()
#Now the player will be given the option to hit if they would like
hit = input(playerName + ": if you would like to hit please type 'y' or press any button to stand").lower()

#These will start at 0 because they player has not won nor bust yet.
total_hits = 0
player_total_wins = 0
player_total_busts = 0

while hit == 'y':
  total_hits = total_hits + 1 #This will increment the total number of hits to 1 because the player decided to hit.
  player_cards_string = player_cards_string + ", " + str(x[total_hits + 3]) #Because it is '+ 3' the hit card will end up being the 4th position in the 'x' array/ the randomly shuffled deck at the top of the code.
  print(player_cards_string)
  if x[total_hits + 3] == "J" or x[total_hits + 3] == "Q" or x[total_hits + 3] == "K":
    x[total_hits + 3] = 10
  player_total_score = player_total_score + x[total_hits + 3]
  print()
  print(playerName + ": your current sum is " + str(player_total_score))

  #This will check if the player's score is 21 and if it is then they automatically win
  if player_total_score == 21:
    print("Blackjack! You win.")
    player_total_wins = 1 #The player's total wins will increase to 1 because they got 21.
    break
  #This will check if the player's score goes over 21, which would lead to a bust.
  if player_total_score > 21:
    print("It's a bust! You lose. The dealer wins on default.")
    player_total_busts = 1 #They player's total bust score will increase to 1 because they went over 21.
    break
#If the player reaches this part in the code then they did not hit 21 nor did they bust. So, they can continue to play.
  hit = input(playerName + ": if you would like to hit please type 'y':   ")

dealer_total_hits = 0
dealer_total_wins = 0
dealer_total_busts = 0

if player_total_wins == 0 and player_total_busts == 0:
  while dealer_total_score < 21:
    dealer_total_hits = dealer_total_hits + 1
    dealer_cards_string = dealer_cards_string + ", " + str(x[total_hits + dealer_total_hits + 3])
    print(dealer_cards_string)
    #This just ensures that if when the dealer hits and gets a jack, queen or king the value is registered as a 10.
    if x[total_hits + dealer_total_hits + 3] == "J" or x[total_hits + dealer_total_hits + 3] == "Q" or x[total_hits + dealer_total_hits + 3] == "K":
      x[total_hits + dealer_total_hits + 3] = 10
    dealer_total_score = dealer_total_score + x[total_hits + dealer_total_hits + 3]
    print("Dealer: your current total is: " + str(dealer_total_score))
    #If the dealers points go over 21 then they will automatically lose 
    if dealer_total_score > 21:
      print("It's a bust! You lose. The player wins on default.")
      break

if player_total_wins == 0 and player_total_busts == 0:
  if player_total_score > dealer_total_score:
    print("Congratulations, " + playerName + " you win")
  elif player_total_score == dealer_total_score:
    print("It's a tie!")
  elif player_total_score < dealer_total_score:
    print("The dealer wins.")
    

