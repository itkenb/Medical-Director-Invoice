from fpdf import FPDF

class GeneratePDF():
    def __init__(self, details, work_days, month, year):
        self.details = details
        self.work_days = work_days
        self.month = month
        self.year = year
        self._generate()

    def _generate(self):
        for location in self.details['locations']:
            pdf = FPDF('P', 'mm', 'Letter')
            pdf.add_font("calibri", "B", "calibrib.ttf")
            pdf.set_font("calibri", "B", 16)
            pdf.set_margin(25.4)
            pdf.add_page()
            pdf.cell(0, 0, self.details["title"], align='C', ln=True)
            pdf.cell(0, 20.4, "", ln=True)
            pdf.cell(0, 10, f"Name of MD Practice: {self.details["entity"]}", ln=True)
            pdf.cell(0, 10, f"Address: {self.details["address"]}", ln=True)
            pdf.cell(0, 20.4, "", ln=True)
            pdf.cell(0, 10, f"Month:    {self.month} {self.year}", ln=True)
            pdf.cell(0,10, f"Location of Services:    {location}", ln=True)
            pdf.cell(0,10, "", ln=True)
            pdf.cell(41.275, 7.5, "", fill=True, border=1)
            pdf.cell(41.275, 7.5, "Date of Service", border=1, align='C')
            pdf.cell(41.275, 7.5, "# of hours", border=1, align='C')
            pdf.cell(41.275, 7.5, "X $150/hr", border=1, align='C', ln=True)

            with pdf.table(text_align=("LEFT", "LEFT", "CENTER", "CENTER"), line_height=7.5, padding=1.25, first_row_as_headings=False) as table:
                for data_row in self.work_days:
                    row = table.row()
                    for datum in data_row:
                        row.cell(datum)

            pdf.cell(0,10, "", ln=True)
            pdf.cell(41.275, 7.5, "", fill=True, border=1)
            pdf.cell(41.275, 7.5, "Total", border=1, align='C')
            pdf.cell(41.275, 7.5, "20", border=1, align='C')
            pdf.cell(41.275, 7.5, "3000.00", border=1, align='C', ln=True)
            pdf.output(f"{self.details['dir']}{self.details['title']} - {self.month} {self.year}- {location}.pdf")

