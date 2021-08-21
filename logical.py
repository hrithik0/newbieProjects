high_income = True
has_good_credit = True

if high_income and has_good_credit:
    print("you are eligible for loan.")
else:
    print("YOU are not eligible for loan")

# question --
length = len(input("Write your name ").strip())
if length < 3:
    print("name must be at least 3 characters.")
elif length > 50:
    print("name can be a maximum of 50 characters.")
else:
    print("name look's good")