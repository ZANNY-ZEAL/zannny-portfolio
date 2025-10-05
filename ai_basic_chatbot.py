import random

responses = {
    "hi": ["Hello!", "Hey!", "Hi there!"],
    "how are you": ["I'm doing great!", "All good here.", "Fantastic, thanks!"],
    "bye": ["Goodbye!", "See ya!", "Take care!"]
}

while True:
    user = input("You: ").lower()
    if user in responses:
        print("Bot:", random.choice(responses[user]))
    elif user == "exit":
        print("Bot: Bye bye!")
        break
    else:
        print("Bot: Sorry, I don’t understand that.")