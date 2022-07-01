from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt 

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to moringa school")

def news_of_today(request):
    date = dt.date.today()
    #FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
     <html>
       <body>
         <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
        </body>
     </html
    '''
    return HttpResponse(html)

def convert_dates(dates):
    #function that gets the weekday number for dates
    day_number = dt.date.weekday(dates)
    #Making a variable of dates in form of Arrays for dates
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','sunday']
    #Returning the actual date of the week
    day = days[day_number]
    return day

    