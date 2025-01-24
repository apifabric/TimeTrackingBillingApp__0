# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class Client(Base):
    """description: Represents a client with financials and budget constraints."""
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    total_hours = Column(DECIMAL(10, 2), default=0)
    total_amount = Column(DECIMAL(10, 2), default=0)
    budget_amount = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)

class Project(Base):
    """description: Tracks project details and monitors project budget."""
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    name = Column(String)
    total_project_hours = Column(DECIMAL(10, 2), default=0)
    total_project_amount = Column(DECIMAL(10, 2), default=0)
    project_budget_amount = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)

class Invoice(Base):
    """description: Manages invoice creation and financial tracking."""
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True)
    invoice_date = Column(Date)
    project_id = Column(Integer, ForeignKey('project.id'))
    invoice_amount = Column(DECIMAL(10, 2), default=0)
    payment_total = Column(DECIMAL(10, 2), default=0)
    invoice_balance = Column(DECIMAL(10, 2), default=0)
    is_paid = Column(Boolean, default=False)

class Task(Base):
    """description: Represents tasks asscoiated with projects, tracking hours and amounts billed."""
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    name = Column(String)
    description = Column(String)
    total_task_hours_worked = Column(DECIMAL(10, 2), default=0)
    total_task_amount_billed = Column(DECIMAL(10, 2), default=0)
    task_budget_hours = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))

class Person(Base):
    """description: Captures personnel data and their billing details."""
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    billing_rate = Column(DECIMAL(10, 2), CheckConstraint(
        'billing_rate > 0 and billing_rate < 200'), default=0)
    total_hours_entered = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)

class Timesheet(Base):
    """description: Track time worked and calculate billing based on hours and rates."""
    __tablename__ = 'timesheet'
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('task.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    date_worked = Column(Date, CheckConstraint('date_worked > "2025-01-01"'))
    hours_worked = Column(DECIMAL(10, 2), CheckConstraint(
        'hours_worked > 0 and hours_worked < 15'), default=0)
    month = Column(Integer)
    year = Column(Integer)
    billing_rate = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)

class Payment(Base):
    """description: Records payment transactions linked to invoices."""
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    payment_amount = Column(DECIMAL(10, 2))
    payment_date = Column(Date)
    notes = Column(String)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    alpha_corp = Client(id=1, name="Alpha Corp", email="contact@alphacorp.com", phone="123-456-7890", total_hours=200.00, total_amount=15000.00, budget_amount=20000.00, is_over_budget=False)
    beta_inc = Client(id=2, name="Beta Inc", email="support@betainc.com", phone="098-765-4321", total_hours=0.00, total_amount=7500.00, budget_amount=10000.00, is_over_budget=False)
    gamma_llc = Client(id=3, name="Gamma LLC", email="info@gammallc.com", phone="234-567-8901", total_hours=50.00, total_amount=5000.00, budget_amount=7000.00, is_over_budget=True)
    delta_plc = Client(id=4, name="Delta PLC", email="service@deltaplc.com", phone="345-678-9012", total_hours=100.00, total_amount=12000.00, budget_amount=15000.00, is_over_budget=False)
    alpha_project = Project(id=1, client_id=1, name="Build Website", total_project_hours=150.0, total_project_amount=12000.00, project_budget_amount=15000.00, is_over_budget=False)
    beta_project = Project(id=2, client_id=2, name="App Development", total_project_hours=250.0, total_project_amount=25000.00, project_budget_amount=23000.00, is_over_budget=True)
    gamma_project = Project(id=3, client_id=3, name="SEO Optimization", total_project_hours=80.0, total_project_amount=8000.00, project_budget_amount=10000.00, is_over_budget=False)
    delta_project = Project(id=4, client_id=4, name="Cloud Migration", total_project_hours=170.0, total_project_amount=18000.00, project_budget_amount=20000.00, is_over_budget=False)
    invoice_1 = Invoice(id=1, invoice_date=date(2025, 2, 15), project_id=1, invoice_amount=12000.00, payment_total=8000.00, invoice_balance=4000.00, is_paid=False)
    invoice_2 = Invoice(id=2, invoice_date=date(2026, 5, 20), project_id=2, invoice_amount=7000.00, payment_total=7000.00, invoice_balance=0.00, is_paid=True)
    invoice_3 = Invoice(id=3, invoice_date=date(2026, 9, 10), project_id=3, invoice_amount=0.00, payment_total=0.00, invoice_balance=0.00, is_paid=True)
    invoice_4 = Invoice(id=4, invoice_date=date(2027, 1, 1), project_id=4, invoice_amount=18000.00, payment_total=16000.00, invoice_balance=2000.00, is_paid=False)
    task_alpha = Task(id=1, project_id=1, name="Design Phase", description="Initial design and prototype", total_task_hours_worked=30.0, total_task_amount_billed=3000.00, task_budget_hours=40.0, is_over_budget=False, invoice_id=1)
    task_beta = Task(id=2, project_id=2, name="Development Phase", description="Core application development", total_task_hours_worked=100.0, total_task_amount_billed=10000.00, task_budget_hours=90.0, is_over_budget=True, invoice_id=2)
    task_gamma = Task(id=3, project_id=3, name="Optimization Phase", description="Enhance site performance", total_task_hours_worked=20.0, total_task_amount_billed=2000.00, task_budget_hours=25.0, is_over_budget=False, invoice_id=3)
    task_delta = Task(id=4, project_id=4, name="Testing Phase", description="End-to-end testing and QA", total_task_hours_worked=50.0, total_task_amount_billed=5000.00, task_budget_hours=55.0, is_over_budget=False, invoice_id=4)
    person_john = Person(id=1, client_id=1, name="John Doe", email="john@alphacorp.com", phone="111-222-3333", billing_rate=150.00, total_hours_entered=60.0, total_amount_billed=9000.00)
    person_jane = Person(id=2, client_id=2, name="Jane Smith", email="jane@betainc.com", phone="222-333-4444", billing_rate=100.00, total_hours_entered=45.0, total_amount_billed=4500.00)
    person_alex = Person(id=3, client_id=3, name="Alex Brown", email="alex@gammallc.com", phone="333-444-5555", billing_rate=175.00, total_hours_entered=30.0, total_amount_billed=5250.00)
    person_emma = Person(id=4, client_id=4, name="Emma Taylor", email="emma@deltaplc.com", phone="444-555-6666", billing_rate=90.00, total_hours_entered=55.0, total_amount_billed=4950.00)
    timesheet_1 = Timesheet(id=1, task_id=1, person_id=1, date_worked=date(2026, 2, 5), hours_worked=15.0, month=2, year=2026, billing_rate=150.00, total_amount_billed=2250.00)
    timesheet_2 = Timesheet(id=2, task_id=2, person_id=2, date_worked=date(2026, 5, 12), hours_worked=10.0, month=5, year=2026, billing_rate=100.00, total_amount_billed=1000.00)
    timesheet_3 = Timesheet(id=3, task_id=3, person_id=3, date_worked=date(2026, 9, 8), hours_worked=5.0, month=9, year=2026, billing_rate=175.00, total_amount_billed=875.00)
    timesheet_4 = Timesheet(id=4, task_id=4, person_id=4, date_worked=date(2026, 12, 21), hours_worked=12.0, month=12, year=2026, billing_rate=90.00, total_amount_billed=1080.00)
    payment_1 = Payment(id=1, invoice_id=1, payment_amount=4000.00, payment_date=date(2026, 3, 1), notes="Initial Payment")
    payment_2 = Payment(id=2, invoice_id=2, payment_amount=7000.00, payment_date=date(2026, 6, 20), notes="Final Settlement")
    payment_3 = Payment(id=3, invoice_id=3, payment_amount=0.00, payment_date=date(2026, 9, 12), notes="No payment required")
    payment_4 = Payment(id=4, invoice_id=4, payment_amount=16000.00, payment_date=date(2027, 2, 1), notes="Majority payment")
    
    
    
    session.add_all([alpha_corp, beta_inc, gamma_llc, delta_plc, alpha_project, beta_project, gamma_project, delta_project, invoice_1, invoice_2, invoice_3, invoice_4, task_alpha, task_beta, task_gamma, task_delta, person_john, person_jane, person_alex, person_emma, timesheet_1, timesheet_2, timesheet_3, timesheet_4, payment_1, payment_2, payment_3, payment_4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
