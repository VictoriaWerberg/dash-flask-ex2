from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")


def Navigation():
    name, surname = "Vika", "Werberg"
    nav_up = [
        { "name" : "Product", "icon":"icon2.png", "arr":True, "number": False },
        { "name" : "Orders", "icon":"icon5.png" , "arr":True, "number": False },
        { "name" : "Checkout", "icon":"icon6.png",  "arr":False, "number": 2 },
        { "name" : "Setting", "icon":"icon8.png", "arr":False,"number": False }
        ]

    nav_down = [
        { "name" : "Help Center", "icon":"icon8.png", "color":False },
        { "name" : "Contact us", "icon":"icon9.png" , "color":False},
        { "name" : "Log out", "icon":"icon10.png" ,"color" :True}
        ]

    cards = [{"number": "89,935", "subtitle": "Total users", "percent":"+1.01%","diff":"10.2",\
             "icon":"c1.png", "color":False},
             {"number": "23,283.5", "subtitle": "Total products", "percent":"+0.49%","diff":"3.1",\
             "icon":"c2.png", "color":False},
             {"number": "46,827", "subtitle": "Total users", "percent":"-0.91","diff":"2.56",\
             "icon":"c3.png", "color":True},
             {"number": "124,854", "subtitle": "Refunded", "percent":"+1.5%","diff":"7.2",\
             "icon":"c4.png", "color":False}                         
             ]  

    lst = [{ "No": "No", "ID":"ID", "Date":"Date", "CustName": "Customer Name", \
           "Location": "Location", "Amount": "Amount", "StatusOrder": "Status Order", "Action":"Action"},
           { "No": 1, "ID":"#12594", "Date":"Dec 1, 2021", "CustName": "Frank Murlo", \
           "Location": "5th Avenu", "Amount": "$56,386", "StatusOrder": "New Order", "Action":"..."}
    ]

    return render_template('index.html', name = name, surname = surname,\
     nav_up = nav_up, nav_down = nav_down, cards = cards, lst = lst)

    
        