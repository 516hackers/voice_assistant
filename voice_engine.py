import speech_recognition as sr
import pyttsx3
import threading
import time
from config import *

class VoiceEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.tts_engine = pyttsx3.init()
        self.is_listening = False
        self.current_text = ""
        self.setup_voice()
    
    def setup_voice(self):
        """Configure natural female voice"""
        voices = self.tts_engine.getProperty('voices')
        # Try to find a natural female voice
        for voice in voices:
            if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                self.tts_engine.setProperty('voice', voice.id)
                break
        else:
            # Fallback to any available voice
            if len(voices) > 1:
                self.tts_engine.setProperty('voice', voices[1].id)
        
        self.tts_engine.setProperty('rate', SPEECH_RATE)
        self.tts_engine.setProperty('volume', VOLUME)
    
    def speak(self, text):
        """Convert text to speech with natural pacing"""
        print(f"🤖 Buddy: {text}")
        # Add small delay for natural conversation flow
        time.sleep(0.3)
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
    
    def continuous_listen(self, callback):
        """Continuously listen for speech"""
        self.is_listening = True
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("🎯 I'm always listening. Just speak naturally...")
            
            while self.is_listening:
                try:
                    # Listen with no timeout for continuous listening
                    audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=5)
                    text = self.recognizer.recognize_google(audio).lower()
                    print(f"👤 You: {text}")
                    callback(text)
                    
                except sr.WaitTimeoutError:
                    continue
                except sr.UnknownValueError:
                    # Don't announce failure, just continue listening
                    continue
                except sr.RequestError as e:
                    print(f"Speech recognition error: {e}")
                    continue
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    continue
    
    def stop_listening(self):
        """Stop continuous listening"""
        self.is_listening = False
