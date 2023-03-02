import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Set the path to the folder containing the audio files
folder_path = "/path/to/audio/folder"

# Set the minimum silence length in milliseconds
min_silence_len = 500

# Set the silence threshold in decibels
silence_thresh = -40

# Loop through all the files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".mp3"):
        # Load the audio file using pydub
        file_path = os.path.join(folder_path, file_name)
        sound = AudioSegment.from_file(file_path, format="mp3")
        
        # Split the audio file on silence
        chunks = split_on_silence(sound, min_silence_len=min_silence_len, silence_thresh=silence_thresh)
        
        # Create a new directory to save the VAD segments
        vad_folder_path = os.path.join(folder_path, "vad")
        os.makedirs(vad_folder_path, exist_ok=True)
        
        # Save each VAD segment as a new file
        for i, chunk in enumerate(chunks):
            chunk_file_name = f"{file_name}_{i}.wav"
            chunk_file_path = os.path.join(vad_folder_path, chunk_file_name)
            chunk.export(chunk_file_path, format="wav")
