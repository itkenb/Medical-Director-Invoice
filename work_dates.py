import os
from datetime import date
from calendar import monthrange

class WorkDates:
    def __init__(self, invoice_param):
        self.year = invoice_param[0]
        self.month = invoice_param[1]
        self.excluded_dates = invoice_param[2]
        self.month_range = monthrange(self.year, self.month)[1]

    def get_work_dates(self):
        day = 1
        # total_hours = 20
        week_work_days = []
        weeks = []
        week_work_hours = []
        work_days = []

        if date(self.year, self.month, day).weekday() not in list(range(0,5)):
            day += 1

        while day <= self.month_range:
            dt = date(self.year, self.month, day)
            if dt.weekday() in list(range(0,5)):
                if dt.strftime("%#m/%#d") not in self.excluded_dates:
                    week_work_days.append(dt.strftime("%#m/%#d"))
            else:
                day += 1
                week_work_hours.append(len(week_work_days))
                weeks.append(week_work_days)
                week_work_days = []
            day += 1
        week_work_hours.append(len(week_work_days))
        weeks.append(week_work_days)

        while sum(week_work_hours) != 20:
            for idx, num in enumerate(week_work_hours):
                if num == 5:
                    week_work_hours[idx] += -1
                    break
        
        if len(weeks[0]) == 0:
            weeks.pop(0)
            week_work_hours.pop(0)
        if len(weeks) > 5:
            weeks.pop(-1)
            week_work_hours.pop(-1)

        for week_idx, w in enumerate(weeks):
            if week_work_hours[week_idx] == 0:
                work_days.append([f"Week {week_idx + 1}", ', ' . join(w), "", ""])
            else:
                work_days.append([f"Week {week_idx + 1}", ', ' . join(w), str(week_work_hours[week_idx]), str(week_work_hours[week_idx] * 150)])
                

        return work_days
