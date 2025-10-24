from assistant import VoiceAssistant

def main():
    print("🚀 Starting Custom Voice Assistant...")
    print("🔧 Initializing components...")
    
    try:
        assistant = VoiceAssistant()
        print("✅ Assistant initialized successfully!")
        print(f"🎯 Wake word: 'assistant'")
        print("💡 Say 'assistant' followed by your command")
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
