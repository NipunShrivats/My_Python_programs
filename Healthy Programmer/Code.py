# HEALTHY PROGRAMMER

## We have to make a program to remind the user :-
# to drink water every 30 minutes,
# to relax eyes every 40 minutes and
# to do some streaching every 60 minutes.

## INSTRUCTIONS
# timestamp - regular intervals (using time module).
# logfile - time data will be logged in. (using datetime module).
# Play audio every time as a reminder.
##################################################################

from pygame import mixer
from datetime import datetime
from time import time

print('\nHEALTHY PROGRAMMER IS RUNNING...\n')

def music(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        '''while loop for initiating the stopper button'''
        stop_music = input()
        if stop_music == stopper:
            mixer.music.stop() #will stop the music
            break # if music is stopped then the below timer code will run again and music will played again in equal time intervals#

def log_now(text):
    '''will create a log file automatically with the action that is implemented and the time at which it has performed'''
    with open('log_file.txt', 'a') as time_file:
        time_file.write(f"{text} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_st = time() # stretching
    water_sec = 5  #(30 * 60) for real implementation
    eye_sec = 14   #(40 * 60) for real implementation
    st_sec = 27    #(60 * 60) for real implementation

    while True:
        ## for water
        if time() - init_water > water_sec:
            print("***** DRINK SOME WATER BRO! *****\nTo stop the alarm type 'x' and press enter.")
            music('D:/MY WORK/2. Python_absolute_beginners/audio_files/retro_alarm.wav', 'x')
            init_water = time()
            log_now('Drank water at')

        ## for eyes
        if time() - init_eyes > eye_sec:
            print("***** RELAX YOUR EYES BRO! *****\nTo stop the alarm type 'x' and press enter.")
            music('D:/MY WORK/2. Python_absolute_beginners/audio_files/retro_alarm.wav', 'x')
            init_eyes = time()
            log_now('Relaxed eyes at')

        ## for stretching
        if time() - init_st > st_sec:
            print("***** DO SOME STRETCHING BRO! *****\nTo stop the alarm type 'x' and press enter.")
            music('D:/MY WORK/2. Python_absolute_beginners/audio_files/retro_alarm.wav', 'x')
            init_st = time()
            log_now('Stretched body at')

########################################################################################################################