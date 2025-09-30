from downloader import YouTubeDownloader
import os

def main():
    print("🧪 YouTube Downloader Test")
    print("=" * 50)
    
    downloader = YouTubeDownloader()
    
    # Test dengan video YouTube
    test_url = input("Masukkan URL YouTube untuk test (kosongkan untuk default): ").strip()
    
    if not test_url:
        test_url = "https://www.youtube.com/watch?v=aqz-KE-bpKQ"  # Video test pendek
        print(f"Menggunakan URL default: {test_url}")
    
    try:
        # Test get info
        print("\n1. 🔍 Mendapatkan info video...")
        info = downloader.get_video_info(test_url)
        print(f"   ✅ Judul: {info['title']}")
        print(f"   ✅ Channel: {info['uploader']}")
        print(f"   ✅ Durasi: {info['duration']} detik")
        
        # Test download
        print("\n2. 📥 Test download (10 detik pertama)...")
        success, message = downloader.download(
            url=test_url,
            format_type="video",
            quality="360p",
            output_path="./test_downloads"
        )
        
        if success:
            print(f"   ✅ {message}")
        else:
            print(f"   ❌ {message}")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n🎯 Test selesai!")

if __name__ == "__main__":
    main()