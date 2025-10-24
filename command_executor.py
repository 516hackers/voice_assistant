import os
import webbrowser
import pyautogui
import subprocess
import time
from memory_manager import MemoryManager

class CommandExecutor:
    def __init__(self):
        self.memory = MemoryManager()
        self.destructive_commands = ['shutdown', 'restart', 'delete', 'format', 'rm', 'del']
        
    def execute_command(self, command_type, target=None, extra_info=None):
        """Execute system commands with safety checks"""
        try:
            # Safety check for destructive commands
            if any(destructive in str(target).lower() for destructive in self.destructive_commands):
                return False, "I need confirmation for safety reasons. Please confirm this action."
            
            if command_type == "open_app":
                return self._open_application(target)
            elif command_type == "open_website":
                return self._open_website(target)
            elif command_type == "search":
                return self._search_web(target)
            elif command_type == "play_music":
                return self._play_music(target)
            elif command_type == "show_file":
                return self._show_file(target)
            elif command_type == "write_note":
                return self._write_note(target)
            elif command_type == "run_script":
                return self._run_script(target)
            elif command_type == "close_app":
                return self._close_application(target)
            elif command_type == "system_info":
                return self._get_system_info()
            elif command_type == "shutdown":
                return self._shutdown_system(extra_info)
            else:
                return False, "I'm not sure how to do that yet."
                
        except Exception as e:
            self.memory.log_command(f"{command_type} {target}", False)
            return False, f"Hmm, I encountered an issue: {str(e)}"
    
    def _open_application(self, app_name):
        """Open applications with intelligent matching"""
        app_name_lower = app_name.lower()
        
        # Application mapping
        app_map = {
            'chrome': 'chrome',
            'browser': self.memory.user_preferences["default_browser"],
            'notepad': 'notepad',
            'calculator': 'calc',
            'paint': 'mspaint',
            'file explorer': 'explorer',
            'cmd': 'cmd',
            'command prompt': 'cmd',
            'vs code': 'code',
            'visual studio code': 'code',
            'word': 'winword',
            'excel': 'excel',
            'powerpoint': 'powerpnt',
            'media player': 'wmplayer',
            'spotify': 'spotify',
            'photoshop': 'photoshop',
            'premiere': 'premiere pro'
        }
        
        # Find matching application
        for key, command in app_map.items():
            if key in app_name_lower:
                try:
                    os.system(f"start {command}")
                    self.memory.add_favorite_app(key)
                    self.memory.log_command(f"open {key}", True)
                    return True, f"opening {key}"
                except:
                    pass
        
        # Try direct execution
        try:
            os.system(f"start {app_name}")
            self.memory.log_command(f"open {app_name}", True)
            return True, f"opening {app_name}"
        except Exception as e:
            self.memory.log_command(f"open {app_name}", False)
            return False, f"Couldn't find {app_name}. Want me to search for it online?"
    
    def _open_website(self, site_name):
        """Open websites with intelligent parsing"""
        site_name_lower = site_name.lower()
        
        website_map = {
            'youtube': 'https://www.youtube.com',
            'google': 'https://www.google.com',
            'facebook': 'https://www.facebook.com',
            'instagram': 'https://www.instagram.com',
            'twitter': 'https://www.twitter.com',
            'github': 'https://www.github.com',
            'whatsapp': 'https://web.whatsapp.com',
            'gmail': 'https://mail.google.com',
            'outlook': 'https://outlook.live.com',
            'linkedin': 'https://www.linkedin.com',
            'netflix': 'https://www.netflix.com',
            'amazon': 'https://www.amazon.com'
        }
        
        for key, url in website_map.items():
            if key in site_name_lower:
                webbrowser.open(url)
                self.memory.log_command(f"open {key}", True)
                return True, f"opening {key}"
        
        # Try as direct URL or search
        if '.' in site_name:
            if not site_name.startswith(('http://', 'https://')):
                site_name = 'https://' + site_name
            webbrowser.open(site_name)
            self.memory.log_command(f"open website {site_name}", True)
            return True, "opening that website"
        else:
            # Treat as search
            return self._search_web(site_name)
    
    def _search_web(self, query):
        """Search the web"""
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(search_url)
        self.memory.log_command(f"search {query}", True)
        return True, f"searching for {query}"
    
    def _play_music(self, query=None):
        """Play music - YouTube for now"""
        if query:
            search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        else:
            search_url = "https://www.youtube.com"
        
        webbrowser.open(search_url)
        self.memory.log_command("play music", True)
        return True, "playing music"
    
    def _show_file(self, file_path):
        """Show files or folders"""
        try:
            if os.path.exists(file_path):
                os.system(f'explorer "{os.path.abspath(file_path)}"')
                self.memory.log_command(f"show {file_path}", True)
                return True, f"showing {file_path}"
            else:
                # Open containing folder
                folder = os.path.dirname(file_path) if os.path.dirname(file_path) else "."
                os.system(f'explorer "{os.path.abspath(folder)}"')
                self.memory.log_command(f"show folder for {file_path}", True)
                return True, f"showing the folder for {file_path}"
        except:
            self.memory.log_command(f"show {file_path}", False)
            return False, f"Couldn't find {file_path}"
    
    def _write_note(self, note):
        """Write notes to file"""
        success = self.memory.save_note(note)
        if success:
            self.memory.log_command("write note", True)
            return True, "note saved"
        else:
            self.memory.log_command("write note", False)
            return False, "Couldn't save the note"
    
    def _run_script(self, script_path):
        """Run scripts or commands"""
        try:
            if script_path.endswith('.py'):
                result = subprocess.run(['python', script_path], capture_output=True, text=True)
            elif script_path.endswith('.bat'):
                result = subprocess.run([script_path], shell=True, capture_output=True, text=True)
            else:
                result = subprocess.run(script_path, shell=True, capture_output=True, text=True)
            
            self.memory.log_command(f"run {script_path}", True)
            return True, f"ran {script_path}"
        except Exception as e:
            self.memory.log_command(f"run {script_path}", False)
            return False, f"Couldn't run {script_path}"
    
    def _close_application(self, app_name):
        """Close applications"""
        try:
            # This is a simplified version - in real implementation you'd use taskkill
            os.system(f'taskkill /f /im {app_name}.exe')
            self.memory.log_command(f"close {app_name}", True)
            return True, f"closing {app_name}"
        except:
            self.memory.log_command(f"close {app_name}", False)
            return False, f"Couldn't close {app_name}"
    
    def _get_system_info(self):
        """Get basic system information"""
        import datetime
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        self.memory.log_command("system info", True)
        return True, f"The time is {current_time} and today is {current_date}"
    
    def _shutdown_system(self, delay=None):
        """Shutdown system with optional delay"""
        try:
            if delay:
                os.system(f"shutdown /s /t {delay}")
                return True, f"shutting down in {delay} seconds"
            else:
                return False, "Please specify a delay for shutdown"
        except:
            return False, "Couldn't initiate shutdown"
