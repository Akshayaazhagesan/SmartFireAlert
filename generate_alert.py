from pydub import AudioSegment
from pydub.generators import Sine
import os

# Tell pydub where ffmpeg is
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
import pyttsx3
from pydub import AudioSegment
from pydub.generators import Sine
import time

# STEP 1: Create a beep sound (1000 Hz, 500 ms)
beep = Sine(1000).to_audio_segment(duration=500)
beep.export("beep.wav", format="wav")

# STEP 2: Use pyttsx3 to speak the alert message
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed if needed
engine.save_to_file("Fire Alert! Please evacuate immediately!", "alert.wav")
engine.runAndWait()

# STEP 3: Wait for file to be saved properly
time.sleep(2)

# STEP 4: Combine beep + short pause + TTS alert
final_audio = AudioSegment.from_wav("beep.wav") + AudioSegment.silent(duration=300) + AudioSegment.from_wav("alert.wav")
final_audio.export("alarm.mp3", format="mp3")

print("✅ Done! You can now use alarm.mp3 in your fire detection.")
