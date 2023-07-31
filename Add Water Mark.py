from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def get_pdf_size(pdf_path):
    pdf = PdfFileReader(pdf_path)
    first_page = pdf.getPage(0)
    return first_page.mediaBox.getWidth(), first_page.mediaBox.getHeight()


def create_watermark(content, input_pdf_path):
    w, h = get_pdf_size(input_pdf_path)
    c = canvas.Canvas("watermark.pdf")
    c.setFont("Helvetica", 40)
    c.setFillAlpha(0.3)
    c.setStrokeAlpha(0.3)
    c.rotate(45)
    c.drawString(120, 50, content)
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
    create_watermark(watermark_text, input_pdf_path)
    add_watermark(input_pdf_path, output_pdf_path, "watermark.pdf")


if __name__ == '__main__':
    pdf_file_in = 'Jiaqi_phd_I20.pdf'
    pdf_file_out = 'watermarked.pdf'
    pdf_file_mark = 'USED ONLY FOR I20 UPDATE, BOCUSA'
    watermark_pdf(pdf_file_in, pdf_file_mark, pdf_file_out)
