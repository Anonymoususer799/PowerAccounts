from fpdf import FPDF

class PDFGenerator(FPDF):
    def __init__(self, title):
        super().__init__()
        self.title = title

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, self.title, border=False, ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_content(self, content):
        self.set_font('Arial', '', 12)
        for line in content:
            self.cell(0, 10, line, ln=True)

def generate_pdf(title, content):
    pdf = PDFGenerator(title)
    pdf.add_page()
    pdf.add_content(content)
    file_path = f'{title.replace(" ", "_")}.pdf'
    pdf.output(file_path)
    return file_path