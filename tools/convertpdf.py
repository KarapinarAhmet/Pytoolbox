from fpdf import FPDF
import os

def convert_to_pdf(txt_file):
    if not os.path.exists(txt_file):
        print(f"{txt_file} bulunamadı!")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    with open(txt_file, "r", encoding="utf-8") as f:
        for line in f:
            pdf.cell(0, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), ln=True)

    output_pdf = os.path.splitext(txt_file)[0] + ".pdf"
    pdf.output(output_pdf)
    print(f"PDF oluşturuldu: {output_pdf}")
