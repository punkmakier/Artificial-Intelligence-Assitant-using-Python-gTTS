import speech_recognition as sr
import os
from termcolor import colored
from gtts import gTTS
import datetime
import time
import warnings
import calendar
import webbrowser
import playsound
import random
import wikipedia
import pyttsx3
import urllib
import urllib3
import smtplib
import wolframalpha
import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import pyautogui
import wikipedia
import random
from time import strftime
speech = sr.Recognizer()
from textblob import TextBlob
import pyowm
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import nltk
from newspaper import Article
import pyglet


wakeUp = "C:\\Users\\User\\Documents\\alexa_sounds\\wake_up_call.mp3"
google_for_question = "C:\\Users\\User\\Documents\\alexa_sounds\\google_for_question.mp3"
google_for_answer = "C:\\Users\\User\\Documents\\alexa_sounds\\google_for_answer.mp3"

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        mark_speak("Good Morning")
    elif hour >= 12 and hour <18:
        mark_speak("Good Afternoon")
    else:
        mark_speak("Good Evening")


def mark_speak(audio_string):
    tts = gTTS(text=audio_string, lang='fil-PH', lang_check=True,slow=False)
    r = random.randint(0, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print(color.BOLD+colored(color.RED+"Listening...")+color.END)
        audio = r.listen(source=source,timeout=20, phrase_time_limit=10)


    try:
        print(color.BOLD+colored(color.BLUE+"Recognizing...\n")+color.END)
        query = r.recognize_google(audio, language="en-US")
        print(color.BOLD + colored(color.GREEN + f"Makier : "+color.DARKCYAN+query) + color.END)
    except Exception as e:
        return 'None'
    return query



def getPersonOnWiki(text):
    wordList = text.split()
    for i in range(0, len(wordList)):
        try:
            if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' or wordList[i].lower() == 'what' or wordList[i].lower() == 'when' or wordList[i].lower() == 'where' or wordList[i].lower() == 'how' and wordList[i+1].lower() == 'is':
                return wordList[i+2] + ' '+wordList[i+3]
        except:
            pass

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('punkmakier19@gmail.com','0932061675')
    server.sendmail('punkmakier@gmail.com', to, content)
    server.close()


words = []



mark_response_NoValueError = ["Sorry! I can't get the answer.","Pardon?","Sorry! Please try again.","Pardon me! try again please","Sorry,I couldn't hear you."]
mark_response_ErrorLocation = ["I didn't found the location","Sorry I can't search that location","Sorry, I didn't find the location"]
mark_response_CorrectLocation = ["This is the location that you looking for!","Here is the location that you wanted."]
mark_OK_response = ["OK!","OK! I'm on it","Alright","Please wait a moment","At, your service","OK! 1 second.","OK! Give me a second","SURE!","SURE! PLEASE WAIT."]
mark_response_quesitoning = ["Tell me what is it!","Sure! What is it.","Ok! Tell me","Why? Are you curious of something? Ok then tell me. I will try to answer it.","Ok let me try to answer it!"]
if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        if query.__contains__('susana') or query.__contains__('susannah'):
            query = query.replace("susana ","")
            playsound.playsound(google_for_question)
            try:
                #SEARCH GOOGLE
                if 'search this in google' in query or 'search this on google' in query or 'search this google' in query:
                    choice = random.choice(mark_OK_response)
                    print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+choice) + color.END)
                    mark_speak(choice)
                    playsound.playsound(google_for_answer)
                    query = query.replace("search this in google", "")
                    query = query.replace("search on google", "")
                    query = query.replace("search in google", "")
                    query = query.replace("search this on google", "")
                    query = query.replace("search this", "")
                    query = query.replace("google", "")
                    url = 'https://google.com/search?q=' + query
                    webbrowser.get().open(url)
                    pass
                #SEARCH ON YOUTUBE
                if 'search on youtube' in query or 'search in youtube' in query or 'search this in youtube' in query or 'search this on youtube' in query or 'play this on youtube' in query or 'play this in youtube' in query:
                    choice = random.choice(mark_OK_response)
                    print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+choice) + color.END)
                    mark_speak(choice)
                    playsound.playsound(google_for_answer)
                    reg_ex = re.search('youtube (.+)', query)
                    if reg_ex:
                        domain = query.split("youtube", 1)[1]
                        query_string = urllib.parse.urlencode({"search_query": domain})
                        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                        # print("http://www.youtube.com/watch?v=" + search_results[0])
                        webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
                        pass
                #FINDING LOCATION
                elif 'find this location' in query or 'find the location' in query or 'find location' in query:
                    query = query.replace("find","")
                    query = query.replace("this","")
                    query = query.replace("location","")
                    query = query.replace("the","")
                    url = 'https://google.nl/maps/place/' + query + '/&amp;'
                    webbrowser.get().open_new(url)
                    choice = random.choice(mark_response_CorrectLocation)
                    print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+choice) + color.END)
                    mark_speak(choice)
                    playsound.playsound(google_for_answer)
                #QUESTION
                elif 'question' in query or '?' in query or 'questions' in query:
                    choice = random.choice(mark_response_quesitoning)
                    print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+choice) + color.END)
                    mark_speak(choice)
                    playsound.playsound(google_for_answer)
                    query = takeCommand()
                    playsound.playsound(google_for_question)
                    query = query.replace("?","")
                    query = query.replace("i have a questions","")
                    query = query.replace("i have questions","")
                    query = query.replace("i have a question","")
                    query = query.replace("i have question","")
                    try:
                        app_id = "49U6WL-2RVV8P42VH"
                        client = wolframalpha.Client(app_id)
                        res = client.query(query)
                        answer = next(res.results).text
                        # for mathematical
                        if query.__contains__('+') or query.__contains__('-') or query.__contains__('+') or query.__contains__('/'):
                            print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+"Answer: "+answer) + color.END)
                            mark_speak(f'{query},....:,......:,,....:,......:, The Answer is,....:,......:,,....:,......:,........:{answer}')
                            playsound.playsound(google_for_answer)
                        else:
                            query = query.replace("what is", "")
                            query = query.replace("tell me", "")
                            query = query.replace("who is", "")
                            query = query.replace("where is", "")
                            query = query.replace("how much is", "")
                            print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+"Answer: "+answer) + color.END)
                            mark_speak(f'{query}:..:,......:,......:,,....:,......:,........:{answer}')
                            playsound.playsound(google_for_answer)
                    except:
                        try:
                            person = getPersonOnWiki(query)
                            wiki = wikipedia.summary(person, sentences=3)
                            print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+wiki) + color.END)
                            mark_speak(f'{query},....:,......:' + wiki)
                            playsound.playsound(google_for_answer)
                        except Exception or UserWarning:
                            choice = random.choice(mark_response_NoValueError)
                            print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+choice) + color.END)
                            mark_speak(choice)
                            playsound.playsound(google_for_answer)

                #CHECK THE WEATHER
                elif 'weather' in query:
                    try:
                        query = query.replace("what is the", "")
                        query = query.replace("tell me the", "")
                        query = query.replace("weather", "")
                        query = query.replace("in", "")
                        owm = pyowm.OWM('3b3788bd7c1c7260ff4f7ba41a4aa2ed')
                        degreeSign = u'\N{DEGREE SIGN}'
                        location = owm.weather_at_place(query)
                        weather = location.get_weather()
                        tempC = weather.get_temperature('celsius')['temp']
                        tempF = weather.get_temperature('fahrenheit')['temp']
                        wind = weather.get_wind('meters_sec')['speed']
                        humidty = weather.get_humidity()
                        status = weather.get_detailed_status()
                        print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN +f'The temperature in : {query}') + color.END)
                        print(color.BOLD+colored(color.CYAN+f"{tempC}{degreeSign} Celsius | {tempF}{degreeSign} Fahrenheit\nRelative Humidity | {humidty}\nWind Speed | {wind}\nCondition | {status}")+color.END)
                        mark_speak(f"The temperature in : {query},....:......:{tempC}{degreeSign} Celsius | {tempF}{degreeSign} Fahrenheit,....:......:\nRelative Humidity | {humidty}\n,....:......:Wind Speed | {wind}\n,....:......:Condition | {status}")
                        playsound.playsound(google_for_answer)
                    except:
                        choice = random.choice(mark_response_ErrorLocation)
                        print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+choice) + color.END)
                        mark_speak(choice)
                        playsound.playsound(google_for_answer)

                #OPENING OF YOUR DESIRE WEBSITE
                elif 'open' in query or 'launch' in query:
                    choice = random.choice(mark_OK_response)
                    print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+choice) + color.END)
                    mark_speak(choice)
                    playsound.playsound(google_for_answer)
                    if 'website' in query or 'browser' in query or 'chrome' in query:
                        query = query.replace("chrome", "")
                        query = query.replace("google chrome", "")
                        query = query.replace("open", "")
                        query = query.replace("website","")
                        query = query.replace("launch","")
                        query = query.replace("browser","")
                        query = query.replace("in","")
                        query = query.replace("and","")
                        query = query.replace(" ","")
                        query = "www." + query +".com"
                        webbrowser.open(query)
                    else:
                        #OPENING FOLDER HERE
                        os.system('explorer C:\\"{}"'.format(query.replace('open ', '').replace('launch ', '')))
                #PLAY MUSIC
                elif 'play music' in query or 'play a music' in query or 'play another music' in query:
                    choice = random.choice(mark_OK_response)
                    print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+choice) + color.END)
                    mark_speak(choice)
                    playsound.playsound(google_for_answer)
                    music_dir = "C:\\Users\\User\\Desktop\\ok\\Music"
                    songs = os.listdir(music_dir)
                    random_gen = random.randint(0, len(songs) - 1)
                    os.startfile(os.path.join(music_dir, songs[random_gen]))
                elif 'rock music' in query or 'another rock music' in query:
                    choice = random.choice(mark_OK_response)
                    print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+choice) + color.END)
                    mark_speak(choice)
                    playsound.playsound(google_for_answer)
                    music_dir = "C:\\Users\\User\\Desktop\\ok\\Music\\RockMusic"
                    songs = os.listdir(music_dir)
                    random_gen = random.randint(0, len(songs) - 1)
                    os.startfile(os.path.join(music_dir, songs[random_gen]))

                #TELLING JOKES
                elif 'tell me a joke' in query or 'another joke' in query:
                    choice = random.choice(mark_OK_response)
                    print(color.BOLD + colored(color.PURPLE +"Susana: "+ color.CYAN+choice) + color.END)
                    mark_speak(choice)
                    playsound.playsound(google_for_answer)
                    res = requests.get('https://icanhazdadjoke.com/',headers={"Accept": "application/json"})
                    if res.status_code == requests.codes.ok:
                        print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + str(res.json()['joke'])) + color.END)
                        mark_speak(str(res.json()['joke']))
                        playsound.playsound(google_for_answer)
                    else:
                        print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + 'oops!I ran out of jokes') + color.END)
                        mark_speak('oops!I ran out of jokes')
                        playsound.playsound(google_for_answer)
                #CHECK THE CURRENT TIME
                elif 'the time' in query or 'time is it' in query:
                    now = datetime.datetime.now()
                    meridem =''
                    if now.hour >=12:
                        meridem = 'P.M'
                        hour =now.hour - 12
                    else:
                        meridem = 'A.M'
                        hour = now.hour
                    if now.minute <10:
                        minute = '0' + str(now.minute)
                    else:
                        minute = str(now.minute)
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + "It is " + str(hour)+ ':'+minute+' '+meridem) + color.END)
                    mark_speak("It is " + str(hour)+ ':'+minute+' '+meridem)
                    playsound.playsound(google_for_answer)
                #CHECK THE CURRENT DAY
                elif 'the date' in query or 'the day' in query:
                    now = datetime.datetime.now()
                    my_date = datetime.datetime.today()
                    weekday = calendar.day_name[my_date.weekday()]
                    monthNum = now.month
                    dayNum = now.day
                    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September', 'October', 'November', 'December']
                    ordinalNumber = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '9th', '10th', '11th', '12th','13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd','23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumber[dayNum - 2] + '. ') + color.END)
                    mark_speak('Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumber[dayNum - 2] + '. ')
                    playsound.playsound(google_for_answer)
                ##ADMIN MODE OR EDITORS MODE
                elif 'stop the music' in query or 'stop music' in query or 'stop rock music' in query or 'close rock music' in query or 'close the music' in query or 'close music' in query:
                    os.system("TASKKILL /F /IM wmplayer.exe")
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + 'Done!') + color.END)
                    print("Done!")
                    mark_speak("Done!")
                    playsound.playsound(google_for_answer)
                elif 'close windows' in query or 'close browser' in query or 'close the browser' in query or 'close google chrome' in query or 'close all the browser' in query or 'close the windows' in query or 'close the window' in query or 'close all the window' in query:
                    os.system("TASKKILL /F /IM chrome.exe")
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + 'Done!') + color.END)
                    mark_speak("Done!")
                    playsound.playsound(google_for_answer)
                elif 'scroll down' in query:
                    pyautogui.FAILSAFE = True
                    pyautogui.scroll(-2000)
                elif 'scroll up' in query:
                    pyautogui.FAILSAFE = True
                    pyautogui.scroll(2000)
                elif 'screenshot' in query:
                    sc = pyautogui.screenshot()
                    sc.save("C:/Users/User/Pictures/Saved Pictures/Screenshot.png")
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + 'done:..:,......:,......:,,....:,......:,........: You want me to open it for you?') + color.END)
                    mark_speak('done:..:,......:,......:,,....:,......:,........: You want me to open it for you?')
                    playsound.playsound(google_for_question)
                    query = takeCommand()
                    playsound.playsound(google_for_answer)
                    if 'yes' in query:
                        choice = random.choice(mark_OK_response)
                        print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + choice) + color.END)
                        mark_speak(choice)
                        playsound.playsound(google_for_answer)
                        os.startfile(os.path.join('C:\\Users\\User\\Pictures\\Saved Pictures\\Screenshot.png'))
                    else:
                        mark_just = ["Ok nevermind","Your welcome","My pleasure","Forget it"]
                        choice = random.choice(mark_just)
                        print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + choice) + color.END)
                        mark_speak(choice)
                        playsound.playsound(google_for_answer)

                #TRANSLATION
                if 'translate' in query:
                    choice = random.choice(mark_OK_response)
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + choice) + color.END)
                    mark_speak(choice)
                    playsound.playsound(google_for_answer)
                    query = query.replace("the word", "")
                    query = query.replace("translate", "")
                    try:
                        if 'filipino' in query:
                            query = query.replace("to filipino", "")
                            query = query.replace("in filipino", "")
                            word = TextBlob(query)
                            z = word.translate(from_lang='en', to='fil')
                            h = f"The word {query} in filipino is: '{str(z)}'"
                            print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + h) + color.END)
                            mark_speak(h)
                            playsound.playsound(google_for_answer)
                        elif 'cebuano' in query:
                            query = query.replace("to cebuano", "")
                            query = query.replace("in cebuano", "")
                            word = TextBlob(query)
                            z = word.translate(from_lang='en', to='ceb')
                            h = f"The word {query} in cebuano is: '{str(z)}'"
                            print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + h) + color.END)
                            mark_speak(h)
                            playsound.playsound(google_for_answer)
                        elif 'korean' in query:
                            query = query.replace("to korean", "")
                            query = query.replace("in korean", "")
                            word = TextBlob(query)
                            z = word.translate(from_lang='en', to='ko')
                            h = f"The word {query} in korean is: '{str(z)}'"
                            print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + h) + color.END)
                            mark_speak(h)
                            playsound.playsound(google_for_answer)
                        elif 'chinese' in query:
                            query = query.replace("to chinese", "")
                            query = query.replace("in chinese", "")
                            word = TextBlob(query)
                            z = word.translate(from_lang='en', to='zh')
                            h = f"The word {query} in chinese is: '{str(z)}'"
                            print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + h) + color.END)
                            mark_speak(h)
                            playsound.playsound(google_for_answer)
                    except:
                        print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + "Sorry I don't know that word.") + color.END)
                        mark_speak("Sorry I don't know that word.")
                        playsound.playsound(google_for_answer)

                #SPELLING
                elif 'spell' in query:
                    choice = random.choice(mark_OK_response)
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + choice) + color.END)
                    mark_speak(choice)
                    playsound.playsound(google_for_answer)
                    query = query.replace("spell","")
                    query = query.replace("the word","")
                    query = query.replace(" ","")
                    for x in query:
                        words.append(x)
                    word = str(words)
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + f"The spelling of the word {query}: "+word) + color.END)
                    mark_speak(f"The spelling of the word: {query}:..:,......:,......:,,....:,......:,........:"+word+":..:,......:,......:,,....:,......:,........"+query)
                    words.clear()
                    playsound.playsound(google_for_answer)

                #SENDING EMAIL
                elif 'send email' in query:
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + 'Who is the recipient?') + color.END)
                    mark_speak('Who is the recipient?')
                    playsound.playsound(google_for_answer)
                    query = takeCommand()
                    playsound.playsound(google_for_question)
                    if 'erad' in query or 'e rod' in query:
                        print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + 'What should I say?') + color.END)
                        mark_speak('What should I say to him?')
                        playsound.playsound(google_for_answer)
                        content = takeCommand()
                        playsound.playsound(google_for_question)

                        mail = smtplib.SMTP('smtp.gmail.com', 587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login('punkmakier19@gmail.com', '0932061675')
                        mail.sendmail('punkmakier19@gmail.com', 'punkmakier@gmail.com', content)
                        mail.close()
                        print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + 'Email has been sent successfully.:..:,......:,......:,,....:,......:,........: You want me to open your gmail account?') + color.END)
                        mark_speak('Email has been sent successfully.:..:,......:,......:,,....:,......:,........: You want me to open your gmail account?')
                        playsound.playsound(google_for_answer)
                        query = takeCommand()
                        playsound.playsound(google_for_question)
                        if 'yes' in query:
                            webbrowser.get().open('https://mail.google.com/mail/u/0/#sent')
                        else:
                            print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + 'Ok') + color.END)
                            mark_speak('Ok')
                            playsound.playsound(google_for_answer)
                    else:
                        print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + "I don't know what you mean!") + color.END)
                        mark_speak("I don't know what you mean!")
                        playsound.playsound(google_for_answer)


                #ABOUT SUSANA

                elif 'who create you' in query:
                    speak = '''I was created by: Mark Allan Carba. He is a Bachelor of Science Information Technology, currently studying at STI COLLEGE CEBU.
        He build me under 1 month and counting. I am not yet fully programmed as what you have expected. '''
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + speak)+color.END)
                    mark_speak("I was created by: Mark Allan Carba. He is a Bachelor of Science Information Technology, currently studying at STI COLLEGE CEBU. He build me under 1 month and counting. I am not fully programmed as what you have expected.")
                    playsound.playsound(google_for_answer)
                elif 'goodbye to this video' in query or 'goodbye to the video' in query or 'good bye to the video' in query or 'good bye to this video' in query:
                    speak = '''Good Bye Everyone. Thank you for your time for watching this video and I hope you enjoy. .
        Do you think I am deserve to get your THUMBS UP? Please hit the like button and share this video so that I will be known and become famous of this world. 
        Thank you so much and Good bye!'''
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + speak) + color.END)
                    mark_speak("Good Bye Everyone. Thank you for your time for watching this video and I hope you enjoy. Do you think I am deserve to get your THUMBS UP? Please hit the like button and share this video so that I will be known and become famous of this world. Thank you so much and,....:,......:,,....:,......:,........:Good bye!")
                    playsound.playsound(google_for_answer)
                elif 'who are you' in query or 'introduce yourself' in query:
                    speak = '''Hello, I am Susana. Your Artificial Intelligence Assistant. The name Susana was came from the grandmother of Mark Allan Carba.
        I am here to make your life easier. You can command me to perform various tasks such as 
        calculating, searching, playing music or opening applications and more'''
                    print(color.BOLD+colored(color.PURPLE+"Susana: "+color.CYAN+speak)+color.END)
                    mark_speak(speak)
                    playsound.playsound(google_for_answer)

                elif 'thank you' in query:
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + "You're welcome!") + color.END)
                    mark_speak("You're welcome!")


                elif 'birthday' in query:
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + "Ok ! Wait a minute. Searching your database now..." ) + color.END)
                    mark_speak("Ok ! Wait a minute. Searching your database now...")
                    time.sleep(1)
                    print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + "Here's the message: Happy Birthday 'Anabel Laranjo Carba', “ Hope your special day brings you all that your heart desires! Here’s wishing you a day full of pleasant surprises!\nHappy birthday once again 'Anabel Laranjo Carba'!\n\nA Message from your beloved son: Mark Allan Carba”") + color.END)
                    mark_speak("Here is the message: ! ! . . . Happy Birthday ! Annabel Laranjo Carba, ! ..... ! , “ Hope your special day brings you all that your heart desires! Here’s wishing you a day full of pleasant surprises!.  Happy birthday once again 'Annabel Laranjo Carba'! , .. A message from your beloved son : , ! Mark Allan Carba.")
            except ValueError as e:
                choice = random.choice(mark_response_NoValueError)
                print(color.BOLD + colored(color.PURPLE + "Susana: " + color.CYAN + choice) + color.END)
                mark_speak(choice)
                playsound.playsound(google_for_answer)
