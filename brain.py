import datetime
import random
import re
from language_manager import LanguageManager
from personality import Personality

class AIBrain:
    def __init__(self):
        self.language_manager = LanguageManager()
        self.personality = Personality()
        self.conversation_context = {}
        self.user_preferences = {}
        
    def set_language(self, language):
        return self.language_manager.set_language(language)
    
    def process_query(self, query):
        """Main AI processing with natural language understanding"""
        query = query.lower().strip()
        
        # Store conversation context
        self.personality.add_to_history(query, "")
        
        # Language detection and switching
        lang_response = self._detect_and_switch_language(query)
        if lang_response:
            return lang_response
        
        # Natural conversation patterns
        response = self._handle_natural_conversation(query)
        if response:
            return response
        
        # System commands with natural language
        response = self._handle_system_commands(query)
        if response:
            return response
        
        # If nothing matched, provide helpful response
        return self._provide_helpful_response(query)
    
    def _detect_and_switch_language(self, query):
        """Detect and switch languages based on input"""
        urdu_keywords = ['ہیلو', 'اسلام', 'کیا', 'کیسے', 'ہے', 'ہوں', 'تم', 'آپ', 'شکریہ', 'براہ', 'کرم', 'مدد']
        english_keywords = ['hello', 'hi', 'how', 'what', 'when', 'where', 'why', 'help', 'thanks', 'thank']
        
        urdu_count = sum(1 for word in urdu_keywords if word in query)
        english_count = sum(1 for word in english_keywords if word in query)
        
        # Language switching commands
        if any(word in query for word in ['urdu', 'اردو', 'urdu mein', 'urdu main']):
            self.set_language("urdu")
            return "زباز تبدیل کر دی گئی ہے۔ اب میں اردو میں بات کروں گی۔"
        
        elif any(word in query for word in ['english', 'انگریزی', 'english mein', 'english main']):
            self.set_language("english")
            return "Language changed to English. I'll speak in English now."
        
        # Auto-detect language
        if urdu_count > english_count and self.language_manager.current_language != "urdu":
            self.set_language("urdu")
            return "میں نے محسوس کیا آپ اردو بول رہے ہیں۔ اب میں اردو میں جواب دوں گی۔"
        
        return None
    
    def _handle_natural_conversation(self, query):
        """Handle natural human conversation"""
        # Greetings
        if any(word in query for word in ['hello', 'hi', 'hey', 'ہیلو', 'اسلام', 'آداب']):
            return self.personality.get_greeting()
        
        # Thanks
        if any(word in query for word in ['thank', 'thanks', 'shukriya', 'شکریہ']):
            return self.personality.get_thanks_response()
        
        # How are you
        if any(word in query for word in ['how are you', 'how you doing', 'کیا حال ہے', 'آپ کیسے ہیں']):
            responses = [
                "I'm doing wonderful, thank you for asking! How about you?",
                "I'm great! Just here and ready to help you. How are you doing?",
                "Doing well, thanks! What's on your mind?",
                "میں ٹھیک ہوں، شکریہ! آپ کیسے ہیں؟",
                "بہت اچھی، آپ کا شکریہ! آپ سُنائیں؟"
            ]
            return random.choice(responses)
        
        # Time queries
        if any(word in query for word in ['time', 'وقت', 'kitna bajaa', 'کٹنا بجا']):
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            if self.language_manager.current_language == "urdu":
                return f"اب وقت ہے {current_time}"
            else:
                return f"The current time is {current_time}"
        
        # Date queries
        if any(word in query for word in ['date', 'today', 'تاریخ', 'aaj', 'آج']):
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            if self.language_manager.current_language == "urdu":
                return f"آج کی تاریخ ہے {current_date}"
            else:
                return f"Today is {current_date}"
        
        # Jokes
        if any(word in query for word in ['joke', 'funny', 'laugh', 'چٹکلہ', 'لطیفہ', 'ہنساؤ']):
            return self._tell_joke()
        
        # Personal questions
        if any(word in query for word in ['who are you', 'your name', 'تم کون ہو', 'آپ کا نام']):
            return self._introduce_self()
        
        # Weather
        if any(word in query for word in ['weather', 'موسم', 'temperature', 'درجہ حرارت']):
            return self._respond_to_weather_query()
        
        return None
    
    def _handle_system_commands(self, query):
        """Handle system commands in natural language"""
        # Opening applications
        open_patterns = [
            r'(?:open|start|launch|run|kholo|کھولو)\s+(.+)',
            r'(?:chal|چل)\s+(.+)',
            r'(?:please|براہ کرم)\s+(?:open|kholo|کھولو)\s+(.+)'
        ]
        
        for pattern in open_patterns:
            match = re.search(pattern, query)
            if match:
                app_name = match.group(1).strip()
                return f"I'll open {app_name} for you"
        
        # Volume control
        if any(word in query for word in ['volume up', 'increase volume', 'awaz barhao', 'آواز بڑھاؤ']):
            return self.language_manager.get_text("volume_up")
        
        if any(word in query for word in ['volume down', 'decrease volume', 'awaz ghatao', 'آواز گھٹاؤ']):
            return self.language_manager.get_text("volume_down")
        
        if any(word in query for word in ['mute', 'silent', 'khamosh', 'خاموش']):
            return self.language_manager.get_text("volume_mute")
        
        # Screenshot
        if any(word in query for word in ['screenshot', 'screen shot', 'screnshot', 'سکرین شاٹ']):
            return self.language_manager.get_text("screenshot")
        
        # Typing
        if 'type' in query or 'type karo' in query or 'ٹائپ' in query:
            text_to_type = query.replace('type', '').replace('type karo', '').replace('ٹائپ', '').strip()
            if text_to_type:
                return f"I'll type: {text_to_type}"
        
        return None
    
    def _tell_joke(self):
        """Tell contextually appropriate jokes"""
        if self.language_manager.current_language == "urdu":
            jokes = [
                "کیا آپ جانتے ہیں کمپیوٹرز کیوں ڈرتے ہیں؟ کیونکہ ان کے وائرس ہوتے ہیں!",
                "ایک استاد نے پوچھا: بیٹا، 2 اور 2 کیا ہوتے ہیں؟ بچہ بولا: جناب، 4! استاد: شاباش! بچہ: اور 4 اور 4؟ استاد: 8! بچہ: اور 8 اور 8؟ استاد: 16! بچہ: اور 16 اور 16؟ استاد: 32! بچہ: اور 32 اور 32؟ استاد: بس کر! تمہیں پتہ ہے میں کون ہوں؟ بچہ: جناب، آپ کیلکولیٹر ہیں!",
                "ایک آدمی ڈاکٹر کے پاس گیا اور کہا: ڈاکٹر صاحب، میں سوچتا بہت زیادہ ہوں۔ ڈاکٹر بولا: کوئی بات نہیں، آپ کی یہ بیماری بھی جلد ختم ہو جائے گی!"
            ]
        else:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "I told my wife she was drawing her eyebrows too high. She looked surprised!",
                "Why don't eggs tell jokes? They'd crack each other up!",
                "What do you call a fake noodle? An impasta!",
                "I'm reading a book about anti-gravity. It's impossible to put down!"
            ]
        return random.choice(jokes)
    
    def _introduce_self(self):
        """Natural self-introduction"""
        if self.language_manager.current_language == "urdu":
            return "میں بڈی ہوں، آپ کی ذاتی معاون! میں یہاں آپ کی ہر ممکن مدد کے لیے ہوں - چاہے کوئی کام کرنا ہو، کوئی سوال پوچھنا ہو، یا بس بات چیت کرنی ہو۔ مجھ سے قدرتی طور پر بات کریں، میں سمجھ جاؤں گی!"
        else:
            return "I'm Buddy, your personal assistant! I'm here to help you with anything you need - whether it's getting things done, answering questions, or just having a chat. Feel free to talk to me naturally!"
    
    def _respond_to_weather_query(self):
        """Helpful response to weather queries"""
        if self.language_manager.current_language == "urdu":
            return "میں ابھی براہ راست موسم کی معلومات نہیں دے سکتی، لیکن میں آپ کے لیے موسم کی ویب سائٹ کھول سکتی ہوں۔ کیا آپ چاہیں گے کہ میں یہ کروں؟"
        else:
            return "I can't provide live weather updates right now, but I can open a weather website for you. Would you like me to do that?"
    
    def _provide_helpful_response(self, query):
        """Provide helpful response when query isn't understood"""
        if self.language_manager.current_language == "urdu":
            responses = [
                f"معاف کیجئے گا، میں '{query}' پوری طرح نہیں سمجھ پائی۔ کیا آپ اسے مختلف الفاظ میں بیان کر سکتے ہیں؟",
                f"میں ابھی '{query}' کے بارے میں پوری طرح واضح نہیں ہوں۔ کیا آپ مزید وضاحت کر سکتے ہیں؟",
                "مجھے افسوس ہے، میں وہ نہیں سمجھ سکی۔ کیا آپ چاہیں گے کہ میں کوئی خاص کام کروں، یا کوئی سوال کا جواب دوں؟",
                "ذرا اس کے بارے میں سوچتی ہوں... جی، میں ابھی اس کے لیے تیار نہیں ہوں۔ کیا آپ کچھ اور پوچھنا چاہیں گے؟"
            ]
        else:
            responses = [
                f"I'm sorry, I didn't quite understand '{query}'. Could you try saying it differently?",
                f"I'm not entirely clear about '{query}'. Could you give me more details?",
                "I apologize, I didn't catch that properly. Would you like me to do something specific, or answer a question?",
                "Let me think about that... Hmm, I'm not quite equipped for that yet. Is there something else I can help you with?"
            ]
        return random.choice(responses)
