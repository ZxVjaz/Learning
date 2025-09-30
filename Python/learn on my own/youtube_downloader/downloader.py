import yt_dlp
import os
from typing import Tuple, Dict, Optional, Callable
from utils import DownloadUtils, ProgressTracker

class YouTubeDownloader:
    def __init__(self):
        self.ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'restrictfilenames': True,
            'noplaylist': True,
        }
        self.progress_tracker = ProgressTracker()
    
    def get_video_info(self, url: str) -> dict:
        """Mendapatkan informasi video"""
        if not DownloadUtils.is_valid_youtube_url(url):
            raise Exception("URL YouTube tidak valid")
            
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
                return {
                    'title': info.get('title', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'duration_formatted': DownloadUtils.format_duration(info.get('duration', 0)),
                    'uploader': info.get('uploader', 'Unknown'),
                    'view_count': info.get('view_count', 0),
                    'thumbnail': info.get('thumbnail', ''),
                    'description': info.get('description', '')[:200] + '...' if info.get('description') else '',
                    'formats': info.get('formats', [])
                }
            except Exception as e:
                raise Exception(f"Gagal mendapatkan info video: {str(e)}")
    
    def create_progress_hook(self) -> Callable:
        """Membuat progress hook function"""
        def progress_hook(d):
            if d['status'] == 'downloading':
                # Extract progress percentage
                percent = d.get('_percent_str', '0%').strip('%')
                try:
                    progress = float(percent) / 100
                except:
                    progress = 0
                
                # Extract download speed
                speed = d.get('_speed_str', '0 B/s')
                
                self.progress_tracker.update(
                    progress=progress,
                    speed=speed,
                    status=f"Downloading... {percent}%"
                )
                
            elif d['status'] == 'finished':
                self.progress_tracker.update(
                    progress=1.0,
                    status="Processing..."
                )
                
        return progress_hook
    
    def download(self, url: str, format_type: str = 'video', 
                quality: str = 'Terbaik', output_path: str = './downloads',
                progress_callback: Optional[Callable] = None) -> Tuple[bool, str]:
        """Download video/audio"""
        
        # Validasi URL
        if not DownloadUtils.is_valid_youtube_url(url):
            return False, "URL YouTube tidak valid"
        
        # Validasi dan buat folder
        is_valid, msg = DownloadUtils.validate_download_path(output_path)
        if not is_valid:
            return False, f"Path tidak valid: {msg}"
        
        # Reset progress tracker
        self.progress_tracker.reset()
        
        # Konfigurasi berdasarkan format
        if format_type == 'audio':
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'restrictfilenames': True,
                'writethumbnail': True,
            }
        else:
            # Konfigurasi untuk video
            if quality == 'Terbaik':
                format_selector = 'best[height<=1080]'
            else:
                height = quality.replace('p', '')
                format_selector = f'best[height<={height}]'
            
            ydl_opts = {
                'format': format_selector,
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'restrictfilenames': True,
                'writethumbnail': True,
            }
        
        # Tambahkan progress hook
        ydl_opts['progress_hooks'] = [self.create_progress_hook()]
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                
                # Dapatkan nama file yang sebenarnya
                filename = ydl.prepare_filename(info)
                if format_type == 'audio':
                    filename = filename.rsplit('.', 1)[0] + '.mp3'
                
                # Cek jika file berhasil dibuat
                if not os.path.exists(filename):
                    return False, "File tidak berhasil dibuat"
                
                file_size = os.path.getsize(filename)
                file_size_formatted = DownloadUtils.format_file_size(file_size)
                
                return True, f"✅ Berhasil didownload!\n📁 {os.path.basename(filename)}\n💾 Size: {file_size_formatted}"
                
        except Exception as e:
            return False, f"❌ Gagal download: {str(e)}"