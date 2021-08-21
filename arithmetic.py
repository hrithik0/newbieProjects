x = 3
for i in range (2):
    if (i + 1) % 2 == 0:
        x *= 3
    else:
        x *= 2
# print(x)
if input("Do you want to see the answer: ").upper() == "Y":
    print(x)
else:
    print("You have not chosen to display the answer.")