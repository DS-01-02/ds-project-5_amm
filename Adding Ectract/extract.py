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
from datetime import date
current_year = date.today().year
def sort_by_key(list):
    return list['date']


def sort_by_key_f(list):
    return list['format']
# tree = ttk.Treeview()
# sg.theme("DarkTeal2")
import sys
import os
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='

file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

error_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAB9JREFUOE9jZKAQMFKon2HUAIbRMGAYDQNQPhr4vAAAJpgAEX/anFwAAAAASUVORK5CYII='
treedata = sg.TreeData()
# sg.theme("LightGreen6")
# sg.theme("LightBrown2")
def add_files_in_folder(parent, dirname):
    files = os.listdir(dirname)
    for f in files:
        fullname = os.path.join(dirname,f)
        if os.path.isdir(fullname):            # if it's a folder, add folder and recurse
            treedata.Insert(parent, fullname, f, values=['  ','File folder'] , icon=folder_icon )
            add_files_in_folder(fullname, fullname)
        else:
            f2 = f.split('.')
            treedata.Insert(parent, fullname ,  text=f2[0]+'.'+f2[1]+'.'+f2[2], values=[ f2[1]+'       ' , f2[2]+'       '] , icon=file_icon)
    return treedata
def make_window(theme=None):
    if theme:
        sg.theme(theme)
    # -----  Layout & Window Create  -----
    menu_def = [['&File', ['&Add','Extract', '&Remove', ['A File', 'All Files'], 'E&xit']],
                ['&Project', ['&faz1', '&faz2', '&faz3', 'faz4']],
                ['&Theme', ['Set A Theme', 'Default Theme']],
                ['&Sort',
                 ['&Name', ['A-Z', 'Z-A'], 'Date', ['Newest To Oldest', 'Oldest To Newest'], 'Type',
                  ['A-Z', 'Z-A']]],
                ['&Help', ['&About...']], ]

    file_list_column = [
        [sg.MenubarCustom(menu_def, pad=(0, 0), k='-CUST MENUBAR-')],
        [sg.Tree(data=treedata, headings=['Date', 'Type', ], auto_size_columns=True, num_rows=20,
                 enable_events=True,
                 expand_x=True,
                 expand_y=True  # background_color='white',header_text_color='blue, text_color='black'
                 , col0_width=20, col0_heading='Name', key='_TREE_', show_expanded=False, background_color='white',
                 header_text_color='blue', text_color='black'), ],
        [sg.Text("Choose a ZipFile: "), sg.Input(key="-IN2-", change_submits=True, size=(40)),
         # sg.Radio( 'Name' ,'rd_bread', key='nam'),sg.Radio( 'Date','rd_bread',key='da'),sg.Radio( 'Type','rd_bread',key='TY')
         sg.FileBrowse(key="-IN-", file_types=(('Zip Files', '*.zip'), ('All Files', '*.*')), ), ],

        # [sg.Tree(data=treedata, headings=['Date', 'Type', ], auto_size_columns=True, num_rows=20,
        #          enable_events=True,
        #          expand_x=True,
        #          expand_y=True  # background_color='white',header_text_color='blue, text_color='black'
        #          , col0_width=20, col0_heading='Name', key='_TREE_', show_expanded=False, background_color='white',
        #          header_text_color='blue', text_color='black'), ],
        #[sg.Button("Extract"), sg.T(""), sg.Button("Add"), sg.T(""), sg.Button("save")],
        #[sg.Text("choose a file for delete:"), sg.Input(key="-IN3-", change_submits=True)
         #   , sg.Button("delete")],# [sg.Button("faz2", size=(5)), ]
    ]
    # sg.theme("LightGreen")
    layout = [
        [sg.Column(file_list_column), ]
    ]
    window = sg.Window("Custom Titlebar with Custom (Simulated) Menubar", layout, use_custom_titlebar=True,
              keep_on_top=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT )#, size=(530 , 530))
    return window
# sg.theme(values['-THEME LIST-'])
menu_def = [['&File', ['&Add', '&Remove', ['A File', 'All Files'], '&Exit']],
    ['&Project',['&faz1','&faz2','&faz3','faz4']],
    ['&Theme', ['Set A Theme', 'Default Theme']],
    ['&Sort',
    ['&Name', ['A-Z', 'Z-A'], 'Date', ['Newest To Oldest', 'Oldest To Newest'], 'Type',
    ['A-Z', 'Z-A']]],
    ['&Help', ['&About...']], ]

# layout = [[sg.MenubarCustom(menu_def, pad=(0, 0), k='-CUST MENUBAR-')],
#             [sg.Multiline(size=(70, 20), reroute_cprint=True, write_only=True, no_scrollbar=True,
#                         k='-MLINE-')]]
# window = sg.Window("Custom Titlebar with Custom (Simulated) Menubar", layout, use_custom_titlebar=True,
#         keep_on_top=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)

add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new")
file_list_column = [
    [sg.MenubarCustom(menu_def, pad=(0, 0), k='-CUST MENUBAR-')],
        [sg.Text("Choose a ZipFile: "), sg.Input(key="-IN2-", change_submits=True , size=(40)),#sg.Radio( 'Name' ,'rd_bread', key='nam'),sg.Radio( 'Date','rd_bread',key='da'),sg.Radio( 'Type','rd_bread',key='TY')
        sg.FileBrowse(key="-IN-", file_types=(('Zip Files', '*.zip'), ('All Files', '*.*')), ),],
    [sg.Tree(data=treedata,headings=['Date', 'Type',], auto_size_columns=True, num_rows=20,
             enable_events=True,
             expand_x=True,
             justification='left',
             expand_y=True#background_color='white',header_text_color='blue, text_color='black'
        , col0_width=20,col0_heading='Name' ,key='_TREE_', show_expanded=False ,background_color='white',header_text_color='blue', text_color='black'),],
    [sg.Button("Extract"), sg.T(""),sg.Button("Add"),sg.T(""),sg.Button("save")],
    [sg.Text("choose a file for delete:"),sg.Input(key="-IN3-" ,change_submits=True )
        ,sg.Button("delete") ],# [sg.Button("faz2" , size=(5)),]
]
# sg.theme("LightGreen")
layout = [
    [sg.Column(file_list_column), ]
]
layout1 = [
    [sg.Text("Inter the name of file "), sg.Input(key="-IN2-", change_submits=False)],
    [sg.Button("Add"), sg.T(""), sg.Button("Cancel")],
]
layout2=[
    [sg.Column(layout1),]
]
# DarkTeal2
sg.theme("DarkTeal2")
# sg.theme("LightGreen")
# window = sg.Window('My File Browser', layout, size=(545, 530) ,use_custom_titlebar=True,
#         keep_on_top=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)
# window_add = sg.Window('Add' , layout2 , size=(340, 75))
t = True
newpath = r'C:\Users\akgh1\PycharmProjects\unzip\new'
list_file_s = []
set_year=()
set_year = set(set_year)
if  os.path.exists(newpath):
    list_dir = os.listdir(newpath)
    for i1 in list_dir:
        name_year = i1.split('.')
        li = []
        li.append(i1)
        if '.txt' in i1 or '.png' in i1 or '.zip' in i1 or '.pdf' in i1 or '.aiff' in i1 or '.jpeg' in i1 \
                or '.wav' in i1 or '.avl' in i1 or '.mkv' in i1 or '.mov' in i1 or '.jpg' in i1 or '.gif' in i1 \
                or '.mp4' in i1:
            list_file_s.append(li)
            set_year.add(int(name_year[1]))
# tree = window['_TREE_']
window_add = sg.Window('Add', layout2, size=(340, 75))
window = make_window('Tan')
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        shutil.rmtree("C:/Users/akgh1/PycharmProjects/unzip/faz2/")
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
            if '.txt' in file or '.png' in file or '.zip' in file or '.pdf' in file or '.aiff' in file or '.jpeg' in file \
                    or '.wav' in file or '.avl' in file or '.mkv' in file or '.mov' in file or '.jpg' in file or '.gif' in file \
                    or '.mp4' in file:
                file_name = os.path.join(source, file)
                shutil.move(file_name, destination)

        files = os.listdir(destination)
        for i in list_file_s:
            i2 = i[0]
            name_year = i2.split('.')
            if int(name_year[1]) > current_year:
                os.remove("C:/Users/akgh1/PycharmProjects/unzip/new/"+i2)
                list_file_s.remove(i)
            else:
                set_year.add(int(name_year[1]))
        treedata = sg.TreeData()
        window["_TREE_"].update(add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new"))
        window['-IN2-'].update('')