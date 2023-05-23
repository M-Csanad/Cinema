from fpdf import FPDF
import os
def pdfCreator():
    try:
        fpdf = FPDF('P', 'mm', 'A4')
        fpdf.add_page()
        fpdf.set_font("helvetica", '',  45)
        fpdf.cell(150, 150, 'Foglalást igazoló dokumentum', ln=True)
        fpdf.output(name = 'foglalas.pdf', dest = '')
        os.open('foglalas.pdf')
    except:
        os.remove('foglalas.pdf')
        pdfCreator()
pdfCreator()
