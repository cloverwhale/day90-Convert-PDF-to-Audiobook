from pdftotext import PdfToText
from texttoaudio import TextToAudio

PDF_FILE = "sample_en_us.pdf"
LOCALE = "en_US"
GENDER = "FEMALE"

pdf = PdfToText(PDF_FILE)

text = pdf.all_text()

for i in range(len(text)):
    text_to_audio = TextToAudio(LOCALE)
    text_to_audio.set_gender(GENDER)
    text_to_audio.convert(text[i], f"output_{i}.mp3")
