import json
import datetime
import os

class MemoryManager:
    def __init__(self):
        self.history_file = "command_history.txt"
        self.notes_file = "user_notes.txt"
        self.preferences_file = "user_preferences.json"
        self.user_preferences = self.load_preferences()
        
    def load_preferences(self):
        """Load user preferences"""
        default_prefs = {
            "default_browser": "chrome",
            "default_editor": "code", 
            "default_music": "youtube",
            "favorite_apps": ["chrome", "code", "notepad"]
        }
        
        try:
            if os.path.exists(self.preferences_file):
                with open(self.preferences_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        
        return default_prefs
    
    def save_preferences(self):
        """Save user preferences"""
        try:
            with open(self.preferences_file, 'w') as f:
                json.dump(self.user_preferences, f, indent=2)
        except:
            pass
    
    def log_command(self, command, success=True):
        """Log executed commands"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "SUCCESS" if success else "FAILED"
        
        log_entry = f"[{timestamp}] {command} - {status}\n"
        
        try:
            with open(self.history_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except:
            pass
    
    def save_note(self, note):
        """Save user notes"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            with open(self.notes_file, 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] {note}\n")
            return True
        except:
            return False
    
    def read_notes(self):
        """Read user notes"""
        try:
            if os.path.exists(self.notes_file):
                with open(self.notes_file, 'r', encoding='utf-8') as f:
                    return f.read()
            return "No notes found."
        except:
            return "Could not read notes."
    
    def add_favorite_app(self, app_name):
        """Add app to favorites"""
        if app_name not in self.user_preferences["favorite_apps"]:
            self.user_preferences["favorite_apps"].append(app_name)
            self.save_preferences()
    
    def get_favorite_apps(self):
        """Get favorite apps"""
        return self.user_preferences.get("favorite_apps", [])
