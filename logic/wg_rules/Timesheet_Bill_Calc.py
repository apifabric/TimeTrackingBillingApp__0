
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.formula(derive=Timesheet.total_amount_billed, as_expression=lambda row: row.billing_rate * row.hours_worked)
  Rule.constraint(validate=Timesheet, as_condition=lambda row: 0 < row.hours_worked < 15, error_msg='Hours worked must be between 0 and 15')
  Rule.constraint(validate=Timesheet, as_condition=lambda row: row.date_worked > date(2025, 1, 1), error_msg='Date worked must be after 2025-01-01')
  Rule.formula(derive=Timesheet.month, as_expression=lambda row: row.date_worked.month)
  Rule.formula(derive=Timesheet.year, as_expression=lambda row: row.date_worked.year)
  Rule.copy(derive=Timesheet.billing_rate, from_parent=Person.billing_rate)
