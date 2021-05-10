import tkinter as tk
from tkinter import Menu
from tkinter import ttk , filedialog
import os
import pygame
from pygame import mixer



root = tk.Tk()
root.title("Music App")
root.geometry("800x600")
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu=Menu(menu_bar,tearoff=0)
edit_menu=Menu(menu_bar,tearoff=0)
track_menu=Menu(menu_bar,tearoff=0)
info_menu=Menu(menu_bar,tearoff=0)

search_bar = tk.Entry()
search_bar.grid(row=0,column=0)\

def open_path():
    pygame.init()
    fd = filedialog
    ask_for_file = fd.askopenfilename()

    global load_music
    load_music = ask_for_file

    pass

def play_music():
    pygame.init()
    global playing_music
    playing_music = True
    #load_music = "/home/raku/Music/Justice Music/FunkJazzSong.wav"

    if playing_music == True:
        mixer.music.load(load_music)
        mixer.music.play()

def stop_music():
    playing_music = False
    mixer.music.stop()
    pass


def menu_options():

    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    menu_bar.add_cascade(label="Track", menu=track_menu)
    menu_bar.add_cascade(label="Info", menu=info_menu)

def file_commands():

    file_menu.add_command(label="New", command=None)
    file_menu.add_command(label="Open" , command=open_path)
    file_menu.add_command(label="Save" , command=None)
    file_menu.add_command(label="Play" , command=play_music)
    file_menu.add_command(label="Stop" , command=stop_music)


def edit_commands():

    edit_menu.add_command(label="Undo", command=None)

def track__menu_commands():

    track_menu.add_command(label="Add" , command=None)
    track_menu.add_command(label="Remove", command=None)

def info_commands():

    info_menu.add_command(label="Add artist", command=None)
    info_menu.add_command(label="Add album", command=None)
    info_menu.add_command(label="Add artwork", command=None)
    info_menu.add_command(label="Add date", command=None)
    info_menu.add_command(label="Add genre", command=None)
    info_menu.add_command(label="Name track", command=None)


def run_command_bar():
    menu_options()
    file_commands()
    edit_commands()
    track__menu_commands()
    info_commands()


if __name__ == "__main__":
    run_command_bar()
    root.mainloop()
