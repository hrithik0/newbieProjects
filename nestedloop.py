for x in range(4):
    for y in range(4):
        coordinates = (x+1, y+1)
        print(coordinates)

# method 1
pattern_coordiantes = (5, 2, 5, 2, 2)
for coordinates in pattern_coordiantes:
    print("X" * coordinates)

# method 2
for i in range(5):
    if (i + 1) == 1 or (i + 1) == 3:
        print("X" * 5)
    else:
        print("X" * 2)
