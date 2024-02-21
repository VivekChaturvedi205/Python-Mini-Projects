import pygame
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_audio_file():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\Users\vk126\OneDrive\Desktop\Py\Alarm-Fast-High-Pitch-A3-Ring-Tone-www.fesliyanstudios.com.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def get_terminal_size():
    try:
        columns, lines = os.get_terminal_size()
        return columns, lines
    except OSError:
        return 80, 24  

def print_centered(message, font_size=3):
    columns, lines = get_terminal_size()
    centered_message = f"{message:^{columns * font_size}}"
    print(centered_message)

##CLEAR= "\033[2J"
##CLEAR_AND_RETURN="\033[H"
def alram(seconds):
    time_elapsed=0
    clear_screen()
    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed+=1
        
        time_left=seconds-time_elapsed
        minute_left= time_left//60
        seconds_left=time_left%60
        
        clear_screen()
        countdown_message = f'Alarm will sound in: {minute_left:02d}:{seconds_left:02d}'
        print_centered(countdown_message,font_size=5)
    play_audio_file()

minutes=int(input("How many minutes to wait:"))
seconds=int(input("How many seconds to wait:"))
total_seconds=minutes*60+seconds
alram(total_seconds)

