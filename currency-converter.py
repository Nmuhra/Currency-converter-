import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk


class RealTimeCurrencyConverter():
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 

        amount = round(amount * self.currencies[to_currency], 4) 
        return amount
def __init__(self, converter):
    tk.Tk.__init__(self)
    self.title = 'Currency Converter'
    self.currency_converter = converter
    self.geometry("500x200")
    self.intro_label = Label(self, text = 'currency converter',  fg = 'blue', relief = tk.RAISED, borderwidth = 3)
    self.intro_label.config(font = ('Courier',15,'bold'))
    self.intro_label.place(x = 10 , y = 5)
    self.date_label.place(x = 170, y= 50)
