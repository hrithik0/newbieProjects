message = input("> ")


def emoji(message):
    output = ""
    words = message.split()
    emojis = {
        ":)": "😊",
        ":(": "😔"
    }
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emoji(message))
