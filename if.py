is_hot = bool
is_cold = bool
whether = input("How is the current whether? ").lower()
if whether == 'hot':
    is_hot = True
    is_cold = False
elif whether == 'cold':
    is_cold = True
    is_hot = False
else:
    is_hot = is_cold = False

if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water!")
elif is_cold:
    print("It's a cold day.")
    print("Wear warm clothes.")
elif not is_hot and not is_cold:
    print("it's a lovely day.")
    print("enjoy your day.")