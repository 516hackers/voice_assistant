import os
import webbrowser
import pyautogui
import subprocess
from language_manager import LanguageManager

class CommandHandler:
    def __init__(self):
        self.applications = {
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'paint': 'mspaint.exe',
            'file explorer': 'explorer.exe',
            'cmd': 'cmd.exe',
            'browser': 'chrome.exe',
            'chrome': 'chrome.exe',
            'firefox': 'firefox.exe',
            'word': 'winword.exe',
            'excel': 'excel.exe',
            'powerpoint': 'powerpnt.exe',
            'media player': 'wmplayer.exe'
        }
        
        self.websites = {
            'youtube': 'https://www.youtube.com',
            'google': 'https://www.google.com',
            'github': 'https://www.github.com',
            'facebook': 'https://www.facebook.com',
            'twitter': 'https://www.twitter.com',
            'instagram': 'https://www.instagram.com',
            'whatsapp': 'https://web.whatsapp.com',
            'gmail': 'https://mail.google.com'
        }
        
        self.language_manager = LanguageManager()
    
    def execute_command(self, command_type, target=None):
        """Execute system commands with natural language understanding"""
        try:
            if command_type == "open_app":
                return self._open_application(target)
            elif command_type == "open_website":
                return self._open_website(target)
            elif command_type == "volume_up":
                return self._volume_up()
            elif command_type == "volume_down":
                return self._volume_down()
            elif command_type == "volume_mute":
                return self._volume_mute()
            elif command_type == "screenshot":
                return self._take_screenshot()
            elif command_type == "type_text":
                return self._type_text(target)
            elif command_type == "scroll_up":
                return self._scroll_up()
            elif command_type == "scroll_down":
                return self._scroll_down()
            elif command_type == "close_window":
                return self._close_window()
            elif command_type == "shutdown":
                return self._shutdown()
            elif command_type == "search":
                return self._search_web(target)
            else:
                return False, "I'm not sure how to do that yet."
        except Exception as e:
            return False, f"Sorry, I encountered an issue: {str(e)}"
    
    def _open_application(self, app_name):
        """Open applications with fuzzy matching"""
        app_name_lower = app_name.lower()
        
        # Fuzzy matching for common applications
        for key, value in self.applications.items():
            if key in app_name_lower or app_name_lower in key:
                try:
                    os.system(f"start {value}")
                    return True, f"Opening {key} for you"
                except:
                    pass
        
        # Try direct opening
        try:
            os.system(f"start {app_name}")
            return True, f"Opening {app_name}"
        except:
            return False, f"Sorry, I couldn't find {app_name}"
    
    def _open_website(self, site_name):
        """Open websites with fuzzy matching"""
        site_name_lower = site_name.lower()
        
        for key, value in self.websites.items():
            if key in site_name_lower or site_name_lower in key:
                webbrowser.open(value)
                return True, f"Opening {key}"
        
        # Try as direct URL
        if not site_name.startswith(('http://', 'https://')):
            site_name = 'https://' + site_name
        webbrowser.open(site_name)
        return True, "Opening that website"
    
    def _volume_up(self):
        """Increase volume"""
        for _ in range(3):
            pyautogui.press('volumeup')
        return True, self.language_manager.get_text("volume_up")
    
    def _volume_down(self):
        """Decrease volume"""
        for _ in range(3):
            pyautogui.press('volumedown')
        return True, self.language_manager.get_text("volume_down")
    
    def _volume_mute(self):
        """Mute volume"""
        pyautogui.press('volumemute')
        return True, self.language_manager.get_text("volume_mute")
    
    def _take_screenshot(self):
        """Take screenshot"""
        screenshot = pyautogui.screenshot()
        filename = f"screenshot_{pyautogui.time()}.png"
        screenshot.save(filename)
        return True, self.language_manager.get_text("screenshot")
    
    def _type_text(self, text):
        """Type text naturally"""
        pyautogui.write(text, interval=0.05)
        return True, self.language_manager.get_text("typing")
    
    def _scroll_up(self):
        """Scroll up"""
        pyautogui.scroll(300)
        return True, self.language_manager.get_text("scrolled_up")
    
    def _scroll_down(self):
        """Scroll down"""
        pyautogui.scroll(-300)
        return True, self.language_manager.get_text("scrolled_down")
    
    def _close_window(self):
        """Close current window"""
        pyautogui.hotkey('alt', 'f4')
        return True, self.language_manager.get_text("closing_window")
    
    def _shutdown(self):
        """Shutdown computer with confirmation"""
        os.system("shutdown /s /t 30")
        return True, "System will shut down in 30 seconds. You can cancel with 'shutdown /a'"
    
    def _search_web(self, query):
        """Search the web"""
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(search_url)
        return True, f"Searching for {query}"
