from google.cloud import texttospeech


class TextToAudio:

    def __init__(self, locale):
        self.locale = locale
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.VoiceSelectionParams(
            language_code=self.locale,
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        self.audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    def set_gender(self, gender):
        try:
            gender_mapping = {
                "NEUTRAL": texttospeech.SsmlVoiceGender.NEUTRAL,
                "MALE": texttospeech.SsmlVoiceGender.MALE,
                "FEMALE": texttospeech.SsmlVoiceGender.FEMALE
            }
            self.voice = texttospeech.VoiceSelectionParams(language_code=self.locale,
                                                           ssml_gender=gender_mapping[gender.upper()])
        except KeyError:
            print("Error: Specified gender is not available.")

    def convert(self, text, output_file):
        synthesis_input = texttospeech.SynthesisInput(text=text)
        response = self.client.synthesize_speech(
            input=synthesis_input,
            voice=self.voice,
            audio_config=self.audio_config
        )
        with open(output_file, "wb") as out:
            out.write(response.audio_content)
            print(f'Audio content written to file "{output_file}"')
