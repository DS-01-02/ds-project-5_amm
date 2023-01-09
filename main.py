import zipfile
import PySimpleGUI as sg
import shutil
import os
import os.path
import json
from collections import deque
from pathlib import Path
import sys
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from datetime import date
current_year = date.today().year
THEME = "DarkBlue"
def sort_by_key(list):
    return list['date']
def settheme(theme):
    global THEME
    THEME =theme
def sort_by_key_f(list):
    return list['format']
def sort_by_key_n(list):
    return list['name']
import sys
import os
sor = ''
Current_Change =" "
Current_choice_for_sort = "A-Z"
undo = []
redo = []
stack=[]
stack_check=[]
stack_index=[]
Par=[]


class Node:

    def __init__(self, key):
        self.key = key
        self.children = []


class Pair:
    def __init__(self, _node, _childrenIndex):
        self.node = _node
        self.childrenIndex = _childrenIndex

currentRootIndex = 0
stack = []
postorderTraversal = []
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg

# dicr = []
# sorted_dicr = []
for_faz3 = []
def sort_dict(list , sor):
    l = len(list)
    for i in range(l - 1):
        for j in range(i + 1, l):
            if (list[i]['name'] > list[j]['name'] and sor == 'name1') or (list[i]['format'] > list[j]['format'] and sor == 'type1') or (list[i]['date'] > list[j]['date'] and sor == 'date1')\
                    or (list[i]['date'] < list[j]['date'] and sor == 'date2')or (list[i]['name'] < list[j]['name'] and sor == 'name2')\
                    or (list[i]['format'] < list[j]['format'] and sor == 'type2'):
                t = list[i]
                list[i] = list[j]
                list[j] = t
    return list
def add_files_in_folder_2(parent, dirname):
    files = os.listdir(dirname)
    sorted_dicr = files
    for f in sorted_dicr:
        fullname = os.path.join(dirname,f)
        if os.path.isdir(fullname):
            for_faz3.append(f)
            for_faz3.append('{')
            treedata.Insert(parent, fullname, f, values=['  ','File folder'] , icon=folder_icon)
            add_files_in_folder_2(fullname, fullname)
        else:
            for_faz3.append(f)
            f2 = f.split('.')
            if f2[2] == 'pdf':
                treedata.Insert(parent, fullname ,  text=f2[0], values=[ f2[1]+'' , f2[2]+''] , icon=pdf_icon)
            elif f2[2] == 'txt':
                treedata.Insert(parent, fullname ,  text=f2[0], values=[ f2[1]+'' , f2[2]+''] , icon=txt_icon)
            elif f2[2] == 'png' or f2[2]=='jpg'or f2[2]=='gif'or f2[2]=='jpeg':
                treedata.Insert(parent, fullname ,  text=f2[0], values=[ f2[1]+'' , f2[2]+''] , icon=png_icon)
            elif f2[2] == 'mp4' or f2[2] == 'mov'or f2[2]=='mkv'or f2[2]=='avl':
                treedata.Insert(parent, fullname, text=f2[0], values=[f2[1] + '', f2[2] + ''], icon=mp4_icon)
            elif f2[2] == 'aiff' or f2[2] == 'wav':
                treedata.Insert(parent, fullname, text=f2[0], values=[f2[1] + '', f2[2] + ''], icon=music_icon)

            else:
                treedata.Insert(parent, fullname ,  text=f2[0], values=[ f2[1]+'' , f2[2]+''] , icon=file_icon)
    for_faz3.append('}')
    return treedata
def MakeTree(root, a):
    for i in range(1, len(a)):
        tmp = newNode(None)
        if a[i] == "{" and i != 1:
            continue
        if a[i] == "{":
            tmp =newNode( a[i - 1])
            root = tmp
            index = -1
            stack_index.append(index)
            stack.append(root)

        elif i + 1 < len(a) and a[i + 1] == "{":
            tmp =newNode(a[i])
            root = tmp
            index = -1
            stack_index.append(index)
            stack.append(root)

        elif a[i] == "}":
            if len(stack) == 0:
                tmp_root = root
                return root

            index = stack_index.pop()

            ab = stack.pop()
            if len(stack) == 0:
                if i == len(a) - 1:
                    tmp_root = root
                return root
            root = stack.pop()
            root.children.append(ab)
            index = stack_index.pop()
            index = index + 1
            stack_index.append((index))
            stack.append(root)
        else:
            tmpp =newNode(a[i])
            root.children.append(tmpp)

            index = stack_index.pop()
            index = index + 1
            stack_index.append(index)
# Driver program
def add_files_in_folder(parent, dirname,sor):
    files = os.listdir(dirname)
    dicr2 = {}
    dicr = []
    sorted_dicr = []
    if sor != '':
        for i in files:
            # i2 = i[0]
            i = i.split('.')
            dicr2['name'] = i[0]
            dicr2['date'] = int(i[1])
            dicr2['format'] = i[2]
            dicr.append(dicr2)
            dicr2 = {}
        if sor == 'date1':
            dicr = sort_dict(dicr ,sor)
        elif sor == 'name1':
            dicr = sort_dict(dicr, sor)
        elif sor == 'type1':
            dicr = sort_dict(dicr, sor)
        elif sor == 'date2':
            dicr = sort_dict(dicr, sor)
        elif sor == 'name2':
            dicr = sort_dict(dicr, sor)
        elif sor == 'type2':
            dicr = sort_dict(dicr, sor)
        sorted_str = ''
        for i in dicr:
            sorted_str += i['name'] + '.'
            sorted_str += str(i['date']) + '.'
            sorted_str += i['format']
            sorted_dicr.append(sorted_str)
            sorted_str = ''
    else:
        sorted_dicr = files
    for f in sorted_dicr:
        fullname = os.path.join(dirname,f)
        if os.path.isdir(fullname):  # if it's a folder, add folder and recurse
            # print(f,'{',end='')
            for_faz3.append(f)
            for_faz3.append('{')
            # sor2 +=f+'{'
            treedata.Insert(parent, fullname, f, values=['  ','File folder'] , icon=folder_icon)
            add_files_in_folder(fullname, fullname , sor)
        else:
            # print(f,end='')
            # sor2 += f
            for_faz3.append(f)
            f2 = f.split('.')
            if f2[2] == 'pdf':
                treedata.Insert(parent, fullname ,  text=f2[0], values=[ f2[1]+'' , f2[2]+''] , icon=pdf_icon)
            elif f2[2] == 'txt':
                treedata.Insert(parent, fullname ,  text=f2[0], values=[ f2[1]+'' , f2[2]+''] , icon=txt_icon)
            elif f2[2] == 'png' or f2[2]=='jpg'or f2[2]=='gif'or f2[2]=='jpeg':
                treedata.Insert(parent, fullname ,  text=f2[0], values=[ f2[1]+'' , f2[2]+''] , icon=png_icon)
            elif f2[2] == 'mp4' or f2[2] == 'mov'or f2[2]=='mkv'or f2[2]=='avl':
                treedata.Insert(parent, fullname, text=f2[0], values=[f2[1] + '', f2[2] + ''], icon=mp4_icon)
            elif f2[2] == 'aiff' or f2[2] == 'wav':
                treedata.Insert(parent, fullname, text=f2[0], values=[f2[1] + '', f2[2] + ''], icon=music_icon)

            else:
                treedata.Insert(parent, fullname ,  text=f2[0], values=[ f2[1]+'' , f2[2]+''] , icon=file_icon)
    # print('}',end='')
    for_faz3.append('}')
    # sor2 += '}'
    return treedata


def make_window(theme=THEME):
    if theme:
        sg.theme(theme)
        THEME = theme
    menu_def = [['&File', ['&New',['New File'],'Extract', '&Remove', ['A File', 'All Files'],'Save', 'E&xit']],
                ['&Option',["Zip","Undo","Redo"]],
                ['&Project', ['&Phase 1', '&Phase 2', '&Phase 3']],
                ['&Theme', ['Set A Theme', 'Default Theme']],
                ['&Sort',['&Name', ['A-Z', 'Z-A'], 'Date', ['Newest To Oldest', 'Oldest To Newest'], 'Type',
                  ['A_Z', 'Z_A']]],
                ['&Help', ['&About...']], ]

    file_list_column = [
        [sg.MenubarCustom(menu_def, pad=(0, 0), k='-CUST MENUBAR-'),sg.Input(background_color='white',text_color="Black",change_submits=True , key='-serch-'),sg.Button('Search')],
        [sg.Button("Undo"),sg.Text("                                                                                                                                           "),sg.Button("Redo")],
        [sg.Tree(data=treedata,
                 enable_events=True,
                 headings=['Date', 'Type'], num_rows=20,
                 # auto_size_columns=True,
                 max_col_width=30,
                 expand_x=True,
                 # col0_width=30,
                 # col_widths=[2,2],
                 change_submits=True,
                 expand_y=True,row_height=20,justification='mid', col0_heading='Name', key='_TREE_', show_expanded=False, background_color='white',
                 header_text_color='black', text_color='black',right_click_menu=['&Right', ["Refresh","Add","Delete","Extract",'&Sort',['&Name', ['A-Z', 'Z-A'], 'Date', ['Newest To Oldest', 'Oldest To Newest'], 'Type',
                  ['A_Z', 'Z_A']],'&Theme', ['Set A Theme', 'Default Theme'],"&Options,",["Zip","Undo","Redo"],'Exit']]), ],
        [sg.Text("Choose a ZipFile: ",key='ch' , visible=True), sg.Input(key="-IN2-", change_submits=True, size=(45),visible=True ,text_color="Black"),
         sg.FileBrowse (key="-IN-", file_types=(('Zip Files', '*.zip'), ('All Files', '*.*')),size=(7,1),visible=True)
            ,sg.Button("Extract" , key='Ex' ,visible=True,size=(7,1)),sg.Button('Save',size=(7,1))],#,sg.Button("SAVE" , key='SA',visible=True)
    ]
    layout = [
        [sg.Column(file_list_column), ]
    ]
    window = sg.Window("File Manager", layout, use_custom_titlebar=True,
              keep_on_top=True ,resizable=True,finalize=True)#, size=(530 , 530)) , right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT
    window["_TREE_"].expand(True, True)
    return window
def make_window_phase3(theme=THEME):
    if theme:
        sg.theme(theme)
        THEME = theme
    menu_def = [['&File', ['&New',['New File'],'Extract', '&Remove', ['A File', 'All Files'],'Save', 'E&xit']],
                ['&Option',["&Inorder","Preorder","&Postorder"]],
                ['&Project', ['&Phase 1', '&Phase 2', '&Phase 3']],
                ['&Theme', ['Set A Theme', 'Default Theme']],
                ['&Sort',['&Name', ['A-Z', 'Z-A'], 'Date', ['Newest To Oldest', 'Oldest To Newest'], 'Type',
                  ['A_Z', 'Z_A']]],
                ['&Help', ['&About...']], ]

    file_list_column = [
        [sg.MenubarCustom(menu_def, pad=(0, 0), k='-CUST MENUBAR-')],
        [sg.Tree(data=treedata,
                 enable_events=True,
                 headings=['Date', 'Type'], num_rows=20,
                 # auto_size_columns=True,
                 max_col_width=30,
                 expand_x=True,
                 # col0_width=30,
                 # col_widths=[2,2],
                 change_submits=True,
                 expand_y=True,row_height=20,justification='mid', col0_heading='Name', key='_TREE_', show_expanded=False, background_color='white',
                 header_text_color='black', text_color='black',right_click_menu=['&Right', ['&Option',["&Inorder","Preorder","&Postorder"],'&Theme', ['Set A Theme', 'Default Theme'],'Exit']]), ],
    [sg.Input(background_color='white',text_color="Black",change_submits=True , key='-ROOT-'),sg.Button('Search for Root'),
    sg.Button('Inorder') , sg.Button('Preorder') , sg.Button('Postorder')],
    ]
    layout = [
        [sg.Column(file_list_column), ]
    ]
    window = sg.Window("Tree Travelsals", layout, use_custom_titlebar=True,
              keep_on_top=True ,resizable=True,finalize=True)#, size=(530 , 530)) , right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT
    window["_TREE_"].expand(True, True)
    return window
new_folder = r'C:/Users/User/PycharmProjects/pythonProject19/new'
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
if os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/Phase2/"):
    shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject19/Phase2/")
add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new" , sor)
t = True
t2 = True
faz1 = True
faz2 = False
faz3 = False
faz4 = False
# THEME = 'Tan'
newpath = r'C:\Users\User\PycharmProjects\pythonProject19\new'
list_file_s = []
set_year=()
list_file_s2 = []
stri3 = ''

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
window = make_window()
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        if os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/Phase2/"):
            shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject19/Phase2/")
        break
    elif event =="Zip":
        if faz1==True:
            if Is_Unzp ==True:
                if not os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/Zip"):
                    os.makedirs("C:/Users/User/PycharmProjects/pythonProject19/Zip")
                dir_name = 'C:/Users/User/PycharmProjects/pythonProject19/Phase3'
                output_filename = "C:/Users/User/PycharmProjects/pythonProject19/Zip/zip"
                shutil.make_archive(output_filename, 'zip', dir_name)
                undo.clear()
                redo.clear()
                Is_Unzp = False

                if os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/dirname/"):
                    shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject19/dirname/")
                if os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/Phase3/"):
                    shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject19/Phase3/")
                list_dir = os.listdir(r'C:/Users/User/PycharmProjects/pythonProject19/new')
                for i1 in list_dir:
                    os.remove("C:/Users/User/PycharmProjects/pythonProject19/new/" + i1)
                treedata = sg.TreeData()
                window["_TREE_"].update(
                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                list_file_s = []
                Is_Unzp = False
            else:
                sg.popup('Nothing for Ziping', title='Warning', keep_on_top=True, text_color="Yellow")
        else:
            sg.popup('You Should Be In Phase 1', title='Error', keep_on_top=True, text_color="Red")
    elif (event == "Extract" or event == 'Ex' ) and values["-IN2-"] != '':
        try:
            if faz1 == True:
                if os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/Zip"):
                    shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject19/Zip")
                zip = zipfile.ZipFile(values["-IN-"])
                names = zip.namelist()
                j = 0
                for i in names:
                    i22 = i.split("/")
                    if(i22[-1] != ""):
                        list_file = []
                        list_file.append(i22[-1])
                        list_file_s.append(list_file)
                        list_file = []

                newpath = r'C:/Users/User/PycharmProjects/pythonProject19/dirname'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                newpath2 = r'C:/Users/User/PycharmProjects/pythonProject19/Phase3'
                if not os.path.exists(newpath2):
                    os.makedirs(newpath2)
                for member in zip.namelist():
                    zip.extract(member, 'dirname')
                for member in zip.namelist():
                    if Is_correct_year(member) == True:
                        zip.extract(member, 'Phase3')


                newpath = r'C:/Users/User/PycharmProjects/pythonProject19/new'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                for i in zip.namelist():
                    if (i[-1] == '/'):
                        source = "C:/Users/User/PycharmProjects/pythonProject19/dirname/" + i
                        destination = "C:/Users/User/PycharmProjects/pythonProject19/new/"
                        files = os.listdir(source)
                        for file in files:
                            if '.txt' in file or '.png' in file or '.zip' in file or '.pdf' in file or '.aiff' in file or '.jpeg' in file \
                                    or '.wav' in file or '.avl' in file or '.mkv' in file or '.mov' in file or '.jpg' in file or '.gif' in file \
                                    or '.mp4' in file:
                                file_name = os.path.join(source, file)
                                shutil.move(file_name, destination)
                source = "C:/Users/User/PycharmProjects/pythonProject19/dirname/"
                destination = "C:/Users/User/PycharmProjects/pythonProject19/new/"
                files = os.listdir(source)

                for file in files:
                    if '.txt' in file or '.png' in file or '.zip' in file or '.pdf' in file or '.aiff' in file or '.jpeg' in file \
                            or '.wav' in file or '.avl' in file or '.mkv' in file or '.mov' in file or '.jpg' in file or '.gif' in file \
                            or '.mp4' in file:
                        file_name = os.path.join(source, file)
                        shutil.move(file_name, destination)

                files = os.listdir(destination)
                tmp_deleting = []
                for i in list_file_s:
                    i2 = i[0]
                    name_year = i2.split('.')
                    if int(name_year[1]) > current_year:
                        os.remove("C:/Users/User/PycharmProjects/pythonProject19/new/" + i2)
                        tmp_deleting.append(i)
                for i in tmp_deleting:
                    list_file_s.remove(i)

                    # else:
                treedata = sg.TreeData()
                window["_TREE_"].update(
                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                window['-IN2-'].update('')
                Is_Unzp = True
            else :
                sg.popup('You Should Be In Phase 1', title='Error', keep_on_top=True,text_color="Red")

        except Exception as e:
            sg.popup_error(f'AN EXCEPTION OCCURRED!', e,keep_on_top=True)

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
                    if int(add[1]) <= current_year:
                        tmp_add = add[0] + "." + add[1] + "." + add[2]
                        if len(add) == 3 and (
                                add[2] == 'txt' or add[2] == 'png' or add[2] == 'jpg' or add[2] == 'mp4' or
                                add[2] == 'gif' or add[2] == 'jpeg' or add[2] == 'mov' or add[2] == 'mkv' or
                                add[2] == 'avl' or add[2] == 'aiff' or add[2] == 'wav' or add[2] == 'pdf') \
                                and add[1] != '':
                            tmp_add=Check_in_Add(tmp_add)
                            add = tmp_add.split('.')
                            add2.append(tmp_add)
                            if add2 in list_file_s:
                                sg.popup('"' + add2[0] + '"' + ' is already exist', keep_on_top=True)
                                pass

                            list_file_s.append(add2)
                            newfile = open(
                                "C:/Users/User/PycharmProjects/pythonProject19/new/" + add[0] + '.' + add[1] + '.' +
                                add[2],
                                'w')
                            if not os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/Phase3/"):
                                os.makedirs("C:/Users/User/PycharmProjects/pythonProject19/Phase3/")
                            tmp_str = os.listdir("C:/Users/User/PycharmProjects/pythonProject19/Phase3/")
                            newfile1 = open(
                                "C:/Users/User/PycharmProjects/pythonProject19/Phase3/" + tmp_str[0] + "/" + add[
                                    0] + '.' + add[1] + '.' + add[2],
                                'w')
                            treedata = sg.TreeData()
                            window["_TREE_"].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
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
                    else :
                        sg.popup('The selected year is greater than the current year', title='Error', keep_on_top=True, text_color="Red")

                window_add.close()
        else :
            sg.popup('You Should Be In Phase 1', title='Error', keep_on_top=True,text_color="Red")
    elif event == "Delete":
        if faz1 == True:
            if values["_TREE_"] != [] and faz1 == True:

                msg_box = sg.popup_yes_no('Are you sure you want to Delete this Files ?', keep_on_top=True)
                if msg_box == "Yes":
                    add2 = []
                    st = values["_TREE_"]
                    st = st[0].split('\\')
                    add2.append(st[1])
                    if add2 in list_file_s:
                        list_file_s.remove(add2)
                        tmp_str = os.listdir("C:/Users/User/PycharmProjects/pythonProject19/Phase3/")
                        if os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/Phase3/" +tmp_str[0]+'/'+ add2[0]):
                            os.remove("C:/Users/User/PycharmProjects/pythonProject19/Phase3/"+tmp_str[0]+'/' + add2[0])
                        os.remove("C:/Users/User/PycharmProjects/pythonProject19/new/" + add2[0])
                        treedata = sg.TreeData()
                        window["_TREE_"].update(
                            add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
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
    elif event=="Phase 2" and faz2 == False:
        if faz3 == True:
            window.close()
            window = make_window(THEME)
        faz2 = True
        faz1 = False
        faz3 = False
        faz4 = False
        faz = 'Phase2'
        if not os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/"+faz):
            os.makedirs("C:/Users/User/PycharmProjects/pythonProject19/"+faz)

        source = "C:/Users/User/PycharmProjects/pythonProject19/new/"
        destination = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/'
        files = os.listdir(source)
        for folder in files:  # add year in set_type
            if '.txt' in folder or '.png' in folder or '.zip' in folder or '.pdf' in folder or '.aiff' in folder or '.jpeg' in folder \
                    or '.wav' in folder or '.avl' in folder or '.mkv' in folder or '.mov' in folder or '.jpg' in folder or '.gif' in folder \
                    or '.mp4' in folder:
                file2 = folder.split('.')
                set_year.add(int(file2[1]))

        for i in set_year: # creat folders with date names
            newpath = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/'+ str(i)
            if not os.path.exists(newpath):
                os.makedirs(newpath)

        for file in files:# move file in new folders
            if '.txt' in file or '.png' in file or '.zip' in file or '.pdf' in file or '.aiff' in file or '.jpeg' in file \
                    or '.wav' in file or '.avl' in file or '.mkv' in file or '.mov' in file or '.jpg' in file or '.gif' in file \
                    or '.mp4' in file:
                file2 = file.split('.')
                file_name = os.path.join(source, file)
                shutil.copy(file_name, destination+ file2[1] + '/')

        for file in set_year:
            source = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/' + str(file)+'/'
            destination = "C:/Users/User/PycharmProjects/pythonProject19/"+faz
            files = os.listdir(source)
            set_type = ()
            set_type = set(set_type)

            for folder in files: # add types in set_type
                if '.txt' in folder or '.png' in folder or '.zip' in folder or '.pdf' in folder or '.aiff' in folder or '.jpeg' in folder \
                        or '.wav' in folder or '.avl' in folder or '.mkv' in folder or '.mov' in folder or '.jpg' in folder or '.gif' in folder \
                        or '.mp4' in folder:
                    file2 = folder.split('.')
                    set_type.add('.'+file2[2])

            for i in set_type: # creat folder with type name
                if '.txt' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/' + str(file)+'/text'
                elif '.pdf' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/' + str(file) + '/pdf'
                elif '.wav' in i or '.aiff' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/' + str(file) + '/voice'
                elif '.jpg' in i or '.png' in i or '.gif' in i or '.jpeg' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/' + str(file) + '/photo'
                else:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/' + str(file) + '/video'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)

            for i in files:
                if '.txt' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/' + str(file)+'/text/'
                elif '.pdf' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/' + str(file) + '/pdf/'
                elif '.wav' in i or '.aiff' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/' + str(file) + '/voice/'
                elif '.jpg' in i or '.png' in i or '.gif' in i or '.jpeg' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/' + str(file) + '/photo/'
                elif '.mp4' in i or '.mov' in i or '.mkv' in i or '.avl' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject19/"+faz+'/' + str(file) + '/video/'
                if '.txt' in i or '.png' in i or '.zip' in i or '.pdf' in i or '.aiff' in i or '.jpeg' in i \
                        or '.wav' in i or '.avl' in i or '.mkv' in i or '.mov' in i or '.jpg' in i or '.gif' in i \
                        or '.mp4' in i:
                    file2 = i.split('.')
                    file_name = os.path.join(source, i)
                    shutil.move(file_name, newpath)

        treedata = sg.TreeData()
        window["_TREE_"].update(add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/Phase2" , ''))

        window['-CUST MENUBAR-'].update('')

    elif (event == "Undo"):
        if faz1 == True:
            if len(undo) != 0:
                a = undo.pop()
                #save current state in redo
                if Current_Change != " ":
                    redo.append(Current_Change)
                tmp = a.split('.')
                while a ==Current_Change and len(undo) != 0:
                    a=undo.pop()
                    tmp=a.split('.')

                if tmp[0] == "default":
                    window.close()
                    window = make_window("DarkBlue")
                    Current_Change = "default.themeandsort"

                if tmp[0] == "settheme":
                    if (a != Current_Change):
                        window.close()
                        window = make_window(tmp[1])
                    settheme(tmp[1])
                    Current_Change = "settheme." + THEME

                elif tmp[0] == "sort" :
                        if tmp[1] == 'Newest To Oldest':
                            Current_Change="sort."+tmp[1]
                            Current_choice_for_sort = tmp[1]
                            sor = 'date2'
                            treedata = sg.TreeData()
                            window['_TREE_'].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                        elif tmp[1] == 'Oldest To Newest':
                            Current_Change="sort."+tmp[1]
                            Current_choice_for_sort = tmp[1]
                            sor = 'date1'
                            treedata = sg.TreeData()
                            window['_TREE_'].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                        elif tmp[1] == 'A-Z':
                            Current_Change="sort."+tmp[1]
                            Current_choice_for_sort = tmp[1]
                            sor = 'name1'
                            treedata = sg.TreeData()
                            window['_TREE_'].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                        elif tmp[1] == 'Z-A':
                            Current_Change="sort."+tmp[1]
                            Current_choice_for_sort = tmp[1]
                            sor = 'name2'
                            treedata = sg.TreeData()
                            window['_TREE_'].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                        elif tmp[1] == 'A_Z':
                            Current_Change="sort."+tmp[1]
                            Current_choice_for_sort = tmp[1]
                            sor = 'type1'
                            treedata = sg.TreeData()
                            window['_TREE_'].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                        elif tmp[1] == 'Z_A':
                            Current_Change="sort."+tmp[1]
                            Current_choice_for_sort = tmp[1]
                            sor = 'type2'
                            treedata = sg.TreeData()
                            window['_TREE_'].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
        else:
            sg.popup("Error","You Should Be In Phase 1", keep_on_top=True,text_color="Red")
    elif (event == "Redo"):
        if faz1 == True:
            if len(redo) !=0:
                for i in range(0,1):
                    a = redo.pop()
                    undo.append(Current_Change)
                    if len(redo) == 0:
                        undo.append(a)
                    tmp = a.split('.')
                    while a == Current_Change and len(undo) != 0:
                        a = redo.pop()
                        tmp = a.split('.')

                    if tmp[0] == "default":
                        window.close()
                        window = make_window("DarkBlue")
                        Current_Change = "default.themeandsort"
                    elif tmp[0] == "settheme":
                        if (a != Current_Change):
                            window.close()
                            window = make_window(tmp[1])
                        settheme(tmp[1])
                        Current_Change = "settheme." + THEME
                    elif tmp[0] == "sort":
                            if tmp[1] == 'Newest To Oldest':
                                Current_Change = "sort." + tmp[1]
                                Current_choice_for_sort = tmp[1]
                                sor = 'date2'
                                treedata = sg.TreeData()
                                window['_TREE_'].update(
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                            elif tmp[1] == 'Oldest To Newest':
                                Current_Change = "sort." + tmp[1]
                                Current_choice_for_sort = tmp[1]
                                sor = 'date1'
                                treedata = sg.TreeData()
                                window['_TREE_'].update(
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                            elif tmp[1] == 'A-Z':
                                Current_Change = "sort." + tmp[1]
                                Current_choice_for_sort = tmp[1]
                                sor = 'name1'
                                treedata = sg.TreeData()
                                window['_TREE_'].update(
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                            elif tmp[1] == 'Z-A':
                                Current_Change = "sort." + tmp[1]
                                Current_choice_for_sort = tmp[1]
                                sor = 'name2'
                                treedata = sg.TreeData()
                                window['_TREE_'].update(
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                            elif tmp[1] == 'A_Z':
                                Current_Change = "sort." + tmp[1]
                                Current_choice_for_sort = tmp[1]
                                sor = 'type1'
                                treedata = sg.TreeData()
                                window['_TREE_'].update(
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                            elif tmp[1] == 'Z_A':
                                Current_Change = "sort." + tmp[1]
                                Current_choice_for_sort = tmp[1]
                                sor = 'type2'
                                treedata = sg.TreeData()
                                window['_TREE_'].update(
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))

        else:
            sg.popup("Error", "You Should Be In Phase 1", keep_on_top=True, text_color="Red")
    elif event =='Set A Theme':
        # window.hide()
        event, values = sg.Window('Choose Theme',[[sg.Combo(sg.theme_list(), readonly=True, k='-THEME LIST-'), sg.OK(),sg.Cancel()]],keep_on_top=True).read(close=True)
        if event == 'OK':
            window.close()
            if len(undo) != 0 :
                tmp_undo = undo.pop()
                undo_tmp = tmp_undo.split('.')
                if Current_Change != " ":
                    cu = Current_Change.split('.')
                    if "settheme" != cu[0]:
                        undo.append(tmp_undo)
                        undo.append(Current_Change)
                    else:
                        undo.append(tmp_undo)
                        undo.append("settheme." + THEME)
            else:
                undo.append("settheme." + THEME)
            settheme(values['-THEME LIST-'])
            Current_Change = "settheme." + THEME
            if faz3==False:
                window = make_window(values['-THEME LIST-'])
            if faz3==True:
                window =make_window_phase3(values['-THEME LIST-'])
        # else:
            # window.un_hide()a
    elif event =='Default Theme':
        window.close()
        if len(undo) != 0:
            tmp_undo = undo.pop()
            undo_tmp = tmp_undo.split('.')
            if Current_Change != " ":
                cu = Current_Change.split('.')
                if "settheme" != cu[0]:
                    undo.append(tmp_undo)
                    undo.append(Current_Change)
                else:
                    undo.append(tmp_undo)
                    undo.append("settheme." + THEME)
        else:
            undo.append("settheme." + THEME)
        settheme("DarkBlue")
        Current_Change = "settheme."+THEME
        if faz3 == False :
            window = make_window()
        if faz3 ==True:
           window = make_window_phase3()
    elif event == 'Phase 1' and faz1 == False:
        if faz3 == True:
            window.close()
            window = make_window(THEME)
        faz1 = True
        faz2 = False
        faz3 = False
        faz4 = False
        set_year.clear()
        if os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/Phase2/"):
            shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject19/Phase2/")
        treedata = sg.TreeData()
        window["_TREE_"].update(add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new" , sor))

    elif event == 'A File':
        # window.hide()
        if faz1 == True:
            sg.theme(THEME)
            layout3 = [
                [sg.Text("Enter the name of file "), sg.Input(key="-IN3-", change_submits=False)],
                [sg.Button("Delete"), sg.T(""), sg.Button("Cancel")],
            ]
            window_delete = sg.Window('Delete', layout3, size=(340, 75), keep_on_top=True)
            while True:
                if t2:
                    event2, values2 = window_delete.read()
                else:
                    # window_delete.un_hide()
                    event2, values2 = window_delete.read()
                if event2 == sg.WIN_CLOSED:
                    window_delete.close()
                    # window.un_hide()
                    t2 = False
                    break
                elif event2 == "Exit" or event2 == 'Cancel':
                    window_delete['-IN3-'].update('')
                    window_delete.hide()
                    # window.un_hide()
                    t2 = False
                    break
                elif event2 == 'Delete' and values2['-IN3-'] != '':
                    add2 = []
                    add2.append(values2["-IN3-"])
                    if add2 in list_file_s:
                        list_file_s.remove(add2)
                        tmp_str = os.listdir("C:/Users/User/PycharmProjects/pythonProject19/Phase3/")
                        if os.path.exists(
                                "C:/Users/User/PycharmProjects/pythonProject19/Phase3/" + tmp_str[0] + '/' + add2[0]):
                            os.remove(
                                "C:/Users/User/PycharmProjects/pythonProject19/Phase3/" + tmp_str[0] + '/' + add2[0])
                        os.remove("C:/Users/User/PycharmProjects/pythonProject19/new/" + add2[0])
                        treedata = sg.TreeData()
                        window["_TREE_"].update(
                            add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
                        window_delete['-IN3-'].update('')
                        window_delete.hide()
                        t2 = False
                        add2 = []
                        # window.un_hide()
                        break
                    else:
                        sg.popup('there is no ' + add2[0] + ' in this folder!', title='error', keep_on_top=True)
            window_delete.close()
        else :
            sg.popup("Error","You Should Be In Phase 1", keep_on_top=True,text_color="Red")

    elif event == 'All Files':

        if faz1==True:
            if os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/Zip"):
                shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject19/Zip")
            if os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/dirname/"):
                shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject19/dirname/")
            if os.path.exists("C:/Users/User/PycharmProjects/pythonProject19/Phase3/"):
                shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject19/Phase3/")
            window.hide()
            msg_box = tk.messagebox.askquestion('Delete All Files', 'Are you sure you want to Delete All Files ?',
                                                icon='warning')
            if msg_box == 'yes':
                undo.clear()
                redo.clear()
                list_dir = os.listdir(r'C:/Users/User/PycharmProjects/pythonProject19/new')
                for i1 in list_dir:
                    os.remove("C:/Users/User/PycharmProjects/pythonProject19/new/" + i1)
                treedata = sg.TreeData()
                window["_TREE_"].update(
                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
            list_file_s = []
            window.un_hide()
        else :
            sg.popup("Error","You Should Be In Phase 1", keep_on_top=True,text_color="Red")


            # else:
            # tk.messagebox.showinfo('Return', 'You will now return to the application screen')

    elif event == 'Newest To Oldest' and faz1 == True:
        if len(undo) != 0:
            tmp_undo = undo.pop()
            undo_tmp = tmp_undo.split('.')
            if Current_Change != " ":
                cu = Current_Change.split('.')
                if "sort" != cu[0]:
                    undo.append(tmp_undo)
                    undo.append(Current_Change)
                else:
                    undo.append(tmp_undo)
                    undo.append("sort." + Current_choice_for_sort)
        else:
            undo.append("default.themeandsort")
            undo.append("sort." + Current_choice_for_sort)
        Current_choice_for_sort = event
        Current_Change= "sort." + Current_choice_for_sort
        sor = 'date2'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/User/PycharmProjects/pythonProject19/new" , sor))
    elif event == 'Oldest To Newest' and faz1 == True:
        if len(undo) != 0:
            tmp_undo = undo.pop()
            undo_tmp = tmp_undo.split('.')
            if Current_Change != " ":
                cu = Current_Change.split('.')
                if "sort" != cu[0]:
                    undo.append(tmp_undo)
                    undo.append(Current_Change)
                else:
                    undo.append(tmp_undo)
                    undo.append("sort." + Current_choice_for_sort)
        else:
            undo.append("default.themeandsort")
            undo.append("sort." + Current_choice_for_sort)
        Current_choice_for_sort = event
        Current_Change= "sort." + Current_choice_for_sort
        sor = 'date1'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
    elif event == 'A-Z' and faz1 == True:
        if len(undo) != 0:
            tmp_undo = undo.pop()
            undo_tmp = tmp_undo.split('.')
            if Current_Change != " ":
                cu = Current_Change.split('.')
                if "sort" != cu[0]:
                    undo.append(tmp_undo)
                    undo.append(Current_Change)
                else:
                    undo.append(tmp_undo)
                    undo.append("sort." + Current_choice_for_sort)
        else:
            undo.append("default.themeandsort")
            undo.append("sort." + Current_choice_for_sort)
        currentRootIndex = event
        Current_Change= "sort." + Current_choice_for_sort
        sor = 'name1'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/User/PycharmProjects/pythonProject19/new" , sor))
    elif event == 'Z-A' and faz1 == True:
        if len(undo) != 0:
            tmp_undo = undo.pop()
            undo_tmp = tmp_undo.split('.')
            if Current_Change != " ":
                cu = Current_Change.split('.')
                if "sort" != cu[0]:
                    undo.append(tmp_undo)
                    undo.append(Current_Change)
                else:
                    undo.append(tmp_undo)
                    undo.append("sort." + Current_choice_for_sort)
        else:
            undo.append("default.themeandsort")
            undo.append("sort." + Current_choice_for_sort)
        undo.append("sort." + Current_choice_for_sort)
        Current_choice_for_sort = event
        Current_Change= "sort." + Current_choice_for_sort
        sor = 'name2'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/User/PycharmProjects/pythonProject19/new" , sor))
    elif event == 'A_Z' and faz1 == True:
        if len(undo) != 0:
            tmp_undo = undo.pop()
            undo_tmp = tmp_undo.split('.')
            if Current_Change != " ":
                cu = Current_Change.split('.')
                if "sort" != cu[0]:
                    undo.append(tmp_undo)
                    undo.append(Current_Change)
                else:
                    undo.append(tmp_undo)
                    undo.append("sort." + Current_choice_for_sort)
        else:
            undo.append("default.themeandsort")
            undo.append("sort." + Current_choice_for_sort)
        Current_choice_for_sort = event
        Current_Change= "sort." + Current_choice_for_sort
        sor = 'type1'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/User/PycharmProjects/pythonProject19/new" , sor))
    elif event == 'Z_A' and faz1 == True:
        if len(undo) != 0:
            tmp_undo = undo.pop()
            undo_tmp = tmp_undo.split('.')
            if Current_Change != " ":
                cu = Current_Change.split('.')
                if "sort" != cu[0]:
                    undo.append(tmp_undo)
                    undo.append(Current_Change)
                else:
                    undo.append(tmp_undo)
                    undo.append("sort." + Current_choice_for_sort)
        else:
            undo.append("default.themeandsort")
            undo.append("sort." + Current_choice_for_sort)
        Current_choice_for_sort = event
        Current_Change= "sort." + Current_choice_for_sort
        sor = 'type2'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))

    elif event =="Refresh":

        window['-serch-'].update('')
        values['-serch-'] = ''
        event = "Search"

    if event == 'Search' :
        exist2 = False
        if values['-serch-'] == '':
            treedata = sg.TreeData()
            if faz1:
                window["_TREE_"].update(
                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/new", sor))
            elif faz2:
                window["_TREE_"].update(
                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject19/Phase2", sor))
            exist2 = True
        list_file_s2 = []
        exist = False
        list_file_s2.append(values['-serch-'])
        for i in list_file_s:
            i = i[0].split('.')
            # list_file_s2 = str(values['-serch-']).split('.')
            if values['-serch-'] == i[0]:
                f2 = i[0] + '.' + i[1] + '.' + i[2]
                exist = True
        if exist and not exist2:
            f2 = f2.split('.')
            treedata = sg.TreeData()
            if f2[2] == 'pdf':
                treedata.Insert('', values['-serch-'], text=f2[0], values=[f2[1] + '', f2[2] + ''], icon=pdf_icon)
            elif f2[2] == 'txt':
                treedata.Insert('', values['-serch-'], text=f2[0], values=[f2[1] + '', f2[2] + ''], icon=txt_icon)
            elif f2[2] == 'png' or f2[2] == 'jpg' or f2[2] == 'gif' or f2[2] == 'jpeg':
                treedata.Insert('', values['-serch-'], text=f2[0], values=[f2[1] + '', f2[2] + ''], icon=png_icon)
            elif f2[2] == 'mp4' or f2[2] == 'mov' or f2[2] == 'mkv' or f2[2] == 'avl':
                treedata.Insert('', values['-serch-'], text=f2[0], values=[f2[1] + '', f2[2] + ''], icon=mp4_icon)
            elif f2[2] == 'aiff' or f2[2] == 'wav':
                treedata.Insert('', values['-serch-'], text=f2[0], values=[f2[1] + '', f2[2] + ''], icon=music_icon)
            window['_TREE_'].update(treedata)
        elif not exist and not exist2:
            sg.popup('"' + values['-serch-'] + '"' + ' is not exist', keep_on_top=True)

