emojis = {
    ":)" : "😊",
    ":(" : "😔"
}

message = input("> ").split()
output =""
for words in message:
    output += emojis.get(words,words) + " "
print(output)