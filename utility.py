#!/usr/bin/env python
# coding: utf-8
#import sys
expense_list = []
budget = 0

def add_expense():
    date = input('The date of the expense in the format YYYY-MM-DD')
    category = input('The category of the expense, such as Food or Travel')
    amount = input('The amount spent ')
    description = input('A brief description of the expense')
    expense_dict = {'date':date, 'category': category, 'amount': amount, 'description': description}
    expense_list.append(expense_dict)

def view_expense(expense_list):
    for expense in expense_list:
        empty_keys = []
        keys = ['date','category','amount','description']
        for key in keys:
            if expense[key] == "":
                empty_keys.append(key)
        if len(empty_keys)==0:
            print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
        else:
            comma_separated_empty_keys = ", ".join(repr(empty_key) for empty_key in empty_keys)
            print(f"{comma_separated_empty_keys} is missing in {expense}")

def set_budget():
    monthly_budget = int(input('Enter total amount allowcated for 1 month budget'))
    return monthly_budget

def total_expense(expense_list):
    budget=set_budget()
    total_expense = 0
    for expense in expense_list:
        if expense['amount'] == '':
            expense['amount'] = 0;
        total_expense += int(expense['amount'])
    if total_expense > budget:
        print('You have exceeded your budget!')
    else:
        balance_amount = budget - total_expense
        print(f"You have Rs {balance_amount} left for the month")

import csv
import os 

def save_expense_csv():

    output_dir = r'E:\simply learn\code\Personal Expense Tracker'
    csv_file_path = os.path.join(output_dir, 'expenses.csv') # Using os.path.join for cross-platform compatibility


    column_names = list(expense_list[0].keys())
    print(f"column names (column headers): {column_names}")
    print(f"Saving data to: {csv_file_path}")

    # 4. Write to the CSV file
    try:
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            # Create a DictWriter object
            # The 'fieldnames' argument is essential here!
            writer = csv.DictWriter(csvfile, fieldnames=column_names)

            # Write the header row
            writer.writeheader()

            # Write each dictionary as a row
            writer.writerows(expense_list)

        print(f"Successfully saved {len(expense_list)} records to '{csv_file_path}'")

    except IOError as e:
        print(f"Error: Could not write to file {csv_file_path}. Please check permissions or path. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# In[ ]:


def load_expense_csv():
    input_dir = r'E:\simply learn\code\Personal Expense Tracker'
    csv_file_path = os.path.join(input_dir, 'expenses.csv')
    global expense_list
    expense_list.clear()
    print(f"Attempting to read data from: {csv_file_path}")
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                expense_list.append(row)
            print(f"Successfully loaded {len(expense_list)} records.")
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found. Please check the path.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the CSV: {e}")


# In[ ]:


def menu():
    menu_sel = int(input('1.Add expense\n2.View expense\n3.Track expense\n4.Save expense\n5.Exit\n'))
    if menu_sel == 1:
        print("You chose Add expense\n")
        add_expense()
    elif menu_sel == 2:
        print("You chose View expense\n")
        view_expense(expense_list)
    elif menu_sel == 3:
        print("You chose Track expense\n")
        total_expense(expense_list)
    elif menu_sel == 4:
        print("You chose Save expense\n")
        save_expense_csv()
    elif menu_sel == 5:
        
        save_expense_csv()
        print("You chose Exit\n")
        #sys.exit(0)
    else:
        print("Invalid choice. Please select 1, 2, 3, 4 or 5.")
    return menu_sel


