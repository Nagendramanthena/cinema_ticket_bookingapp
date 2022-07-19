import main
import sqlite3
import random
import string










def changedb(seat_i):
    connection = sqlite3.Connection("tickets.db")
    connection.execute("""
    update "THEATRE" set "occupied" = 1
    where "seat_id" = ?
    """, [seat_i])
    connection.commit()
    connection.close()

def changebalance(seat_i,accountholde,cv,cardnumbe):
    price = main.price(seat_id=seat_i)
    balance = main.amount(accountholde, cv, cardnumbe)
    newbalance = balance - price
    connection = sqlite3.Connection("banking.db")
    connection.execute("""
    update "Bank" set "balance" = ?
    where "cv" = ? and "accountholder" = ? and "cardnumber" = ?
    """, [newbalance, cv, accountholde, cardnumbe])
    connection.commit()
    connection.close()
    #return (str(price) + " rupees has been debited from your bank "+f"Your new balance is {newbalance}")

def confirm(seat_i,cv,accountholde,cardnumbe):
    price = main.price(seat_id=seat_i)
    balance  = main.amount(accountholde,cv,cardnumbe)
    if(balance == "incorrectdetails"):
        return  "incorrect card details please try again"
    else:
        if(price<=balance):
            result = main.confirmation(seat_i, cv, cardnumbe, accountholde)
            if result == "cv":
                return ("incorrect card details ,no user found ,please recheck your card details. :(")
            elif result == "o":
                return "seat occupied"
            elif result == "s":
                changedb(seat_i)
                changebalance(seat_i,accountholde,cv,cardnumbe)
                ticket_id = res = ''.join(random.choices(string.ascii_uppercase +
                                                         string.digits, k=7))
                return (f"purchase succesful + your ticket_id:{ticket_id}")

        else:
            return ("insufficent balance in bank account")

def price_of_ticket(seat_id):
    return main.price(seat_id)

def balance_of_accountholder(ah,cv,cn):
    return  main.amount(ah,cv,cn)

def remainingbalance(seta_id,ah,cv,cn):
    ba = balance_of_accountholder(ah,cv,cn)
    p = price_of_ticket(seat_id=seta_id)
    if(p<ba):
        return ba-p
    else:
        return "insufficent balance"






