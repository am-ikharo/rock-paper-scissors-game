rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
game_images = [rock, paper, scissors]
options = ["rock", "paper", "scissors"]
random_num = random.randint(0,2)
user_pick = int(input("pick your option between rock = 0, paper = 1 and scissors = 2:\n "))
print(game_images[user_pick])
print(f"you choose {options[user_pick]}")
computer_pick = random_num
print(game_images[computer_pick])
print(f"computer choose {options[computer_pick]}")



if user_pick == 0 and computer_pick == 2:
    print("you win")
elif computer_pick == 0 and user_pick == 2:
    print("you lose")   
elif user_pick >= 3:
    print("you enter an invalid number") 
elif computer_pick > user_pick:
    print("you lose")    
elif user_pick > computer_pick:
    print("you win")
elif computer_pick == user_pick:
    print("its a draw")
