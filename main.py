import random
from replit import clear
from art import logo
import itertools

def create_deck():
  suits = ["♠", "♥", "♦", "♣"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  return list(itertools.product(ranks, suits))

def shuffled(deck):
  random.shuffle(deck)
  return deck
  
def deal_card(deck, card):
  """Returns a random card from the deck."""
  card = random.choice(deck)
  deck.remove(card)
  return deck, card

def deal_n_cards(deck, player, numofcards):
  player_hand = []
  for i in range(numofcards):
    deck, player = deal_card(deck, player)
    player_hand.append(player)
  return deck, player_hand

def calc_hand(player):
  score = 0
  ace_count = 0
  for card in player:
    if (card[0] == "J") or (card[0] == "Q") or (card[0] == "K"):
      score += 10
    elif card[0] == "A":
      score += 11
      ace_count +=1
    else:
      score += int(card[0])
  if (score > 21) and (ace_count > 0):
    score -= 10
  if (score == 21) and (len(player) == 2):
    return 0
  return score

def initiate_deck(cards):
  cards = create_deck()
  cards = shuffled(cards)
  #print("Initial deck: ", cards)
  return cards

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤\n"
  if user_score == computer_score:
    return "Draw 🙃\n"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱\n"
  elif user_score == 0:
    return "Win with a Blackjack 😎\n"
  elif user_score > 21:
    return "You went over. You lose 😭\n"
  elif computer_score > 21:
    return "Opponent went over. You win 😁\n"
  elif user_score > computer_score:
    return "You win 😃\n"
  else:
    return "You lose 😤\n"

def play_game():
  
  card = ()
  cards = []
  temp_cards = []
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  cards = initiate_deck(cards)
  
  cards, temp_cards = deal_n_cards(cards,temp_cards,2)
  user_cards += temp_cards
    
  cards, temp_cards = deal_n_cards(cards,temp_cards,2)
  computer_cards += temp_cards
     
  while not is_game_over:
    
    user_score = calc_hand(user_cards)
    computer_score = calc_hand(computer_cards)
    print(f"Your cards: {user_cards} \nCurrent score: {user_score}\n")
    print(f"Computer's first card: {computer_cards[0]}\n")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      
      user_should_deal = input("Type 'y' to get another card,\
      type 'n' to pass: ")
      
      if user_should_deal == "y":
        cards, card = deal_card(cards, card)
        user_cards.append(card)
                
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    cards, card = deal_card(cards, card)
    computer_cards.append(card)
    computer_score = calc_hand(computer_cards)

  print(f"\nYour final hand: {user_cards}\nFinal score: {user_score}")
  print(f"\nComputer's final hand: {computer_cards}\nFinal score: {computer_score}\n")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  print(logo)
  play_game()




