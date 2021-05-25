import tkinter as tk
from tkinter import Menu
from tkinter import ttk , filedialog , Label , Button , Scale , Frame
import pygame
import os
from pygame import mixer
from PIL import Image , ImageTk


root = tk.Tk()
root.title("Music App")
root.geometry("420x330")
root.configure(bg="black")
root.option_add("*background" , "black")
root.option_add("*foreground" , "red")

pygame.init()

track_box = tk.Listbox(selectbackground="red")
track_box.grid()

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

error_label = Label(root,text = " ")
error_label.grid(row=1,column=0)


file_menu=Menu(menu_bar,tearoff=0 , background = "black" , foreground= "red")
edit_menu=Menu(menu_bar,tearoff=0 , background = "black" , foreground= "red")
track_menu=Menu(menu_bar,tearoff=0 , background = "black" , foreground= "red")
info_menu=Menu(menu_bar,tearoff=0 , background = "black" , foreground= "red")


def visual_music():
    pass

def press_buttons():

    btn_frames = Frame(root)
    btn_frames.grid(row=3,column=0)

    play_btn_label = Button(btn_frames,text="Play" , command=play_music, padx = 30, pady =30)
    play_btn_label.grid(row=3,column=1)

    stop_btn_label = Button(btn_frames,text="Stop" , command=stop_music, padx = 30, pady =30)
    stop_btn_label.grid(row=3,column=2)

    pause_btn_label = Button(btn_frames,text="Pause" , command=pause_music, padx = 30, pady =30)
    pause_btn_label.grid(row=3,column=3)

    unpause_btn_label = Button(btn_frames,text="Unpause" , command=unpause_music, padx = 30, pady =30)
    unpause_btn_label.grid(row=3,column=4)


def open_path():

    fd = filedialog
    ask_for_file = fd.askopenfilename(initialdir = "/home/raku/Music/Justice Music" , title = " Load a sound file", filetypes= (("wav files","*.wav"), ("mp3 files" , "*.mp3") ,))
    just_the_title = ask_for_file.replace("/home/raku/Music/Justice Music/" , "")

    global load_music
    load_music = ask_for_file
    track_box.insert(0, just_the_title)

def play_music():

    try:
        global playing_music
        playing_music = True
        #load_music = "/home/raku/Music/Justice Music/FunkJazzSong.wav"

        if playing_music == True:
            mixer.music.load(load_music)
            mixer.music.play()
            error_label.config(text="")
    except:
        error_label.config(text="Please select a sound file first!!!")

def stop_music():

    playing_music = False
    mixer.music.stop()

def pause_music():

    mixer.music.pause()

def unpause_music():

    mixer.music.unpause()

def add_cover_art():

    image_set = False
    image_size = 400, 400

    ca_file = filedialog
    find_art = ca_file.askopenfilename()

    open_image = Image.open(find_art)
    open_image.thumbnail(image_size)
    show_image = ImageTk.PhotoImage(open_image)

    art_image = Label(root, image=show_image)
    art_image.image = show_image
    art_image.grid(row=0,column=1)

def duration_bar():

    slider_frame = Frame(root)
    slider_frame.grid(row=2)

    dur_bar = tk.Scale(slider_frame,sliderlength=10,length=413,from_=0,to=100,orient="horizontal")
    dur_bar.grid(row=4,column=2)
    dur_bar["state"] = "disabled"

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
    press_buttons()
    file_commands()
    edit_commands()
    track__menu_commands()
    info_commands()
    duration_bar()


if __name__ == "__main__":
    run_command_bar()
    root.mainloop()
