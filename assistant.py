from voice_engine import VoiceEngine
from brain import AIBrain
from command_handler import CommandHandler
from config import WAKE_WORD

class VoiceAssistant:
    def __init__(self):
        self.voice_engine = VoiceEngine()
        self.ai_brain = AIBrain()
        self.command_handler = CommandHandler()
        self.is_listening = False
    
    def process_command(self, command):
        """Process voice commands and decide action"""
        if not command or command == "unknown":
            return "I didn't catch that. Could you please repeat?"
        
        # System control commands
        if "open" in command:
            app_name = command.replace("open", "").strip()
            if "website" in command or "web" in command:
                site_name = command.replace("open", "").replace("website", "").replace("web", "").strip()
                success, response = self.command_handler.execute_command("open_website", site_name)
                return response
            else:
                success, response = self.command_handler.execute_command("open_app", app_name)
                return response
        
        elif "volume up" in command:
            success, response = self.command_handler.execute_command("volume_up")
            return response
        
        elif "volume down" in command:
            success, response = self.command_handler.execute_command("volume_down")
            return response
        
        elif "mute" in command:
            success, response = self.command_handler.execute_command("volume_mute")
            return response
        
        elif "screenshot" in command:
            success, response = self.command_handler.execute_command("screenshot")
            return response
        
        elif "type" in command:
            text = command.replace("type", "").strip()
            success, response = self.command_handler.execute_command("type_text", text)
            return response
        
        elif "scroll up" in command:
            success, response = self.command_handler.execute_command("scroll_up")
            return response
        
        elif "scroll down" in command:
            success, response = self.command_handler.execute_command("scroll_down")
            return response
        
        elif "close" in command and "window" in command:
            success, response = self.command_handler.execute_command("close_window")
            return response
        
        elif "shutdown" in command or "turn off" in command:
            success, response = self.command_handler.execute_command("shutdown")
            return response
        
        elif "exit" in command or "quit" in command or "stop" in command:
            self.is_listening = False
            return "Goodbye! Have a great day!"
        
        else:
            # Use AI brain for conversational responses
            return self.ai_brain.process_query(command)
    
    def run(self):
        """Main assistant loop"""
        self.voice_engine.speak("Voice assistant activated. Say 'assistant' to wake me up!")
        self.is_listening = True
        
        while self.is_listening:
            # Listen for wake word
            wake_text = self.voice_engine.listen_for_wake_word()
            
            if WAKE_WORD in wake_text:
                self.voice_engine.speak("Yes? I'm listening...")
                
                # Listen for command
                command = self.voice_engine.listen_for_command()
                
                if command:
                    # Process the command
                    response = self.process_command(command)
                    self.voice_engine.speak(response)
                    
                    # Check if we should exit
                    if not self.is_listening:
                        break
