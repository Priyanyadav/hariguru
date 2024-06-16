# apps/home/utils.py

from http.client import HTTPResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from .models import customer

def generate_customer_report():
    # Fetch customer data from the database
    customers = customer.objects.all()

    # Create a response object
    response = HTTPResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="customer_report.pdf"'

    # Define page size and margins
    page_width, page_height = letter
    left_margin = 50
    right_margin = 50

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter, leftMargin=left_margin, rightMargin=right_margin)
    elements = []

    # Define table data and style
    table_data = [['Customer Name', 'Email', 'Mobile', 'Address']]
    for customerr in customers:
        table_data.append([
            customerr.cname,
            customerr.email,
            str(customerr.mobile),
            customerr.address
        ])

    # Create table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Create table
    customer_table = Table(table_data)

    # Apply table style
    customer_table.setStyle(table_style)
    elements.append(customer_table)

    # Build PDF document
    doc.build(elements)

    return response
