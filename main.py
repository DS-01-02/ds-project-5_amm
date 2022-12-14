import zipfile
import PySimpleGUI as sg
import shutil
import os
import os.path
import json
from pathlib import Path
import sys
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import tkinter.ttk as ttk
file_list_column = [
    [
        sg.Text("Choose a ZipFile: "), sg.Input(key="-IN2-", change_submits=True),
        sg.FileBrowse(key="-IN-", file_types=(('Zip Files', '*.zip'), ('All Files', '*.*')), ), ],
    [sg.Button("Extract"), sg.T(""), sg.Button("Add"),sg.T(""),sg.Button("save")],[], [sg.Text("choose a file for delete"),sg.Input(key="-IN3-" ,change_submits=True )
        ,sg.Button("delete")],
]
layout = [
    [sg.Column(file_list_column), ]
]
window = sg.Window('My File Browser', layout, size=(560, 460))
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    elif event == "Extract" and values["-IN2-"] != '':
        zip = zipfile.ZipFile(values["-IN-"])
        names = zip.namelist()
        j = 0
        for i in names:
            if ("/" in i):
                while ('/' in i[j:len(i)]):
                    j = j + 1
                if (i[j:] != ''):
                    f = i[j:]
                    list_file = f.strip().split()
                    list_file_s.append(list_file)
                j = 0
            else:
                list_file = i.strip().split()
                list_file_s.append(list_file)
        # window["-FILE LIST-"].update(list_file_s)
        newpath = r'C:\Users\akgh1\PycharmProjects\unzip\dirname'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        for member in zip.namelist():
                zip.extract(member, 'dirname')

        newpath = r'C:\Users\akgh1\PycharmProjects\unzip\new'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        for i in zip.namelist():
            if (i[-1] == '/'):
                source = "C:/Users/akgh1/PycharmProjects/unzip/dirname/" + i
                destination = "C:/Users/akgh1/PycharmProjects/unzip/new/"
                files = os.listdir(source)
                for file in files:
                    if '.txt' in file or '.png' in file or '.zip' in file or '.pdf' in file or '.aiff' in file or '.jpeg' in file \
                            or '.wav' in file or '.avl' in file or '.mkv' in file or '.mov' in file or '.jpg' in file or '.gif' in file \
                            or '.mp4' in file:
                        file_name = os.path.join(source, file)
                        shutil.move(file_name, destination)
        source = "C:/Users/akgh1/PycharmProjects/unzip/dirname/"
        destination = "C:/Users/akgh1/PycharmProjects/unzip/new/"
        files = os.listdir(source)
        for file in files:
            file_name = os.path.join(source, file)
            shutil.move(file_name, destination)
        treedata = sg.TreeData()