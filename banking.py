import sqlite3
connection = sqlite3.Connection("banking.db")

# connection = sqlite3.Connection("banking.db")
# connection.execute("""
# create table "Bank" (
#  "cardnumber" INTEGER,
#  "Cv" INTEGER,
#  "holder" TEXT,
#  "balance" INTEGER
# )
# """)
# connection.commit()
# connection.close()
def insert(cardnumber,acc,cv,bala):
    connection.execute("""
    insert into "Bank" ("cardnumber","accountholder","cv","balance") VALUES(?,?,?,?)
      
    """,[cardnumber,acc,cv,bala])
    connection.commit()

for i in range(10,30):
    insert(12345678+i,"john",12*i,100*i)

connection.close()

