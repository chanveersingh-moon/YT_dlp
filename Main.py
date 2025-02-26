import yt_dlp

def download_video(url, output_path="Downloads"):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
 print("If you do not know how copy URl then input |no|")
if __name__ == "__main__":
    video_url = input("Enter YouTube video URL extratced form vedio: ")
    download_video(video_url)
