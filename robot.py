from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3, datetime, sys, wikipedia, wolframalpha, os, smtplib, random, webbrowser, pygame, subprocess
from requests.packages.urllib3.packages.six.moves import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


client = wolframalpha.Client('Your_App_ID')

folder = 'C:\\Users\\skt\\Music\\YouTube\\'

engine = pyttsx3.init()
voices = engine.getProperty('voices')

b_music = ['Micro']
pygame.mixer.init()
pygame.mixer.music.load(folder + random.choice(b_music) + '.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)


def speak(audio):
    print('Karen:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Try again')
        pass

    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


class Widget:
    def __init__(self):
        root = Tk()
        root.title('karen(YT-1)')
        root.config(background='Red')
        root.geometry('350x600')
        root.resizable(0, 0)
        root.iconbitmap(r'C:\Users\skt\Documents\KarenMark\Untitled-1.ico')
        img = ImageTk.PhotoImage(Image.open(r"C:\Users\skt\Documents\KarenMark\karen image 2.png"))
        panel = Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="no")

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click \'Start Listening\' to Give commands')

        userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
        userFrame.pack(fill="both", expand="yes")

        left2 = Message(userFrame, textvariable=self.userText, bg='dodgerBlue', fg='white')
        left2.config(font=("Comic Sans MS", 10, 'bold'))
        left2.pack(fill='both', expand='yes')

        compFrame = LabelFrame(root, text="VJ", font=('Black ops one', 10, 'bold'))
        compFrame.pack(fill="both", expand="yes")

        left1 = Message(compFrame, textvariable=self.compText, bg='Red', fg='white')
        left1.config(font=("Comic Sans MS", 10, 'bold'))
        left1.pack(fill='both', expand='yes')

        btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepSkyBlue', fg='white',
                     command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white',
                      command=root.destroy).pack(fill='x', expand='no')

        speak('Hello, I am karen! What should I do for You?')
        self.compText.set('Hello, I am karen! What should I do for You?')

        root.bind("<Return>", self.clicked)  # handle the enter key event of your keyboard
        root.mainloop()

    def clicked(self):
        print('Working')
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        if 'open cleaner' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\CCleaner\CCleaner.exe')

        elif 'open google chrome' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

        elif 'open powerpoint' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\Microsoft Office\Office14\POWERPNT.EXE')


        elif 'youtube' in query:

            speak('Ok!')
            reg_ex = re.search('youtube (.+)', query)


            if reg_ex:
                domain = query.split("youtube", 1)[1]

                query_string = urllib.parse.urlencode({"search_query": domain})

                html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)

                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

                # print("http://www.youtube.com/watch?v=" + search_results[0])

                webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))

                pass

        if 'open google and search' in query:
            reg_ex = re.search('open google and search (.*)', query)
            search_for = query.split("search", 1)[1]
            print(search_for)
            url = 'https://www.google.com/'
            if reg_ex:
                subgoogle = reg_ex.group(1)
                url = url + 'r/' + subgoogle
            speak('Okay!')
            driver = webdriver.firefox(executable_path= '\Desktop\geckodriver')
            driver.get('http://www.google.com')
            search = driver.find_element_by_name('q')
            search.send_keys(str(search_for))
            search.send_keys(Keys.RETURN)  # hit return after you enter search text

        elif 'open gmail' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'open Facebook' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.facebook.com')

        elif 'who is your owner' in query:
            self.compText.set('okay')
            speak('vino is my owner I am his personal assistant')


        elif 'shutdown' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('shutdown -s')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            self.compText.set(random.choice(stMsgs))
            speak(random.choice(stMsgs))

        elif 'email' in query:
            self.compText.set('Who is the recipient? ')
            speak('Who is the recipient? ')
            recipient = myCommand()
            self.userText.set(recipient)
            recipient = recipient.lower()

            if 'me' in recipient:
                try:
                    self.compText.set('What should I say? ')
                    speak('What should I say? ')
                    content = myCommand()
                    self.userText.set(content)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Username')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    self.compText.set('Email sent!')
                    speak('Email sent!')

                except:
                    self.compText.set('Email sent!')
                    speak('Sorry ' + 'Sir' + '!, I am unable to send your message at this moment!')



        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            self.compText.set('Okay')
            speak('okay')
            self.compText.set('Bye Sir, have a good day.')
            speak('Bye Sir, have a good day.')

        elif 'hello' in query:
            self.compText.set('Hello Sir')
            speak('Hello Sir')


        elif 'bye' in query:
            self.compText.set('Bye ' + 'Sir' + ', have a good day.')
            speak('Bye ' + 'Sir' + ', have a good day.')

        elif 'My song' in query:
            music_folder = 'C:\\Users\\skt\\Music\\YouTube\\'
            music = ['Edison', 'bensound-actionable', 'bensound-buddy', 'Micro', 'Lucid_Dreamer']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')

        else:
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    self.compText.set(results)
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    self.compText.set(results)
                    speak(results)

            except:
                speak('I don\'t know Sir! Google is smarter than me!')
                self.compText.set('I don\'t know Sir! Google is smarter than me!')
                webbrowser.open('www.google.com')



if __name__ == '__main__':
    greetMe()
    widget = Widget()