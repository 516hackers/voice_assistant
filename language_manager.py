class LanguageManager:
    def __init__(self):
        self.current_language = "english"
        self.translations = {
            "english": {
                "wake_word": "buddy",
                "listening": "I'm listening...",
                "not_understood": "I'm sorry, I didn't quite understand that. Could you repeat?",
                "goodbye": "Goodbye! Have a great day!",
                "activated": "Hello! I'm Buddy, your personal assistant. I'm here to help you with anything you need. You can talk to me naturally - no need for special commands!",
                "thinking": "Let me think about that...",
                "ready": "I'm ready when you are!",
                "opening": "Opening",
                "volume_up": "Turning up the volume",
                "volume_down": "Turning down the volume", 
                "volume_mute": "Muting the sound",
                "screenshot": "Taking a screenshot for you",
                "closing_window": "Closing the current window",
                "shutting_down": "Shutting down the system in 5 seconds",
                "scrolled_up": "Scrolling up",
                "scrolled_down": "Scrolling down",
                "typing": "Typing that out for you",
                "searching": "Searching for that online"
            },
            "urdu": {
                "wake_word": "buddy",
                "listening": "میں سن رہی ہوں...",
                "not_understood": "معاف کیجئے گا، میں سمجھ نہیں پائی۔ کیا آپ دہرا سکتے ہیں؟",
                "goodbye": "الوداع! آپ کا دن اچھا گزرے!",
                "activated": "ہیلو! میں بڈی ہوں، آپ کی ذاتی معاون۔ میں آپ کی ہر ممکن مدد کے لیے یہاں ہوں۔ آپ مجھ سے قدرتی طور پر بات کر سکتے ہیں - کسی خاص حکم کی ضرورت نہیں!",
                "thinking": "ذرا اس کے بارے میں سوچتی ہوں...",
                "ready": "میں تیار ہوں!",
                "opening": "کھول رہی ہوں",
                "volume_up": "آواز بڑھا رہی ہوں",
                "volume_down": "آواز گھٹا رہی ہوں", 
                "volume_mute": "آواز بند کر رہی ہوں",
                "screenshot": "آپ کے لیے سکرین شاٹ لے رہی ہوں",
                "closing_window": "موجودہ ونڈو بند کر رہی ہوں",
                "shutting_down": "سسٹم 5 سیکنڈ میں بند ہو رہا ہے",
                "scrolled_up": "اوپر سکرول کر رہی ہوں",
                "scrolled_down": "نیچے سکرول کر رہی ہوں",
                "typing": "وہ ٹائپ کر رہی ہوں",
                "searching": "اسے آن لائن ڈھونڈ رہی ہوں"
            }
        }
    
    def set_language(self, language):
        if language in self.translations:
            self.current_language = language
            return True
        return False
    
    def get_text(self, key, format_args=None):
        if self.current_language in self.translations:
            if key in self.translations[self.current_language]:
                text = self.translations[self.current_language][key]
                if format_args and isinstance(text, str):
                    return text.format(*format_args)
                return text
        return key
