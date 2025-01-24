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
    """description: Represents clients in the system."""
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    total_hours = Column(DECIMAL(10, 2), default=0)
    total_amount = Column(DECIMAL(10, 2), default=0)
    budget_amount = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)

class Project(Base):
    """description: Represents projects associated with clients."""
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=True)
    name = Column(String, nullable=False)
    total_project_hours = Column(DECIMAL(10, 2), default=0)
    total_project_amount = Column(DECIMAL(10, 2), default=0)
    project_budget_amount = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)

class Invoice(Base):
    """description: Represents invoices related to a specific project."""
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_date = Column(Date, nullable=True)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=True)
    invoice_amount = Column(DECIMAL(10, 2), default=0)
    payment_total = Column(DECIMAL(10, 2), default=0)
    invoice_balance = Column(DECIMAL(10, 2), default=0)
    is_paid = Column(Boolean, default=False)

class Task(Base):
    """description: Represents tasks within projects."""
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    total_task_hours_worked = Column(DECIMAL(10, 2), default=0)
    total_task_amount_billed = Column(DECIMAL(10, 2), default=0)
    task_budget_hours = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean, default=False)
    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=True)

class Person(Base):
    """description: Represents personnel and their billing information."""
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    billing_rate = Column(DECIMAL(10, 2), default=0)
    total_hours_entered = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)

class Timesheet(Base):
    """description: Represents timesheets logging work done by personnel."""
    __tablename__ = 'timesheet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey('task.id'), nullable=True)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=True)
    date_worked = Column(Date, nullable=True)
    hours_worked = Column(DECIMAL(10, 2), default=0)
    month = Column(Integer, nullable=True)
    year = Column(Integer, nullable=True)
    billing_rate = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)

class Payment(Base):
    """description: Represents payments made against invoices."""
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=True)
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
    client_1 = Client(id=1, name="Acme Corp", email="acme@corp.com", phone="123-456-7890", total_hours=0, total_amount=0, budget_amount=1000, is_over_budget=False)
    client_2 = Client(id=2, name="Beta Inc", email="beta@inc.com", phone="234-567-8901", total_hours=0, total_amount=0, budget_amount=2000, is_over_budget=False)
    client_3 = Client(id=3, name="Gamma LLC", email="gamma@llc.com", phone="345-678-9012", total_hours=0, total_amount=0, budget_amount=1500, is_over_budget=False)
    client_4 = Client(id=4, name="Delta Co", email="delta@co.com", phone="456-789-0123", total_hours=0, total_amount=0, budget_amount=500, is_over_budget=False)
    project_1 = Project(id=1, client_id=1, name="Project Alpha", total_project_hours=0, total_project_amount=0, project_budget_amount=800, is_over_budget=False)
    project_2 = Project(id=2, client_id=1, name="Project Beta", total_project_hours=0, total_project_amount=0, project_budget_amount=1200, is_over_budget=False)
    project_3 = Project(id=3, client_id=2, name="Project Gamma", total_project_hours=0, total_project_amount=0, project_budget_amount=1500, is_over_budget=False)
    project_4 = Project(id=4, client_id=3, name="Project Delta", total_project_hours=0, total_project_amount=0, project_budget_amount=1000, is_over_budget=False)
    invoice_1 = Invoice(id=1, invoice_date=date(2025, 6, 15), project_id=1, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
    invoice_2 = Invoice(id=2, invoice_date=date(2025, 7, 10), project_id=2, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
    invoice_3 = Invoice(id=3, invoice_date=date(2025, 8, 25), project_id=3, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
    invoice_4 = Invoice(id=4, invoice_date=date(2025, 9, 5), project_id=4, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
    task_1 = Task(id=1, project_id=1, name="Design", description="Design phase", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=100, is_over_budget=False, invoice_id=1)
    task_2 = Task(id=2, project_id=1, name="Development", description="Development phase", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=200, is_over_budget=False, invoice_id=2)
    task_3 = Task(id=3, project_id=2, name="Testing", description="Testing phase", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=150, is_over_budget=False, invoice_id=3)
    task_4 = Task(id=4, project_id=2, name="Deployment", description="Deployment phase", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=120, is_over_budget=False, invoice_id=4)
    person_1 = Person(id=1, client_id=1, name="Alice", email="alice@corp.com", phone="111-222-3333", billing_rate=150, total_hours_entered=0, total_amount_billed=0)
    person_2 = Person(id=2, client_id=1, name="Bob", email="bob@inc.com", phone="222-333-4444", billing_rate=125, total_hours_entered=0, total_amount_billed=0)
    person_3 = Person(id=3, client_id=2, name="Charlie", email="charlie@co.com", phone="333-444-5555", billing_rate=100, total_hours_entered=0, total_amount_billed=0)
    person_4 = Person(id=4, client_id=3, name="Diana", email="diana@llc.com", phone="444-555-6666", billing_rate=175, total_hours_entered=0, total_amount_billed=0)
    timesheet_1 = Timesheet(id=1, task_id=1, person_id=1, date_worked=date(2026, 1, 8), hours_worked=7.5, month=1, year=2026, billing_rate=150, total_amount_billed=1125)
    timesheet_2 = Timesheet(id=2, task_id=2, person_id=2, date_worked=date(2026, 2, 10), hours_worked=10, month=2, year=2026, billing_rate=125, total_amount_billed=1250)
    timesheet_3 = Timesheet(id=3, task_id=3, person_id=3, date_worked=date(2026, 3, 12), hours_worked=12.5, month=3, year=2026, billing_rate=100, total_amount_billed=1250)
    timesheet_4 = Timesheet(id=4, task_id=4, person_id=4, date_worked=date(2026, 4, 15), hours_worked=8, month=4, year=2026, billing_rate=175, total_amount_billed=1400)
    payment_1 = Payment(id=1, invoice_id=1, payment_amount=500, payment_date=date(2026, 1, 20), notes="Partial payment")
    payment_2 = Payment(id=2, invoice_id=2, payment_amount=650, payment_date=date(2026, 2, 15), notes="Half payment")
    payment_3 = Payment(id=3, invoice_id=3, payment_amount=900, payment_date=date(2026, 3, 25), notes="Nearly paid")
    payment_4 = Payment(id=4, invoice_id=4, payment_amount=0, payment_date=date(2026, 4, 10), notes="No payment")
    
    
    
    session.add_all([client_1, client_2, client_3, client_4, project_1, project_2, project_3, project_4, invoice_1, invoice_2, invoice_3, invoice_4, task_1, task_2, task_3, task_4, person_1, person_2, person_3, person_4, timesheet_1, timesheet_2, timesheet_3, timesheet_4, payment_1, payment_2, payment_3, payment_4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
