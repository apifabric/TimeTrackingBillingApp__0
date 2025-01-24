import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not 2358495917114931273 in succeeded_hashes:  # avoid duplicate inserts
            instance = client_1 = Client(name="Acme Corp", email="contact@acme.com", phone="1234567890", total_hours=0, total_amount=0, budget_amount=5000, is_over_budget=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2358495917114931273)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6221718854129425853 in succeeded_hashes:  # avoid duplicate inserts
            instance = client_2 = Client(name="Global Inc", email="info@global.com", phone="0987654321", total_hours=0, total_amount=0, budget_amount=10000, is_over_budget=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6221718854129425853)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1831319466323685076 in succeeded_hashes:  # avoid duplicate inserts
            instance = client_3 = Client(name="Innovate LLC", email="hello@innovate.com", phone="1122334455", total_hours=0, total_amount=0, budget_amount=3000, is_over_budget=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1831319466323685076)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5929296410317997702 in succeeded_hashes:  # avoid duplicate inserts
            instance = client_4 = Client(name="Techies", email="support@techies.com", phone="5566778899", total_hours=0, total_amount=0, budget_amount=7500, is_over_budget=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5929296410317997702)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2618223179039538063 in succeeded_hashes:  # avoid duplicate inserts
            instance = project_1 = Project(client_id=1, name="Website Redesign", total_project_hours=0, total_project_amount=0, project_budget_amount=2000, is_over_budget=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2618223179039538063)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6080953323316201112 in succeeded_hashes:  # avoid duplicate inserts
            instance = project_2 = Project(client_id=2, name="Mobile App Development", total_project_hours=0, total_project_amount=0, project_budget_amount=5000, is_over_budget=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6080953323316201112)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4854321333550728504 in succeeded_hashes:  # avoid duplicate inserts
            instance = project_3 = Project(client_id=3, name="Cloud Migration", total_project_hours=0, total_project_amount=0, project_budget_amount=8000, is_over_budget=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4854321333550728504)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7825814919663707926 in succeeded_hashes:  # avoid duplicate inserts
            instance = project_4 = Project(client_id=4, name="Security Audit", total_project_hours=0, total_project_amount=0, project_budget_amount=3000, is_over_budget=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7825814919663707926)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3367748439366938075 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice_1 = Invoice(invoice_date=date(2025, 2, 1), project_id=1, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3367748439366938075)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2932080207031302953 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice_2 = Invoice(invoice_date=date(2025, 3, 15), project_id=2, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2932080207031302953)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7719351830516303132 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice_3 = Invoice(invoice_date=date(2025, 5, 10), project_id=3, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7719351830516303132)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5336949402670235208 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice_4 = Invoice(invoice_date=date(2025, 6, 20), project_id=4, invoice_amount=0, payment_total=0, invoice_balance=0, is_paid=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5336949402670235208)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6610636202261449198 in succeeded_hashes:  # avoid duplicate inserts
            instance = task_1 = Task(project_id=1, name="Design Phase", description="Create mockups and wireframes.", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=50.0, is_over_budget=False, invoice_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6610636202261449198)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7826401091315704719 in succeeded_hashes:  # avoid duplicate inserts
            instance = task_2 = Task(project_id=2, name="Development Phase", description="Develop core features and functionalities.", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=150.0, is_over_budget=False, invoice_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7826401091315704719)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1724296836090930790 in succeeded_hashes:  # avoid duplicate inserts
            instance = task_3 = Task(project_id=3, name="Testing Phase", description="Perform QA testing.", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=100.0, is_over_budget=False, invoice_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1724296836090930790)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8239038463632671378 in succeeded_hashes:  # avoid duplicate inserts
            instance = task_4 = Task(project_id=4, name="Deployment Phase", description="Deploy application to production.", total_task_hours_worked=0, total_task_amount_billed=0, task_budget_hours=60.0, is_over_budget=False, invoice_id=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8239038463632671378)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2123073639015767699 in succeeded_hashes:  # avoid duplicate inserts
            instance = person_1 = Person(client_id=1, name="Alice", email="alice@acme.com", phone="1231231234", billing_rate=50.0, total_hours_entered=0, total_amount_billed=0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2123073639015767699)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6521298207621052243 in succeeded_hashes:  # avoid duplicate inserts
            instance = person_2 = Person(client_id=2, name="Bob", email="bob@global.com", phone="2342342345", billing_rate=75.0, total_hours_entered=0, total_amount_billed=0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6521298207621052243)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1146572117815525146 in succeeded_hashes:  # avoid duplicate inserts
            instance = person_3 = Person(client_id=3, name="Charlie", email="charlie@innovate.com", phone="3453453456", billing_rate=100.0, total_hours_entered=0, total_amount_billed=0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1146572117815525146)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3376148194798064654 in succeeded_hashes:  # avoid duplicate inserts
            instance = person_4 = Person(client_id=4, name="Dana", email="dana@techies.com", phone="4564564567", billing_rate=120.0, total_hours_entered=0, total_amount_billed=0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3376148194798064654)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4525530598978367043 in succeeded_hashes:  # avoid duplicate inserts
            instance = timesheet_1 = Timesheet(task_id=1, person_id=1, date_worked=date(2025, 2, 10), hours_worked=8, month=2, year=2025, billing_rate=50.0, total_amount_billed=400.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4525530598978367043)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8238879318730114984 in succeeded_hashes:  # avoid duplicate inserts
            instance = timesheet_2 = Timesheet(task_id=2, person_id=2, date_worked=date(2025, 3, 12), hours_worked=6, month=3, year=2025, billing_rate=75.0, total_amount_billed=450.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8238879318730114984)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3946098470696517215 in succeeded_hashes:  # avoid duplicate inserts
            instance = timesheet_3 = Timesheet(task_id=3, person_id=3, date_worked=date(2025, 5, 8), hours_worked=10, month=5, year=2025, billing_rate=100.0, total_amount_billed=1000.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3946098470696517215)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8727226104058857896 in succeeded_hashes:  # avoid duplicate inserts
            instance = timesheet_4 = Timesheet(task_id=4, person_id=4, date_worked=date(2025, 6, 15), hours_worked=7.5, month=6, year=2025, billing_rate=120.0, total_amount_billed=900.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8727226104058857896)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5518924278558773392 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment_1 = Payment(invoice_id=1, payment_amount=200.0, payment_date=date(2025, 2, 20), notes="Initial deposit")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5518924278558773392)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3173214580673991393 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment_2 = Payment(invoice_id=2, payment_amount=300.0, payment_date=date(2025, 3, 18), notes="Partial payment")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3173214580673991393)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3560597479832750359 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment_3 = Payment(invoice_id=3, payment_amount=400.0, payment_date=date(2025, 5, 15), notes="Quarterly payment")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3560597479832750359)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4619695064789517690 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment_4 = Payment(invoice_id=4, payment_amount=500.0, payment_date=date(2025, 6, 25), notes="Final payment")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4619695064789517690)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
