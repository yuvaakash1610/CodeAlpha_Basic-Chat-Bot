# 🤖 Simple Rule-Based Chatbot

A beginner-friendly Python chatbot that uses simple if-else logic to respond to user inputs. Perfect for learning basic programming concepts!

## ✨ Features

- 💬 Interactive conversation interface
- 👋 Responds to greetings (hello, hi, hey)
- 🤔 Answers "how are you" questions
- 👋 Says goodbye when you leave
- ❓ Built-in help command
- 🔄 Continuous conversation loop

## 🎯 Learning Objectives

This project demonstrates key programming concepts:
- **if-elif-else** statements for decision making
- **Functions** to organize code
- **Loops** for continuous operation
- **Input/Output** handling
- **String manipulation** (lower(), strip())

## 📋 Prerequisites

- Python 3.x installed on your computer
- Basic understanding of Python (helpful but not required!)

## 🚀 Getting Started

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/simple-chatbot.git
cd simple-chatbot
```

2. No additional packages needed! This chatbot uses only Python standard library.

### Running the Chatbot

Simply run the Python file:
```bash
python chatbot.py
```

## 💻 Usage

### Example Conversation

```
🤖 SIMPLE CHATBOT
==================================================
Type 'bye' to exit the chat

You: hello
Bot: Hi! How can I help you today?

You: how are you
Bot: I'm fine, thanks! How about you?

You: who are you
Bot: I'm a simple chatbot created to assist you!

You: help
Bot: You can say: hello, how are you, bye, or ask me my name!

You: bye
Bot: Goodbye! Have a great day!
```

## 🗣️ Supported Commands

| User Input | Bot Response |
|------------|--------------|
| hello, hi, hey | Hi! How can I help you today? |
| how are you | I'm fine, thanks! How about you? |
| bye, goodbye | Goodbye! Have a great day! |
| your name, who are you | I'm a simple chatbot created to assist you! |
| help | You can say: hello, how are you, bye, or ask me my name! |
| anything else | I'm sorry, I don't understand that. Try saying 'help' for options! |

## 📂 Project Structure

```
simple-chatbot/
│
├── chatbot.py          # Main chatbot program
├── README.md           # Project documentation
└── LICENSE             # MIT License (optional)
```

## 🔧 How It Works

The chatbot uses a simple rule-based system:

1. **User Input**: Takes text input from the user
2. **Processing**: Converts input to lowercase and checks for keywords
3. **Matching**: Uses if-elif-else statements to match patterns
4. **Response**: Returns predefined responses based on matches
5. **Loop**: Continues conversation until user says goodbye

### Code Structure

```python
def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    
    if "hello" in user_input:
        return greet()
    elif "how are you" in user_input:
        return check_wellbeing()
    # ... more conditions
```

## 🎨 Customization

### Adding New Responses

You can easily add more responses by editing the `get_bot_response()` function:

```python
# Add this to the function
elif "your favorite color" in user_input:
    return "I like all colors!"
```

### Creating New Functions

Add specialized response functions:

```python
def tell_joke():
    """Function to tell a joke"""
    return "Why did the Python programmer not respond to the question? Because they didn't get the input()!"
```

## 🚀 Enhancement Ideas

Want to make the chatbot better? Try these:

- [ ] Add more conversation patterns
- [ ] Remember user's name
- [ ] Tell jokes or fun facts
- [ ] Add time-based greetings (Good morning/evening)
- [ ] Store conversation history
- [ ] Add emoji support
- [ ] Create a GUI interface with Tkinter
- [ ] Integrate with AI APIs for smarter responses

## 🐛 Troubleshooting

**Problem**: Chatbot doesn't understand my input  
**Solution**: Check the supported commands with the 'help' command. The chatbot uses keyword matching, so try using simpler phrases.

**Problem**: Program exits immediately  
**Solution**: Make sure you're running the script with Python 3 and that the file is not corrupted.

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Learning Resources

New to Python? Check out these resources:
- [Python Official Documentation](https://docs.python.org/3/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)

## 👤 Author

K Yuvaakash

GitHub: https://github.com/yuvaakash1610

Linked In: www.linkedin.com/in/yuvaakash-kannan-450751360

## 🌟 Acknowledgments

- Thanks to the Python community for inspiration
- Built as a learning project for beginners
- Perfect for understanding basic chatbot logic

## 📊 Version History

* **v1.0.0** (2024)
    - Initial release
    - Basic greeting and farewell functionality
    - Help command
    - Continuous conversation loop

## 💡 FAQ

**Q: Can this chatbot learn from conversations?**  
A: No, this is a rule-based chatbot. It doesn't learn or store information. For learning chatbots, look into machine learning and NLP.

**Q: Can I use this for commercial purposes?**  
A: Yes, under the MIT License, you're free to use it however you like!

**Q: How do I make it smarter?**  
A: Consider integrating APIs like OpenAI GPT, Google Dialogflow, or IBM Watson for more intelligent responses.

---

⭐ If you found this project helpful, please give it a star on GitHub!

📫 Questions? Open an issue or reach out!
