letters = ["a", "b", "c"]
for letter in letters:
    print(f"{letter} has index {letters.index(letter)}")

for index, letter in enumerate(letters):
    print(index, letter)