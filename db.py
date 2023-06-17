from peewee import *

# enter the username and password of your database
# The port should be modified to the actual mysql port
mysql_database = MySQLDatabase("budget_tracker", user="", password="", host="localhost", port=0)


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
