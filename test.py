from fpdf import FPDF
import os
def pdfCreator():
    try:
        fpdf = FPDF('P', 'mm', 'A4')

        fpdf.add_page()
        fpdf.set_margin(15)
        fpdf.add_font("helvetica", '', r'font\helvetica.ttf', uni=True)

        fpdf.set_font("helvetica", 'BI',  24)
        fpdf.cell(0, 30, 'FOGLALÁST AZONOSÍTÓ DOKUMENTUM', True, True, 'C')

        fpdf.set_font("helvetica", 'BI',  30)
        fpdf.cell(0, 40, '', 0, True, 'C')

        fpdf.set_font("helvetica", 'U',  18)
        fpdf.cell(0, 20, 'Foglaló személy', 0, 0, 'L',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  15)
        fpdf.cell(0, 20, '<<------------------------->>', 0, 0, 'C',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  18)
        fpdf.cell(0, 20, 'Személy neve', 0,True, 'R',)
        fpdf.ln(0.33)

        fpdf.set_font("helvetica", 'U',  18)
        fpdf.cell(0, 20, 'Jegy típusa', 0, 0, 'L',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  15)
        fpdf.cell(0, 20, '<<------------------------->>', 0, 0, 'C',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  18)
        fpdf.cell(0, 20, 'Jegyek neve', 0, True, 'R',)
        fpdf.ln(0.33)

        fpdf.set_font("helvetica", 'U',  18)
        fpdf.cell(0, 20, 'Teremszám', 0, 0, 'L',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  15)
        fpdf.cell(0, 20, '<<------------------------->>', 0, 0, 'C',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  18)
        fpdf.cell(0, 20, 'Teremszám', 0, True, 'R',)
        fpdf.ln(0.33)

        fpdf.set_font("helvetica", 'U',  18)
        fpdf.cell(0, 20, 'Lefoglalt székek', 0, 0, 'L',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  15)
        fpdf.cell(0, 20, '<<------------------------->>', 0, 0, 'C',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  18)
        fpdf.cell(0, 20, 'Székek ide', 0, True, 'R',)
        fpdf.ln(0.33)


        fpdf.set_font("helvetica", '',  15)
        fpdf.cell(0, 40, 'FILM INFORMÁCIÓ', 0, True, 'C',)
        fpdf.ln(1)

        fpdf.set_font("helvetica", 'U',  18)
        fpdf.cell(0, 0, 'Film címe', 0, 0, 'L',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  15)
        fpdf.cell(0, 10, '<<------------------------->>', 0, 0, 'C',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  18)
        fpdf.cell(0, 10, 'Filmcím', 0, True, 'R',)
        fpdf.ln(0.33)

        fpdf.set_font("helvetica", 'U',  18)
        fpdf.cell(0, 0, 'Vetítés', 0, 0, 'L',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  15)
        fpdf.cell(0, 10, '<<------------------------->>', 0, 0, 'C',)
        fpdf.ln(0.33)
        fpdf.set_font("helvetica", '',  18)
        fpdf.cell(0, 10, 'percben', 0, True, 'R',)
        fpdf.ln(0.33)

        fpdf.output('sikeres_foglalas.pdf', True)

    except Exception as ex:
        print(ex)

pdfCreator()
