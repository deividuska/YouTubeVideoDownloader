"""
This script downloads a YouTube video with a resolution of 720p using the PyTube library.
The video URL and the location where the video will be saved are specified in the script.
A progress bar is displayed during the download process.
"""

# Import the YouTube class from the pytube module
from pytube import YouTube

# Specify the URL of the video that you want to download
video_url = 'https://youtu.be/your-video-url'

# Specify the location where you want to save the video
save_path = 'videos'

# Create a YouTube object
yt = YouTube(video_url)

# Fetch the video stream with 720p resolution
video = yt.streams.get_by_resolution('720p')

# Define a progress callback function to display a progress bar
def progress_function(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    print(f' {percent}% [{status}]', end='\r')

# Assign the callback function to the YouTube object
yt.register_on_progress_callback(progress_function)

# Check if the stream is available
if video:
    # Download the video with a progress bar
    video.download(output_path=save_path)
    print(f'\nVideo downloaded successfully at {save_path}')
else:
    print('720p resolution not available for this video')
  
