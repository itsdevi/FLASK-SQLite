import expense_tracker

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses by Category")
        print("4. Generate Report by Category")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = int(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            expense_tracker.add_one(amount, category,date)
        
        elif choice == '2':
            expense_tracker.show_all()
        
        elif choice == '3':
            category = input("Enter category: ")
            cat=expense_tracker.filter_by_category(category)
            for c in cat:
                print(f"Amount: {c[0]} Category: {c[1]} Date: {c[2]}")
        
        elif choice == '4':
            report = expense_tracker.generate_report_by_category()
            for row in report:
                print(f"Category: {row[0]}, Total: {row[1]}")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()


# expense_tracker.add_one('3500','food','10-march')
# expense_tracker.add_one('2000','vehicle','19-may')
# expense_tracker.add_one('7000','food','22-jan')
# expense_tracker.add_one('900','bills','22-jan')

# expense_tracker.add_one('450','food','30-may')
# expense_tracker.add_one('200','vehicle','17-april')
# expense_tracker.add_one('790','food','25-may')
# expense_tracker.add_one('810','bills','23-july')


# expense_tracker.show_all()

# expense_tracker.sort_categories()

# food_expenses = expense_tracker.filter_by_category('food')
# print("\nFood Expenses:")
# for expense in food_expenses:
#     print(f"Amount: {expense[0]} Category: {expense[1]} Date: {expense[2]}")