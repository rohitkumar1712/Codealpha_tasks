# ============================================
# Task 4: Basic Rule-Based Chatbot
# ============================================

def chatbot():
    print("=" * 50)
    print("        WELCOME TO BASIC CHATBOT")
    print("=" * 50)
    print("Type 'bye' to end the conversation.\n")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "hi":
            print("Bot: Hello! How can I help you?")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! How about you?")

        elif user == "i am fine":
            print("Bot: That's great to hear!")

        elif user == "what is your name":
            print("Bot: My name is Python Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python programming.")

        elif user == "what can you do":
            print("Bot: I can answer simple predefined questions.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "help":
            print("Bot: You can ask me:")
            print("     - hello")
            print("     - hi")
            print("     - how are you")
            print("     - what is your name")
            print("     - who created you")
            print("     - what can you do")
            print("     - thank you")
            print("     - bye")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")


# Start the chatbot
chatbot()