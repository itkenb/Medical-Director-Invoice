import os
import json
from datetime import date
from clear import Clear
from work_dates import WorkDates
from generate_pdf import GeneratePDF

class Invoice:
    def __init__(self):
        self.invoice_param = self._get_invoice_param()
        self.month_name = date(self.invoice_param[0], self.invoice_param[1], 1).strftime("%B")
        # WorkDates(self.invoice_param).get_work_dates()
        self.work_days = WorkDates(self.invoice_param).get_work_dates()
        self.details = self._get_details()
        self._generate_pdf()

    def _get_invoice_param(self):
        Clear()
        year = int(input("Year:\n>> "))
        month = int(input("Month:\n>> "))
        excluded = input("Exclude dates: (Separate with comma ex(1/24,1/25))\n>> ")

        exclude_dates = excluded.split(',')

        # year = 2024
        # month = 1

        return year, month, exclude_dates

    def _get_details(self):
        with open("details.json", "r", encoding='utf-8') as f:
            details = json.load(f)

        return details
    
    def _generate_pdf(self):
        GeneratePDF(self.details, self.work_days, self.month_name, self.invoice_param[0])
        Clear()
        os.startfile(self.details["dir"])
        print("PDF Generated...")


if __name__ == "__main__":
    Invoice()
