import database

# add record to db
database.add_one('samuel','john','sam78@gmail.com')
# add many records to  db
list1= [
    ('a','b','ab@gmail.com'),
    ('james','sunny','james@123.com')

]
database.add_many(list1)
# delete record (rowid needs to be sent as string)
database.delete_one('1')
# print
database.show_all()