from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import letter # Note: Make sure report lab is installed (pip install reportlab)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os


pdf_list = []


####################################### File Functions #######################################   

def get_file_name(title):
    num = 1
    while True:
        file_name = f"{title}_{num}.pdf"  
        if not os.path.exists(file_name):
            return file_name
        num += 1
        

def pdf_maker(file_data, title):
    if title == "":
        title = "Worksheet"

    file_name = get_file_name(title)

    if not file_name.endswith(".pdf"):
        file_name += ".pdf"

    doc = SimpleDocTemplate(file_name, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    for item_type, content in file_data:
        if item_type == "label":
            # Add label text as a paragraph
            elements.append(Paragraph(content, styles['Normal']))
            elements.append(Spacer(1, 5))
        elif item_type == "table":
            # Add table
            t = Table(content)
            t.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.grey),
                ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                ('GRID', (0,0), (-1,-1), 1, colors.black),
                ('BACKGROUND',(0,1),(-1,-1),colors.beige)
            ]))
            elements.append(Spacer(1, 10))
            elements.append(t)
            elements.append(Spacer(1, 10))

    doc.build(elements)

    print(f"✅ Saved PDF as {file_name}")


def save_pdf():
    
    item_list = []
    for item, item_type in pdf_list:
        if item_type == 'L':
            item_list.append(("label", item.cget("text")))
        elif item_type == "T":
            item_list.append(("table", item))
            
    pdf_maker(item_list, "")    
    
  