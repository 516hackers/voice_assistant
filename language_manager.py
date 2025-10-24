class LanguageManager:
    def __init__(self):
        self.current_language = "english"
        self.translations = {
            "english": {
                "wake_word": "buddy",
                "greetings": ["Hello!", "Hi there!", "Hey!"],
                "listening": "Yes? I'm listening...",
                "not_understood": "I didn't understand that. Could you please repeat?",
                "goodbye": "Goodbye! Have a great day!",
                "activated": "Voice assistant activated. Say 'Buddy' to wake me up!",
                "listening_for_wake": "Listening for wake word...",
                "listening_for_command": "Listening for command...",
                "opening": "Opening",
                "volume_up": "Volume increased",
                "volume_down": "Volume decreased",
                "volume_mute": "Volume muted",
                "screenshot": "Screenshot taken and saved",
                "closing_window": "Closing current window",
                "shutting_down": "Shutting down in 5 seconds",
                "scrolled_up": "Scrolled up",
                "scrolled_down": "Scrolled down",
                "typing": "Typing: {}",
                "capabilities": [
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
            },
            "urdu": {
                "wake_word": "buddy",
                "greetings": ["ہیلو!", "اسلام علیکم!", "آداب!"],
                "listening": "جی میں سن رہا ہوں...",
                "not_understood": "میں سمجھا نہیں۔ براہ کرم دہرائیں۔",
                "goodbye": "الوداع! آپ کا دن اچھا گزرے!",
                "activated": "وائس اسسٹنٹ فعال ہو گیا۔ 'بڈی' کہہ کر مجھے جگائیں!",
                "listening_for_wake": "جگانے والا لفظ سن رہا ہوں...",
                "listening_for_command": "حکم سن رہا ہوں...",
                "opening": "کھول رہا ہوں",
                "volume_up": "آواز بڑھائی گئی",
                "volume_down": "آواز گھٹائی گئی", 
                "volume_mute": "آواز بند کی گئی",
                "screenshot": "سکرین شاٹ لے کر محفوظ کر لیا گیا",
                "closing_window": "موجودہ ونڈو بند کر رہا ہوں",
                "shutting_down": "5 سیکنڈ میں بند ہو رہا ہے",
                "scrolled_up": "اوپر سکرول کیا",
                "scrolled_down": "نیچے سکرول کیا",
                "typing": "ٹائپ کر رہا ہوں: {}",
                "capabilities": [
                    "میں آپ کی مدد کر سکتا ہوں:",
                    "• ایپلیکیشنز اور ویب سائٹس کھولنے میں",
                    "• سسٹم کی آواز اور ترتیبات کنٹرول کرنے میں",
                    "• وقت اور تاریخ بتانے میں",
                    "• حساب کتاب کرنے میں",
                    "• لطیفے سنانے میں", 
                    "• فائلوں اور فولڈرز کو منظم کرنے میں",
                    "• سکرین شاٹ لینے میں",
                    "• اور بہت کچھ!"
                ]
            }
        }
    
    def set_language(self, language):
        """Set current language"""
        if language in self.translations:
            self.current_language = language
            return True
        return False
    
    def get_text(self, key, format_args=None):
        """Get translated text"""
        if self.current_language in self.translations:
            if key in self.translations[self.current_language]:
                text = self.translations[self.current_language][key]
                if format_args and isinstance(text, str):
                    return text.format(*format_args)
                return text
        return key
    
    def get_wake_word(self):
        """Get wake word for current language"""
        return self.get_text("wake_word")
