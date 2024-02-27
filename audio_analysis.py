import librosa
import matplotlib.pyplot as plt
from glob import glob
import os

F2F_paths = "data/Face-to-Face/**/*.mp4"

globs = glob(F2F_paths)

for idx, audio_path in enumerate(globs):
    y, sr = librosa.load(audio_path)

    librosa.display.waveshow(y, sr=sr)
    plt.title(os.path.basename(audio_path))
    plt.show()

    if idx > 20:
        break

