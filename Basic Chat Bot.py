# Simple Rule-Based Chatbot

def greet():
    """Function to handle greeting"""
    return "Hi! How can I help you today?"

def check_wellbeing():
    """Function to respond to 'how are you' type questions"""
    return "I'm fine, thanks! How about you?"

def say_goodbye():
    """Function to handle goodbye"""
    return "Goodbye! Have a great day!"

def get_bot_response(user_input):
    """
    Main function to process user input and return appropriate response
    
    Args:
        user_input (str): The user's message
        
    Returns:
        str: Bot's response
    """
    # Convert input to lowercase for easier matching
    user_input = user_input.lower().strip()
    
    # Check for greetings
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return greet()
    
    # Check for "how are you" type questions
    elif "how are you" in user_input or "how r u" in user_input:
        return check_wellbeing()
    
    # Check for goodbye
    elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return say_goodbye()
    
    # Check for name questions
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm a simple chatbot created to assist you!"
    
    # Check for help
    elif "help" in user_input:
        return "You can say: hello, how are you, bye, or ask me my name!"
    
    # Default response if no match found
    else:
        return "I'm sorry, I don't understand that. Try saying 'help' for options!"

def main():
    """Main function to run the chatbot"""
    print("=" * 50)
    print("🤖 SIMPLE CHATBOT")
    print("=" * 50)
    print("Type 'bye' to exit the chat\n")
    
    # Main conversation loop
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if user wants to exit
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            print("Bot:", say_goodbye())
            break
        
        # Get and display bot response
        response = get_bot_response(user_input)
        print("Bot:", response)
        print()  # Empty line for better readability

# Run the chatbot
if __name__ == "__main__":
    main()