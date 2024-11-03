from google.cloud import texttospeech
import re

class GoogleTextToSpeechService:

    # This class is used to generate audio files from text using Google Text-to-Speech API.
    # Gemini uses this class to generate audio files for talk during meetings.

    client = texttospeech.TextToSpeechClient()

    async def generate_audio(self, text, output_file: str):
         # clear punctuation marks from text
        text = str(text)  
        text = re.sub(r'[^\w\s]', '', text)

        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code='tr-TR',
            name='tr-TR-Wavenet-C',
            ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = self.client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        with open(f'{output_file}.mp3', 'wb') as out:
            out.write(response.audio_content)
