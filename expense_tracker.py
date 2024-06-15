import sqlite3

# create table inside database

conn=sqlite3.connect('expenses.db')
c= conn.cursor()
c.execute("""CREATE TABLE expense(
          amount INTEGER NOT NULL,
          category TEXT,
          date TEXT) """)

conn.commit()
conn.close()

# print all records in table
def show_all():
    conn=sqlite3.connect('expenses.db')
    c= conn.cursor()
    c.execute("SELECT * FROM expense")
    items=c.fetchall()
    print("AMOUNT  CATEGORY  DATE")
    for item in items:
        print(item[0], item[1]+ " " +item[2])
    conn.commit()
    conn.close()

# add record to table
def add_one(amount,category,date):
    conn=sqlite3.connect('expenses.db')
    c= conn.cursor()
    c.execute("INSERT INTO expense VALUES(?,?,?)",(amount,category,date))
    conn.commit()
    conn.close()

# sort expenses into categories
def sort_categories():
    conn=sqlite3.connect('expenses.db')
    c=conn.cursor()
    c.execute("SELECT category FROM expense GROUP BY category ")
    items= c.fetchall()
    for item in items:
        print(item[0])
    conn.commit()
    conn.close()

# print records of single category
def filter_by_category(category):
    conn=sqlite3.connect('expenses.db')
    c=conn.cursor()
    c.execute("SELECT * FROM expense WHERE category = ?", (category,))
    expenses = c.fetchall()
    conn.close()
    return expenses
    

#  generate total expense  
def generate_report_by_category():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM expense GROUP BY category")
    report = c.fetchall()
    conn.close()
    return report


