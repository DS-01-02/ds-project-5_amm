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
    elif event == "Add":
        # window_add['Start update'].update(disabled=True)
        # if not t:
        #     window_add.un_hide()
        while True:
            if t:
                event2, values2 = window_add.read()
            else:
                window_add.un_hide()
                event2, values2 = window_add.read()
            if event2 == sg.WIN_CLOSED:
                break
            elif event2 == "Exit" or event2 == 'Cancel':
                window_add.hide()
                t = False
                break
            elif event2 == 'Add' and values2['-IN2-'] != '':
                add2 = []
                # print('added')
                add = str(values2['-IN2-'])
                add = add.split('.')
                add2.append(values2['-IN2-'])
                if len(add) == 3 and (add[2]=='txt' or add[2]=='png' or add[2]=='jpg' or add[2]=='mp4' or
                                      add[2]=='txt' or add[2] =='txt' or add[2] == 'txt' or add[2] == 'txt' or add[2]=='txt' ) \
                        and add[1] != '' and (add2 not in list_file_s):
                    list_file_s.append(add2)
                    window["-FILE LIST-"].update(list_file_s)
                    window_add.hide()
                    t = False
                    add2 = []
                    break
                else:
                    pass
    elif event == "delete":
        add2 = []
        add2.append(values["-IN3-"])
        if add2 in list_file_s:
            list_file_s.remove(add2)
            window["-FILE LIST-"].update(list_file_s)
        # print(' ')
    elif event == "save":
        if len(list_file_s) != 0:
            dicr = []
            dicr2 = {}
            for i in list_file_s:
                j = i[0]
                j = j.split('.')
                dicr2['name'] = j[0]
                dicr2['date'] = int(j[1])
                dicr2['format'] = j[2]
                dicr.append(dicr2)
                dicr2 = {}
            with open('sorted_date.json', 'w') as json_file:
                json.dump(sorted(dicr, key=sort_by_key), json_file)
            with open('sorted_format.json', 'w') as json_file:
                json.dump(sorted(dicr, key=sort_by_key_f), json_file)
            sg.popup('files was saved',title='save')
# window = Tk()
# button = Button(text="Browse",command=openFile)
# button.pack()
# window.geometry("420x30")
# window.title("ali")
# icon = PhotoImage(file='folder.png')
# window.iconphoto(True,icon)
# window.config(background='#34eb89')
# zip = zipfile.ZipFile('C:/Users/akgh1/Desktop/sort.zip')
# names =zip.namelist()
# window.mainloop()




# layout = [
#     [sg.Tree(treedata,headings=['name' , 'size' , 'format'], col0_width=80, num_rows=20, show_expanded=True, enable_events=True, key='-TREE-')],
#     [sg.StatusBar("", size=(0, 1), key='-STATUS-')],
# ]
#
# window = sg.Window("File Browser", layout, finalize=True)
# tree = window['-TREE-']
# # tree.Widget.configure(show='tree')  # Hide header
# tree.bind('<Double-1>', "DOUBLE-CLICK-")
# status = window['-STATUS-']
# while True:
#
#     event, values = window.read()
#
#     if event == sg.WINDOW_CLOSED:
#         break
#     status.update('')
#     if event == '-TREE-DOUBLE-CLICK-':
#         parent_key = values['-TREE-'][0]
#         node = data[parent_key]
#         if node['kind'] == DIR and node['children'] == None:
#             parent_path = Path(node['path']).joinpath(node['file'])
#             try:
#                 files = sorted(list(parent_path.iterdir()), key=lambda file:file.is_file())
#             except:
#                 status.update("Access is denied")
#                 continue
#             node['children'] = []
#             for item in files:
#                 key = new_key()
#                 kind, path, file = item.is_dir(), str(item.parent), item.name
#                 treedata.insert(parent_key, key, str(file), [], icon=folder_icon if kind == DIR else file_icon)
#                 node['children'].append(key)
#                 data[key] = {'kind':kind, 'path':path, 'file':file, 'children':None}
#             tree.update(values=treedata)
#             iid = tree.KeyToID[parent_key]
#             tree.Widget.see(iid)

# window.close()
#!/usr/bin/env python
# import sys
# import os
# if sys.version_info[0] >= 3:
#     import PySimpleGUI as sg
# else:
#     import PySimpleGUI27 as sg
#
# folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
#
# file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'
#
# # STARTING_PATH = sg.PopupGetFolder('Folder to display')
# #
# treedata = sg.TreeData()
#
# def add_files_in_folder(parent, dirname):
#     files = os.listdir(dirname)
#     for f in files:
#         fullname = os.path.join(dirname,f)
#         if os.path.isdir(fullname):            # if it's a folder, add folder and recurse
#             treedata.Insert(parent, fullname, f, values=[] , icon=folder_icon)
#             add_files_in_folder(fullname, fullname)
#         else:
#             treedata.Insert(parent, fullname, f, values=[] , icon=file_icon)
#
# add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new/")
#

# layout = [[ sg.Text('File and folder browser Test') ],
#           [ sg.Tree(data=treedata, headings=['col1', 'col2', 'col3'], auto_size_columns=True, num_rows=20,
#                     col0_width=30, key='_TREE_', show_expanded=False,),],
#           [ sg.Button('Ok'), sg.Button('Cancel')]]
#
# window = sg.Window('Tree Element Test').Layout(layout)

#
# while True:     # Event Loop
#     event, values = window.Read()
#     if event in (None, 'Cancel'):
#         break
#     # print(event, values)
# import PySimpleGUI as sg
#
#
# data = {
#     'First': {
#         'Title': 'an inner node',
#         'data': ['some data', 'some extra info']},
#     'Second': {
#         'Title': 'an inner node',
#         'data': ['a second piece of data', 'some more info']}
# }

#
# def build_treedata(data: dict):
#     my_data = sg.TreeData()
#     for item in data:
#         my_data.insert(parent='', key=f'-{item}-', text=item, values=[] , icon=folder_icon)
#         my_data.insert(parent=f'-{item}-', key=f'-{item}_title-',
#                         text=data[item]['Title'],
#                         values=[data[item]['data'][0], data[item]['data'][1]] , icon=file_icon)
#     return my_data
#
# def append_to_dict(data: dict, root_name: str, title: str, info: list):
#     data[root_name] = {
#             'Title': title,
#             'data': info}
#     return data

# initial_treedata = build_treedata(data)
#
# layout = [
#     [sg.Tree(data=initial_treedata, headings=['a heading', 'another heading'], key='-TREE-')],
#     [sg.Input('Third', key='-root_name-', size=(15, 1))],
#     [sg.Input('I added this', key='-title-', size=(10, 1)), sg.Input('very important; info', key='-data-')],
#     [sg.Button('Append new data to the Tree', key='-submit-')]
# ]
#
# window = sg.Window('Try appending this tree!', layout)
#
# while True:
#     event, values = window.read()
#
#     if event in [sg.WIN_CLOSED]:
#         break
#
#     elif event == '-submit-':
#         data = append_to_dict(data, values['-root_name-'], values['-title-'], values['-data-'].split(';'))
#         new_treedata = build_treedata(data)
#         window['-TREE-'].update(values=new_treedata)


# window.close()