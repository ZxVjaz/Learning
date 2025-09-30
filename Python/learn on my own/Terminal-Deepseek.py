import requests
import os
import time
from datetime import datetime

class DeepSeekTerminalChat:
    def __init__(self):
        self.api_key = "(isi sendiri dengan API mu)"  # Ganti dengan API key-mu
        self.base_url = "https://api.deepseek.com/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        self.conversation = []
        self.message_count = 0
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        print("╔" + "═" * 60 + "╗")
        print("║" + " " * 20 + "🤖 DEEPSEEK CHAT" + " " * 23 + "║")
        print("║" + " " * 18 + "Terminal Edition v1.0" + " " * 20 + "║")
        print("╚" + "═" * 60 + "╝")
        print("\n🎯 Commands: [clear] [quit] [history] [save]")
        print("─" * 62)
    
    def show_thinking_animation(self):
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for i in range(15):
            print(f"\r🔄 {frames[i % len(frames)]} Thinking...", end="", flush=True)
            time.sleep(0.1)
        print("\r" + " " * 30, end="\r")
    
    def get_bot_response(self, user_message):
        self.conversation.append({"role": "user", "content": user_message})
        
        payload = {
            "model": "deepseek-chat",
            "messages": self.conversation,
            "stream": False,
            "temperature": 0.7,
            "max_tokens": 2000
        }
        
        try:
            self.show_thinking_animation()
            
            response = requests.post(self.base_url, headers=self.headers, json=payload, timeout=45)
            
            if response.status_code == 200:
                bot_reply = response.json()["choices"][0]["message"]["content"]
                self.conversation.append({"role": "assistant", "content": bot_reply})
                self.message_count += 1
                return bot_reply
            else:
                error_msg = f"❌ API Error {response.status_code}: {response.text}"
                return error_msg
                
        except requests.exceptions.Timeout:
            return "❌ Request timeout - coba lagi ya"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def show_conversation_history(self):
        if not self.conversation:
            print("\n📝 No conversation history yet")
            return
            
        print(f"\n📜 Conversation History ({len(self.conversation)//2} messages):")
        print("─" * 50)
        for i, msg in enumerate(self.conversation):
            if msg["role"] == "user":
                print(f"👤 You: {msg['content'][:80]}{'...' if len(msg['content']) > 80 else ''}")
            else:
                print(f"🤖 AI: {msg['content'][:80]}{'...' if len(msg['content']) > 80 else ''}")
    
    def save_conversation(self):
        if not self.conversation:
            print("\n💾 No conversation to save")
            return
            
        filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("DeepSeek Terminal Chat History\n")
            f.write("=" * 40 + "\n\n")
            
            for i, msg in enumerate(self.conversation):
                role = "You" if msg["role"] == "user" else "DeepSeek"
                f.write(f"{role}: {msg['content']}\n\n")
        
        print(f"💾 Conversation saved as: {filename}")
    
    def format_bot_response(self, text):
        """Format response biar rapih"""
        lines = text.split('\n')
        formatted_lines = []
        
        for line in lines:
            if line.strip():
                # Indent untuk paragraph
                if not line.startswith(('•', '-', '1.', '2.', '3.')):
                    formatted_lines.append(f"   {line}")
                else:
                    formatted_lines.append(f"  {line}")
        
        return '\n'.join(formatted_lines)
    
    def run_chat(self):
        self.clear_screen()
        self.print_banner()
        
        print("🚀 Starting chat session...\n")
        
        while True:
            try:
                user_input = input("💬 You: ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print(f"\n👋 Goodbye! Total messages: {self.message_count}")
                    break
                    
                elif user_input.lower() == 'clear':
                    self.clear_screen()
                    self.print_banner()
                    continue
                    
                elif user_input.lower() == 'history':
                    self.show_conversation_history()
                    continue
                    
                elif user_input.lower() == 'save':
                    self.save_conversation()
                    continue
                
                # Get AI response
                response = self.get_bot_response(user_input)
                
                # Display response
                print(f"🤖 DeepSeek:\n{self.format_bot_response(response)}\n")
                print("─" * 62)
                
            except KeyboardInterrupt:
                print(f"\n\n🛑 Session interrupted. Total messages: {self.message_count}")
                break
            except Exception as e:
                print(f"\n❌ Unexpected error: {e}")

# Main execution
if __name__ == "__main__":
    print("Initializing DeepSeek Terminal Chat...")
    
    # Cek API key
    chat = DeepSeekTerminalChat()
    if chat.api_key == "YOUR_DEEPSEEK_API_KEY":
        print("\n❌ Please set your DeepSeek API key first!")
        print("1. Daftar di platform.deepseek.com")
        print("2. Dapatkan API key")
        print("3. Ganti 'YOUR_DEEPSEEK_API_KEY' dengan key asli\n")
    else:
        chat.run_chat()