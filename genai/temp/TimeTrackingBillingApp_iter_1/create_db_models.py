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
    """description: Client table holding client information and budget status."""
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    total_hours = Column(DECIMAL(10, 2), default=0)
    total_amount = Column(DECIMAL(10, 2), default=0)
    budget_amount = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)

class Project(Base):
    """description: Project table associated with clients, holds project specifics and budget status."""
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    name = Column(String)
    total_project_hours = Column(DECIMAL(10, 2), default=0)
    total_project_amount = Column(DECIMAL(10, 2), default=0)
    project_budget_amount = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)

class Invoice(Base):
    """description: Invoice table details the amount due based on project tasking."""
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_date = Column(DateTime)
    project_id = Column(Integer, ForeignKey('project.id'))
    invoice_amount = Column(DECIMAL(10, 2), default=0)
    payment_total = Column(DECIMAL(10, 2), default=0)
    invoice_balance = Column(DECIMAL(10, 2), default=0)
    is_paid = Column(Boolean, default=False)

class Task(Base):
    """description: Task table defining task specifics, hours worked, amount billed, and budget status."""
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    name = Column(String)
    description = Column(String)
    total_task_hours_worked = Column(DECIMAL(10, 2), default=0)
    total_task_amount_billed = Column(DECIMAL(10, 2), default=0)
    task_budget_hours = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))

class Person(Base):
    """description: Person table records employee details along with hours and billing."""
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    billing_rate = Column(DECIMAL(10, 2), default=0)
    total_hours_entered = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)

class Timesheet(Base):
    """description: Timesheet table that tracks employee hours worked on tasks."""
    __tablename__ = 'timesheet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey('task.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    date_worked = Column(DateTime)
    hours_worked = Column(DECIMAL(10, 2), default=0)
    month = Column(Integer, default=0)
    year = Column(Integer, default=0)
    billing_rate = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)

class Payment(Base):
    """description: Payment records towards invoices of projects."""
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    payment_amount = Column(DECIMAL(10, 2), default=0)
    payment_date = Column(DateTime)
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
    client_1 = Client(name="Acme Corp", email="contact@acme.com", phone="1234567890", total_hours=0, total_amount=0, budget_amount=5000, is_over_budget=False)
    client_2 = Client(name="Global Inc", email="info@global.com", phone="0987654321", total_hours=0, total_amount=0, budget_amount=10000, is_over_budget=False)
    client_3 = Client(name="Innovate LLC", email="hello@innovate.com", phone="1122334455", total_hours=0, total_amount=0, budget_amount=3000, is_over_budget=False)
    client_4 = Client(name="Techies", email="support@techies.com", phone="5566778899", total_hours=0, total_amount=0, budget_amount=7500, is_over_budget=False)
    project_1 = Project(client_id=1, name="Website Redesign", total_project_hours=0, total_project_amount=0, project_budget_amount=2000, is_over_budget=False)
    project_2 = Project(client_id=2, name="Mobile App Development", total_project_hours=0, total_project_amount=0, project_budget_amount=5000, is_over_budget=False)
    project_3 = Project(client_id=3, name="Cloud Migration", total_project_hours=0, total_project_amount=0, project_budget_amount=8000, is_over_budget=False)
    project_4 = Project(client_id=4, name="Security Audit", total_project_hours=0, total_project_amount=0, project_budget_amount=3000, is_over_budget=False)
    invoice_1 = Invoice(invoice_date=date(2025, 2, 1), project_id=1, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
    invoice_2 = Invoice(invoice_date=date(2025, 3, 15), project_id=2, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
    invoice_3 = Invoice(invoice_date=date(2025, 5, 10), project_id=3, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
    invoice_4 = Invoice(invoice_date=date(2025, 6, 20), project_id=4, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
    task_1 = Task(project_id=1, name="Design Phase", description="Create mockups and wireframes.", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=50.0, is_over_budget=False, invoice_id=1)
    task_2 = Task(project_id=2, name="Development Phase", description="Develop core features and functionalities.", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=150.0, is_over_budget=False, invoice_id=2)
    task_3 = Task(project_id=3, name="Testing Phase", description="Perform QA testing.", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=100.0, is_over_budget=False, invoice_id=3)
    task_4 = Task(project_id=4, name="Deployment Phase", description="Deploy application to production.", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=60.0, is_over_budget=False, invoice_id=4)
    person_1 = Person(client_id=1, name="Alice", email="alice@acme.com", phone="1231231234", billing_rate=50.0, total_hours_entered=0, total_amount_billed=0)
    person_2 = Person(client_id=2, name="Bob", email="bob@global.com", phone="2342342345", billing_rate=75.0, total_hours_entered=0, total_amount_billed=0)
    person_3 = Person(client_id=3, name="Charlie", email="charlie@innovate.com", phone="3453453456", billing_rate=100.0, total_hours_entered=0, total_amount_billed=0)
    person_4 = Person(client_id=4, name="Dana", email="dana@techies.com", phone="4564564567", billing_rate=120.0, total_hours_entered=0, total_amount_billed=0)
    timesheet_1 = Timesheet(task_id=1, person_id=1, date_worked=date(2025, 2, 10), hours_worked=8, month=2, year=2025, billing_rate=50.0, total_amount_billed=400.0)
    timesheet_2 = Timesheet(task_id=2, person_id=2, date_worked=date(2025, 3, 12), hours_worked=6, month=3, year=2025, billing_rate=75.0, total_amount_billed=450.0)
    timesheet_3 = Timesheet(task_id=3, person_id=3, date_worked=date(2025, 5, 8), hours_worked=10, month=5, year=2025, billing_rate=100.0, total_amount_billed=1000.0)
    timesheet_4 = Timesheet(task_id=4, person_id=4, date_worked=date(2025, 6, 15), hours_worked=7.5, month=6, year=2025, billing_rate=120.0, total_amount_billed=900.0)
    payment_1 = Payment(invoice_id=1, payment_amount=200.0, payment_date=date(2025, 2, 20), notes="Initial deposit")
    payment_2 = Payment(invoice_id=2, payment_amount=300.0, payment_date=date(2025, 3, 18), notes="Partial payment")
    payment_3 = Payment(invoice_id=3, payment_amount=400.0, payment_date=date(2025, 5, 15), notes="Quarterly payment")
    payment_4 = Payment(invoice_id=4, payment_amount=500.0, payment_date=date(2025, 6, 25), notes="Final payment")
    
    
    
    session.add_all([client_1, client_2, client_3, client_4, project_1, project_2, project_3, project_4, invoice_1, invoice_2, invoice_3, invoice_4, task_1, task_2, task_3, task_4, person_1, person_2, person_3, person_4, timesheet_1, timesheet_2, timesheet_3, timesheet_4, payment_1, payment_2, payment_3, payment_4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
