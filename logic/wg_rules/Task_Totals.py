
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.sum(derive=Task.total_task_hours_worked, as_sum_of=Timesheet.hours_worked)
  Rule.sum(derive=Task.total_task_amount_billed, as_sum_of=Timesheet.total_amount_billed)
  Rule.formula(derive=Task.is_over_budget, as_expression=lambda row: row.total_task_hours_worked > row.task_budget_hours)
