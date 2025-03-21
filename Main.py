import yt_dlp
import os
import json

COUNTER_FILE = "download_counter.json"
MAX_DOWNLOADS = 10

def load_counter():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as file:
            data = json.load(file)
            return data.get("count", 0)
    return 0

def save_counter(count):
    with open(COUNTER_FILE, "w") as file:
        json.dump({"count": count}, file)

def download_video(url, output_path="Downloads"):
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    count = load_counter()
    if count >= MAX_DOWNLOADS:
        print(f"You have exceeded the limit of {MAX_DOWNLOADS} downloads.")
        return

    while count < MAX_DOWNLOADS:
        video_url = input("Enter YouTube video URL (or type 'no' if you need help copying): ").strip()
        if video_url.lower() == "no":
            print("Go to the YouTube video, click 'Share', then 'Copy Link'.")
            continue

        download_video(video_url)
        count += 1
        save_counter(count)
        print(f"Downloaded: {count} of {MAX_DOWNLOADS} videos.")

        if count >= MAX_DOWNLOADS:
            print("You have reached the maximum download limit.")
            break

        print("\nChoose an option:")
        print("1. Download next video")
        print("2. Re-download same video")
        print("3. Exit")
        choice = input("Enter option (1/2/3): ").strip()

        if choice == '1':
            continue
        elif choice == '2':
            download_video(video_url)
            count += 1
            save_counter(count)
            print(f"Downloaded: {count} of {MAX_DOWNLOADS} videos.")
        elif choice == '3':
            print("Exiting. Have a good day!")
            break
        else:
            print("Invalid option, exiting for safety.")
            break

if __name__ == "__main__":
    main()