from fpdf import FPDF
import pandas as pd

# Defining PDF parameters
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,  margin=0)

# Extracting data from CSV file
df = pd.read_csv("topics.csv")

for index, rows in df.iterrows():
    for i in range(rows["Pages"]):
        pdf.add_page()

        # Adding Header for the First Page
        if i == 0:
            pdf.set_font(family="Times", style="B", size=24)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(w=0, h=12, txt=rows["Topic"], ln=1, align='L')
            pdf.line(10, 21, 200, 21)
            # Break lines for Footer
            pdf.ln(265)
        else:
            pdf.ln(277)

        # if You want lines
        # for y in range(21, 288, 10):
        #     pdf.line(10, y, 200, y)

        # Adding Footer
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=rows["Topic"], align='R')

# PDF file name
pdf.output("Output.pdf")
