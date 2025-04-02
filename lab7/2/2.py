from tkinter import *
import pygame, os


root=Tk()
root.title("Music player ot Aru :P")
root.iconbitmap('c:/Users/ASUS/PP_2/lab7/2/icon.ico')
root.geometry("600x400")
root.configure(bg="#ACACAC")

play_img= PhotoImage(file='C:/Users/ASUS/PP_2/lab7/2/play.png')
pause_img= PhotoImage(file='C:/Users/ASUS/PP_2/lab7/2/pause.png')
next_img= PhotoImage(file='C:/Users/ASUS/PP_2/lab7/2/next.png')
prev_img= PhotoImage(file='C:/Users/ASUS/PP_2/lab7/2/prev.png')

pygame.mixer.init()

BASE_PATH = "C:/Users/ASUS/PP_2/lab7/2/"

playlist= ["young.mp3", "love_getting_high.mp3", "borderline.mp3"]
current=0
is_paused= False

search_entry= Entry(root, width=30)
search_entry.place(x=210, y=20)


def search():
    global current
    song_name=search_entry.get().lower()
    for i, song in enumerate(playlist):
        if song_name in song.lower():
            current=i
            play()
            return
    print("Song is not found")

def play():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused= False
    else:
        pygame.mixer.music.load(os.path.join(BASE_PATH, playlist[current]))
        pygame.mixer.music.play()
        is_paused= False
        play_button.config(image=pause_img)
    play_button.config(image=pause_img)

def pause():
    global is_paused
    pygame.mixer.music.pause()
    is_paused= True
    play_button.config(image=play_img)

def toggle_play_pause(event=None):
    if is_paused:
        play()
    else:
        pause()

def next_song(event=None):
    global current
    pygame.mixer.music.stop()
    current= (current+1)%len(playlist)
    play()

def prev_song(event=None):
    global current
    pygame.mixer.music.stop()
    current= (current-1)%len(playlist)
    play()

def set_volume(val):
    volume= float(val)/100
    pygame.mixer.music.set_volume(volume)


search_button= Button(root, text="Find", command=search, bg=root["bg"])
search_button.place(x=400, y=18)

play_button= Button(root, image=play_img, command=toggle_play_pause, bd=0, highlightthickness=0, bg=root["bg"])
play_button.place(x=290, y=300)
    

next_button= Button(root, image=next_img, command=next_song, bd=0, highlightthickness=0, bg=root["bg"])
next_button.place(x=330,y=300)

prev_button= Button(root, image=prev_img, command=prev_song, bd=0, highlightthickness=0, bg=root["bg"])
prev_button.place(x=250, y=300)

volume_slider= Scale(root, from_=0, to=100, orient= HORIZONTAL, length=200, command= set_volume, bg="#ACACAC")
volume_slider.set(50)
volume_slider.place(x=200, y=250)

root.bind("<space>", toggle_play_pause)
root.bind("<Right>", next_song)
root.bind("<Left>", prev_song)

root.mainloop()