# list of stocks.


apple = { "Company": "Apple",
          "Ticker" : "APPL",
          "Price" : "400",
          "Location": "USA"
}


tesla = { "Company": "Tesla",
          "Ticker" : "TSLA",
          "Price" : "340.55",
          "Location": "USA"
}

coke = { "Company": "Coca Cola",
          "Ticker" : "KO",
          "Price" : "66.75",
          "Location": "USA"
}

def apple_stock():
    global apple
    for i, v in list(apple.items()):
        print(i,"-----", v)

def tesla_stock():
    global tesla
    for i, v in list(tesla.items()):
        print(i,"-----", v)

def coke_stock():
    global coke
    for i, v in list(coke.items()):
        print(i, "-----", v)