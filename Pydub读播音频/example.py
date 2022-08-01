from pydub import AudioSegment
from pydub.playback import play


"""
pip3 install pydub
brew install ffmpeg
pip3 install ffmpeg-python
"""
song = AudioSegment.from_wav("0.wav")
play(song)
print(type(song))
song = song.set_frame_rate(24000)
song = song.set_channels(1)
print(len(song.raw_data), song.raw_data)
# song.export('new_o.wav', format='wav')
# 读取1s
audio_length = 1 * 1000
begin_song = song[: audio_length]
end_song = song[1:]
# 加10db
begin_song += 10
# 减5db
end_song -= 5
# 连接音频
new_song = begin_song + end_song
