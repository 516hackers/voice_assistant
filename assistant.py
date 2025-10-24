import threading
from voice_engine import VoiceEngine
from brain import AIBrain
from personality import Personality

class VoiceAssistant:
    def __init__(self):
        self.voice_engine = VoiceEngine()
        self.ai_brain = AIBrain()
        self.personality = Personality()
        self.is_running = False
        
    def process_input(self, text):
        """Process user input and respond naturally"""
        if not text or len(text.strip()) < 2:
            return
        
        # Get AI response and speak it
        response = self.ai_brain.process_query(text)
        self.voice_engine.speak(response)
        
        # Check for exit conditions
        if any(word in text for word in ['exit', 'quit', 'stop', 'bye', 'goodbye']):
            self.stop()
    
    def run(self):
        """Main assistant loop with continuous listening"""
        self.is_running = True
        
        # Welcome message
        self.voice_engine.speak("Hello! I'm Buddy, your personal assistant. I'm here to help you with anything you need!")
        
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
