#pip install moviepy

from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("Sample.mp4")

videoClip.write_gif("Sample.gif")