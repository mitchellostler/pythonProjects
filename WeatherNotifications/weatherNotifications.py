#! python
#WeatherNotification.py a script that uses your gps coordinates to give you weather notifications
#Script uses BeautifulSoup to parse for location data, then aqcuires weather data based on these coordinates
#Weather data is via OpenWeatherMap API

import bs4, sys, webbrowser, requests, os

listOfStrings = []

infoDict = {

'Latitude'   : '',
'Longitude'  : '',
'Country'    : '',
'Region'     : '',
'City'       : '',

}

print('Aquiring Data')
#Parse and save location data
def getLoc(infoDict, listOfStrings):
    
    #get html page from mylocation.org
    res = requests.get('https://mylocation.org/')
    res.raise_for_status()
    #TODO: add try except statement here?

    locationSoup = bs4.BeautifulSoup(res.text, features="html.parser")
    listOfatt = locationSoup.select('td')

    for i in range(2, 12):
        listOfStrings.append(listOfatt[i].getText())

    for i in range(len(listOfStrings)):
        if(listOfStrings[i] in infoDict.keys()):
            infoDict[listOfStrings[i]] = listOfStrings[i + 1]
        
#print('\nYOUR LOCATION IS:\n')

def printDictAndList(infoDict, listOfStrings):
    for i in range(10):
        if not (i & 1):
            print(listOfStrings[i] + ': ' + infoDict[listOfStrings[i]] + '\n')


#TODO: Use location data to parse and save weather data
def getWeatherForLoc():
    print('LOCATING WEATHER DATA: \n')

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?&lat='
        + infoDict['Latitude'] + '&lon=' + infoDict['Longitude'] +
        '&APPID=e50662920d54ae644a40721ee2042bf1'
        )
    
    json_response = r.json()
    weatherDict = json_response['main']
    
    return weatherDict



#TODO: return data
def saveWData(weatherDict):
    wString = ''
    for i in weatherDict:
        holder = '\n' + i + ': ' + '%.1f' % (weatherDict[i] - 273)
        wString += holder
    return wString

#TODO: Create notifications

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              sound name frog""".format(text, title))
              
#Send Message to number of choice
def sendMessage(phoneNum, message):
    os.system("""
        osascript -e '
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{}" of targetService
        send "{}" to targetBuddy
    end tell
    '""".format(phoneNum, message))


#Execute program
getLoc(infoDict, listOfStrings)
printDictAndList(infoDict, listOfStrings)
notify("Your Morning Weather Report", saveWData(getWeatherForLoc()))
sendMessage(6047216461, saveWData(getWeatherForLoc()))



#TODO: Setup timer schedule
