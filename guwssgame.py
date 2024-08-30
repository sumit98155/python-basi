#guess game
secret_key = 07
guess_count = 0 #initialization
guess_limit = 3 #condition check

while guess_count < guess_limit:
    guess = int(input("enter your guess number :"))
    guess_count = guess_count +1
    if guess == secret_key:
        print("hurray...! you won the game!!")
        break
    else:
        print("sorry.....! try again")