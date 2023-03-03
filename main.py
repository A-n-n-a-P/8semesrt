from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.add_font('DejaVu', '',fname='font\\DejaVuSerif-Italic.ttf', uni=True)
pdf.set_font("DejaVu", size=30)
pdf.cell(200, 10, txt="СЕРТИФИКАТ", ln=1, align="C")
pdf.output("D:\\Popova\\pdf\\Certificate.pdf")
