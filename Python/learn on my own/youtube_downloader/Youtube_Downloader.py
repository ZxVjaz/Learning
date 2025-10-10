import os
import yt_dlp
import sys

def get_input(prompt):
    print(prompt, end='', flush=True)
    return sys.stdin.readline().strip()

def create_download_folder():
    folder = "download"
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def get_video_formats(url):
    ydl_opts = {'listformats': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info

def download_media(url, media_type, resolution=None):
    download_folder = create_download_folder()
    
    # Jika Anda perlu menentukan lokasi FFmpeg, ganti path di bawah ini
    ffmpeg_path = \
    None
    # Ganti dengan path ke ffmpeg Anda atau None jika sudah di PATH
    
    if media_type == "video":
        if resolution == "terbaik":
            format_string = "bestvideo+bestaudio/best"
        else:
            format_string = f"bestvideo[height<={resolution}]+bestaudio/best"
        
        ydl_opts = {
            'format': format_string,
            'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }
    else:  # audio
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    # Jika ffmpeg_path ditentukan, tambahkan ke ydl_opts
    if ffmpeg_path:
        ydl_opts['ffmpeg_location'] = ffmpeg_path

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download berhasil!")
    except Exception as e:
        print(f"Terjadi error: {str(e)}")

def main():
    print("=== YouTube Downloader ===")
    print("-------------------------")
    print(' Created by @Memeyann_')
    print("-------------------------")
    url = get_input("Masukkan URL YouTube: ")
    
    print("\nPilih jenis unduhan:")
    print("1. Video")
    print("2. Audio")
    pilihan = input("Masukkan pilihan (1/2): ").strip()

    if pilihan == "1":
        # Dapatkan daftar resolusi yang tersedia
        info = get_video_formats(url)
        available_resolutions = sorted(
            {f['height'] for f in info['formats'] if f.get('height') is not None},
            reverse=True
        )
        
        print("\nResolusi yang tersedia:")
        for i, res in enumerate(available_resolutions, 1):
            print(f"{i}. {res}p")
        print(f"{len(available_resolutions)+1}. Terbaik")
        
        try:
            pilih_res = int(input("Pilih resolusi (nomor): "))
            if 1 <= pilih_res <= len(available_resolutions):
                resolution = available_resolutions[pilih_res-1]
            elif pilih_res == len(available_resolutions)+1:
                resolution = "terbaik"
            else:
                print("Pilihan tidak valid!")
                return
        except ValueError:
            print("Input harus angka!")
            return

        download_media(url, "video", resolution)

    elif pilihan == "2":
        download_media(url, "audio")

    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()