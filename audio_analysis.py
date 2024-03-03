import librosa
import matplotlib.pyplot as plt
from glob import glob
import os
from pydub import AudioSegment
import numpy as np

SILENCE_THRESHOLD = -96.0


def get_bit_depth(audio_file):
    audio = AudioSegment.from_file(audio_file)
    sample_width = audio.sample_width
    bit_depth = sample_width * 8  # Convert bytes to bits
    return bit_depth


def analyze_audio(audio_file):
    audio = AudioSegment.from_file(audio_file)

    bit_depth = get_bit_depth(audio_file)
    print(f'bit_depth: {bit_depth}')

    # Define chunk length in milliseconds
    chunk_length_ms = 1000  # 1 second

    # Split audio into 1-second chunks
    chunks = [audio[i:i+chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

    # Calculate the dBFS for each chunk
    dbfs_values = [chunk.dBFS for chunk in chunks]

    # Convert the list of dBFS values to a NumPy array
    dbfs_array = np.array(dbfs_values)

    # Replace -inf values with the chosen silence threshold
    dbfs_array = np.where(np.isneginf(dbfs_array), SILENCE_THRESHOLD, dbfs_array)

    return dbfs_array


def plot_sound_levels(dbfs_values, title='Sound Level Overview'):
    plt.figure(figsize=(10, 6))
    plt.plot(dbfs_values)
    plt.title(title)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Average dBFS')
    plt.grid(True)
    plt.show()


def plot_sound_levels_overview(dbfs_data, title='Sound Level Overview'):
    plt.figure(figsize=(15, 8))

    # Flags to ensure each label is only added once
    silent_label_added = False
    non_silent_label_added = False

    for key, val in dbfs_data.items():
        data, is_silent, partly_silent = val
        if is_silent and not silent_label_added:
            plt.plot(data, color='blue', alpha=0.7, label='Silent')
            silent_label_added = True  # Ensure label is added only once
        elif not is_silent and not non_silent_label_added:
            plt.plot(data, color='green', alpha=0.7, label='Non-Silent')
            non_silent_label_added = True  # Ensure label is added only once
        else:
            # Plot without adding a label
            color = 'blue' if is_silent else 'green'
            plt.plot(data, color=color, alpha=0.7)

    plt.title(title)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Average dBFS')
    plt.grid(True)
    plt.legend()  # Display the legend
    plt.show()


def main():
    F2F_paths = "data/Zoom/**/*.mp4"

    globs = glob(F2F_paths)

    dbfs_data = {}  # This will store tuples of (dbfs_values, is_silent)

    for path in globs:
        # audio_file = 'data/Face-to-Face/F1A/F1A.mp4'
        dbfs_values = analyze_audio(path)

        print(f'{os.path.basename(path)} mean: {np.mean(dbfs_values)}')
        print(f'{os.path.basename(path)} std: {np.std(dbfs_values)}')

        file_mean = np.mean(dbfs_values)
        is_silent = file_mean < -90
        partly_silent = np.any(dbfs_values == SILENCE_THRESHOLD)

        if is_silent:
            print(f'file {os.path.basename(path)} is silent')

        dbfs_data[path] = (dbfs_values, is_silent, partly_silent)

    plot_sound_levels_overview(dbfs_data)

if __name__ == '__main__':
    main()