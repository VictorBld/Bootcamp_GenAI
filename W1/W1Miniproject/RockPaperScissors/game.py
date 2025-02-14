class Game():
  def __init__(self):
    return

  def get_user_item(self):
    user_item=input("Choose between Rock, Paper and Scissors : ")
    user_item=user_item.lower()
    while user_item not in ["rock", "paper", "scissors"]:
      user_item=input("Choose between Rock, Paper and Scissors : ")
      user_item=user_item.lower()
    return user_item
  
  def get_computer_item(self):
    import random
    computer_item=random.choice(["rock", "paper", "scissors"])
    return computer_item

  def get_game_result(self, user_item, computer_item):
    if user_item == computer_item:
      return "You drew!"
    elif user_item == "rock" and computer_item == "scissors":
      return "You win!"
    elif user_item == "paper" and computer_item == "rock":
      return "You win!"
    elif user_item == "scissors" and computer_item == "paper":
      return "You win!"
    else:
      return "You lose!"

  def play(self):
      user_item=self.get_user_item()
      computer_item=self.get_computer_item()
      print(f"You chose {user_item}")
      print(f"The computer chose {computer_item}")
      print(self.get_game_result(user_item, computer_item))
      if(self.get_game_result(user_item, computer_item))=="You win!":
        return "win"
      elif(self.get_game_result(user_item, computer_item))=="You lose!":
        return "lose"
      else:
        return "draw"


    