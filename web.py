import justpy as jp
import index
import pywhatkit


def webpage():
    wp = jp.QuasarPage(tailwind=True)
    div = jp.Div(a=wp, classes="bg-blue-400 h-screen grid grid-cols-1 justify-items-center	box-sizing: border-box ")
    jp.H1(a=div,text="WATCH MY SHOW",classes="p-5 m-5 text-3xl")
    jp.H1(a=div,text="Book your tickets online",classes="p-5 m-5 text-3xl")
    in1 = jp.Input(a=div, placeholder="enter cardnumber",classes="form-input w-15 h-10 p-4 m-4")
    in2 = jp.Input(a=div, placeholder="enter cv",classes="form-input w-15 h-10 p-4 m-4")
    in3 = jp.Input(a=div, placeholder="enter seat_id",classes="form-input w-25 h-10 p-4 m-4")
    in4 = jp.Input(a=div, placeholder="enter accountholder name",classes="form-input h-10  w-25 p-4 m-4")
    divv = jp.Div(a=div,text="result ....")
    pri = jp.Div(a=div,text='price')
    balance = jp.Div(a=div,text="balance")
    jp.Button(a=div,text="Book",classes="border border-blue-500  w-20 m-2 py-1 px-4 rounded text-blue-600 hover:bg-green-500 hover:text-white",
              click=click_on,input1 = in1,input2 = in2,input3 = in3,input4 = in4,result = divv,price= pri,balance = balance)
    return wp

def click_on(widget,msg):
    in1 = widget.input1
    in2 = widget.input2
    in3 = widget.input3
    in4 = widget.input4
    print("Into the index")
    ticketprice = index.price_of_ticket(in3.value)
    balance = index.balance_of_accountholder(in4.value,in2.value,in1.value)
    body = "Hello we are from watch my show," \
           "This is an autogeneretaed message ,Your purchase is succesful,  " \
           f"TicketPrice: {ticketprice}" \
           f"Your bank balance: {balance} " \
           f"{ticketprice} rupees has been debited from your account"
    widget.result.text = index.confirm(in3.value, int(in2.value), in4.value, int(in1.value))
    widget.price.text = ticketprice
    widget.balance.text = balance

    pywhatkit.sendwhatmsg("+918985236289"
                          "", body, 20, 28)

jp.Route("/",webpage)
jp.justpy()
