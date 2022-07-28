from PyPDF2 import PdfReader


class PdfToText:

    def __init__(self, file):
        self.reader = PdfReader(file)
        self.number_of_pages = len(self.reader.pages)

    def all_text(self):
        text = []
        for i in range(self.number_of_pages):
            text.append(self.reader.pages[i].extract_text())
        return text

    def page_text(self, page):
        try:
            return self.reader.pages[page].extract_text()
        except IndexError:
            return "Error: Specified page number is not available."
