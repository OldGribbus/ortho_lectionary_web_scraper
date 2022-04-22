 Orthodox lectionary web scraper
-----------------------------------
This is a simple Python web scraper I made using beautiful soup to quickly access the daily readings from this website https://www.holytrinityorthodox.com/calendar/index.php. 
I plan to eventually move the thing to be entirely offline and include various features such as the lives of the saints.

Commands:

orthocalendar [function] [date] 

Calling the script without any extra arguments will print the current day's readings. 

[function] tells the program what to print - the commands are: readings, saints, hymns, all.
The commands cause the program to print only what has been presented (the all command prints every available piece of info).

[date] sets what date the script will print out. 

These can be set via a config file. 
