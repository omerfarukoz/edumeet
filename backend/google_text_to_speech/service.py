from google.cloud import texttospeech


class GoogleTextToSpeechService:

    client = texttospeech.TextToSpeechClient()

    def generate_audio(self, text, output_file: str):
           
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code='tr-TR',
            name='tr-TR-Wavenet-C',
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
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