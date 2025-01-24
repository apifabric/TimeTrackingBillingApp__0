
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.sum(derive=Person.total_hours_entered, as_sum_of=Timesheet.hours_worked)
  Rule.formula(derive=Person.total_amount_billed, as_expression=lambda row: row.total_hours_entered * row.billing_rate)
  Rule.constraint(validate=Person, as_condition=lambda row: 0 < row.billing_rate < 200, error_msg='Billing rate must be between 0 and 200')
