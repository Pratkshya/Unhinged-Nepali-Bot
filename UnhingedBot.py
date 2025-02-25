import random

class UnhingedBot:
    def __init__(self):
        self.responses = [
            "ma ta bhandina",
            "timi ta dherei kaam chor chhau re",
            "malai k tha tyo bhaneko k ho",
            "tyo kta ta dherei bhau khancha hai",
            "you deserve so much better",
            "exam aaisako, padhna chhodera k garira",
            "guliyo jerry hau, timi ta meri hau, aaru lai dhan ko paat, timi lai paan ko paat",
            "k k sodhchhe sodhchhe",
            "aha ma ta boldina",
            "ho ta",
            "kata bidesh ma ho?",
        ]

    def get_response(self, user_input):
        if user_input.lower() in ["bye", "exit", "quit"]:
            return "kina risako? bolana bola"
        return random.choice(self.responses)

# Main loop
if __name__ == "__main__":
    bot = UnhingedBot()
    print("Nepali Bot🤖: Welcome to your exquisite experience. Type anything or 'bye' to leave.")

    while True:
        user_input = input("You: ")
        response = bot.get_response(user_input)
        print(f"UnhingedBot 🤖: {response}")
        if user_input.lower() in ["bye", "exit", "quit"]:
            break
