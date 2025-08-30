import mysql.connector
from tabulate import tabulate
from datetime import datetime

cursor = None
conn = None

def create_connection():
    try:
        global conn
        conn = mysql.connector.connect(
            host="Localhost",
            user="root",
            password="akshay",
            database="projects"
        )

        global cursor
        cursor = conn.cursor()

        cursor.execute("create database if not exists expense_db")
        cursor.execute("use expense_db")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE NOT NULL,
            category VARCHAR(50) NOT NULL,
            amount DECIMAL(10,2) NOT NULL,
            note VARCHAR(255)
        )
        """)

        conn.commit()
        print("Table expenses Created Successfully")
    except mysql.connector.Error as e:
        print("Exception Occured : ", e)


def add_expense():
    global conn, cursor
    date = input("Enter the Date (YYYY-MM-DD) : ")
    category = input("Enter the expense category (Food, Travel, Grocery, etc.) : ").title()
    amount = float(input("Enter the amount : "))
    note = input("Enter the note (optional) : ").lower()

    query = "insert into expenses (date, category, amount, note) values (%s, %s, %s, %s)"
    values = (date, category, amount, note)

    cursor.execute(query, values)
    conn.commit()
    print("Expense Added successfully")


def view_expenses():
    global conn, cursor
    cursor.execute("select * from expenses")
    print()
    rows = cursor.fetchall()
    if rows:
        headers = ["SR", "Date", "Category", "Amount", "Comment"]
        print(tabulate(rows, headers, tablefmt="grid"))
    else:
        print("No expenses found")


def filters():
    global conn, cursor
    print("\n--- Available Filters ---")
    print("1 : Filter by Serial Number (ID)")
    print("2 : Filter by Exact Date (YYYY-MM-DD)")
    print("3 : Filter by Date Range (YYYY-MM-DD to YYYY-MM-DD)")
    print("4 : Filter by Exact Amount")
    print("5 : Filter by Amount Range")
    print("6 : Filter by Category (Food, Travel, Grocery, etc.)")
    print("7 : Filter by Note")
    print("------------------------\n")
    filter_no = int(input("Choose the filter you want to apply on database : "))
    match filter_no:
        case 1:
            sr_no = int(input("Enter the serial number of which expense you want ? : "))
            cursor.execute(f"select * from expenses where id = {sr_no}")
            rows = cursor.fetchall()
            if rows:
                headers = ["SR", "Date", "Category", "Amount", "Comment"]
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print(f"No Expense found with this Serial id : {sr_no}")
        case 2:
            while True:
                date_input = input("Enter the date (YYYY-MM-DD) of which you want expense: ")
                try:
                    date_obj = datetime.strptime(date_input, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invalid date format! Please enter in YYYY-MM-DD format.")
            cursor.execute(f"select * from expenses where date = '{date_obj}'")
            rows = cursor.fetchall()
            if rows:
                headers = ["SR", "Date", "Category", "Amount", "Comment"]
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print(f"No Expense found with this date : '{date_obj}'")
        case 3:
            while True:
                start_date = input("Enter the starting date (YYYY-MM-DD) : ")
                end_date = input("Enter the Ending date (YYYY-MM-DD) : ")
                try:
                    date_obj1 = datetime.strptime(start_date, "%Y-%m-%d").date()
                    date_obj2 = datetime.strptime(end_date, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invalid date format! Please enter in YYYY-MM-DD format.")
            cursor.execute(f"select * from expenses where date >= '{date_obj1}' and date <= '{date_obj2}'")
            rows = cursor.fetchall()
            if rows:
                headers = ["SR", "Date", "Category", "Amount", "Comment"]
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print(f"No Expense found with this date : '{date_obj1}' to '{date_obj2}'")
        case 4:
            amount = float(input("Enter the amount of which you want expense : "))
            cursor.execute(f"select * from expenses where amount = '{amount}'")
            rows = cursor.fetchall()
            if rows:
                headers = ["SR", "Date", "Category", "Amount", "Comment"]
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print(f"No Expense found with this amount : '{amount}'")
        case 5:
            amount1 = float(input("Enter the starting/First amount of your expense : "))
            amount2 = float(input("Enter the Ending/Second amount of your expense : "))
            cursor.execute(f"select * from expenses where amount >= {amount1} and amount <= {amount2}")
            rows = cursor.fetchall()
            if rows:
                headers = ["SR", "Date", "Category", "Amount", "Comment"]
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print(f"No Expense found with this amount : '{amount1}' to '{amount2}'")
        case 6:
            cate = input("Enter the category you want to filter : ").title()
            cursor.execute(f"select * from expenses where category = '{cate}'")
            rows = cursor.fetchall()
            if rows:
                headers = ["SR", "Date", "Category", "Amount", "Comment"]
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print(f"No Expense found with this category : '{cate}'")
        case 7:
            note = input("Enter the note you want to filter : ")
            cursor.execute(f"select * from expenses where note = '{note}'")
            rows = cursor.fetchall()
            if rows:
                headers = ["SR", "Date", "Category", "Amount", "Comment"]
                print(tabulate(rows, headers, tablefmt="grid"))
            else:
                print(f"No Expense found with this note : '{note}'")
        case _:
            print("Invalid filter number kindly choose from above filters...")


def delete_expenses():
    print("\n--- Available Deletion Filters ---")
    print("1 : Delete by Serial Number (ID)")
    print("2 : Delete by Exact Date (YYYY-MM-DD)")
    print("3 : Delete by Date Range (YYYY-MM-DD to YYYY-MM-DD)")
    print("4 : Delete by Exact Amount")
    print("5 : Delete by Amount Range")
    print("6 : Delete by Category (Food, Travel, Grocery, etc.)")
    print("7 : Delete by Note")
    print("-------------------------------\n")

    how = int(input("Choose how you want to delete the expenses: "))
    match how:
        case 1:
            sr_no = int(input("Enter the serial number of which expense you want to delete? : "))
            cursor.execute(f"DELETE FROM expenses WHERE id = {sr_no}")
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Record/Expense with ID/SR No {sr_no} deleted successfully...")
            else:
                print(f"No record found with ID/SR No {sr_no}")
            print_table()

        case 2:
            while True:
                date_input = input("Enter the date (YYYY-MM-DD) of which you want to delete records/Expenses: ")
                try:
                    date_obj = datetime.strptime(date_input, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invalid date format! Please enter in YYYY-MM-DD format.")
            cursor.execute(f"DELETE FROM expenses WHERE date = '{date_obj}'")
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Record/Expense with Date {date_obj} deleted successfully...")
            else:
                print(f"No records found with this date: {date_obj}")
            print_table()

        case 3:
            while True:
                start_date = input("Enter the starting date (YYYY-MM-DD) : ")
                end_date = input("Enter the Ending date (YYYY-MM-DD) : ")
                try:
                    date_obj1 = datetime.strptime(start_date, "%Y-%m-%d").date()
                    date_obj2 = datetime.strptime(end_date, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invalid date format! Please enter in YYYY-MM-DD format.")
            cursor.execute(f"DELETE FROM expenses WHERE date >= '{date_obj1}' AND date <= '{date_obj2}'")
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Records/Expenses between Date {date_obj1} and {date_obj2} deleted successfully...")
            else:
                print(f"No records found between {date_obj1} and {date_obj2}")
            print_table()

        case 4:
            amount = float(input("Enter the exact amount of which you want to delete expenses: "))
            cursor.execute(f"DELETE FROM expenses WHERE amount = '{amount}'")
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Record/Expense with Amount {amount} deleted successfully...")
            else:
                print(f"No records found with Amount: {amount}")
            print_table()

        case 5:
            amount1 = float(input("Enter the starting/First amount of your expense: "))
            amount2 = float(input("Enter the Ending/Second amount of your expense: "))
            cursor.execute(f"DELETE FROM expenses WHERE amount >= {amount1} AND amount <= {amount2}")
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Records/Expenses between Amount {amount1} and {amount2} deleted successfully...")
            else:
                print(f"No records found between Amount {amount1} and {amount2}")
            print_table()

        case 6:
            cate = input("Enter the category you want to filter: ").title()
            cursor.execute(f"DELETE FROM expenses WHERE category = '{cate}'")
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Record/Expense with Category {cate} deleted successfully...")
            else:
                print(f"No records found with Category: {cate}")
            print_table()

        case 7:
            note = input("Enter the note you want to filter: ")
            cursor.execute(f"DELETE FROM expenses WHERE note = '{note}'")
            conn.commit()
            if cursor.rowcount > 0:
                print(f"Record/Expense with Note {note} deleted successfully...")
            else:
                print(f"No records found with Note: {note}")
            print_table()

        case _:
            print("Invalid operation...")


def print_table():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    if rows:
        headers = ["SR", "Date", "Category", "Amount", "Comment"]
        print(tabulate(rows, headers, tablefmt="grid"))
    else:
        print("No records found in the table.")


def main():
    while True:
        print("\n--- Choose Operation ---")
        print("1 : Add Expense")
        print("2 : View Expenses")
        print("3 : Filter Expenses")
        print("4 : Delete Expenses")
        print("5 : Exit")
        print("------------------------\n")

        choice = int(input("Choose an operation: "))
        match choice:
            case 1:
                add_expense()
            case 2:
                view_expenses()
            case 3:
                filters()
            case 4:
                delete_expenses()
            case 5:
                print("Exiting program...")
                break
            case _:
                print("Invalid choice! Please select a valid operation.")

create_connection()
main()

if conn is not None and conn.is_connected():
    conn.commit()
    conn.close()
    print("Connection closed safely")