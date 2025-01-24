import logging
from logic_bank.logic_bank import DeclareRule, Rule, LogicBank
from database.models import *

log = logging.getLogger(__name__)

def declare_logic():
    """
        declare_logic - declare rules
        this function is called from logic/declare_logic.py
    """
    log.info("declare_logic - active rules")
    
    # Exported Rules:
    # Person_Totals 
    # Total Hours entered is sum of timesheet hours worked. Total amount billed is total hours entered times billing rate. Billing rate must be greater than 0 and less than 200.
    Rule.sum(derive=Person.total_hours_entered, as_sum_of=Timesheet.hours_worked)
    Rule.formula(derive=Person.total_amount_billed, as_expression=lambda row: row.total_hours_entered * row.billing_rate)
    Rule.constraint(validate=Person, as_condition=lambda row: 0 < row.billing_rate < 200, error_msg='Billing rate must be between 0 and 200')
    
    # Timesheet_Bill_Calc 
    # The total amount billed is the Person billing rate times hours worked. Hours worked must be greater than 0 and less than 15. Date worked must be greater than 2025-01-01. Month is extracted using datetime from the date worked. Year is extracted using datetime from the date worked. Copy billing rate from Person billing rate.
    Rule.formula(derive=Timesheet.total_amount_billed, as_expression=lambda row: row.billing_rate * row.hours_worked)
    Rule.constraint(validate=Timesheet, as_condition=lambda row: 0 < row.hours_worked < 15, error_msg='Hours worked must be between 0 and 15')
    Rule.constraint(validate=Timesheet, as_condition=lambda row: row.date_worked > date(2025, 1, 1), error_msg='Date worked must be after 2025-01-01')
    Rule.formula(derive=Timesheet.month, as_expression=lambda row: row.date_worked.month)
    Rule.formula(derive=Timesheet.year, as_expression=lambda row: row.date_worked.year)
    Rule.copy(derive=Timesheet.billing_rate, from_parent=Person.billing_rate)
    
    # Task_Totals 
    # Total task hours worked is the sum of Timesheet hours worked. Total task amount billed is the sum of Timesheet total amount billed. Formula: is Over Budget  when total task hours worked exceeds task budget hours.
    Rule.sum(derive=Task.total_task_hours_worked, as_sum_of=Timesheet.hours_worked)
    Rule.sum(derive=Task.total_task_amount_billed, as_sum_of=Timesheet.total_amount_billed)
    Rule.formula(derive=Task.is_over_budget, as_expression=lambda row: row.total_task_hours_worked > row.task_budget_hours)
    
    # Project_Totals 
    # Total project hours is the sum of Task total task hours worked. Total project amount is the sum of Task total amount billed. Formula: set  is Over Budget when total project amount exceeds project budget amount.
    Rule.sum(derive=Project.total_project_hours, as_sum_of=Task.total_task_hours_worked)
    Rule.sum(derive=Project.total_project_amount, as_sum_of=Task.total_task_amount_billed)
    Rule.formula(derive=Project.is_over_budget, as_expression=lambda row: row.total_project_amount > row.project_budget_amount)
    
    # Invoice_Totals 
    # Invoice Amount is the sum of Task total amount billed. Payment total is the sum of Payment. Invoice balance is invoice amount less payment total. Formula: invoice_paid is true when invoice balance is zero.
    Rule.sum(derive=Invoice.invoice_amount, as_sum_of=Task.total_task_amount_billed)
    Rule.sum(derive=Invoice.payment_total, as_sum_of=Payment.payment_amount)
    Rule.formula(derive=Invoice.invoice_balance, as_expression=lambda row: row.invoice_amount - row.payment_total)
    Rule.formula(derive=Invoice.is_paid, as_expression=lambda row: row.invoice_balance == 0)
    