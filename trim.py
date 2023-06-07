from audioclipextractor import AudioClipExtractor, SpecsParser
import os, glob

path = r"C:/Users/Administrator/Downloads/audio/Acapella/*.wav"
files = glob.glob(path)
number = 0

while(number < 20):
    audio = files[number]
    audio_s = audio.split("/")[-1]  
    audio_s = audio_s.split("\\")[-1] 
    audio_s = audio_s.split(".")[0]

    number = number + 1
    os.system(f"ffmpeg -i {audio} -af silenceremove=start_periods=1:stop_periods=-1:start_threshold=-30dB:stop_threshold=-30dB:start_silence=0.5:stop_silence=0.5 {audio_s}-silence.wav")
    ext = AudioClipExtractor(f"{audio_s}-silence.wav", 'C:/Users/Administrator/ffmpeg/bin/ffmpeg.exe')
    
    specs = '''
        0 15 
        15 30 
        30 45
        45 60
        60 75
        75 90
    '''
    os.makedirs(f'C:/Users/Administrator/Downloads/audio/{audio_s}/')
    ext.extract_clips(specs, f'C:/Users/Administrator/Downloads/audio/{audio_s}/', zip_output=False)
    os.remove(f'C:/Users/Administrator/Downloads/{audio_s}-silence.wav')
