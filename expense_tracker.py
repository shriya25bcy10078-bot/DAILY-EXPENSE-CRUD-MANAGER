from expense import Expense
import calendar
from datetime import datetime


def main():

    print("==========DAILY EXPENSE MANAGER==========")

    file_path_expense = "expense.csv"
    budget = 10000
    #Get user input
    expense = user_input()

    #Expense to a file
    expense_file(expense, file_path_expense)

    #Summarize expense
    summarize_expense(file_path_expense, budget)

    pass
    

def user_input():
    name_expense = input("Enter name of expense - ")
    amount_expense = float(input("Enter amount of expense - "))

    category_expense = ['Needs', 'Wants']
    sub_category_need = ['🍔  Food','🏡  Home','📖  Learn']
    sub_category_want = ['🎬  Entertainment','🛍️  Shopping','✔️  Others']

    print("Enter category based on number given : ")
   
    while True:
        for i, category_name in enumerate(category_expense):
            print(f"{i+1}. {category_name} ")
        
        range_category = f"[1 - {len(category_expense)}]"
        try:
            choice = int(input("Enter category number from {range_category} - "))-1

        except Exception:
            pass

        if choice in range(len(category_expense)):
            category_choice = category_expense[choice]
            if choice == 0 :
                for j, sub_category_name in enumerate(sub_category_need):
                    print(f"{j+1}.{sub_category_name}")

                range_subcategory = f"[1 - {len(sub_category_need)}]"
                sub_choice = int(input("Enter category number from {range_subcategory} - "))-1
                sub_category_choice = sub_category_need[sub_choice]

            else :
                for j, sub_category_name in enumerate(sub_category_want):
                    print(f"{j+1}.{sub_category_name}")

                range_subcategory = f"[1 - {len(sub_category_want)}]"
                sub_choice = int(input("Enter category number from {range_subcategory} - "))-1
                sub_category_choice = sub_category_want[sub_choice]
   

            new_expense = Expense(name=name_expense, category = category_choice,sub_category=sub_category_choice,amount = amount_expense)
            return new_expense

        else:
            print("Invalid. Enter again.")
            
        

def expense_file(expense : Expense ,file_path_expense):
    print("Saving User Expense : {expense} to {file_path_expense}")

    with open (file_path_expense, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category},{expense.sub_category}\n")

def summarize_expense(file_path_expense, budget):
    print("Summary of Expense")
    expenses : list[Expense] = []
    with open(file_path_expense, "r") as f:
        lines = f.readlines()

        for line in lines:
            stripped_line = line.strip()
            if not stripped_line:
                continue
            if stripped_line.count(',')!=3:
                print(f"Warning: Skipping corrupted line in file: '{stripped_line}'")
                continue 
            name_expense, amount_expense, category_name, sub_category_name = stripped_line.split(",")
            line_expense = Expense(name = name_expense, amount = float(amount_expense), category = category_name, sub_category = sub_category_name)

            expenses.append(line_expense)
        
    amount_by_category = {}
    for expense in expenses:
        key = expense.category

        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Categories : ")
    for key, amount in amount_by_category.items():
        print(f"   {key}: Rs{amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent Rs {total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"Remaining Budget : Rs{remaining_budget:.2f}")

    now = datetime.now()

    days_in_month = calendar.monthrange(now.year, now.month)[1]

    remaining_days = days_in_month - now.day

    print("Remaining days in the current month : ", remaining_days)

    daily_budget = remaining_budget/remaining_days
    print(f"Budget Per Day : Rs{daily_budget:.2f}")


    print(amount_by_category)

def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main() #to ensure that the this method runs only in this file
