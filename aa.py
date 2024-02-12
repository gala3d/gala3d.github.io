from moviepy.editor import VideoFileClip

clip = VideoFileClip("./top/2.mp4")
clip_resized = clip.resize(height=1024)  # Resize video to height of 1024 pixels
clip_resized.write_videofile("./2.mp4")
