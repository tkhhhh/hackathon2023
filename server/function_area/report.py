
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.validators import Auto
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing, String
from reportlab.platypus import SimpleDocTemplate, Paragraph

from api_service.load_api import LoadApi
from function_area.transaction import Transaction
from api.pie_chart import *
import datetime, os

import tempfile

class Report(object):
    def __init__(self, account_id, authJWT):
        self.load_api = LoadApi(authJWT)
        self.account_id = account_id
        self.authJWT = authJWT
        self.transaction_obj = Transaction(account_id, authJWT)

    def create_report(self):
        f = os.path.abspath("tmp/report.pdf")
        doc = SimpleDocTemplate(f)

        elements = []
        styles = getSampleStyleSheet()
        ptext = Paragraph('Budget Report', styles["Normal"])
        elements.append(ptext)
        

        # Create pie chart
        data = create_pie_chart_data(self.authJWT, self.account_id)
        print(data)
        drawing = Drawing(width=400, height=200)
        my_title = String(170, 40, 'Spending by category', fontSize=14)
        pie = Pie()
        pie.sideLabels = True
        pie.x = 150
        pie.y = 65
        
        pie.data = list(data.values())
        pie.labels = list(data.keys())
        pie.slices.strokeWidth = 0.5
        drawing.add(my_title)
        drawing.add(pie)
        
        # Add legend
        legend = Legend()
        legend.alignment = 'right'
        legend.x = 10
        legend.y = 70
        legend.colorNamePairs = Auto(obj=pie)
        drawing.add(legend)

        elements.append(drawing)
        
        transactions = self.transaction_obj.get_recent_transaction(7, 1000)
        for t in transactions:
            ptext = Paragraph(str(t), styles["Normal"])
            elements.append(ptext)
        doc.build(elements)
        return f

        
