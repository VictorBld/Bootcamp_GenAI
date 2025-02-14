from game import Game


def get_user_menu_choice():
  print("Menu :")
  choice=input("(g) Play a new game \n(x) Show scores and exit\n : ")
  while choice not in ["g", "x"]:
    print("Invalid choice, select again")
    choice=input("(g) Play a new game \n(x) Show scores and exit\n : ")
  if choice == "g" :
    return 'Play a new game'
  elif choice == "x" :
    return 'Show scores and exit'


def print_results(results):
  print("Game results : ")
  print(f"You won {results['win']} times.")
  print(f"You lose : {results['lose']} times.")
  print(f"You drew : {results['draw']} times.")


def main():
  while True :
    if get_user_menu_choice() == 'Play a new game':
      game=Game()
      result=game.play()
      if result=="win":
        results["win"]+= 1
      elif result=="lose":
        results["lose"]+= 1
      else:
        results["draw"]+= 1
    if get_user_menu_choice() == 'Show scores and exit':
      print_results(results)
      print("Thanks for playing!")
      break

results={'win' : 0, 'lose' : 0, 'draw' : 0}

main()

  