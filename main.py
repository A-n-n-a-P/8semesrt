from fpdf import FPDF

def input(text, position, gorizontal, vertical, size, align):
    pdf.add_font('DejaVu', '', fname='font\\DejaVuSerif-Italic.ttf')
    pdf.set_font("DejaVu", size=size)
    pdf.ln(position)
    pdf.cell(gorizontal, vertical, txt=text, align=align)



pdf = FPDF()
pdf.add_page()

ussr="СССР"
diplom="Диплом"
degree="Ⅰ степени"
name="Юрий Алексеевич"
lastName="Гагарин"



input(ussr, 23, 180, 10, 60, "C")
input(diplom, 23, 180, 10, 60, "C")
input(degree, 23, 180, 10, 60, "C")
input(ussr, 23, 180, 10, 60, "C")
#pdf.image('D:\\Popova\\pdf\\hedgehog.jpg', x=10, y=10, w=100)



pdf.output("D:\\Popova\\pdf\\Certificate.pdf")
