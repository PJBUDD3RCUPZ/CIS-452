from gtts import gTTS
import os

mytext = "his course introduces basic techniques for visualization, quantitative analysis intelligent visualunderstanding, virtualization, digital animation, computer and video games, and web multimedia. Topics include data visualization, computer vision, visual analysis, the process of creating animated video clips from start to finish (including story creation, storyboarding, modeling, animation, and post-production), and computer virtualization; several key techniques include graphic design, video editing, motion generation, motion capture, multimedia, real-time rendering, visualization tools, and virtual machine"

language = 'fr'

recording = gTTS(text = mytext, lang = language)
recording.save("frRecording.mp3")
os.system("start frRecording.mp3")