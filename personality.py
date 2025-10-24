import random
import datetime

class Personality:
    def __init__(self):
        self.user_name = None
        self.conversation_history = []
        
    def add_to_history(self, user_input, response):
        """Keep conversation history"""
        self.conversation_history.append({"user": user_input, "assistant": response})
        if len(self.conversation_history) > 10:
            self.conversation_history.pop(0)
        
    def get_greeting(self):
        """Natural human-like greetings"""
        hour = datetime.datetime.now().hour
        
        if 5 <= hour < 12:
            greetings = [
                "Good morning! Ready to tackle the day together?",
                "Morning sunshine! What can I help you with today?",
                "Hello there! Beautiful morning, isn't it?",
                "Rise and shine! How can I assist you?"
            ]
        elif 12 <= hour < 17:
            greetings = [
                "Good afternoon! How's your day going?",
                "Afternoon! What can I do for you?",
                "Hello! Hope you're having a productive day.",
                "Hi there! Ready to get things done?"
            ]
        elif 17 <= hour < 22:
            greetings = [
                "Good evening! How was your day?",
                "Evening! Time to relax and get things done.",
                "Hello! Wonderful evening, isn't it?",
                "Hi! Hope you had a great day."
            ]
        else:
            greetings = [
                "Still up? I'm here if you need anything!",
                "Working late? Don't worry, I'm here with you!",
                "Hello night owl! What can I do for you?",
                "Hi! Even at night, I'm here to help!"
            ]
        
        return random.choice(greetings)
    
    def get_confirmation(self, action):
        """Natural confirmations for actions"""
        confirmations = [
            f"Sure thing, {action} for you...",
            f"Got it! {action} now...",
            f"Alright, {action} for you...",
            f"On it! {action}...",
            f"Perfect! {action}...",
            f"Okay, {action}...",
            f"Right away! {action}...",
            f"Consider it done! {action}..."
        ]
        return random.choice(confirmations)
    
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
    
    def get_search_response(self, query):
        """Responses for search actions"""
        responses = [
            f"Got it! Here's what I found about {query}...",
            f"Sure! Searching for {query}...",
            f"Alright, looking up {query} for you...",
            f"On it! Searching the web for {query}..."
        ]
        return random.choice(responses)
    
    def get_music_response(self):
        """Responses for music actions"""
        responses = [
            "Perfect! Opening some relaxing music for you 🎶",
            "Great choice! Playing music for you...",
            "Awesome! Let me play some tunes for you 🎵",
            "Sure thing! Starting some music for you..."
        ]
        return random.choice(responses)
