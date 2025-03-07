import random


done = False
wins, losses, ties = 0, 0, 0

names ={'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

while not done:
    user_choice = input("Enter a choice (R, P, S) (Q to quit): ").upper()

    if user_choice == 'Q':
        done = True
        continue
    
    if user_choice not in names:
        print ("Invalid choice. Please enter R, P, or S.")
        continue

    computer_choice = random.choice(['R', 'P', 'S'])

    if user_choice == computer_choice:
        print(f"Both players selected {names[user_choice]}. It's a tie!")
        ties += 1
    elif user_choice == 'R':
        if computer_choice == 'P':
            print(f"Rock vs Paper, {names[computer_choice]} wins!")
            losses += 1
        else:
            print (f"Rock vs paper, {names[user_choice]} wins!")
            wins += 1
    elif user_choice == 'P':
        if computer_choice == 'S':
            print(f"Paper vs Scissors, {names[computer_choice]} wins!")
            losses += 1
        else:  
            print(f"Paper vs Scissors, {names[user_choice]} wins!")
            wins += 1
    elif user_choice == 'S':
        if computer_choice == 'R':
            print(f"Scissors vs Rock, {names[computer_choice]} wins!")
            losses += 1
        else:
            print (f"Scissors vs Rock, {names[user_choice]} wins!")
            wins += 1
    print (f"Score - You: {wins}, Computer: {losses}, Ties: {ties}")

print (" Thanks for playing!")  
