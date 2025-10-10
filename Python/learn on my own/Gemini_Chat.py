import requests
import json
import os
from datetime import datetime
import time

class GeminiChatTerminal:
    def __init__(self, api_key):
        """
        Inisialisasi chatbot dengan API key Google Gemini
        """
        if not api_key or "YOUR_API_KEY" in api_key:
            raise ValueError("API Key tidak valid. Silakan ganti 'YOUR_API_KEY' dengan API key Anda.")
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
        self.history = []

    def _show_thinking_animation(self):
        """Menampilkan animasi saat menunggu respons API."""
    
    def send_message(self, message):
        """
        Mengirim pesan ke Gemini via HTTP API
        """
        # Mulai animasi sebelum mengirim request
        # self._show_thinking_animation() # Dijalankan di chat_loop

        try:
            # Prepare the conversation history in Gemini API format
            contents = []
            for msg in self.history:
                role = "user" if msg['role'] == 'user' else "model"
                contents.append({
                    "role": role,
                    "parts": [{"text": msg['content']}]
                })
            
            # Add the current message
            contents.append({
                "role": "user", 
                "parts": [{"text": message}]
            })
            
            # Prepare the request payload
            payload = {
                "contents": contents,
                "generationConfig": {
                    "temperature": 0.7,
                    "topK": 40,
                    "topP": 0.95,
                    "maxOutputTokens": 2048,
                }
            }
            
            # Send request to Gemini API
            headers = {'Content-Type': 'application/json'}
            
            # Hapus animasi sebelum menampilkan hasil
            print("\r" + " " * 30, end="\r")
            response = requests.post(self.api_url, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            
            # Parse response
            result = response.json()
            response_text = result['candidates'][0]['content']['parts'][0]['text']
            
            # Save to history
            self.history.extend([
                {'role': 'user', 'content': message},
                {'role': 'model', 'content': response_text}
            ])
            
            return response_text
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return None

def main():
    # API key Anda
    API_KEY = "AIzaSyCT5-mKYXAjbKXoF9Z0gHQnhyw2LLmWcRo"
    
    try:
        chatbot = GeminiChatTerminal(API_KEY)
        chat_loop(chatbot)
    except ValueError as e:
        print(f"\n❌ Error Inisialisasi: {e}")
        print("Silakan buka file skrip ini dan masukkan API key Anda.")

def chat_loop(chatbot):
    """
    Loop chat utama
    """
    print("\n🤖 GEMINI TERMINAL CHAT")
    print("Ketik 'exit' untuk keluar dari program.")
    print("-" * 50)
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'exit':
            print("👋 Terima kasih! Sampai jumpa!")
            break
        elif not user_input:
            continue
        
        # Kirim pesan ke Gemini
        # Kita akan menggunakan threading untuk animasi agar tidak memblokir request
        import threading
        stop_animation = threading.Event()
        def animate():
            frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
            i = 0
            while not stop_animation.is_set():
                print(f"\rGemini: {frames[i % len(frames)]} Thinking...", end="", flush=True)
                time.sleep(0.1)
                i += 1
            print("\r" + " " * 30, end="\r")

        animation_thread = threading.Thread(target=animate)
        animation_thread.start()

        response = chatbot.send_message(user_input)
        
        stop_animation.set()
        animation_thread.join()

        if response:
            print(f"Gemini: {response}")
        else:
            # Pesan error sudah ditampilkan di dalam send_message()
            pass

if __name__ == "__main__":
    main()