import tkinter as tk
from tkinter import messagebox
import os
import platform
import threading
import time

class ShutdownGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Shutdown Controller")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Style configuration
        self.bg_color = "#2C3E50"
        self.button_color = "#E74C3C"
        self.button_color_restart = "#3498DB"
        self.text_color = "#ECF0F1"
        
        self.root.configure(bg=self.bg_color)
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="SHUTDOWN CONTROLLER", 
            font=("Arial", 18, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.root,
            text="Pilih aksi yang ingin dilakukan:",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.text_color
        )
        subtitle_label.pack(pady=10)
        
        # Shutdown Button
        shutdown_btn = tk.Button(
            self.root,
            text="SHUTDOWN",
            font=("Arial", 14, "bold"),
            bg=self.button_color,
            fg=self.text_color,
            width=15,
            height=2,
            command=self.initiate_shutdown
        )
        shutdown_btn.pack(pady=15)
        
        # Restart Button
        restart_btn = tk.Button(
            self.root,
            text="RESTART",
            font=("Arial", 14, "bold"),
            bg=self.button_color_restart,
            fg=self.text_color,
            width=15,
            height=2,
            command=self.initiate_restart
        )
        restart_btn.pack(pady=15)
        
        # Status Label
        self.status_label = tk.Label(
            self.root,
            text="Siap...",
            font=("Arial", 10),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.status_label.pack(pady=20)
        
        # Cancel Button (initially hidden)
        self.cancel_btn = tk.Button(
            self.root,
            text="BATALKAN",
            font=("Arial", 10, "bold"),
            bg="#27AE60",
            fg=self.text_color,
            command=self.cancel_action,
            state=tk.DISABLED
        )
        self.cancel_btn.pack(pady=10)
        
        self.countdown_active = False
        self.action_type = None
    
    def initiate_shutdown(self):
        self.action_type = "shutdown"
        self.confirm_action("shutdown")
    
    def initiate_restart(self):
        self.action_type = "restart"
        self.confirm_action("restart")
    
    def confirm_action(self, action_type):
        action_text = "SHUTDOWN" if action_type == "shutdown" else "RESTART"
        
        result = messagebox.askyesno(
            "Konfirmasi",
            f"Apakah Anda yakin ingin {action_text}?\n\n"
            f"Komputer akan {action_text} dalam 5 detik setelah konfirmasi.\n"
            "Pastikan semua pekerjaan sudah disimpan!"
        )
        
        if result:
            self.start_countdown(action_type)
        else:
            self.status_label.config(text="Aksi dibatalkan oleh pengguna")
    
    def start_countdown(self, action_type):
        self.countdown_active = True
        self.cancel_btn.config(state=tk.NORMAL)
        
        # Disable action buttons during countdown
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and widget["text"] in ["SHUTDOWN", "RESTART"]:
                widget.config(state=tk.DISABLED)
        
        # Start countdown in separate thread
        countdown_thread = threading.Thread(target=self.countdown, args=(action_type,))
        countdown_thread.daemon = True
        countdown_thread.start()
    
    def countdown(self, action_type):
        action_text = "shutdown" if action_type == "shutdown" else "restart"
        
        for i in range(5, 0, -1):
            if not self.countdown_active:
                self.update_status("Aksi dibatalkan")
                self.reset_buttons()
                return
            
            self.update_status(f"{action_text.capitalize()} dalam {i} detik...")
            time.sleep(1)
        
        if self.countdown_active:
            self.update_status(f"Melakukan {action_text}...")
            self.execute_action(action_type)
    
    def update_status(self, text):
        self.root.after(0, lambda: self.status_label.config(text=text))
    
    def cancel_action(self):
        self.countdown_active = False
        self.cancel_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Aksi dibatalkan")
        self.reset_buttons()
    
    def reset_buttons(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and widget["text"] in ["SHUTDOWN", "RESTART"]:
                widget.config(state=tk.NORMAL)
    
    def execute_action(self, action_type):
        system_name = platform.system().lower()
        
        try:
            if action_type == "shutdown":
                if system_name == "windows":
                    os.system("shutdown /s /t 1")
                elif system_name == "linux" or system_name == "darwin":
                    os.system("shutdown -h now")
                else:
                    messagebox.showerror("Error", "Sistem operasi tidak didukung")
            
            elif action_type == "restart":
                if system_name == "windows":
                    os.system("shutdown /r /t 1")
                elif system_name == "linux" or system_name == "darwin":
                    os.system("shutdown -r now")
                else:
                    messagebox.showerror("Error", "Sistem operasi tidak didukung")
        
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

def main():
    root = tk.Tk()
    app = ShutdownGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()