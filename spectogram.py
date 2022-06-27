import librosa
import glob

def generate_spec(path):
    file, sr = librosa.load(path)
    y = librosa.stft(file)
    return y