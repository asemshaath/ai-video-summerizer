import os
import openai
import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment

from dotenv import load_dotenv
from pytube import YouTube

load_dotenv('./configs/.env')


# Prompt for YouTube URL
yt = YouTube('https://www.youtube.com/watch?v=2M_kCCcNDts')
# print(yt.streams)
video = yt.streams.filter(only_audio=True).first()
# print(video)

# out_file = video.download(output_path=".")
# os.rename(out_file, 'audio.mp4')


# Return the response of chat gpt when passing the prompt
def gptPrompt(m_prompt):
    openai.organization = os.getenv('OPENAI_ORG')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    openai.Model.list()

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=m_prompt,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6,
    )

    return response.choices[0].text

def mp4_to_text(mp4_file):
    # Convert MP4 audio file to WAV
    wav_audio_file = "temp_audio.wav"
    audio = AudioSegment.from_file(wav_audio_file, format='mp4')
    audio.export(wav_audio_file, format='wav')

    # Initialize the speech recognizer
    recognizer = sr.Recognizer()

    # Load the WAV audio file
    audio = sr.AudioFile(wav_audio_file)

    # Recognize speech from the audio file
    with audio as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)

    # Delete the temporary WAV file
    os.remove(wav_audio_file)

    return text


def main():    
    levels = ["Begginer", "Intermediate", "Proffesional"]
    print(mp4_to_text('audio.mp4'))
    print(gptPrompt("Name 3 countries with letter P"))

if __name__ == "__main__":
    main()

