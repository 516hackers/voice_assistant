import threading
import re
from voice_engine import VoiceEngine
from brain import AIBrain
from command_handler import CommandHandler
from personality import Personality

class VoiceAssistant:
    def __init__(self):
        self.voice_engine = VoiceEngine()
        self.ai_brain = AIBrain()
        self.command_handler = CommandHandler()
        self.personality = Personality()
        self.is_running = False
        
    def process_input(self, text):
        """Process user input and respond naturally"""
        if not text or len(text.strip()) < 2:
            return
        
        print(f"💭 Processing: {text}")
        
        # Get AI response
        response = self.ai_brain.process_query(text)
        
        # Execute any system commands
        command_response = self._execute_commands(text)
        if command_response:
            response = command_response
        
        # Speak the response
        self.voice_engine.speak(response)
        
        # Check for exit conditions
        if any(word in text for word in ['exit', 'quit', 'stop', 'bye', 'خروج', 'روکو', 'الوداع']):
            self.stop()
    
    def _execute_commands(self, text):
        """Execute system commands from natural language"""
        text_lower = text.lower()
        
        # Opening applications
        open_match = re.search(r'(?:open|start|launch|run|kholo|کھولو)\s+(.+)', text_lower)
        if open_match:
            app_name = open_match.group(1).strip()
            success, response = self.command_handler.execute_command("open_app", app_name)
            return response
        
        # Opening websites
        website_match = re.search(r'(?:open|go to|visit|kholo|کھولو)\s+(?:website|site|web)?\s*(.+)', text_lower)
        if website_match:
            site_name = website_match.group(1).strip()
            success, response = self.command_handler.execute_command("open_website", site_name)
            return response
        
        # Volume control
        if any(word in text_lower for word in ['volume up', 'increase volume', 'awaz barhao', 'آواز بڑھاؤ']):
            success, response = self.command_handler.execute_command("volume_up")
            return response
        
        if any(word in text_lower for word in ['volume down', 'decrease volume', 'awaz ghatao', 'آواز گھٹاؤ']):
            success, response = self.command_handler.execute_command("volume_down")
            return response
        
        if any(word in text_lower for word in ['mute', 'silent', 'khamosh', 'خاموش']):
            success, response = self.command_handler.execute_command("volume_mute")
            return response
        
        # Screenshot
        if any(word in text_lower for word in ['screenshot', 'screen shot', 'سکرین شاٹ']):
            success, response = self.command_handler.execute_command("screenshot")
            return response
        
        # Typing
        type_match = re.search(r'type\s+(.+)', text_lower)
        if type_match:
            text_to_type = type_match.group(1).strip()
            success, response = self.command_handler.execute_command("type_text", text_to_type)
            return response
        
        return None
    
    def run(self):
        """Main assistant loop with continuous listening"""
        self.is_running = True
        
        # Welcome message
        self.voice_engine.speak(self.ai_brain.language_manager.get_text("activated"))
        
        # Start continuous listening
        listen_thread = threading.Thread(target=self.voice_engine.continuous_listen, args=(self.process_input,))
        listen_thread.daemon = True
        listen_thread.start()
        
        print("🎯 Assistant is now actively listening. Speak naturally!")
        
        # Keep main thread alive
        try:
            while self.is_running:
                threading.Event().wait(1)
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """Stop the assistant gracefully"""
        self.is_running = False
        self.voice_engine.stop_listening()
        farewell = self.personality.get_farewell()
        self.voice_engine.speak(farewell)
        print("\n👋 Assistant stopped.")
