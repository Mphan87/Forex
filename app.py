from operator import truediv
from unittest import result
from flask import Flask, request, render_template, flash
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes

app= Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

c = CurrencyRates()
cc = CurrencyCodes()

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/results')
def check():
    frm = request.args["frm"]
    to = request.args["to"]
    amount = request.args["amt"]
    dict_file = open("currency.txt")
    words = [w.strip() for w in dict_file]
    dict_file.close()

    if frm not in words:
        flash("Please enter a valid Currency Code: EUR USD JPY BGN CZK DKK HUF PLN RON SEK CHF ISK NOK HRK TRY AUD BRL CAD CNY HKD IDR INR KRW MXN MYR NZD PHP SGD THB ZAR GBP")
    
        return render_template('home.html')
    
    if to not in words:
        flash("Please enter a valid Currency Code: EUR USD JPY BGN CZK DKK HUF PLN RON SEK CHF ISK NOK HRK TRY AUD BRL CAD CNY HKD IDR INR KRW MXN MYR NZD PHP SGD THB ZAR GBP")
    
        return render_template('home.html')

    if amount == "":
        flash("Please enter a value")
        return render_template('home.html')

    else:
        symbol = cc.get_symbol(to)
        result = round(c.convert(frm, to, float(amount)),2)
        return render_template('results.html', result = result, symbol = symbol)














 
        
   
        
