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

treedata = sg.TreeData()

def add_files_in_folder(parent, dirname):
    files = os.listdir(dirname)
    for f in files:
        fullname = os.path.join(dirname,f)
        if os.path.isdir(fullname):            # if it's a folder, add folder and recurse
            treedata.Insert(parent, fullname, f, values=['','folder       '] , icon=folder_icon )
            add_files_in_folder(fullname, fullname)
        else:
            f2 = f.split('.')
            treedata.Insert(parent, fullname ,  text=f2[0], values=[ f2[1]+'       ' , f2[2]+'       '] , icon=file_icon)
    return treedata


add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new")
file_list_column = [
    [
        sg.Text("Choose a ZipFile: "), sg.Input(key="-IN2-", change_submits=True),
        sg.FileBrowse(key="-IN-", file_types=(('Zip Files', '*.zip'), ('All Files', '*.*')), ), ],
    [sg.Tree(data=treedata,headings=['Date', 'Type'], auto_size_columns=True, num_rows=20,
             col0_width=30, key='_TREE_', show_expanded=False,background_color='white',header_text_color='blue', text_color='black', col0_heading='name'),],
    [sg.Button("Extract"), sg.T(""), sg.Button("Add"),sg.T(""),sg.Button("save")],[], [sg.Text("choose a file for delete"),sg.Input(key="-IN3-" ,change_submits=True )
        ,sg.Button("delete")],
]
layout = [
    [sg.Column(file_list_column), ]
]
sg.theme("DarkTeal2")
layout1 = [
    [sg.Text("Inter the name of file "), sg.Input(key="-IN2-", change_submits=False)],
    [sg.Button("Add"), sg.T(""), sg.Button("Cancel")],
]
# sg.theme("DarkTeal2")
window = sg.Window('My File Browser', layout, size=(560, 460))
window_add = sg.Window('Add' , layout1 , size=(340, 100))
t = True
list_file_s = []
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
        window["_TREE_"].update(add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new"))
    elif event == "New File" or event == "Add":
        if faz1 == True:

            sg.theme(THEME)
            layout1 = [
                [sg.Text("Enter the name of file "), sg.Input(key="-IN2-", change_submits=False)],
                [sg.Button("Add"), sg.T(""), sg.Button("Cancel")],
            ]
            layout2 = [
                [sg.Column(layout1), ]
            ]
            window_add = sg.Window('Add', layout2, size=(340, 75),keep_on_top=True)
            while True:
                if t:
                    event2, values2 = window_add.read()
                else:
                    event2, values2 = window_add.read()
                if event2 == sg.WIN_CLOSED:
                    window_add.close()

                    break
                elif event2 == "Exit" or event2 == 'Cancel':
                    window_add.hide()

                    t = False
                    break
                elif event2 == 'Add' and values2['-IN2-'] != '':

                    add2 = []
                    add = str(values2['-IN2-'])
                    add = add.split('.')
                    add2.append(values2['-IN2-'])
                    if len(add) == 3 and (add[2] == 'txt' or add[2] == 'png' or add[2] == 'jpg' or add[2] == 'mp4' or
                                          add[2] == 'gif' or add[2] == 'jpeg' or add[2] == 'mov' or add[2] == 'mkv' or
                                          add[2] == 'avl'or add[2] == 'aiff' or add[2] == 'wav' or add[2] == 'pdf') \
                            and add[1] != '':
                        if add2 in list_file_s:
                            sg.popup('"' + add2[0] + '"' + ' is already exist' , keep_on_top=True)
                            pass
                        if int(add[1]) > current_year:
                            add[1] = str(current_year)
                        list_file_s.append(add2)
                        newfile = open(
                            "C:/Users/akgh1/PycharmProjects/unzip/new/" + add[0] + '.' + add[1] + '.' + add[2],
                            'w')
                        if not os.path.exists("C:/Users/akgh1/PycharmProjects/unzip/Phase3/"):
                            os.makedirs("C:/Users/akgh1/PycharmProjects/unzip/Phase3/")
                        tmp_str=os.listdir("C:/Users/akgh1/PycharmProjects/unzip/Phase3/")
                        newfile1 = open(
                            "C:/Users/akgh1/PycharmProjects/unzip/Phase3/"+tmp_str[0]+"/" + add[0] + '.' + add[1] + '.' + add[2],
                            'w')
                        treedata = sg.TreeData()
                        window["_TREE_"].update(
                            add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new" , sor))
                        window_add['-IN2-'].update('')
                        newfile.close()
                        newfile1.close()
                        # window["-FILE LIST-"].update(list_file_s)
                        window_add.hide()
                        t = False
                        add2 = []

                        break
                    else:

                        pass
                window_add.close()
        else :
            sg.popup('You Should Be In Phase 1', title='Error', keep_on_top=True,text_color="Red")
    elif event == "Delete":
        if faz1 == True:
            if values["_TREE_"] != [] and faz1 == True:
                # msg_box = tk.messagebox.askquestion('Delete All Files', 'Are you sure you want to Delete this Files ?',
                #                                     icon='warning')
                msg_box = sg.popup_yes_no('Are you sure you want to Delete this Files ?', keep_on_top=True)
                if msg_box == "Yes":
                    add2 = []
                    st = values["_TREE_"]
                    st = st[0].split('\\')
                    add2.append(st[1])
                    if add2 in list_file_s:
                        list_file_s.remove(add2)
                        tmp_str = os.listdir("C:/Users/akgh1/PycharmProjects/unzip/Phase3/")
                        if os.path.exists("C:/Users/akgh1/PycharmProjects/unzip/Phase3/" +tmp_str[0]+'/'+ add2[0]):
                            os.remove("C:/Users/akgh1/PycharmProjects/unzip/Phase3/"+tmp_str[0]+'/' + add2[0])
                        os.remove("C:/Users/akgh1/PycharmProjects/unzip/new/" + add2[0])
                        treedata = sg.TreeData()
                        window["_TREE_"].update(
                            add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new", sor))
            else:
                sg.popup('You Should Choose A File For Deleting', title='Warning', keep_on_top=True,text_color="Yellow")
        else:
            sg.popup('You Should Be In Phase 1', title='Error', keep_on_top=True,text_color="Red")

            # window['_TREE_'].update('')
            # else:
            #     sg.popup('there is no ' + add2[0] + ' in this folder!', title='error',background_color='white',text_color='blue', icon=error_icon , keep_on_top=True)
    elif event == "Save" and faz1 == True:
        if len(list_file_s) != 0:
            dicr = []
            dicr2 = {}
            for i in list_file_s:
                i2 = i[0]
                i2 = i2.split('.')
                dicr2['name'] = i2[0]
                dicr2['date'] = int(i2[1])
                dicr2['format'] = i2[2]
                dicr.append(dicr2)
                dicr2 = {}


            with open('sorted_date.json', 'w') as json_file:
                json.dump(sorted(dicr, key=sort_by_key), json_file)
            with open('sorted_format.json', 'w') as json_file:
                json.dump(sorted(dicr, key=sort_by_key_f), json_file)
            sg.popup('files was saved', title='save' , keep_on_top=True,text_color="Green")
