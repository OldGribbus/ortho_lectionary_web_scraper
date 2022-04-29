from bs4 import BeautifulSoup
from datetime import date
import requests 
import sys # for command line arguments (sys.argv)
import re

def webscraping(arguments = ''):

    today = date.today()
    year = today.year
    month = today.month
    day = today.day

    url = f"https://www.holytrinityorthodox.com/calendar/index.php?year={year}&today={day}&month={month}&trp=0&tzo=13"
    page = requests.get(url).text
    doc = BeautifulSoup(page,'html.parser') 
    
    def calendar_date_fast():
        calendar = doc.find('td', 'cellbg')
        for string in (calendar.p.span.b.strings):
            print(string.strip()

    def scripture_readings():
        readings_tag = doc.find('b', string ='The Scripture Readings')
        # Look for the sibling 'normaltext' class. 
        readings = readings_tag.parent.find_all(string=re.compile(':'))
        
        print(f"The scripture readings for {year}/{month}/{day}:")
        print("-----------------")
        for reading in readings:
            print(reading)
        print("-----------------")
    
    # - Only execute the functions that were called - #
    calendar_date_and_tone()
    scripture_readings()

if __name__ == "__main__":
    #add the ability to have multiple commands - fasting days, saints,and troparia. 
    webscraping(sys.argv)
    # the idea would be to return certain values maybe? No values put in just returns the current day + readings. Anything else needs to be specified. 
