import speech_recognition as sr
import pyttsx3
from config import WAKE_WORD, LANGUAGE, LISTEN_TIMEOUT, COMMAND_TIMEOUT
from language_manager import LanguageManager

class VoiceEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.tts_engine = pyttsx3.init()
        self.language_manager = LanguageManager()
        self.setup_voice()
    
    def setup_voice(self):
        """Configure text-to-speech settings"""
        voices = self.tts_engine.getProperty('voices')
        # Use available voices (index might vary by system)
        if len(voices) > 1:
            self.tts_engine.setProperty('voice', voices[1].id)  # Female voice
        self.tts_engine.setProperty('rate', 150)
        self.tts_engine.setProperty('volume', 0.8)
    
    def set_language(self, language):
        """Set language for voice engine"""
        return self.language_manager.set_language(language)
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"🤖 Buddy: {text}")
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
    
    def listen_for_wake_word(self):
        """Continuously listen for the wake word"""
        with self.microphone as source:
            print(self.language_manager.get_text("listening_for_wake"))
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            try:
                audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=3)
                text = self.recognizer.recognize_google(audio).lower()
                print(f"👤 You said: {text}")
                return text
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                return ""
            except sr.RequestError as e:
                print(f"Speech recognition error: {e}")
                return ""
    
    def listen_for_command(self):
        """Listen for command after wake word"""
        with self.microphone as source:
            print(self.language_manager.get_text("listening_for_command"))
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            try:
                audio = self.recognizer.listen(source, timeout=COMMAND_TIMEOUT, phrase_time_limit=COMMAND_TIMEOUT)
                command = self.recognizer.recognize_google(audio).lower()
                print(f"💬 Command: {command}")
                return command
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                return "unknown"
            except sr.RequestError as e:
                print(f"Speech recognition error: {e}")
                return "error"
