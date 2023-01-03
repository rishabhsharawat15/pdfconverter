from fpdf import FPDF
import pandas as pd


#orientation stand for portrait or landscape ,unit=mm , format is page size
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)#rgb
    # width of box ,height ,ln which line should the text(txt) is placed , border 0 means no border
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
         ln=1,border=0)

    #till above title is added now we add line ----------
    for y in range(20, 298, 10):
        #pdf.line(x1,y1,x2,y2) x1,y1 be strating codinate and similarly end cordinates
        #x1 is distance from left x1 + x2 = 210 in A4
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")