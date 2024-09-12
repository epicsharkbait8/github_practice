import random
def playGame():
  print("Lets play rock, paper, scissors!")
  play = input("Rock, Paper, or Scissors?")
  choices = ["Rock", "Paper", "Scissors"]
  opp = random.choice(choices)
  print("Computer chose " + opp)
  if opp == "Rock" and play == "Paper":
    print("You win!")
  if opp == "Paper" and play == "Scissors":
     print("You win!")
  if opp == "Scissors" and play == "Rock":
     print("You win!")
  if opp == "Rock" and play == "Scissors":
     print("You lose!")
  if opp == "Paper" and play == "Rock":
     print("You lose!")
  if opp == "Scissors" and play == "Paper":
     print("You lose!")
  if opp == "Rock" and play == "Rock":
     print("Tie!")
  if opp == "Paper" and play == "Paper":
     print("Tie!")
  if opp == "Scissors" and play == "Scissors":
     print("Tie!")
playGame()