import customtkinter as ctk
from tkinter import messagebox, filedialog
import threading
import os
from downloader import YouTubeDownloader

# Konfigurasi theme
ctk.set_appearance_mode("System")  # "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

class YouTubeDownloaderApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("YouTube Downloader Pro")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        
        self.downloader = YouTubeDownloader()
        self.setup_ui()
        self.setup_bindings()
    
    def setup_ui(self):
        # Header
        header_frame = ctk.CTkFrame(self.root)
        header_frame.pack(pady=20, padx=20, fill="x")
        
        ctk.CTkLabel(header_frame, 
                    text="🎬 YouTube Downloader Pro", 
                    font=ctk.CTkFont(size=24, weight="bold")).pack(pady=10)
        
        ctk.CTkLabel(header_frame, 
                    text="Download video/audio dari YouTube dengan mudah",
                    font=ctk.CTkFont(size=12)).pack(pady=5)
        
        # URL Input Section
        url_frame = ctk.CTkFrame(self.root)
        url_frame.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(url_frame, text="YouTube URL:").pack(anchor="w", pady=(10,5), padx=10)
        self.url_entry = ctk.CTkEntry(url_frame, 
                                     placeholder_text="https://www.youtube.com/watch?v=...",
                                     height=35)
        self.url_entry.pack(pady=5, padx=10, fill="x")
        
        # Get Info Button
        self.info_btn = ctk.CTkButton(url_frame, 
                                     text="🔍 Dapatkan Info Video", 
                                     command=self.get_video_info)
        self.info_btn.pack(pady=10, padx=10)
        
        # Video Info Display
        self.info_frame = ctk.CTkFrame(self.root)
        self.info_frame.pack(pady=10, padx=20, fill="x")
        self.info_frame.pack_forget()  # Sembunyikan awal
        
        # Download Options
        options_frame = ctk.CTkFrame(self.root)
        options_frame.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(options_frame, 
                    text="📥 Download Options", 
                    font=ctk.CTkFont(weight="bold")).pack(anchor="w", pady=(10,5), padx=10)
        
        # Format Selection
        format_frame = ctk.CTkFrame(options_frame)
        format_frame.pack(pady=5, padx=10, fill="x")
        
        ctk.CTkLabel(format_frame, text="Format:").pack(anchor="w", pady=(5,2))
        self.format_var = ctk.StringVar(value="video")
        ctk.CTkRadioButton(format_frame, text="Video (MP4)", 
                          variable=self.format_var, value="video").pack(anchor="w", pady=2)
        ctk.CTkRadioButton(format_frame, text="Audio (MP3)", 
                          variable=self.format_var, value="audio").pack(anchor="w", pady=2)
        
        # Quality Selection
        quality_frame = ctk.CTkFrame(options_frame)
        quality_frame.pack(pady=5, padx=10, fill="x")
        
        ctk.CTkLabel(quality_frame, text="Kualitas:").pack(anchor="w", pady=(5,2))
        self.quality_combo = ctk.CTkComboBox(quality_frame, 
                                           values=["Terbaik", "1080p", "720p", "480p", "360p"])
        self.quality_combo.set("Terbaik")
        self.quality_combo.pack(anchor="w", pady=5, fill="x")
        
        # Download Location
        location_frame = ctk.CTkFrame(options_frame)
        location_frame.pack(pady=5, padx=10, fill="x")
        
        ctk.CTkLabel(location_frame, text="Lokasi Simpan:").pack(anchor="w", pady=(5,2))
        
        location_input_frame = ctk.CTkFrame(location_frame)
        location_input_frame.pack(fill="x", pady=5)
        
        self.location_var = ctk.StringVar(value=os.path.join(os.getcwd(), "downloads"))
        self.location_entry = ctk.CTkEntry(location_input_frame, 
                                         textvariable=self.location_var)
        self.location_entry.pack(side="left", fill="x", expand=True, padx=(0,5))
        
        ctk.CTkButton(location_input_frame, text="📁", 
                     width=40, command=self.browse_location).pack(side="right")
        
        # Progress Section
        progress_frame = ctk.CTkFrame(self.root)
        progress_frame.pack(pady=20, padx=20, fill="x")
        
        self.progress_label = ctk.CTkLabel(progress_frame, text="Siap untuk download")
        self.progress_label.pack(pady=5)
        
        self.progress_bar = ctk.CTkProgressBar(progress_frame)
        self.progress_bar.pack(pady=5, padx=10, fill="x")
        self.progress_bar.set(0)
        
        # Download Button
        self.download_btn = ctk.CTkButton(self.root, 
                                         text="⬇️ Download Sekarang", 
                                         font=ctk.CTkFont(size=16, weight="bold"),
                                         height=40,
                                         command=self.start_download)
        self.download_btn.pack(pady=20, padx=20, fill="x")
        
        # Status Text
        self.status_text = ctk.CTkTextbox(self.root, height=100)
        self.status_text.pack(pady=10, padx=20, fill="both", expand=True)
        self.log_status("Aplikasi siap! Masukkan URL YouTube dan pilih opsi download.")
    
    def setup_bindings(self):
        self.url_entry.bind("<Return>", lambda e: self.get_video_info())
    
    def browse_location(self):
        folder = filedialog.askdirectory()
        if folder:
            self.location_var.set(folder)
    
    def get_video_info(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Masukkan URL YouTube terlebih dahulu!")
            return
        
        self.info_btn.configure(state="disabled", text="Mendapatkan info...")
        
        def get_info_thread():
            try:
                info = self.downloader.get_video_info(url)
                self.root.after(0, self.display_video_info, info)
            except Exception as e:
                self.root.after(0, self.show_error, f"Gagal mendapatkan info: {str(e)}")
            finally:
                self.root.after(0, lambda: self.info_btn.configure(state="normal", text="🔍 Dapatkan Info Video"))
        
        threading.Thread(target=get_info_thread, daemon=True).start()
    
    def display_video_info(self, info):
        # Clear previous info
        for widget in self.info_frame.winfo_children():
            widget.destroy()
        
        # Show info frame
        self.info_frame.pack(pady=10, padx=20, fill="x")
        
        ctk.CTkLabel(self.info_frame, 
                    text="📹 Informasi Video", 
                    font=ctk.CTkFont(weight="bold")).pack(anchor="w", pady=(10,5), padx=10)
        
        info_text = f"Judul: {info['title']}\n"
        info_text += f"Channel: {info['uploader']}\n"
        info_text += f"Durasi: {self.format_duration(info['duration'])}\n"
        info_text += f"Views: {info['view_count']:,}"
        
        ctk.CTkLabel(self.info_frame, 
                    text=info_text, 
                    justify="left").pack(anchor="w", pady=5, padx=10)
        
        self.log_status(f"Info video berhasil didapatkan: {info['title']}")
    
    def format_duration(self, seconds):
        if not seconds:
            return "Unknown"
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return f"{minutes:02d}:{seconds:02d}"
    
    def start_download(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Masukkan URL YouTube!")
            return
        
        # Validasi lokasi
        if not os.path.exists(self.location_var.get()):
            try:
                os.makedirs(self.location_var.get())
            except:
                messagebox.showerror("Error", "Lokasi simpan tidak valid!")
                return
        
        self.download_btn.configure(state="disabled", text="Downloading...")
        self.progress_bar.set(0)
        
        threading.Thread(target=self.download_video, daemon=True).start()
    
    def download_video(self):
        try:
            url = self.url_entry.get()
            format_type = self.format_var.get()
            quality = self.quality_combo.get()
            output_path = self.location_var.get()
            
            self.root.after(0, self.log_status, f"Memulai download...")
            self.root.after(0, lambda: self.progress_bar.set(0.1))
            
            def progress_hook(d):
                if d['status'] == 'downloading':
                    percent = d.get('_percent_str', '0%').strip('%')
                    try:
                        progress = float(percent) / 100
                        self.root.after(0, lambda: self.progress_bar.set(progress))
                        self.root.after(0, self.log_status, f"Downloading: {percent}%")
                    except:
                        pass
                elif d['status'] == 'finished':
                    self.root.after(0, lambda: self.progress_bar.set(1.0))
                    self.root.after(0, self.log_status, "Download selesai! Processing...")
            
            success, message = self.downloader.download(
                url=url,
                format_type=format_type,
                quality=quality,
                output_path=output_path,
                progress_hook=progress_hook
            )
            
            if success:
                self.root.after(0, self.log_status, f"✅ {message}")
                self.root.after(0, lambda: messagebox.showinfo("Sukses", message))
            else:
                self.root.after(0, self.log_status, f"❌ {message}")
                self.root.after(0, lambda: messagebox.showerror("Error", message))
                
        except Exception as e:
            self.root.after(0, self.log_status, f"❌ Error: {str(e)}")
            self.root.after(0, lambda: messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}"))
        finally:
            self.root.after(0, lambda: self.download_btn.configure(state="normal", text="⬇️ Download Sekarang"))
            self.root.after(0, lambda: self.progress_bar.set(0))
    
    def log_status(self, message):
        self.status_text.configure(state="normal")
        self.status_text.insert("end", f"{message}\n")
        self.status_text.see("end")
        self.status_text.configure(state="disabled")
    
    def show_error(self, message):
        messagebox.showerror("Error", message)
        self.log_status(f"❌ {message}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = YouTubeDownloaderApp()
    app.run()