from assistant import VoiceAssistant

def main():
    print("🚀 Starting Enhanced Buddy Assistant...")
    print("🔧 Initializing natural language processing...")
    print("🎯 Features:")
    print("   • Continuous listening - no wake word needed")
    print("   • Natural human-like conversations")
    print("   • Urdu and English understanding")
    print("   • Real-time system control")
    print("   • Female personality with emotions")
    print("-" * 60)
    
    try:
        assistant = VoiceAssistant()
        print("✅ Buddy is ready!")
        print("💬 Just start speaking naturally...")
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
