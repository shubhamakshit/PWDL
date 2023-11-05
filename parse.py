import csv
import re
import os
os.system('sudo apt install  ffmpeg -y')
def convert_url(url):
    # Replace "*.cloudfront" with "d26g5bnklkwsh4.cloudfront"
    converted_url = re.sub(r"([a-z0-9]+)\.cloudfront\.net", r"d26g5bnklkwsh4.cloudfront.net", url)
    # Replace "<int>.mp4" with "hls/720/main.m3u8"
    converted_url = converted_url.replace('/dash/audio', '')
    converted_url = re.sub(r"\d+\.mp4", "hls/720/main.m3u8", converted_url)
    return converted_url

def sanitize_name(name):
    # Remove unsafe characters and replace them with a dot (.)
    sanitized_name = re.sub(r"[^\w.]", ".", name)
    return sanitized_name

def download_video(name, link):
    # Execute FFmpeg command to download the video
    command = f'ffmpeg -i "{link}" -c copy "{name}.mp4"'
    os.system(command)

input_file = "input.csv"  # Path to the CSV file containing the input data

# Read data from the CSV file
with open(input_file, "r") as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Skip the header row if present
    # Process each row in the CSV file
    count=1
    for row in csv_data:
        name = row[0].strip()
        link = row[1].strip()
        
        converted_link = convert_url(link)
        
        sanitized_name = sanitize_name(name)
        # Download the video using FFmpeg
        download_video(sanitized_name, converted_link)
