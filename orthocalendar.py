from bs4 import BeautifulSoup
from datetime import date
import requests 
import sys # for command line arguments 
import re

def webscraping(arguments = ''):
    today = date.today()
    year = today.year
    month = today.month
    day = today.day

    url = f"https://www.holytrinityorthodox.com/calendar/index.php?year={year}&today={day}&month={month}&trp=0&tzo=13"
    page = requests.get(url).text
    doc = BeautifulSoup(page,'html.parser') 
    
    def scripture_readings():
        readings_tag = doc.find('b', string="The Scripture Readings")
        readings = readings_tag.parent.find_all(string=re.compile(':'))
        
        print(f"The scripture readings for {year}/{month}/{day}:")
        print("-----------------")
        for reading in readings:
            print(reading)
        print("-----------------")

    # The function below is in quarentine - there is no string attribute to 'calendar' 
    # def calendar_date_and_tone():
    #     calendar = doc.find('b', string=re.compile('Week '))
    #     print (calendar.string)
    
    # - Only execute the functions that were called - #
    scripture_readings()
    # calendar_date_and_tone()

if __name__ == "__main__":
    #add the ability to have multiple commands - fasting days, saints,and troparia. 
    webscraping(sys.argv)
    # the idea would be to return certain values maybe? No values put in just returns the current day + readings. Anything else needs to be specified. 
