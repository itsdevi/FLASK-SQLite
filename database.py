import sqlite3

# conn = sqlite3.connect('customer.db')

# # cursor
# c= conn.cursor()

def show_all():

    conn = sqlite3.connect('customer.db')
    c= conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items= c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c= conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)",(first,last,email))
    conn.commit()
    conn.close()

def add_many(list):
    conn = sqlite3.connect('customer.db')
    c= conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)",(list))
    conn.commit()
    conn.close()



def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c= conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid =(?)",(id))
    conn.commit()
    conn.close()











# table - case sensitive
# many_customers= [('west','brown','west@brown.com'),('steff','kumar','steffy23@gmail.com'),('anne','smith','anne96istyping@mail.com')]
# c.execute("INSERT INTO customers VALUES ('mary','cooper','mary9@email.com')")

#c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

# update record
# c.execute("""UPDATE customers SET first_name = 'bob'
#           WHERE rowid = 1

# """)
# delete from table

# c.execute("DELETE FROM customers WHERE rowid=4")
# query database
# c.execute("SELECT rowid, * FROM customers ")

#print(c.fetchall())
#print(c.fetchone()[0])  prints john
# commit command

# conn.commit()

#  close connection
# conn.close()
