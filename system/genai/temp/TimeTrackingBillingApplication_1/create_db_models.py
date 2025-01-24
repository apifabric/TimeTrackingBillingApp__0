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
    """description: Represents client details including financial information."""
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    total_hours = Column(DECIMAL(10, 2), default=0)
    total_amount = Column(DECIMAL(10, 2), default=0)
    budget_amount = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)

class Project(Base):
    """description: Tracks project-specific information and financial metrics."""
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    name = Column(String, nullable=True)
    total_project_hours = Column(DECIMAL(10, 2), default=0)
    total_project_amount = Column(DECIMAL(10, 2), default=0)
    project_budget_amount = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)

class Invoice(Base):
    """description: Captured invoice details and financial status."""
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_date = Column(Date, nullable=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    invoice_amount = Column(DECIMAL(10, 2), default=0)
    payment_total = Column(DECIMAL(10, 2), default=0)
    invoice_balance = Column(DECIMAL(10, 2), default=0)
    is_paid = Column(Boolean, default=False)

class Task(Base):
    """description: Represents individual tasks within a project."""
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    total_task_hours_worked = Column(DECIMAL(10, 2), default=0)
    total_task_amount_billed = Column(DECIMAL(10, 2), default=0)
    task_budget_hours = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))

class Person(Base):
    """description: Contains personal details and billing information for individuals."""
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    billing_rate = Column(DECIMAL(10, 2), default=0)
    total_hours_entered = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)

class Timesheet(Base):
    """description: Records time entries and calculates billing based on individual time worked."""
    __tablename__ = 'timesheet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey('task.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    date_worked = Column(Date, nullable=True)
    hours_worked = Column(DECIMAL(10, 2), default=0)
    month = Column(Integer, nullable=True)
    year = Column(Integer, nullable=True)
    billing_rate = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)

class Payment(Base):
    """description: Manages payment records against invoices."""
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    payment_amount = Column(DECIMAL(10, 2), default=0)
    payment_date = Column(Date, nullable=True)
    notes = Column(String, nullable=True)


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
    client_1 = Client(name="Client A", email="clienta@example.com", phone="123-456-7890", total_hours=100, total_amount=10000, budget_amount=15000, is_over_budget=False)
    client_2 = Client(name="Client B", email="clientb@example.com", phone="234-567-8901", total_hours=200, total_amount=21000, budget_amount=25000, is_over_budget=False)
    client_3 = Client(name="Client C", email="clientc@example.com", phone="345-678-9012", total_hours=120, total_amount=11000, budget_amount=12000, is_over_budget=False)
    client_4 = Client(name="Client D", email="clientd@example.com", phone="456-789-0123", total_hours=80, total_amount=9000, budget_amount=8000, is_over_budget=True)
    project_1 = Project(client_id=1, name="Project Alpha", total_project_hours=50, total_project_amount=5000, project_budget_amount=7000, is_over_budget=False)
    project_2 = Project(client_id=2, name="Project Beta", total_project_hours=75, total_project_amount=7600, project_budget_amount=8000, is_over_budget=False)
    project_3 = Project(client_id=3, name="Project Gamma", total_project_hours=90, total_project_amount=9200, project_budget_amount=9200, is_over_budget=False)
    project_4 = Project(client_id=4, name="Project Delta", total_project_hours=60, total_project_amount=6200, project_budget_amount=6000, is_over_budget=True)
    invoice_1 = Invoice(invoice_date=date(2026, 5, 20), project_id=1, invoice_amount=5000, payment_total=4000, invoice_balance=1000, is_paid=False)
    invoice_2 = Invoice(invoice_date=date(2026, 6, 15), project_id=2, invoice_amount=7600, payment_total=7600, invoice_balance=0, is_paid=True)
    invoice_3 = Invoice(invoice_date=date(2026, 7, 10), project_id=3, invoice_amount=9200, payment_total=9200, invoice_balance=0, is_paid=True)
    invoice_4 = Invoice(invoice_date=date(2026, 8, 5), project_id=4, invoice_amount=6200, payment_total=6200, invoice_balance=0, is_paid=True)
    task_1 = Task(project_id=1, name="Task 1", description="Task Description 1", total_task_hours_worked=20, total_task_amount_billed=2000, task_budget_hours=25, is_over_budget=False, invoice_id=1)
    task_2 = Task(project_id=2, name="Task 2", description="Task Description 2", total_task_hours_worked=15, total_task_amount_billed=1500, task_budget_hours=20, is_over_budget=False, invoice_id=2)
    task_3 = Task(project_id=3, name="Task 3", description="Task Description 3", total_task_hours_worked=30, total_task_amount_billed=3000, task_budget_hours=30, is_over_budget=False, invoice_id=3)
    task_4 = Task(project_id=4, name="Task 4", description="Task Description 4", total_task_hours_worked=10, total_task_amount_billed=1000, task_budget_hours=8, is_over_budget=True, invoice_id=4)
    person_1 = Person(client_id=1, name="Employee A", email="empA@example.com", phone="999-999-0001", billing_rate=100, total_hours_entered=20, total_amount_billed=2000)
    person_2 = Person(client_id=2, name="Employee B", email="empB@example.com", phone="999-999-0002", billing_rate=120, total_hours_entered=15, total_amount_billed=1800)
    person_3 = Person(client_id=3, name="Employee C", email="empC@example.com", phone="999-999-0003", billing_rate=110, total_hours_entered=30, total_amount_billed=3300)
    person_4 = Person(client_id=4, name="Employee D", email="empD@example.com", phone="999-999-0004", billing_rate=90, total_hours_entered=10, total_amount_billed=900)
    timesheet_1 = Timesheet(task_id=1, person_id=1, date_worked=date(2026, 3, 5), hours_worked=10, month=3, year=2026, billing_rate=100, total_amount_billed=1000)
    timesheet_2 = Timesheet(task_id=2, person_id=2, date_worked=date(2026, 4, 10), hours_worked=8, month=4, year=2026, billing_rate=120, total_amount_billed=960)
    timesheet_3 = Timesheet(task_id=3, person_id=3, date_worked=date(2026, 5, 22), hours_worked=10, month=5, year=2026, billing_rate=110, total_amount_billed=1100)
    timesheet_4 = Timesheet(task_id=4, person_id=4, date_worked=date(2026, 6, 17), hours_worked=7, month=6, year=2026, billing_rate=90, total_amount_billed=630)
    payment_1 = Payment(invoice_id=1, payment_amount=3000, payment_date=date(2026, 5, 25), notes="Initial payment")
    payment_2 = Payment(invoice_id=2, payment_amount=7600, payment_date=date(2026, 6, 20), notes="Full payment")
    payment_3 = Payment(invoice_id=3, payment_amount=9200, payment_date=date(2026, 7, 15), notes="Complete payment")
    payment_4 = Payment(invoice_id=4, payment_amount=6200, payment_date=date(2026, 8, 10), notes="Paid in full"
    
    
    
    session.add_all([client_1, client_2, client_3, client_4, project_1, project_2, project_3, project_4, invoice_1, invoice_2, invoice_3, invoice_4, task_1, task_2, task_3, task_4, person_1, person_2, person_3, person_4, timesheet_1, timesheet_2, timesheet_3, timesheet_4, payment_1, payment_2, payment_3, payment_4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
