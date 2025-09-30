import os
import re
import math
from typing import Optional, Tuple
from datetime import datetime
import threading

class DownloadUtils:
    @staticmethod
    def format_file_size(size_bytes: int) -> str:
        """Format ukuran file menjadi readable string"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB", "TB"]
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_names[i]}"
    
    @staticmethod
    def format_duration(seconds: int) -> str:
        """Format durasi dalam detik menjadi HH:MM:SS"""
        if not seconds:
            return "Unknown"
        
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return f"{minutes:02d}:{seconds:02d}"
    
    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """Membersihkan nama file dari karakter tidak valid"""
        # Remove invalid characters for Windows
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '')
        
        # Remove extra spaces and trim
        filename = re.sub(r'\s+', ' ', filename).strip()
        
        # Limit length to 200 characters
        if len(filename) > 200:
            name, ext = os.path.splitext(filename)
            filename = name[:200-len(ext)] + ext
        
        return filename
    
    @staticmethod
    def is_valid_youtube_url(url: str) -> bool:
        """Validasi apakah URL YouTube valid"""
        youtube_patterns = [
            r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w-]+',
            r'^(https?://)?(www\.)?youtube\.com/playlist\?list=',
            r'^(https?://)?(www\.)?youtube\.com/shorts/'
        ]
        
        return any(re.match(pattern, url) for pattern in youtube_patterns)
    
    @staticmethod
    def get_file_extension(format_type: str, quality: str) -> str:
        """Dapatkan ekstensi file berdasarkan format dan kualitas"""
        if format_type == 'audio':
            return '.mp3'
        else:
            return '.mp4'
    
    @staticmethod
    def create_download_folder(base_path: str = "downloads") -> str:
        """Membuat folder download dengan timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_name = f"youtube_downloads_{timestamp}"
        folder_path = os.path.join(base_path, folder_name)
        
        os.makedirs(folder_path, exist_ok=True)
        return folder_path
    
    @staticmethod
    def get_available_disk_space(path: str) -> Tuple[int, str]:
        """Mendapatkan available disk space"""
        try:
            import shutil
            total, used, free = shutil.disk_usage(path)
            return free, DownloadUtils.format_file_size(free)
        except:
            return 0, "Unknown"

class ProgressTracker:
    """Class untuk melacak progress download"""
    
    def __init__(self):
        self.current_progress = 0
        self.current_speed = "0 B/s"
        self.current_status = ""
        self.lock = threading.Lock()
    
    def update(self, progress: float, speed: str = "", status: str = ""):
        """Update progress dengan thread safety"""
        with self.lock:
            self.current_progress = progress
            if speed:
                self.current_speed = speed
            if status:
                self.current_status = status
    
    def get_progress(self) -> Tuple[float, str, str]:
        """Dapatkan progress current"""
        with self.lock:
            return self.current_progress, self.current_speed, self.current_status
    
    def reset(self):
        """Reset progress tracker"""
        with self.lock:
            self.current_progress = 0
            self.current_speed = "0 B/s"
            self.current_status = ""

class FileManager:
    """Class untuk management file dan folder"""
    
    @staticmethod
    def get_files_in_folder(folder_path: str) -> list:
        """Dapatkan list file dalam folder"""
        try:
            if not os.path.exists(folder_path):
                return []
            
            files = []
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isfile(item_path):
                    files.append({
                        'name': item,
                        'path': item_path,
                        'size': FileManager.get_file_size(item_path),
                        'modified': datetime.fromtimestamp(os.path.getmtime(item_path))
                    })
            
            # Sort by modified date (newest first)
            files.sort(key=lambda x: x['modified'], reverse=True)
            return files
        except:
            return []
    
    @staticmethod
    def get_file_size(file_path: str) -> str:
        """Dapatkan ukuran file yang diformat"""
        try:
            size = os.path.getsize(file_path)
            return DownloadUtils.format_file_size(size)
        except:
            return "Unknown"
    
    @staticmethod
    def delete_file(file_path: str) -> bool:
        """Hapus file"""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
        except:
            pass
        return False
    
    @staticmethod
    def open_file_location(file_path: str):
        """Buka lokasi file di file explorer"""
        try:
            import subprocess
            folder_path = os.path.dirname(file_path)
            if os.name == 'nt':  # Windows
                os.startfile(folder_path)
            elif os.name == 'posix':  # macOS/Linux
                subprocess.call(['open' if sys.platform == 'darwin' else 'xdg-open', folder_path])
            return True
        except:
            return False

def format_quality_string(quality: str) -> str:
    """Format string kualitas untuk display"""
    quality_map = {
        'best': 'Terbaik',
        '1080p': '1080p (Full HD)',
        '720p': '720p (HD)',
        '480p': '480p (SD)',
        '360p': '360p',
        '240p': '240p'
    }
    return quality_map.get(quality, quality)

def validate_download_path(path: str) -> Tuple[bool, str]:
    """Validasi path download"""
    try:
        # Cek jika path ada
        if not os.path.exists(path):
            # Coba buat folder
            os.makedirs(path, exist_ok=True)
        
        # Cek jika writable
        test_file = os.path.join(path, 'test_write.tmp')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        
        return True, "Path valid dan writable"
        
    except PermissionError:
        return False, "Tidak ada izin menulis ke folder ini"
    except Exception as e:
        return False, f"Error: {str(e)}"

# Test functions
def test_utils():
    """Test semua utility functions"""
    print("🧪 Testing Utility Functions...")
    
    # Test format file size
    print(f"📏 1000 bytes = {DownloadUtils.format_file_size(1000)}")
    print(f"📏 1500000 bytes = {DownloadUtils.format_file_size(1500000)}")
    
    # Test format duration
    print(f"⏱️ 3665 seconds = {DownloadUtils.format_duration(3665)}")
    
    # Test sanitize filename
    test_filename = 'File<with>invalid"chars?.mp4'
    print(f"📝 Sanitized: {DownloadUtils.sanitize_filename(test_filename)}")
    
    # Test YouTube URL validation
    test_urls = [
        'https://www.youtube.com/watch?v=abc123',
        'https://youtu.be/abc123',
        'invalid-url'
    ]
    for url in test_urls:
        print(f"🔗 {url} = {DownloadUtils.is_valid_youtube_url(url)}")

if __name__ == "__main__":
    test_utils()