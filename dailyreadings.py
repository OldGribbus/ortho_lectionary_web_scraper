from bs4 import BeautifulSoup
from datetime import date
import requests 
import sys # for command line arguments 
import re

def webscraping():
    today = date.today()
    year = today.year
    month = today.month
    day = today.day
    print (year, month, day)

    url = f"https://www.holytrinityorthodox.com/calendar/index.php?year={year}&today={day}&month={month}&trp=0&tzo=13"
    page = requests.get(url).text
    doc = BeautifulSoup(page,'html.parser') 
    
    readings_tag = doc.find('b', string="The Scripture Readings")
    readings = readings_tag.parent.find_all(string=re.compile(':'))
    
    print("The scripture readings: ")
    print("-----------------")
    for reading in readings:
        print(reading)
    print("-----------------")

if __name__ == "__main__":
    webscraping()
