import random
import datetime

class Personality:
    def __init__(self):
        self.user_name = None
        self.mood = "happy"
        self.conversation_history = []
        
    def get_greeting(self):
        """Natural human-like greetings"""
        hour = datetime.datetime.now().hour
        greetings = {
            "morning": [
                "Good morning! I hope you're starting your day well. What can I do for you?",
                "Morning! Ready to tackle the day together?",
                "Hello there! Beautiful morning, isn't it? How can I help?",
                "Rise and shine! What would you like me to do for you today?"
            ],
            "afternoon": [
                "Good afternoon! How's your day going so far?",
                "Afternoon! Need any help with your tasks?",
                "Hello! Hope you're having a productive day. What can I do for you?",
                "Hi there! How can I assist you this afternoon?"
            ],
            "evening": [
                "Good evening! How was your day?",
                "Evening! Time to relax and get things done. What do you need?",
                "Hello! Wonderful evening, isn't it? How can I help?",
                "Hi! Hope you had a great day. What would you like me to do?"
            ],
            "night": [
                "Still up? I'm here if you need anything!",
                "Working late? I'm here to help you out.",
                "Hello! Quiet night? What can I do for you?",
                "Hi there! Need some nighttime assistance?"
            ]
        }
        
        if 5 <= hour < 12:
            return random.choice(greetings["morning"])
        elif 12 <= hour < 17:
            return random.choice(greetings["afternoon"])
        elif 17 <= hour < 22:
            return random.choice(greetings["evening"])
        else:
            return random.choice(greetings["night"])
    
    def get_thanks_response(self):
        """Natural responses to thanks"""
        responses = [
            "You're most welcome! Happy to help.",
            "Anytime! That's what I'm here for.",
            "No problem at all! Let me know if you need anything else.",
            "My pleasure! Always here to assist you.",
            "You're welcome! Feel free to ask for anything.",
            "Glad I could help! What else can I do for you?"
        ]
        return random.choice(responses)
    
    def get_apology(self):
        """When something goes wrong"""
        apologies = [
            "I'm sorry, I didn't quite get that. Could you repeat?",
            "Oops, I missed that. Could you say it again?",
            "Sorry, my mind wandered for a second. What was that?",
            "I didn't catch that completely. Mind repeating?",
            "Apologies, could you say that one more time?"
        ]
        return random.choice(apologies)
    
    def get_confirmation(self):
        """Confirming actions"""
        confirmations = [
            "Sure thing!",
            "On it!",
            "Consider it done!",
            "Right away!",
            "I'm on it!",
            "Working on that now!"
        ]
        return random.choice(confirmations)
    
    def get_farewell(self):
        """Natural goodbye messages"""
        farewells = [
            "Goodbye! Take care and talk to you soon!",
            "See you later! Don't hesitate to call if you need anything!",
            "Bye for now! I'll be here when you need me!",
            "Alright then! Have a wonderful time!",
            "Until next time! It was nice talking to you!"
        ]
        return random.choice(farewells)
    
    def add_to_history(self, user_input, response):
        """Keep conversation history"""
        self.conversation_history.append({"user": user_input, "assistant": response})
        if len(self.conversation_history) > 10:  # Keep last 10 exchanges
            self.conversation_history.pop(0)
