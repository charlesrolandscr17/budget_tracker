import datetime
import os

from pymysql import Date

import db
from tabulate import tabulate


def display(tables):
    # Display a table for the data
    print(tables.capitalize())
    total, num_rows = 0, 0
    items = ""
    if tables == "income":
        items = db.GeneralIncome.select()
    elif tables == "recurring":
        items = db.RecurringExpenditure.select()
    elif tables == "nonrecurring":
        items = db.NonRecurringExpenditure.select()

    table = []
    for item in items:
        total += item.amount
        num_rows += 1
        table.append([item.id, item.name, item.amount, item.date])

    table.append([f"{num_rows} Row(s)", "Total", total, ''])
    print(tabulate(table, tablefmt="fancy_grid", headers=["id", "Name", "Amount", "Date"]))


def add_item(table):
    # Insert data into database
    name = input('Name: ')
    amount = int(input('Amount: '))
    date_input = input('Date: (Format: YYYY-MM-DD)')
    date = datetime.date.today() if date_input == "today" or date_input == "" else Date(int(date_input.split('-')[0]), int(date_input.split('-')[1]), int(date_input.split('-')[2]))
    if table == "income":
        gi = db.GeneralIncome(name=name, amount=amount,
                              date=date)
        gi.save()
    elif table == 'recurring':
        r = db.RecurringExpenditure(name=name, amount=amount,
                                    date=date)
        r.save()
    elif table == 'nonrecurring':
        nr = db.NonRecurringExpenditure(name=name, amount=amount,
                                        date=date)
        nr.save()

    print("Added Successfully...")


def clear(table):
    # Clear the table
    delete_item = input("Are you sure you want to clear table?:(y: yes, n:no")
    if table == "income" and delete_item.lower() == "y":
        db.mysql_database.drop_tables([db.GeneralIncome])
        db.create_income_tables()
    elif table == 'recurring' and delete_item.lower() == "y":
        db.mysql_database.drop_tables([db.RecurringExpenditure()])
        db.create_recurring_tables()
    elif table == 'nonrecurring' and delete_item.lower() == "y":
        db.mysql_database.drop_tables([db.NonRecurringExpenditure()])
        db.create_non_tables()

    print("Table Cleared")


def delete(table):
    # Delete an item from table
    item = input("Enter the id of the item you want to delete: ")
    if table == "income":
        db.GeneralIncome.delete_by_id(item)
    elif table == 'recurring':
        db.RecurringExpenditure.delete_by_id(item)
    elif table == 'nonrecurring':
        db.NonRecurringExpenditure.delete_by_id(item)

    print(f"Item {item} deleted successfully...")


def run():
    # Main function
    table = ""
    txt = """
    Select (1, 2, 3) for any of the following options;
    1. General Income
    2. Recurring Expenditure
    3. Non Recurring Expenditure
    q or exit: To exit
    Ans:"""

    txt2 = """
    1. Display
    2. Add
    3. Clear
    4. Delete
    cls: Clear Screen
    b: back
    Ans:"""

    while True:
        os.system("cls")
        option = input(txt)

        if option == "q" or option.lower() == "exit":
            break

        while True:
            option2 = input(txt2)
            if option == "1":
                table = "income"
            elif option == "2":
                table = "recurring"
            elif option == "3":
                table = "nonrecurring"
            else:
                print("Invalid Option")

            if option2 == "1":
                display(table)
            elif option2 == "2":
                add_item(table)
            elif option2 == "3":
                clear(table)
            elif option2 == "4":
                delete(table)
            elif option2 == "cls":
                os.system('cls')
            elif option2 == 'b':
                break
            else:
                print("Invalid option")


if __name__ == "__main__":
    run()
