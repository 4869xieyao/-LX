# 导入editor包中的AudioFileClip类
from moviepy.editor import AudioFileClip

#要转换的MP4路径
mp4 = AudioFileClip("C:\\Users\\kid\\Desktop\\VideoDom\\xunlianji2.mp4")
mp4.write_audiofile("C:\\Users\\kid\\Desktop\\VideoDom\\EG2.mp3")
print("导入完成")
