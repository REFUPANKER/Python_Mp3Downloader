import os
import yt_dlp
from pydub import AudioSegment

outputFolder = r'C:\Users\Computer\Documents\Rockstar Games\GTA V\User Music'

def download_youtube_audio(url, output_path=outputFolder):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': './',  # Proje dizinindeki ffmpeg.exe'yi kullanır
        'quiet': True,
        'noplaylist': True  # Sadece tek video indirin
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Video bilgilerini al
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', 'Unknown Title')

        print(f"Processing: {video_title}")

        # Video indir
        ydl.download([url])

    print(f"Download completed: {video_title}")

def list_music_files(folder):
    try:
        files = os.listdir(folder)
        if files:
            print("Music Files:")
            for file in files:
                print(file)
        else:
            print("No files found in the output folder.")
    except FileNotFoundError:
        print("Output folder not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("-" * 40)
        print("""Commands:
exit  > quit
start > open output folder 
list  > list music files""")
        command = input("Enter command or paste YouTube URL: ").strip()
        
        match command.lower():
            case 'exit':
                print("App ended")
                break
            case 'start':
                os.startfile(outputFolder)
            case 'list':
                list_music_files(outputFolder)
            case _:
                # Assume it's a URL
                download_youtube_audio(command)

if __name__ == "__main__":
    main()
