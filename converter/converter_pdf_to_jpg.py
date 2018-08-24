from tkinter import filedialog as fd
from wand.color import Color
from wand.image import Image


def generator(pages_count, pdf_img):
    """Generator, runs through each page from the list"""

    page = 0
    while page < pages_count:
        yield pdf_img.sequence[page]
        page += 1


def new_file():
    """Opens the selected pdf file,
    creates a list of all pages and creates a new file as wide as one page and height as the sum of all the pages.
    Next combines one page into a new file and converts it to jpeg"""
    with Image(filename=file_path) as img_pdf:
        pdf_list = img_pdf.sequence
        pages = len(pdf_list)
        with Image(width=img_pdf.width, height=img_pdf.height*pages, background=Color("white")) as img_jpg:
            count = 0
            for img in generator(pages, img_pdf):
                img_jpg.composite(img, top=img.height * count, left=0)
                count += 1
            img_jpg.convert('jpeg')
            img_jpg.save(filename="new.jpg")


file_path = fd.askopenfilename(filetypes=(("PDF File", "*.pdf"), ("All Files", "*.*")))
new_file()
