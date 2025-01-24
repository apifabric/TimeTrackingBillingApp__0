
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.sum(derive=Invoice.invoice_amount, as_sum_of=Task.total_task_amount_billed)
  Rule.sum(derive=Invoice.payment_total, as_sum_of=Payment.payment_amount)
  Rule.formula(derive=Invoice.invoice_balance, as_expression=lambda row: row.invoice_amount - row.payment_total)
  Rule.formula(derive=Invoice.is_paid, as_expression=lambda row: row.invoice_balance == 0)
