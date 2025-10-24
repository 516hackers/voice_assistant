import datetime
import random

class AIBrain:
    def __init__(self):
        self.conversation_context = {}
        self.learned_commands = {}
        self.user_preferences = {}
    
    def process_query(self, query, context=None):
        """Main AI processing logic - completely custom"""
        query = query.lower().strip()
        
        # Store context for follow-up questions
        if context:
            self.conversation_context.update(context)
        
        # Greetings and basic interaction
        if any(word in query for word in ['hello', 'hi', 'hey', 'howdy']):
            return self._generate_greeting()
        
        elif any(word in query for word in ['time', 'current time']):
            return self._get_current_time()
        
        elif any(word in query for word in ['date', 'today', 'current date']):
            return self._get_current_date()
        
        elif any(word in query for word in ['thank', 'thanks']):
            return self._generate_thanks_response()
        
        elif any(word in query for word in ['how are you', 'how you doing']):
            return self._generate_mood_response()
        
        elif any(word in query for word in ['what can you do', 'your capabilities']):
            return self._list_capabilities()
        
        elif any(word in query for word in ['joke', 'tell joke', 'make me laugh']):
            return self._tell_joke()
        
        elif any(word in query for word in ['calculate', 'math', 'what is']):
            return self._simple_calculation(query)
        
        elif any(word in query for word to ['who are you', 'your name', 'introduce yourself']):
            return self._introduce_self()
        
        elif any(word in query for word in ['weather', 'temperature']):
            return self._respond_to_weather_query()
        
        elif any(word in query for word in ['remember that', 'remember this']):
            return self._remember_information(query)
        
        elif any(word in query for word in ['what did i say', 'recall that']):
            return self._recall_information()
        
        else:
            return self._handle_unknown_query(query)
    
    def _generate_greeting(self):
        """Generate contextual greeting"""
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            greeting = "Good morning!"
        elif 12 <= hour < 18:
            greeting = "Good afternoon!"
        else:
            greeting = "Good evening!"
        
        responses = [
            f"{greeting} How can I assist you today?",
            f"{greeting} What can I do for you?",
            f"{greeting} I'm here to help!"
        ]
        return random.choice(responses)
    
    def _get_current_time(self):
        """Get current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"
    
    def _get_current_date(self):
        """Get current date"""
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}"
    
    def _generate_thanks_response(self):
        """Respond to thanks"""
        responses = [
            "You're welcome!",
            "Happy to help!",
            "Anytime!",
            "Glad I could assist you!"
        ]
        return random.choice(responses)
    
    def _generate_mood_response(self):
        """Respond to how are you"""
        moods = [
            "I'm functioning optimally, thank you for asking!",
            "I'm doing great! Ready to help you.",
            "All systems are operational! How can I assist you?",
            "I'm running smoothly today!"
        ]
        return random.choice(moods)
    
    def _list_capabilities(self):
        """List what the assistant can do"""
        capabilities = [
            "I can help you with:",
            "• Opening applications and websites",
            "• Controlling system volume and settings",
            "• Telling time and date",
            "• Performing calculations",
            "• Telling jokes",
            "• Managing files and folders",
            "• Taking screenshots",
            "• And much more!"
        ]
        return "\n".join(capabilities)
    
    def _tell_joke(self):
        """Tell a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a fake noodle? An impasta!",
            "Why did the math book look so sad? Because it had too many problems!"
        ]
        return random.choice(jokes)
    
    def _simple_calculation(self, query):
        """Perform simple math calculations"""
        try:
            # Extract numbers and operation
            if 'plus' in query or '+' in query:
                numbers = [int(s) for s in query.split() if s.isdigit()]
                if len(numbers) >= 2:
                    result = sum(numbers)
                    return f"The answer is {result}"
            
            elif 'minus' in query or '-' in query:
                numbers = [int(s) for s in query.split() if s.isdigit()]
                if len(numbers) >= 2:
                    result = numbers[0] - sum(numbers[1:])
                    return f"The answer is {result}"
            
            elif 'multiply' in query or 'times' in query or '*' in query:
                numbers = [int(s) for s in query.split() if s.isdigit()]
                if len(numbers) >= 2:
                    result = 1
                    for num in numbers:
                        result *= num
                    return f"The answer is {result}"
            
            return "I can help with basic addition, subtraction, and multiplication. Try saying 'calculate 5 plus 3'"
        
        except:
            return "Sorry, I couldn't calculate that. Please try again with simple numbers."
    
    def _introduce_self(self):
        """Introduce the assistant"""
        return "I'm your custom AI assistant! I'm built with pure Python to help you control your system and answer questions. I don't rely on external APIs - everything I do is programmed directly!"
    
    def _respond_to_weather_query(self):
        """Respond to weather queries"""
        responses = [
            "I don't have real-time weather data, but I recommend checking a weather website for accurate information.",
            "For current weather conditions, you might want to check your local weather service.",
            "I'm not connected to weather services, but I can help you open a weather website!"
        ]
        return random.choice(responses)
    
    def _remember_information(self, query):
        """Remember user information"""
        # Extract information to remember
        info = query.replace('remember that', '').replace('remember this', '').strip()
        if info:
            self.user_preferences['last_remembered'] = info
            return f"I'll remember that: {info}"
        return "What would you like me to remember?"
    
    def _recall_information(self):
        """Recall remembered information"""
        if 'last_remembered' in self.user_preferences:
            return f"You told me: {self.user_preferences['last_remembered']}"
        return "I don't have anything remembered yet. Tell me something with 'remember that'."
    
    def _handle_unknown_query(self, query):
        """Handle queries the AI doesn't understand"""
        responses = [
            f"I'm not sure how to help with '{query}'. Could you rephrase that?",
            f"I don't understand '{query}'. Try asking me to open something, calculate, or tell you a joke.",
            f"Sorry, I'm still learning. I didn't understand '{query}'.",
            f"Could you explain '{query}' differently? I want to help!"
        ]
        return random.choice(responses)
