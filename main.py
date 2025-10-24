from assistant import VoiceAssistant

def main():
    print("🚀 Starting Real Human-Like AI Assistant...")
    print("🔧 Initializing advanced AI system...")
    print("🎯 Features:")
    print("   • Natural human-like conversations")
    print("   • Full system control")
    print("   • Intelligent command understanding") 
    print("   • Continuous listening")
    print("   • Memory and preferences")
    print("-" * 60)
    
    try:
        assistant = VoiceAssistant()
        print("✅ Buddy is fully operational!")
        print("💬 Just speak naturally - I understand everything!")
        print("🛠️  Try: 'Open Chrome', 'Search for weather', 'Play music', 'Write a note'")
        print("⏹️  Say 'exit', 'quit', or 'bye' to stop")
        print("-" * 60)
        
        # Start the assistant
        assistant.run()
        
    except KeyboardInterrupt:
        print("\n\n🛑 Assistant stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
