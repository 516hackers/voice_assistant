import datetime
import random
import re
from command_executor import CommandExecutor
from personality import Personality

class AIBrain:
    def __init__(self):
        self.command_executor = CommandExecutor()
        self.personality = Personality()
        self.conversation_context = {}
        
    def process_query(self, query):
        """Main AI processing with natural language understanding"""
        query = query.lower().strip()
        
        # Store conversation context
        self.personality.add_to_history(query, "")
        
        print(f"🔍 Analyzing: '{query}'")
        
        # Extract intent and execute commands
        response = self._understand_and_execute(query)
        
        # Store response in history
        self.personality.add_to_history(query, response)
        return response
    
    def _understand_and_execute(self, query):
        """Understand natural language and execute appropriate commands"""
        
        # GREETINGS AND BASIC CONVERSATION
        if any(word in query for word in ['hello', 'hi', 'hey']):
            return self.personality.get_greeting()
        
        if any(phrase in query for phrase in ['how are you', 'how you doing']):
            return "I'm doing great! Ready to help you with anything. What's on your mind?"
        
        if any(word in query for word in ['thank', 'thanks']):
            return self.personality.get_thanks_response()
        
        # OPENING APPLICATIONS
        open_patterns = [
            r'(?:open|start|launch)\s+(.+)',
            r'(?:can you|please)\s+open\s+(.+)',
            r'(?:i want to|i need to)\s+open\s+(.+)'
        ]
        
        for pattern in open_patterns:
            match = re.search(pattern, query)
            if match:
                app_name = match.group(1).strip()
                success, action = self.command_executor.execute_command("open_app", app_name)
                return self.personality.get_confirmation(action) if success else action
        
        # SEARCHING
        search_patterns = [
            r'search\s+(?:for\s+)?(.+)',
            r'look up\s+(.+)',
            r'find\s+(.+)',
            r'google\s+(.+)'
        ]
        
        for pattern in search_patterns:
            match = re.search(pattern, query)
            if match:
                search_query = match.group(1).strip()
                success, action = self.command_executor.execute_command("search", search_query)
                return self.personality.get_search_response(search_query) if success else action
        
        # PLAYING MUSIC
        music_patterns = [
            r'play\s+(.+)',
            r'play\s+(?:some|me)\s+(.+)',
            r'start\s+(?:some|the)\s+music',
            r'put on\s+(?:some|some\s+)?music'
        ]
        
        for pattern in music_patterns:
            match = re.search(pattern, query)
            if match:
                music_query = match.group(1).strip() if match.groups() else None
                success, action = self.command_executor.execute_command("play_music", music_query)
                return self.personality.get_music_response() if success else action
        
        # WEBSITES
        website_patterns = [
            r'open\s+(?:website\s+)?(.+)',
            r'go to\s+(.+)',
            r'visit\s+(.+)'
        ]
        
        for pattern in website_patterns:
            match = re.search(pattern, query)
            if match:
                website = match.group(1).strip()
                success, action = self.command_executor.execute_command("open_website", website)
                return self.personality.get_confirmation(action) if success else action
        
        # NOTES AND REMINDERS
        note_patterns = [
            r'write\s+(?:a\s+)?note\s+(.+)',
            r'remember\s+that\s+(.+)',
            r'create\s+(?:a\s+)?reminder\s+(.+)',
            r'note\s+down\s+(.+)'
        ]
        
        for pattern in note_patterns:
            match = re.search(pattern, query)
            if match:
                note = match.group(1).strip()
                success, action = self.command_executor.execute_command("write_note", note)
                return self.personality.get_confirmation("note saved") if success else action
        
        # TIME AND DATE
        if any(word in query for word in ['time', 'current time']):
            success, action = self.command_executor.execute_command("system_info")
            return action if success else "I couldn't get the system information"
        
        if any(word in query for word in ['date', 'today', 'what day']):
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            return f"Today is {current_date}"
        
        # JOKES
        if any(word in query for word in ['joke', 'make me laugh', 'tell me something funny']):
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "I told my wife she was drawing her eyebrows too high. She looked surprised!",
                "Why don't eggs tell jokes? They'd crack each other up!",
                "What do you call a fake noodle? An impasta!",
                "Why did the scarecrow win an award? He was outstanding in his field!"
            ]
            return random.choice(jokes)
        
        # WHAT CAN YOU DO
        if any(phrase in query for phrase in ['what can you do', 'your capabilities', 'help me']):
            capabilities = [
                "I can open applications like Chrome, VS Code, Notepad, and more",
                "I can search the web for anything you need",
                "I can play music on YouTube",
                "I can open websites and files",
                "I can write notes and reminders for you", 
                "I can tell you the time, date, and system information",
                "I can run scripts and commands",
                "I can tell jokes and have conversations",
                "Basically, I'm here to help with almost anything on your computer!"
            ]
            return "Here's what I can do for you: " + ". ".join(capabilities)
        
        # If no specific command matched
        return self._provide_helpful_response(query)
    
    def _provide_helpful_response(self, query):
        """Provide helpful responses for unrecognized queries"""
        
        if any(word in query for word in ['what', 'why', 'how', 'when']):
            return "That's an interesting question! I'm better at helping with tasks than answering complex questions. Is there something I can do for you?"
        
        elif any(word in query for word in ['can you', 'could you']):
            return "I'd love to help! Could you be more specific about what you'd like me to do?"
        
        else:
            responses = [
                "I understand. What would you like me to help you with?",
                "Got it! How can I assist you with that?",
                "I hear you. What action would you like me to take?",
                "Noted! Is there something specific you'd like me to do?",
                "I'm here to help! What would you like me to do next?"
            ]
            return random.choice(responses)
