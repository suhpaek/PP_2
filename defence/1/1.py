import pygame
import tkinter as tk 
import sys

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("borderline.mp3")
pygame.mixer.music.play(-1)

texts= ["Hello world!", "Поставьте пожалуйста высокий балл:P)", "I love PP2!!!!", "Im gonna cry if i will get 0 points T-T", "Snova hello world"]

current=0

def change():
    global current
    current= (current+1)%len(texts)
    label.config(text=texts[current])

root=tk.Tk()
root.title("Defence")
root.geometry("600x400")
root.configure(bg="WHITE")

label= tk.Label(root, text= texts[current], font=("arial",20), bg="WHITE")
label.pack(pady=40)

button = tk.Button(root, text="Change", font=("Arial", 16), command=change)
button.pack()                   

root.mainloop()