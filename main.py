import random


def choose_options():
  options = ("rock", "paper", "scissors")
  user_option = input("rock, paper, scissors => ").lower().strip()
  
  if not user_option in options:
    print("Error, choice beetwen the options below")
    print("Rock, paper or scissors")
    return None, None
    
  computer_option = random.choice(options)
  
  print("User option is =>", user_option)
  print("Computer option is =>", computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, draw_counter, user_wins, computer_wins):
  if user_option == computer_option:
    print("DRAW!")
    draw_counter += 1
  elif user_option == "rock":
    if computer_option == "scissors":
      print("Rock beats scissors")
      print("YOU WIN!")
      user_wins += 1
    else:
      print("Paper beats rock")
      print("COMPUTER WINS!")
      computer_wins += 1
  elif user_option == "paper":
    if computer_option == "rock":
      print("Paper beats rock")
      print("YOU WIN!")
      user_wins += 1
    else:
      print("Scissors beats paper")
      print("COMPUTER WINS!")
      computer_wins += 1
  elif user_option == "scissors":
    if computer_option == "paper":
      print("Scissors beats paper")
      print("YOU WIN!")
      user_wins += 1
    else:
      print("Rock beats scissors")
      print("COMPUTER WINS!")
      computer_wins += 1
  return draw_counter, user_wins, computer_wins

def check_winner(draw_counter, user_wins, computer_wins):
  if user_wins == 2:
    print("YOU ARE THE FINAL WINNER!!!")
    print("*" * 5)
    print(f"YOU BEAT THE COMPUTER {user_wins} to {computer_wins}")
    print(f"You draw {draw_counter} times!")
    exit()
  if computer_wins == 2:
    print("COMPUTER IS THE FINAL WINNER!!!")
    print("*" * 5)
    print(f"COMPUTER BEATS YOU {computer_wins} to {user_wins}")
    print(f"You draw {draw_counter} times!")
    exit()
def run_game():
  user_wins = 0
  computer_wins = 0
  draw_counter = 0
  rounds = 1
  
  while True:
  
    print("*" * 10)
    print("ROUND", rounds)
    print(f"User: {user_wins} - Computer: {computer_wins}")
    print("*" * 10)
    rounds += 1
    
    user_option, computer_option = choose_options()
    draw_counter, user_wins, computer_wins = check_rules(user_option, computer_option, draw_counter, user_wins, computer_wins)
    check_winner(draw_counter, user_wins, computer_wins)
    
run_game()