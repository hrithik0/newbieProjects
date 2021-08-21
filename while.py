i = 1
while i <= 5:
    print(i)
    i += 1


guess_count = 0
while guess_count < 3:
    guess = int(input("Guess:"))
    if guess == 9:
        print("you have guessed it right.")
        print("You Won!")
        break
    guess_count += 1
else:
    print("you lost!")