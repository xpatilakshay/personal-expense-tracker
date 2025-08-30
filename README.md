# personal-expense-tracker
Personal Expense Tracker is a Python-based application that helps users track and manage their personal expenses. It allows adding, viewing, filtering, and deleting expense records, with data stored in a MySQL database for easy access and persistence.

# Personal Expense Tracker

## Description
This is a simple Personal Expense Tracker built using Python and MySQL. The application allows users to:

- Add new expenses.
- View and filter expenses by various criteria.
- Delete expenses based on different filters such as serial number, date, amount, category, etc.
- Store expenses in a MySQL database.

## Features
- **Add Expense**: Allows the user to input expenses including date, category, amount, and an optional note.
- **View Expenses**: Displays all expenses stored in the database in a tabular format.
- **Filter Expenses**: Allows filtering of expenses based on different criteria (Serial Number, Date, Amount, etc.)
- **Delete Expense**: Enables deletion of records based on user-defined criteria.
  
## Technologies Used
- **Python**: Main programming language for building the application.
- **MySQL**: Used for storing and managing expense data.
- **Tabulate**: A Python library for pretty-printing tables.
  
## Installation

### Clone the Repository
```bash
git clone https://github.com/your-username/personal-expense-tracker.git
```
### Install Dependencies

#### Create a virtual environment:

```bash
python3 -m venv venv
```

### Activate the virtual environment:

#### On Windows:

```bash
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
source venv/bin/activate
```

#### Install required Python libraries:

```bash
pip install mysql-connector-python tabulate
```
