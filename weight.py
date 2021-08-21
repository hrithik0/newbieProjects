current_weight = int(input("Weight: "))
if input("(L)bs or (K)g: ").lower() == 'l':
    current_weight = current_weight * 0.45
    print(f"Your weight in Kilograms is {current_weight}kg")
else:
    current_weight = current_weight / 0.45
    print(f"Your weight in Pounds is {current_weight}lbs")
