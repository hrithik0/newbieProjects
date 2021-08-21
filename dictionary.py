phone = input("Phone: ")
numbers = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}
phone_number = ""
for number in phone:
    phone_number = phone_number + " " + numbers.get(number)
print(phone_number)