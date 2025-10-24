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
    
    def set_language(self, language):
        """Set language for all components"""
        self.voice_engine.set_language(language)
        self.ai_brain.set_language(language)
        self.command_handler.set_language(language)
    
    def process_command(self, command):
        """Process voice commands and decide action"""
        if not command or command == "unknown":
            return self.voice_engine.language_manager.get_text("not_understood")
        
        # Language switching
        if "urdu" in command or "اردو" in command:
            self.set_language("urdu")
            return "زباز تبدیل کر دی گئی ہے۔ اب میں اردو میں بات کروں گا۔"
        
        elif "english" in command or "انگریزی" in command:
            self.set_language("english") 
            return "Language changed to English. I will now speak in English."
        
        # System control commands
        if "open" in command or "کھولو" in command:
            if "website" in command or "web" in command or "ویب سائٹ" in command:
                site_name = command.replace("open", "").replace("website", "").replace("web", "").replace("کھولو", "").replace("ویب سائٹ", "").strip()
                success, response = self.command_handler.execute_command("open_website", site_name)
                return response
            else:
                app_name = command.replace("open", "").replace("کھولو", "").strip()
                success, response = self.command_handler.execute_command("open_app", app_name)
                return response
        
        elif "volume up" in command or "آواز بڑھاؤ" in command:
            success, response = self.command_handler.execute_command("volume_up")
            return response
        
        elif "volume down" in command or "آواز گھٹاؤ" in command:
            success, response = self.command_handler.execute_command("volume_down")
            return response
        
        elif "mute" in command or "خاموش" in command:
            success, response = self.command_handler.execute_command("volume_mute")
            return response
        
        elif "screenshot" in command or "سکرین شاٹ" in command:
            success, response = self.command_handler.execute_command("screenshot")
            return response
        
        elif "type" in command or "ٹائپ" in command:
            text = command.replace("type", "").replace("ٹائپ", "").strip()
            success, response = self.command_handler.execute_command("type_text", text)
            return response
        
        elif "scroll up" in command or "اوپر سکرول" in command:
            success, response = self.command_handler.execute_command("scroll_up")
            return response
        
        elif "scroll down" in command or "نیچے سکرول" in command:
            success, response = self.command_handler.execute_command("scroll_down")
            return response
        
        elif "close" in command and "window" in command or "بند کرو" in command:
            success, response = self.command_handler.execute_command("close_window")
            return response
        
        elif "shutdown" in command or "turn off" in command or "بند کرو" in command:
            success, response = self.command_handler.execute_command("shutdown")
            return response
        
        elif "exit" in command or "quit" in command or "stop" in command or "روکو" in command:
            self.is_listening = False
            return self.voice_engine.language_manager.get_text("goodbye")
        
        else:
            # Use AI brain for conversational responses
            return self.ai_brain.process_query(command)
    
    def run(self):
        """Main assistant loop"""
        self.voice_engine.speak(self.voice_engine.language_manager.get_text("activated"))
        self.is_listening = True
        
        while self.is_listening:
            # Listen for wake word or direct commands
            wake_text = self.voice_engine.listen_for_wake_word()
            
            # Improved wake word detection with variations
            wake_words = ['buddy', 'body', 'badi', 'بڈی', 'بدی']
            wake_word_detected = any(wake_word in wake_text for wake_word in wake_words)
            
            # Also respond to direct greetings
            greetings = ['hello', 'hi', 'hey', 'ہیلو', 'اسلام علیکم', 'آداب']
            direct_greeting = any(greeting in wake_text for greeting in greetings)
            
            if wake_word_detected or direct_greeting:
                if wake_word_detected:
                    self.voice_engine.speak(self.voice_engine.language_manager.get_text("listening"))
                else:
                    # If user directly greeted, respond and continue listening
                    response = self.ai_brain.process_query(wake_text)
                    self.voice_engine.speak(response)
                    continue
                
                # Listen for command after wake word
                command = self.voice_engine.listen_for_command()
                
                if command:
                    # Process the command
                    response = self.process_command(command)
                    self.voice_engine.speak(response)
                    
                    # Check if we should exit
                    if not self.is_listening:
                        break
