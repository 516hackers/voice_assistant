from assistant import VoiceAssistant

def main():
    print("🚀 Starting Buddy Voice Assistant...")
    print("🔧 Initializing components...")
    
    try:
        assistant = VoiceAssistant()
        print("✅ Buddy initialized successfully!")
        print(f"🎯 Wake word: 'buddy'")
        print("🌐 Languages: English & Urdu")
        print("💡 Say 'buddy' followed by your command")
        print("💬 Say 'switch to urdu' or 'switch to english' to change language")
        print("⏹️  Say 'exit' or 'quit' to stop the assistant")
        print("-" * 50)
        
        # Start the assistant
        assistant.run()
        
    except KeyboardInterrupt:
        print("\n\n🛑 Assistant stopped by user")
    except Exception as e:
        print(f"❌ Error starting assistant: {e}")

if __name__ == "__main__":
    main()
