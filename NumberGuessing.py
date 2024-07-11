import random as r

def play_game():
    n = r.randint(1,50)
    attempts = 0
    num = int(input("Guess the Number 1-50: "))

    while n!=num:
        attempts+=1
        if num < n:
            print("Too Low")
            num = int(input("Enter Again: "))

        elif num > n:
            print("Too High")
            num = int(input("Enter Again: "))

    attempts+=1
    print(f"You Guessed it Right in {attempts} attempts")
    
while True:
    play_game()
    play_again = input("Do you want to Play Again? (y/n):").lower()
    if play_again != "y":
        break

print("Thanks for Playing")
input("Press any key to exit....")
