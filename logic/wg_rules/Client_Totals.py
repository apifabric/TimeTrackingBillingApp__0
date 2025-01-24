
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.sum(derive=Client.total_hours, as_sum_of=Project.total_task_hours_worked)
  Rule.sum(derive=Client.total_amount, as_sum_of=Task.total_task_amount_billed)
  Rule.formula(derive=Client.is_over_budget, as_expression=lambda row: row.total_amount > row.budget_amount)
