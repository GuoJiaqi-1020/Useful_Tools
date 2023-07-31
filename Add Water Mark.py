import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def create_watermark(content):
    c = canvas.Canvas("watermark.pdf")
    c.setFont("Helvetica", 80)
    c.setFillAlpha(0.3)
    c.setStrokeAlpha(0.3)
    c.rotate(45)
    c.drawString(100, 100, content)
    c.save()


def add_watermark(input_pdf, output_pdf, watermark):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)


def watermark_pdf(input_pdf_path, watermark_text, output_pdf_path):
    create_watermark(watermark_text)
    add_watermark(input_pdf_path, output_pdf_path, "watermark.pdf")


if __name__ == "__main__":
    watermark_pdf("source.pdf", "Used only for I-20 Update, BOCUSA, 2023/7/31", "result.pdf")
