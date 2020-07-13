from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime


class SQLManager:
    Base = declarative_base()

    class ToDoTable(Base):
        __tablename__ = 'task'
        id = Column(Integer, primary_key=True)
        task = Column(String)
        deadline = Column(Date, default=datetime.today().date())

    def __init__(self, database_name):
        self.engine = create_engine(f'sqlite:///{database_name}?check_same_thread=False')
        SQLManager.Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def get_all_tasks(self):
        tasks = dict()
        for row in self.session.query(SQLManager.ToDoTable).order_by(SQLManager.ToDoTable.deadline).all():
            tasks[row.task] = row.deadline
        return tasks

    def get_tasks_for_deadline(self, date):
        tasks = dict()
        query = self.session.query(SQLManager.ToDoTable).filter(SQLManager.ToDoTable.deadline == date)
        for row in query:
            tasks[row.task] = row.deadline
        return tasks

    def get_missed_tasks(self):
        tasks = dict()
        query = self.session.query(SQLManager.ToDoTable) \
            .filter(SQLManager.ToDoTable.deadline < datetime.today().date()) \
            .order_by(SQLManager.ToDoTable.deadline).all()
        for row in query:
            tasks[row.task] = row.deadline
        return tasks

    def add_task(self, text, date):
        new_row = SQLManager.ToDoTable(task=text, deadline=date)
        self.session.add(new_row)
        self.session.commit()

    def delete_task(self, task):
        self.session.query(SQLManager.ToDoTable) \
            .filter(SQLManager.ToDoTable.task == task).delete()
        self.session.commit()
