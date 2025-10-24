import os
import webbrowser
import pyautogui
import subprocess

class CommandHandler:
    def __init__(self):
        self.applications = {
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'paint': 'mspaint.exe',
            'file explorer': 'explorer.exe',
            'cmd': 'cmd.exe',
            'browser': 'chrome.exe',
            'word': 'winword.exe',
            'excel': 'excel.exe'
        }
        
        self.websites = {
            'youtube': 'https://www.youtube.com',
            'google': 'https://www.google.com',
            'github': 'https://www.github.com',
            'facebook': 'https://www.facebook.com',
            'twitter': 'https://www.twitter.com',
            'instagram': 'https://www.instagram.com'
        }
    
    def execute_command(self, command_type, target=None):
        """Execute system commands"""
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
            else:
                return False, "Unknown command type"
        except Exception as e:
            return False, f"Error executing command: {str(e)}"
    
    def _open_application(self, app_name):
        """Open applications"""
        app_key = app_name.lower()
        if app_key in self.applications:
            os.system(f"start {self.applications[app_key]}")
            return True, f"Opening {app_name}"
        else:
            # Try to open directly
            try:
                os.system(f"start {app_name}")
                return True, f"Opening {app_name}"
            except:
                return False, f"Could not find application: {app_name}"
    
    def _open_website(self, site_name):
        """Open websites"""
        site_key = site_name.lower()
        if site_key in self.websites:
            webbrowser.open(self.websites[site_key])
            return True, f"Opening {site_name}"
        else:
            # Try to open as URL
            if not site_name.startswith(('http://', 'https://')):
                site_name = 'https://' + site_name
            webbrowser.open(site_name)
            return True, f"Opening website"
    
    def _volume_up(self):
        """Increase volume"""
        for _ in range(5):
            pyautogui.press('volumeup')
        return True, "Volume increased"
    
    def _volume_down(self):
        """Decrease volume"""
        for _ in range(5):
            pyautogui.press('volumedown')
        return True, "Volume decreased"
    
    def _volume_mute(self):
        """Mute volume"""
        pyautogui.press('volumemute')
        return True, "Volume muted"
    
    def _take_screenshot(self):
        """Take screenshot"""
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        return True, "Screenshot taken and saved"
    
    def _type_text(self, text):
        """Type text"""
        pyautogui.write(text, interval=0.1)
        return True, f"Typed: {text}"
    
    def _scroll_up(self):
        """Scroll up"""
        pyautogui.scroll(100)
        return True, "Scrolled up"
    
    def _scroll_down(self):
        """Scroll down"""
        pyautogui.scroll(-100)
        return True, "Scrolled down"
    
    def _close_window(self):
        """Close current window"""
        pyautogui.hotkey('alt', 'f4')
        return True, "Closing current window"
    
    def _shutdown(self):
        """Shutdown computer"""
        os.system("shutdown /s /t 5")
        return True, "Shutting down in 5 seconds"
