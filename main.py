import  sqlite3
import string
import random


def show_available_tickets():
    connection  = sqlite3.Connection('tickets.db')
    cursor  = connection.cursor()
    result = cursor.execute("""
    select "seat_id","price" from "THEATRE"
    where "occupied" != 1
    """)
    re = result.fetchall()
    connection.close()
    return re

def _ticket_availability(seat):
    connection = sqlite3.Connection("tickets.db")
    cursor = connection.cursor()
    res = cursor.execute("""
    select "occupied" from "THEATRE"
    where "seat_id" = ? and "occupied" = 0 
    """,[seat])
    result  = res.fetchall()
    connection.close()
    if(len(result)!=0):
        return True
    else:
        return False

def price(seat_id):
    connection = sqlite3.Connection("tickets.db")
    cursor = connection.cursor()
    re = cursor.execute("""
    select "price" from "THEATRE"
    where "seat_id" = ?
    """,[seat_id])
    res = re.fetchall()
    connection.close()
    return res[0][0]

def _check_card_details(cardnumber,cv,accountholder):
    con = sqlite3.Connection("banking.db")
    cursor = con.cursor()
    result = cursor.execute("""
    select "accountholder" from "Bank" 
    where "cardnumber" = ? and "cv" =?  and "accountholder" = ?
    """,[cardnumber,cv,accountholder])
    re = result.fetchall()
    con.close()

    if len(re)!=0:
        return True
    else:
        return False



def amount(accountholder,cv,cardnumber):
    connection = sqlite3.Connection("banking.db")
    cursor = connection.cursor()
    re = cursor.execute("""
    select "balance" from "Bank"
    where "accountholder" = ? and "cv" = ? and "cardnumber" = ?
    
    """,[accountholder,cv,cardnumber])
    result = re.fetchall()
    connection.close()
    if len(result)!=0:
        return result[0][0]
    else:
        return "incorrectdetails"

def reqamount():
    con = sqlite3.Connection("tickets.db")
    con.cursor()

def confirmation(seat_id,cv,cardnum,accholder):
    if _ticket_availability(seat_id) == True:
        if _check_card_details(cardnum,cv,accholder) == True:
            return "s"
        else:
            return "cv"
    else:
        return "o"



#print(_check_card_details(123456789,490,"krishna"))
#
# print(amount("krishna",490,123456789))
#print(price("A2"))
# cn = int(input("enter cardnumber :"))
# cv = int(input("enter cv :"))
# ah = input("enter name of accontholder :")
# si = str(input("enter seat_id :"))
# print(_ticket_availability(si))
#print(_check_card_details(123456789,490,"krishna"))
print(amount("kr",789,123))
