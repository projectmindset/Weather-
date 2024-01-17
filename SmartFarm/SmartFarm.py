'''
This is a Smart Farm project.

An interactive web app that aims to advise new time farmers/investors of the following:
    -> current weather (API's)
    -> crop recommendations based on the current weather and season
    -> the estimated buying values of the crops (API's)
    -> some tutorials on how to prepare for irrigation, planting, harvesting etc..(youtube API)

INPUT VARIABLES:
    -name + email + password
    -location
    -Size of farm in acres

OUTPUT VARIABLES
    -current weather
    -current season
    -crop recommendations
    -buying & selling values for those crops

FLOW OF THE SITE:
    REGISTRATION
1. user inputs name, email + password
2. stored into a database/ text file

    ENTRY
3. user inputs their location
4. get weather information from that location
5. print the weather information
6. get the season and print it out (summer, spring, winter, autumn)
7. based on the season + temperature + humidity, 
        print out the list of crops that can be grown 
8. user selects the crops they want to see
9. print out the buying/selling prices of respective crops
10. print out youtube videos designed to outline the planting/harvesting/logistics process
'''

import datetime
import calendar
import time
import requests
from weatherAPI import collect_weather_information

#list of season based crops
spring = ['Sugarcane', 'Cotton', 'Jute', 'Tobacco' ]
summer = ['Tea', 'Coffee', 'Areca Nut', 'Cashew Nut', 'Coconut', 'Areca Nut', 'Oil Palm', 'Cocoa', 'Rubber']
autumn = ['Mango', 'Banana', 'Papaya', 'Pineapple', 'Guava', 'Citrus', 'Lemon', 'Grapes', 'Litchi', 'Pomegranate', 'Fig', 'Aonla', 'Avocado', 'Date Palm', 'Kiwi Fruit', 'Apple', 'Cherry', 'Almond', 'Apricot', 'Walnut', 'Pistachio Nut', 'Strawberry']
winter = ['Black Pepper', 'Cardamom', 'Ginger', 'Turmeric', 'Clove', 'Nutmeg', 'Cinnamon', 'Fenugreek', 'Cumin Fennel', 'Vanilla', 'Saffron', 'Chilli', 'Tamarind', 'Garlic', 'Coriander']

seasons_dict = {
    'spring' : spring,
    'summer' : summer, 
    'autumn' : autumn, 
    'winter' : winter
}

#list of seasons and their respective months
months_seasons = {
    'January' : 'Winter',
    'February' : 'Winter',
    'March' : 'Spring', 
    'April' : 'Spring', 
    'May' : 'Spring', 
    'August' : 'Summer', 
    'September' : 'Summer',
    'October' : 'Summer',
    'November' : 'Fall', 
    'December' : 'Fall'
}

print("-----------------------------")
print("Welcome to Smart Farm")
time.sleep(2)

#function to greet and get user details

name = input("Enter name: ")
time.sleep(1)
email = input("Enter email: ")
time.sleep(1)
password = input("Password: ")
time.sleep(1)
type = input("Farmer (F) or Investor (I): ")
time.sleep(1)
farm_size = input("Farm size in acres: ")
time.sleep(1)
date = datetime.datetime.now()


# opening the file and entering the user data
with open('userinformation.txt', 'w') as file:
    file.writelines(f"email: {email} \n")
    file.writelines(f"password: {password} \n")
    file.writelines(f"type: {type} \n")
    file.writelines(f"acres: {farm_size} \n")
    file.writelines(f"Date created: {date} \n")


print(f"Welcome {name}, account created successfully")

# getting the month only from the above date
months = date.month

# using calendar library to output the NAME of the month
month_name = calendar.month_name[months]
print(" ")

season = months_seasons[month_name]
time.sleep(1)
print(f"current season: {season}")
time.sleep(1)
print(f"Best {season} crops to grow are: ")

if season == 'Summer':
    print(summer)
elif season == 'Spring':
    print(spring)
elif season == 'Autumn':
    print(autumn)
else:
    print(winter)

# print(current_season)
def summer_crops():
    print(summer)
    # asking the user to select a crop to learn more about
    time.sleep(1)
    chosen_crop = int(input('Which crop do you want to learn more about from the above: '))
    print('')







