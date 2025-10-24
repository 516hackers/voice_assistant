import datetime
import random
from language_manager import LanguageManager

class AIBrain:
    def __init__(self):
        self.conversation_context = {}
        self.learned_commands = {}
        self.user_preferences = {}
        self.language_manager = LanguageManager()
    
    def set_language(self, language):
        """Set language for AI responses"""
        return self.language_manager.set_language(language)
    
    def process_query(self, query, context=None):
        """Main AI processing logic with Urdu support"""
        query = query.lower().strip()
        
        # Store context for follow-up questions
        if context:
            self.conversation_context.update(context)
        
        # Language switching commands
        if any(word in query for word in ['urdu', 'اردو']):
            self.set_language("urdu")
            return "زباز تبدیل کر دی گئی ہے۔ اب میں اردو میں بات کروں گا۔"
        
        elif any(word in query for word in ['english', 'انگریزی']):
            self.set_language("english")
            return "Language changed to English. I will now speak in English."
        
        # Greetings and basic interaction
        if any(word in query for word in ['hello', 'hi', 'hey', 'ہیلو', 'اسلام علیکم', 'آداب']):
            return self._generate_greeting()
        
        elif any(word in query for word in ['time', 'current time', 'وقت', 'کٹنا بجا']):
            return self._get_current_time()
        
        elif any(word in query for word in ['date', 'today', 'current date', 'تاریخ', 'آج']):
            return self._get_current_date()
        
        elif any(word in query for word in ['thank', 'thanks', 'شکریہ', 'شکریا']):
            return self._generate_thanks_response()
        
        elif any(word in query for word in ['how are you', 'how you doing', 'کیا حال ہے', 'آپ کیسے ہیں']):
            return self._generate_mood_response()
        
        elif any(word in query for word in ['what can you do', 'your capabilities', 'کیا کر سکتے ہو', 'تمہاری صلاحیتیں']):
            return self._list_capabilities()
        
        elif any(word in query for word in ['joke', 'tell joke', 'make me laugh', 'لطیفہ', 'چٹکلہ', 'ہنساؤ']):
            return self._tell_joke()
        
        elif any(word in query for word in ['calculate', 'math', 'what is', 'حساب کرو', 'حساب کتاب']):
            return self._simple_calculation(query)
        
        elif any(word in query for word in ['who are you', 'your name', 'introduce yourself', 'تم کون ہو', 'اپنا تعارف کرواؤ']):
            return self._introduce_self()
        
        elif any(word in query for word in ['weather', 'temperature', 'موسم', 'درجہ حرارت']):
            return self._respond_to_weather_query()
        
        elif any(word in query for word in ['remember that', 'remember this', 'یاد رکھو', 'یاد کرلو']):
            return self._remember_information(query)
        
        elif any(word in query for word in ['what did i say', 'recall that', 'میں نے کیا کہا تھا', 'یاد کرو']):
            return self._recall_information()
        
        else:
            return self._handle_unknown_query(query)
    
    def _generate_greeting(self):
        """Generate contextual greeting"""
        hour = datetime.datetime.now().hour
        
        if self.language_manager.current_language == "urdu":
            if 5 <= hour < 12:
                greeting = "صبح بخیر!"
            elif 12 <= hour < 18:
                greeting = "دوپہر بخیر!"
            else:
                greeting = "شام بخیر!"
            
            responses = [
                f"{greeting} میں آپ کی کس طرح مدد کر سکتا ہوں؟",
                f"{greeting} آپ کے لیے کیا کر سکتا ہوں؟",
                f"{greeting} میں آپ کی خدمت کے لیے حاضر ہوں!"
            ]
        else:
            if 5 <= hour < 12:
                greeting = "Good morning!"
            elif 12 <= hour < 18:
                greeting = "Good afternoon!"
            else:
                greeting = "Good evening!"
            
            responses = [
                f"{greeting} How can I assist you today?",
                f"{greeting} What can I do for you?",
                f"{greeting} I'm here to help!"
            ]
        
        return random.choice(responses)
    
    def _get_current_time(self):
        """Get current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        
        if self.language_manager.current_language == "urdu":
            return f"موجودہ وقت {current_time} ہے"
        else:
            return f"The current time is {current_time}"
    
    def _get_current_date(self):
        """Get current date"""
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        
        if self.language_manager.current_language == "urdu":
            return f"آج {current_date} ہے"
        else:
            return f"Today is {current_date}"
    
    def _generate_thanks_response(self):
        """Respond to thanks"""
        if self.language_manager.current_language == "urdu":
            responses = [
                "خوش آمدید!",
                "مدد کر کے خوشی ہوئی!",
                "کسی بھی وقت!",
                "خوشی ہوئی کہ میں مدد کر سکا!"
            ]
        else:
            responses = [
                "You're welcome!",
                "Happy to help!",
                "Anytime!",
                "Glad I could assist you!"
            ]
        
        return random.choice(responses)
    
    def _generate_mood_response(self):
        """Respond to how are you"""
        if self.language_manager.current_language == "urdu":
            moods = [
                "میں بہترین طریقے سے کام کر رہا ہوں، پوچھنے کا شکریہ!",
                "میں ٹھیک ہوں! آپ کی مدد کے لیے تیار ہوں۔",
                "تمام سسٹمز کام کر رہے ہیں! میں آپ کی کس طرح مدد کر سکتا ہوں؟",
                "آج میں بہتر طریقے سے چل رہا ہوں!"
            ]
        else:
            moods = [
                "I'm functioning optimally, thank you for asking!",
                "I'm doing great! Ready to help you.",
                "All systems are operational! How can I assist you?",
                "I'm running smoothly today!"
            ]
        
        return random.choice(moods)
    
    def _list_capabilities(self):
        """List what the assistant can do"""
        capabilities = self.language_manager.get_text("capabilities")
        return "\n".join(capabilities)
    
    def _tell_joke(self):
        """Tell a random joke"""
        if self.language_manager.current_language == "urdu":
            jokes = [
                "ایک استاد نے طالب علم سے پوچھا: تمہاری عمر کتنی ہے؟ طالب علم بولا: ابھی تو پوری ہے سر!",
                "ایک آدمی ڈاکٹر کے پاس گیا اور کہا: ڈاکٹر صاحب، میں سوچتا بہت زیادہ ہوں۔ ڈاکٹر بولا: کوئی بات نہیں، آپ کی یہ بیماری بھی جلد ختم ہو جائے گی!",
                "بیٹا: ابو، آپ کو پتہ ہے کہ مچھلی کیوں پڑھائی نہیں کرتی؟ باپ: کیوں؟ بیٹا: کیونکہ اس کا دماغ پانی میں ڈوبا رہتا ہے!",
                "استاد: تمہارے گھر میں سب سے ذہین کون ہے؟ طالب علم: میرا کتا۔ استاد: تمہیں کیسے پتہ؟ طالب علم: وہ ہر وقت پڑھائی کے بارے میں بات کرتا ہے، ہر وقت کہتا رہتا ہے: 'وع وع'!"
            ]
        else:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? He was outstanding in his field!",
                "Why don't eggs tell jokes? They'd crack each other up!",
                "What do you call a fake noodle? An impasta!",
                "Why did the math book look so sad? Because it had too many problems!"
            ]
        
        return random.choice(jokes)
    
    def _simple_calculation(self, query):
        """Perform simple math calculations"""
        try:
            # Extract numbers and operation
            if any(word in query for word in ['plus', 'جمع', 'اضافہ']):
                numbers = [int(s) for s in query.split() if s.isdigit()]
                if len(numbers) >= 2:
                    result = sum(numbers)
                    if self.language_manager.current_language == "urdu":
                        return f"جواب ہے {result}"
                    else:
                        return f"The answer is {result}"
            
            elif any(word in query for word in ['minus', 'منفی', 'کم']):
                numbers = [int(s) for s in query.split() if s.isdigit()]
                if len(numbers) >= 2:
                    result = numbers[0] - sum(numbers[1:])
                    if self.language_manager.current_language == "urdu":
                        return f"جواب ہے {result}"
                    else:
                        return f"The answer is {result}"
            
            elif any(word in query for word in ['multiply', 'times', 'ضرب', 'گنا']):
                numbers = [int(s) for s in query.split() if s.isdigit()]
                if len(numbers) >= 2:
                    result = 1
                    for num in numbers:
                        result *= num
                    if self.language_manager.current_language == "urdu":
                        return f"جواب ہے {result}"
                    else:
                        return f"The answer is {result}"
            
            if self.language_manager.current_language == "urdu":
                return "میں بنیادی جمع، تفریق، اور ضرب میں مدد کر سکتا ہوں۔ '5 جمع 3 حساب کرو' کہہ کر آزمائیں"
            else:
                return "I can help with basic addition, subtraction, and multiplication. Try saying 'calculate 5 plus 3'"
        
        except:
            if self.language_manager.current_language == "urdu":
                return "معذرت، میں یہ حساب نہیں کر سکا۔ براہ کرم آسان اعداد کے ساتھ دوبارہ کوشش کریں۔"
            else:
                return "Sorry, I couldn't calculate that. Please try again with simple numbers."
    
    def _introduce_self(self):
        """Introduce the assistant"""
        if self.language_manager.current_language == "urdu":
            return "میں آپ کا ذاتی AI اسسٹنٹ بڈی ہوں! میں خالص پائیتھن میں بنایا گیا ہوں تاکہ آپ کے سسٹم کو کنٹرول کرنے اور سوالات کے جوابات دینے میں مدد کر سکوں۔ میں بیرونی APIs پر انحصار نہیں کرتا - جو کچھ بھی میں کرتا ہوں وہ براہ راست پروگرام کیا گیا ہے!"
        else:
            return "I'm your custom AI assistant Buddy! I'm built with pure Python to help you control your system and answer questions. I don't rely on external APIs - everything I do is programmed directly!"
    
    def _respond_to_weather_query(self):
        """Respond to weather queries"""
        if self.language_manager.current_language == "urdu":
            responses = [
                "میرے پاس لائیو موسمیاتی ڈیٹا نہیں ہے، لیکن درست معلومات کے لیے میں آپ کو موسم کی ویب سائٹ چیک کرنے کا مشورہ دیتا ہوں۔",
                "موجودہ موسمی حالات کے لیے، آپ اپنی مقامی موسمی سروس چیک کر سکتے ہیں۔",
                "میں موسمی سروسز سے منسلک نہیں ہوں، لیکن میں آپ کی موسم کی ویب سائٹ کھولنے میں مدد کر سکتا ہوں!"
            ]
        else:
            responses = [
                "I don't have real-time weather data, but I recommend checking a weather website for accurate information.",
                "For current weather conditions, you might want to check your local weather service.",
                "I'm not connected to weather services, but I can help you open a weather website!"
            ]
        
        return random.choice(responses)
    
    def _remember_information(self, query):
        """Remember user information"""
        # Extract information to remember
        if self.language_manager.current_language == "urdu":
            info = query.replace('یاد رکھو', '').replace('یاد کرلو', '').strip()
        else:
            info = query.replace('remember that', '').replace('remember this', '').strip()
        
        if info:
            self.user_preferences['last_remembered'] = info
            if self.language_manager.current_language == "urdu":
                return f"میں یہ یاد رکھوں گا: {info}"
            else:
                return f"I'll remember that: {info}"
        
        if self.language_manager.current_language == "urdu":
            return "آپ کیا چاہتے ہیں کہ میں یاد رکھوں؟"
        else:
            return "What would you like me to remember?"
    
    def _recall_information(self):
        """Recall remembered information"""
        if 'last_remembered' in self.user_preferences:
            if self.language_manager.current_language == "urdu":
                return f"آپ نے مجھے بتایا تھا: {self.user_preferences['last_remembered']}"
            else:
                return f"You told me: {self.user_preferences['last_remembered']}"
        
        if self.language_manager.current_language == "urdu":
            return "میرے پاس ابھی تک کوئی چیز یاد نہیں ہے۔ 'یاد رکھو' کہہ کر مجھے کچھ بتائیں۔"
        else:
            return "I don't have anything remembered yet. Tell me something with 'remember that'."
    
    def _handle_unknown_query(self, query):
        """Handle queries the AI doesn't understand"""
        if self.language_manager.current_language == "urdu":
            responses = [
                f"میں سمجھا نہیں کہ '{query}' سے آپ کی کیا مراد ہے۔ براہ کرم اسے دوسرے الفاظ میں بیان کریں؟",
                f"میں '{query}' نہیں سمجھ سکا۔ مجھے کچھ کھولنے، حساب کرنے، یا لطیفہ سنانے کو کہیں۔",
                f"معذرت، میں ابھی سیکھ رہا ہوں۔ میں '{query}' نہیں سمجھ سکا۔",
                f"کیا آپ '{query}' کو مختلف طریقے سے بیان کر سکتے ہیں؟ میں مدد کرنا چاہتا ہوں!"
            ]
        else:
            responses = [
                f"I'm not sure how to help with '{query}'. Could you rephrase that?",
                f"I don't understand '{query}'. Try asking me to open something, calculate, or tell you a joke.",
                f"Sorry, I'm still learning. I didn't understand '{query}'.",
                f"Could you explain '{query}' differently? I want to help!"
            ]
        
        return random.choice(responses)
