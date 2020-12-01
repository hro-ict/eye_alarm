import datetime

from playsound import playsound
import time
from easygui import *
import  threading



def music():
    playsound("music.mp3")
def message():
    msgbox("De tijd om te rusten\n\nHet is nu {}:{}:{}\n\nDe volgende pauze: {}:{}:{}".format(a.hour,
                                                                                       a.minute,
                                                                                       a.second,
                                                                                       volgende.hour,
                                                                                       volgende.minute,
                                                                                       volgende.second))

#functie voor aftellen

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

while True:
    countdown(1200) #20 minuten
    a = datetime.datetime.now()
    verschil= datetime.timedelta(minutes=21)
    volgende= a+verschil
    t1= threading.Thread(target= music)
    t2= threading.Thread(target= message)
    t1.start()
    t2.start()
    






