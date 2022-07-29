from pdftotext import PdfToText
from texttoaudio import TextToAudio

PDF_FILE = "sample_en_us.pdf"
LOCALE = "en_US"

pdf = PdfToText(PDF_FILE)

text = pdf.all_text()
text_to_audio = TextToAudio(LOCALE)
# optional set gender
# text_to_audio.set_gender("FEMALE")

for i in range(len(text)):
    text_to_audio.convert(text[i], f"output_{i}.mp3")
