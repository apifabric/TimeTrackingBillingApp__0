
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.sum(derive=Project.total_project_hours, as_sum_of=Task.total_task_hours_worked)
  Rule.sum(derive=Project.total_project_amount, as_sum_of=Task.total_task_amount_billed)
  Rule.formula(derive=Project.is_over_budget, as_expression=lambda row: row.total_project_amount > row.project_budget_amount)
