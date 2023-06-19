from peewee import *


mysql_database = SqliteDatabase("budget.db")


class BaseModel(Model):
    class Meta:
        database = mysql_database


class RecurringExpenditure(BaseModel):
    id = AutoField()
    name = CharField()
    amount = IntegerField()
    date = DateField()


class NonRecurringExpenditure(BaseModel):
    id = AutoField()
    name = CharField()
    amount = IntegerField()
    date = DateField()


class GeneralIncome(BaseModel):
    id = AutoField()
    name = CharField()
    amount = IntegerField()
    date = DateField()


def create_non_tables():
    NonRecurringExpenditure.create_table()


def create_income_tables():
    GeneralIncome.create_table()


def create_recurring_tables():
    RecurringExpenditure.create_table()
