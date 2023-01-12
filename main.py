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
Is_Unzp = False
if os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/Phase3/"):
    Is_Unzp = True
stack=[]
stack_check=[]
stack_index=[]
Par=[]
inorder_list_phase3=[]
postorder_list_phase3=[]
preorderlist_phase3 =[]
for_faz3 = []
def Is_correct_year(name = "") :
    if name[len(name)-1]=="/":
        return True
    elif name.find('/') != -1:
        tmp_name = name.split('/')
        filename = tmp_name[len(tmp_name) - 1]
        check_year_def = filename.split('.')
        if int(check_year_def[1]) > current_year:
            return False
        else:
            return True
    elif name.find('.') !=-1:
        check_year_def = name.split('.')
        if int(check_year_def[1]) > current_year:
            return False
        else:
            return True
    else:
        return True


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

# Utility function to create a new tree node
def newNode(key=Node):
    temp = Node(key)
    return temp

def postorder(root):
    global currentRootIndex
    global stack
    global postorderTraversal
    postorderTraversal.clear()
    while (root != None or len(stack) != 0):
        if (root != None):

            stack.append(Pair(root, currentRootIndex))
            currentRootIndex = 0

            if (len(root.children) >= 1):
                root = root.children[0]
            else:
                root = None
            continue

        temp = stack.pop()
        postorderTraversal.append(temp.node.key)

        while (len(stack) != 0 and temp.childrenIndex ==
               len(stack[-1].node.children) - 1):
            temp = stack[-1]
            stack.pop()

            postorderTraversal.append(temp.node.key)

        if (len(stack) != 0):
            root = stack[-1].node.children[temp.childrenIndex + 1]
            currentRootIndex = temp.childrenIndex + 1

    return postorderTraversal

def preorder(root):
    Stack = deque([])
    Par =newNode()

    Preorder = []
    Preorder.append(root.key)
    Stack.append(root)
    while len(Stack) > 0:

        flag = 0

        if len((Stack[len(Stack) - 1]).children) == 0:
            X = Stack.pop()

        else:
            Par = Stack[len(Stack) - 1]

        if Par != None:
            for i in range(0, len(Par.children)):
                if Par.children[i] !=None:
                    if Par.children[i].key not in Preorder:
                        flag = 1
                        Stack.append(Par.children[i])
                        Preorder.append(Par.children[i].key)
                        break;

        if flag == 0:
            if len(Stack):
                Stack.pop()

    return (Preorder)
def inorder(node):
    if node == None:
        return

    # Total children count
    total = len(node.children)
    if total %2==0:
        index=int(total/2)
        for i in range(index):
            ab=inorder(node.children[i])
        inorder_list_phase3.append(node.key)
        index=total - int(total/2)
        for j in range(index,total):
            ab=inorder(node.children[j])



    elif total!=1:
        index= int(total /2)+1
        for i in range(index):
            ab=inorder(node.children[i])
        inorder_list_phase3.append(node.key)
        index = total-(int(total /2))
        for j in range (index,total):
            ab=inorder(node.children[j])
    else :
        index = int(total / 2) + 1
        for i in range(index):
            ab = inorder(node.children[i])
        inorder_list_phase3.append(node.key)

def Search(root,value):
    if (root == None):
        return;

    # using queue
    q = []  # Create a queue
    q.append(root);  # Enqueue root
    while (len(q) != 0):

        n = len(q);

        # If this node has childrenren
        while (n > 0):

            # Dequeue an item from queue
            p = q[0]
            q.pop(0);
            if p != None:
                if value == p.key:
                    return p

            # Enqueue all children of the dequeued item
            if p!=None:
                for i in range(len(p.children)):
                    if p != None:
                        q.append(p.children[i]);

                n -= 1


    if len(q)==0:
        return

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



if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'
pdf_icon = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAABEklEQVR4nOXUsUtCURTHccf6H4LgUVK74FpbQ+GkT0xwqGzSQcFCekEuEhSRSJO+RYR6ZIRQlE8kDFrCyaGWZvFv8MU3XndwsOw+VII68FvO5X7gnAvX5ZpkoSoaqmIOTWheJzI7JQsaqArDYlV1WF8w8c9MjwXsvb1gNa7kUCTBXrcjhyIzcrOK9fzwmXc9AwElPxL4RYy/AEa9kEtCdhOCc3ASh+wWhNygBcTZftABuOeH5i3clOA0Aa9tKB/BeU70ihnY9TkEn0yoV+A4Bu0WbHhEzwYf7+Bw2yHYuIadNXHJBlOrUDMEaI8dXnQAJlbgLN1fvHkJ9xcQX4bCAcSWfvuV1f8Eaj9+sIPRvgXHUR/MH2414AmKSAAAAABJRU5ErkJggg=='
error_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAB9JREFUOE9jZKAQMFKon2HUAIbRMGAYDQNQPhr4vAAAJpgAEX/anFwAAAAASUVORK5CYII='
#png_icon2 = b'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAAC/klEQVR4nLXRa0hTYRzH8QcTbxxdnjUvueVQz3SaGpWX2UUN7UKCpdB8Y1H0Qiu0UgkldWqZ03RKoC9EtNKKiFQKWczEF5VJF3vRG19EpuKYaW5Tsiu/OJtOTZ3bygNfznM45/w/50LIoo3D4XwQCoWfrYmiqBl3d66MWLoJBIJhvV4Pa5KmpX0JChJ/5fJ4ZeuKtN17gIT9B7Q0TV9bN+TO/Yd4NfDeMohFdDqd1Uj2hVzIqxQol1+Hl5f3Dy6PJzOLTE1NWYUolcpfBQUFP/Pz83/Px+fztWaRiYkJw80qlQrx8fEWp1KpTHBTU1ODWUSj0YD9ZPX1DahR1GL223dDY2Nq0/rv2OsaGxtNiEQieW0WUavVmJicRFm5HNU1CsOQtwPv4ORGobGl2SKksLCwbU1EMz5uQvTTM2AiwkFaMkFHiPGoq8sw+NPwCHT66RURds6ayMjoqAk5m3cRLjnJIH1lIMp8cMMY3LrdCk9GiKiEOGh1etuQj0NDBuSYNA30rlCQF6VGpK8MpCMXzh40SFEqHM8nIToxDhUVctsRZzcKpDNvAeibq/UcqGAhyM0zcMg+DIrjZjviknloOdBnzK7hNFzDA0DuZsFJutt2xDF37l+skn1VOlwjg2B/ap/tiH1iOMilZLNt2O4H+42UbYiyuxeXi2RrJiu9grq6OgwODlqGuG2itYJgEfhiBlvEoiUJQwLhuzVoxQShgUti56yKuDJ87ban1SDtOSu2o0cBTr/c7H9iY+dYh+wVg/h7gkglICmRcK1Ih3dqLBwqj4MEbgY5GP4fEJE3SGEKiJ8HSIwIJIRv2DsdjQZTchLMjSw4P7MC4UWFaJYhjBdI+h6Q6nQjIuAa90d2gmQkGB7CrvYEfLpKENZdBcnzevNIVF3Om4gexfI3mV/HiEBykkBixSAZiSABXiA+NEhzpumaiN7atT+X78sahKoqwTwpN+TfUbyw7pSBUV41xh63FyPgcanpfGh3FXz7FeYRZw9aTTH82X+NnbN48B+XfV3UxQsnKAAAAABJRU5ErkJggg=='
png_icon = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAABMElEQVR4nM3Uz0vCYBzH8f19RqduRXhOyEMEmYd+EREh/djJyIWty2DUKIl+YBaFW6RBDBlqECJGaCQxNU/1iafRltDXYI3wC294+D7PXsdxXM9PRJCje0m15EURQY5yvKjE4dHwohLvAIt1d5Hgwb27/h88LAGpCpCuAidlZ8/ObMfu2JtfQa0GZOtA4dXJaAKZZyt2/n7HdlqtC6ibQK5hPb6utqHcPiLfeneQVieYM61vSJA9uiybWNrV4V84xvD8ESY3r6BWmji9e8KipGFoSsLa/g2MxpsNk+D0duYT+amBkARfMAbfqJV/TkZCf+gOUthXgzMJ9I9t2WhfMIZZ8YIGQ0IWgdVzBJZTZCMrZxhfT2NiQ7UjwfDOi6tIMGm0XUWCfx2egZ7/vnp+PgAfTTupXBvuHgAAAABJRU5ErkJggg=='
# png_icon = b'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAABj0lEQVR4nO3TS0sCURgGYH9JyxbtgiBql00XdZLgzCBmLbJNi0g0K4IWrYIIiYiEBCGCFtEiIn+AjougKDAhwkrtIogaGd5Ccd4wMUOZsUGHCHrhXZ7v4ZzDp1D8RswcZq1eJM0cILXW0jkPZkQBkxs9Vi8KvjiQyEmvLw5YOeRNHLqFb+HBvN2HLJqI3YdsaY4YsuzwI9cM4vAjV5rzj8j3XJkCwEWA4JuMiP2qvANzXiCakQlZPa8uW+BVJuQuWb6NKwTwcj2X1Dj+HPL49Iz1jW0cHp2A5/nWI/ehMIh+EpSG+WwJq0ANEZMXxoMA0lIAqga6jOHF4kanQiwAIqlUGtForA4Ihh5Axox1QKW2TTuKxWJE0SinZxcJLTOBAZqFc3f/CwiFxYFK12xbGVFAOcx2qEf1/PdDO8493ARuwRimGgLVslpBpF/DLP18ECNYpYZZEEHISisQSkMWhRGatbQEocm0MKLStQ+OsPlmgCGt7p2i2TbRz+9Tk16ajLtoYriW3vFjSkW6aod+AC+SdEwCtiWhAAAAAElFTkSuQmCC'
#mp4_icon= b'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAABxklEQVR4nOXWTUsbURQGYFf9F7ZduHJXkr0UJC6E4kJF6EasiqhZCAU/KHUnBlKjiDOoBKMSlURRYxQVlWQMET8maGbOvXco/Reu3LwyI4iisXNjRMEDL8zAmfPce2cWU1b2GsU5/0xkZojMs/8ltprUg8rsF2mEiOoYM+EmM9EVNLb2XQWVac+LItX13fJQMUi1LCSDLMQTaGofuE3Hz6HL6bn1ipIi7JHYz79DZD+lYXBYcZ39lCaPGEYeWibrOoaRl0f0XA6rG9uuo+dy8oi9usBYGMMuEhgLO/1v58V7Rv999KlC/THPU8XGpwrVG/xbXhDxhqx+b8hCCdJfeCch69fd5kCSoWVeoEYViBwQGsMC8UPCkkZonuNOT3CT4evEfcSe4xpJZBk03UQ0Tc55dy5yLKQZ/EscySNCQ1ggkaUHO5FGNo8Ie6eEC/MG2TshLKYJEzsMsUOGP1scPTH+PMQ+rm9TAucGOYg92L73KRZSZ4TjcxOneRNV40Uiyi5D7aRwrpczhO8RgaENdm/VbVGO32syOxmx/KX4ujwjlr8gUjlofuiNs67IAenFpjfOuuw5BRG7ZP5WHkmGiD49CbxUXQPC1KVWbctzLAAAAABJRU5ErkJggg=='
mp4_icon = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAACaElEQVR4nOXU3UuTYRjHcfFf0Ck5oyRrzoQeiKIaW7NtokJakNCbkbCyBjozxMpsWRsx6VGGL4T0GFZzU6dzpAfDcmEYDRwZtlAhcAmRe3euclD+Ylube3KF4UEHXfA9u+8P93VyJyT8n5M96CjK0tt7NxJL7zgcBdkDC6NsvR0biei3j8aCpsapJXxbAURG17qR4NnvK0DrpB8irdNEA8+99GJ4fhn7h53rwrL1duQbXDDZAmgY9eH4QxcdzBm0Y++QY92v4/Q5UahxoUzrgbjLDQnlpoPNVj+Ckz8SXpmlnsO2lkmw9QtrsH06Bwo0LlQNekN3hie+4mqHlw6Wjnmgfv8l9Mrt1AwYxU1IylMgTaIFe2AVJfodEGqdKHnshlTtxbg1gE6DH8r2RTq4+4kDxc/cYD2YBaOIRJLwdjRmuRpZ/Z+Qo/kIvmIWBS0fcLbLjWrKg3bdElT3l9DW+guoehdemXORQrKgYU1bL/SAX/MGggoLBJUWnGi0oanPF7pjfrWMTpWPDh412EBqxrGlUI7k3Bu00vLugFv+IoxFqrSggpyHeSIAfc9ndDfFgJn3pszZJ1U4UkUhNbceDP71aEyRYi32M5HUgrZHdmg7/OglY8BNJSq3knoaXrm0GSm8a6GYQjm458fiYsHK5NbQnZHni9CR/hjwGOnhnLqLS0odNgvqkMKtBVNwC7zy32PBCqpfg+y2oUxhRW29bSYKpp9um07l1CBS+qGb4P3hZfE6Uzs9vfrdyGSJOy4bMiLtlA6xd0mNRLz2SIzEAYmROBhMbCRKrrzNFNfNZchkSPy7P+5fzQ9jZbF6W9VYzQAAAABJRU5ErkJggg=='
music_icon = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAC+UlEQVR4nNXS+09SYRgHcLR/od/6pa3a8of63ZUaYKiJmZXVRC01rZbO5VQKNcnbLMsylpdpdtHlpbWurNtSqym5QknAgJIjKCAIhobA8Yjf5rE0drSf69mevefZ8+zznvfdy2L9VwEWAsZ5eXxX7P58HAgVIoMjRF64EGU8Ia5ECiGJFKImUoiLkUIU7c5HZng0WKyANbERTskjW9QpzMVxQSXtAnWGC6qEB+p6FKjb0aDu8UG1RoNq2APf5QigYDdwgv1wVVS5U8InwoswkSWCd2gApF4D0qgBadKCtGpB2nUgp3QgHTqQkzp4DQr8qD0JZHOBhDA+A1SH1hQQXBHcQ2qsFfMzDpDGlb5Xr4Avhwsk7SpggiE14m/cAngJox/ifN4Fe0UVHCnJ8MSx4UqPWe7NTRD0tUAQJmYeOUQi/so5zwBHEkphjsjGRFQ6LPFpsB477g9mcoDDq4Cfd9SJNewSeAiTHzic0wrbCzncBiuwsABL04MV0KwHlcaG7wCbCQ7uaBQrQy/BrTf7gepGmX99p2v5220ygEiNh0EgqGSA8uAWcS+3Ds7RST+gt3nYr37X9nHlfk0mvMzKxcvj5RIGKOU9vtTCl8JOTPsBPdVj9Gq3z+JmvRwVxT3LPZvFhitnm9CUdaeZAbZEvG2oDVNg8qubHtbedqNjgwtdyUsbvOk3IbF8EKLawWVw3OrEybLXKMuTdjDAu6Hyew2bLHCo5uhhaa4TVZt/oK9xhq7nfQsYMH7HtGepvxjEpAu8GwpkF75/xgDbt6kftK3zwdDnoYd98wuYslL4W/SbZxDUOYqUUvkrBvhko+584/p51B9yQDs4ixG9G9qxWWhMS6myuaD8I2WmacQ9HUHQfSNOn+tnPhuwENi8xWIuDJlFxpEp7Mu3IFhixPZbBILa9XRu/bXS2TlKY3uvqszFxQhkgL/R+hD1hZL9mu6cUypZatGQ7KhY9SlRpNPEXPsyHFutUh6sUg4IKoc+JJUpuhf/bE3sn42fD3USo+60klMAAAAASUVORK5CYII='
txt_icon = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAABZ0lEQVR4nGNgQANXrlzhuXTpkiAu/OjRMU4GYsGNG5f0rl69/PfatSv/ceFpc5d9bOqZ5kOUgdevX3bAZxgI905d8N8/ruRvS98sf6oZ6BKSQ5yh14kwcNnqjf9L6vvBuK5j6tctW3YrUWQgOr5+/bID/Q1cvWHb/0kzF+PFIDVEG3j23Nn/h44cw4tBaog2cOHydf/rO6bhxYuWr6dzGP63t2d5lxFZ+7y56gAp+F1GZC1IL4aBn4Od9D4HufwnCwc76WEY+MXf1QCm4GOM//+7u7f9v3Xs0P+nU7r/P549GYyfTu4Ci4HkQGpg6r/4uxrgNRCE3xSm/38ya/L/z8Gu/+9tXvv/3qa1YDZIDCSHrPYLKQZ+ivL5f2fXVjD+GOVLvoEfUsL/v6opBGt+XZUPxm8K08BiIDmCBn7ysRf5HOp27GOk5zVSMEgPSC/WpENMAYuMQWpBerAaBgOEqgBkDFKLbgAAQ0AolZ/f/oEAAAAASUVORK5CYII='
treedata = sg.TreeData()
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
def add_files_in_folder(parent, dirname,sor):
    files = os.listdir(dirname)
    dicr2 = {}
    dicr = []
    sorted_dicr = []
    if sor != '':
        for i in files:
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
            for_faz3.append(f)
            for_faz3.append('{')

            treedata.Insert(parent, fullname, f, values=['  ','File folder'] , icon=folder_icon)
            add_files_in_folder(fullname, fullname , sor)
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
                 max_col_width=30,
                 expand_x=True,
                 change_submits=True,
                 expand_y=True,row_height=20,justification='mid', col0_heading='Name', key='_TREE_', show_expanded=False, background_color='white',
                 header_text_color='black', text_color='black',right_click_menu=['&Right', ["Refresh","Add","Delete","Extract",'&Sort',['&Name', ['A-Z', 'Z-A'], 'Date', ['Newest To Oldest', 'Oldest To Newest'], 'Type',
                  ['A_Z', 'Z_A']],'&Theme', ['Set A Theme', 'Default Theme'],"&Options",["Zip","Undo","Redo"],'Exit']]), ],
        [sg.Text("Choose a ZipFile: ",key='ch' , visible=True), sg.Input(key="-IN2-", change_submits=True, size=(45),visible=True ,text_color="Black"),
         sg.FileBrowse (key="-IN-", file_types=(('Zip Files', '*.zip'), ('All Files', '*.*')),size=(7,1),visible=True)
            ,sg.Button("Extract" , key='Ex' ,visible=True,size=(7,1)),sg.Button('Save',size=(7,1))],
    ]
    layout = [
        [sg.Column(file_list_column), ]
    ]
    window = sg.Window("File Manager", layout, use_custom_titlebar=True,
              keep_on_top=True ,resizable=True,finalize=True)
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
                 max_col_width=30,
                 expand_x=True,
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
              keep_on_top=True ,resizable=True,finalize=True)
    window["_TREE_"].expand(True, True)
    return window
new_folder = r'C:/Users/User/PycharmProjects/pythonProject18/new'
if not os.path.exists(new_folder):
    os.makedirs(new_folder)
if os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/Phase2/"):
    shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject18/Phase2/")
add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new" , sor)
t = True
t2 = True
faz1 = True
faz2 = False
faz3 = False
faz4 = False
newpath = r'C:\Users\User\PycharmProjects\pythonProject18\new'
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
        if os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/Phase2/"):
            shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject18/Phase2/")
        break
    elif event =="Zip":
        if faz1==True:
            if Is_Unzp ==True:
                if not os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/Zip"):
                    os.makedirs("C:/Users/User/PycharmProjects/pythonProject18/Zip")
                dir_name = 'C:/Users/User/PycharmProjects/pythonProject18/Phase3'
                output_filename = "C:/Users/User/PycharmProjects/pythonProject18/Zip/zip"
                shutil.make_archive(output_filename, 'zip', dir_name)
                undo.clear()
                redo.clear()
                Is_Unzp = False

                if os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/dirname/"):
                    shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject18/dirname/")
                if os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/Phase3/"):
                    shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject18/Phase3/")
                list_dir = os.listdir(r'C:/Users/User/PycharmProjects/pythonProject18/new')
                for i1 in list_dir:
                    os.remove("C:/Users/User/PycharmProjects/pythonProject18/new/" + i1)
                treedata = sg.TreeData()
                window["_TREE_"].update(
                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                list_file_s = []
                Is_Unzp = False
            else:
                sg.popup('Nothing for Ziping', title='Warning', keep_on_top=True, text_color="Yellow")
        else:
            sg.popup('You Should Be In Phase 1', title='Error', keep_on_top=True, text_color="Red")
    elif (event == "Extract" or event == 'Ex' ) and values["-IN2-"] != '':
        try:
            if faz1 == True:
                if os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/Zip"):
                    shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject18/Zip")
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

                newpath = r'C:/Users/User/PycharmProjects/pythonProject18/dirname'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                newpath2 = r'C:/Users/User/PycharmProjects/pythonProject18/Phase3'
                if not os.path.exists(newpath2):
                    os.makedirs(newpath2)
                for member in zip.namelist():
                    zip.extract(member, 'dirname')
                for member in zip.namelist():
                    if Is_correct_year(member) == True:
                        zip.extract(member, 'Phase3')


                newpath = r'C:/Users/User/PycharmProjects/pythonProject18/new'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                for i in zip.namelist():
                    if (i[-1] == '/'):
                        source = "C:/Users/User/PycharmProjects/pythonProject18/dirname/" + i
                        destination = "C:/Users/User/PycharmProjects/pythonProject18/new/"
                        files = os.listdir(source)
                        for file in files:
                            if '.txt' in file or '.png' in file or '.zip' in file or '.pdf' in file or '.aiff' in file or '.jpeg' in file \
                                    or '.wav' in file or '.avl' in file or '.mkv' in file or '.mov' in file or '.jpg' in file or '.gif' in file \
                                    or '.mp4' in file:
                                file_name = os.path.join(source, file)
                                shutil.move(file_name, destination)
                source = "C:/Users/User/PycharmProjects/pythonProject18/dirname/"
                destination = "C:/Users/User/PycharmProjects/pythonProject18/new/"
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
                        os.remove("C:/Users/User/PycharmProjects/pythonProject18/new/" + i2)
                        tmp_deleting.append(i)
                for i in tmp_deleting:
                    list_file_s.remove(i)

                treedata = sg.TreeData()
                window["_TREE_"].update(
                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
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
                                "C:/Users/User/PycharmProjects/pythonProject18/new/" + add[0] + '.' + add[1] + '.' +
                                add[2],
                                'w')
                            if not os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/Phase3/"):
                                os.makedirs("C:/Users/User/PycharmProjects/pythonProject18/Phase3/")
                            tmp_str = os.listdir("C:/Users/User/PycharmProjects/pythonProject18/Phase3/")
                            newfile1 = open(
                                "C:/Users/User/PycharmProjects/pythonProject18/Phase3/" + tmp_str[0] + "/" + add[
                                    0] + '.' + add[1] + '.' + add[2],
                                'w')
                            treedata = sg.TreeData()
                            window["_TREE_"].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                            window_add['-IN2-'].update('')
                            newfile.close()
                            newfile1.close()
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
                        tmp_str = os.listdir("C:/Users/User/PycharmProjects/pythonProject18/Phase3/")
                        if os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/Phase3/" +tmp_str[0]+'/'+ add2[0]):
                            os.remove("C:/Users/User/PycharmProjects/pythonProject18/Phase3/"+tmp_str[0]+'/' + add2[0])
                        os.remove("C:/Users/User/PycharmProjects/pythonProject18/new/" + add2[0])
                        treedata = sg.TreeData()
                        window["_TREE_"].update(
                            add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
            else:
                sg.popup('You Should Choose A File For Deleting', title='Warning', keep_on_top=True,text_color="Yellow")
        else:
            sg.popup('You Should Be In Phase 1', title='Error', keep_on_top=True,text_color="Red")

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
        if not os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/"+faz):
            os.makedirs("C:/Users/User/PycharmProjects/pythonProject18/"+faz)

        source = "C:/Users/User/PycharmProjects/pythonProject18/new/"
        destination = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/'
        files = os.listdir(source)
        for folder in files:
            if '.txt' in folder or '.png' in folder or '.zip' in folder or '.pdf' in folder or '.aiff' in folder or '.jpeg' in folder \
                    or '.wav' in folder or '.avl' in folder or '.mkv' in folder or '.mov' in folder or '.jpg' in folder or '.gif' in folder \
                    or '.mp4' in folder:
                file2 = folder.split('.')
                # add year in set_type
                set_year.add(int(file2[1]))

        for i in set_year: # creat folders with date names
            newpath = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/'+ str(i)
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
            source = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/' + str(file)+'/'
            destination = "C:/Users/User/PycharmProjects/pythonProject18/"+faz
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
                    newpath = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/' + str(file)+'/text'
                elif '.pdf' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/' + str(file) + '/pdf'
                elif '.wav' in i or '.aiff' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/' + str(file) + '/voice'
                elif '.jpg' in i or '.png' in i or '.gif' in i or '.jpeg' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/' + str(file) + '/photo'
                else:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/' + str(file) + '/video'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)

            for i in files:
                if '.txt' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/' + str(file)+'/text/'
                elif '.pdf' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/' + str(file) + '/pdf/'
                elif '.wav' in i or '.aiff' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/' + str(file) + '/voice/'
                elif '.jpg' in i or '.png' in i or '.gif' in i or '.jpeg' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/' + str(file) + '/photo/'
                elif '.mp4' in i or '.mov' in i or '.mkv' in i or '.avl' in i:
                    newpath = "C:/Users/User/PycharmProjects/pythonProject18/"+faz+'/' + str(file) + '/video/'
                if '.txt' in i or '.png' in i or '.zip' in i or '.pdf' in i or '.aiff' in i or '.jpeg' in i \
                        or '.wav' in i or '.avl' in i or '.mkv' in i or '.mov' in i or '.jpg' in i or '.gif' in i \
                        or '.mp4' in i:
                    file2 = i.split('.')
                    file_name = os.path.join(source, i)
                    shutil.move(file_name, newpath)

        treedata = sg.TreeData()
        window["_TREE_"].update(add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/Phase2" , ''))

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
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                        elif tmp[1] == 'Oldest To Newest':
                            Current_Change="sort."+tmp[1]
                            Current_choice_for_sort = tmp[1]
                            sor = 'date1'
                            treedata = sg.TreeData()
                            window['_TREE_'].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                        elif tmp[1] == 'A-Z':
                            Current_Change="sort."+tmp[1]
                            Current_choice_for_sort = tmp[1]
                            sor = 'name1'
                            treedata = sg.TreeData()
                            window['_TREE_'].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                        elif tmp[1] == 'Z-A':
                            Current_Change="sort."+tmp[1]
                            Current_choice_for_sort = tmp[1]
                            sor = 'name2'
                            treedata = sg.TreeData()
                            window['_TREE_'].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                        elif tmp[1] == 'A_Z':
                            Current_Change="sort."+tmp[1]
                            Current_choice_for_sort = tmp[1]
                            sor = 'type1'
                            treedata = sg.TreeData()
                            window['_TREE_'].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                        elif tmp[1] == 'Z_A':
                            Current_Change="sort."+tmp[1]
                            Current_choice_for_sort = tmp[1]
                            sor = 'type2'
                            treedata = sg.TreeData()
                            window['_TREE_'].update(
                                add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
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
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                            elif tmp[1] == 'Oldest To Newest':
                                Current_Change = "sort." + tmp[1]
                                Current_choice_for_sort = tmp[1]
                                sor = 'date1'
                                treedata = sg.TreeData()
                                window['_TREE_'].update(
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                            elif tmp[1] == 'A-Z':
                                Current_Change = "sort." + tmp[1]
                                Current_choice_for_sort = tmp[1]
                                sor = 'name1'
                                treedata = sg.TreeData()
                                window['_TREE_'].update(
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                            elif tmp[1] == 'Z-A':
                                Current_Change = "sort." + tmp[1]
                                Current_choice_for_sort = tmp[1]
                                sor = 'name2'
                                treedata = sg.TreeData()
                                window['_TREE_'].update(
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                            elif tmp[1] == 'A_Z':
                                Current_Change = "sort." + tmp[1]
                                Current_choice_for_sort = tmp[1]
                                sor = 'type1'
                                treedata = sg.TreeData()
                                window['_TREE_'].update(
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                            elif tmp[1] == 'Z_A':
                                Current_Change = "sort." + tmp[1]
                                Current_choice_for_sort = tmp[1]
                                sor = 'type2'
                                treedata = sg.TreeData()
                                window['_TREE_'].update(
                                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))

        else:
            sg.popup("Error", "You Should Be In Phase 1", keep_on_top=True, text_color="Red")
    elif event =='Set A Theme':
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
        if os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/Phase2/"):
            shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject18/Phase2/")
        treedata = sg.TreeData()
        window["_TREE_"].update(add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new" , sor))

    elif event == 'A File':
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
                    event2, values2 = window_delete.read()
                if event2 == sg.WIN_CLOSED:
                    window_delete.close()
                    t2 = False
                    break
                elif event2 == "Exit" or event2 == 'Cancel':
                    window_delete['-IN3-'].update('')
                    window_delete.hide()
                    t2 = False
                    break
                elif event2 == 'Delete' and values2['-IN3-'] != '':
                    add2 = []
                    add2.append(values2["-IN3-"])
                    if add2 in list_file_s:
                        list_file_s.remove(add2)
                        tmp_str = os.listdir("C:/Users/User/PycharmProjects/pythonProject18/Phase3/")
                        if os.path.exists(
                                "C:/Users/User/PycharmProjects/pythonProject18/Phase3/" + tmp_str[0] + '/' + add2[0]):
                            os.remove(
                                "C:/Users/User/PycharmProjects/pythonProject18/Phase3/" + tmp_str[0] + '/' + add2[0])
                        os.remove("C:/Users/User/PycharmProjects/pythonProject18/new/" + add2[0])
                        treedata = sg.TreeData()
                        window["_TREE_"].update(
                            add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
                        window_delete['-IN3-'].update('')
                        window_delete.hide()
                        t2 = False
                        add2 = []
                        break
                    else:
                        sg.popup('there is no ' + add2[0] + ' in this folder!', title='error', keep_on_top=True)
            window_delete.close()
        else :
            sg.popup("Error","You Should Be In Phase 1", keep_on_top=True,text_color="Red")

    elif event == 'All Files':

        if faz1==True:
            if os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/Zip"):
                shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject18/Zip")
            if os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/dirname/"):
                shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject18/dirname/")
            if os.path.exists("C:/Users/User/PycharmProjects/pythonProject18/Phase3/"):
                shutil.rmtree("C:/Users/User/PycharmProjects/pythonProject18/Phase3/")
            window.hide()
            msg_box = tk.messagebox.askquestion('Delete All Files', 'Are you sure you want to Delete All Files ?',
                                                icon='warning')
            if msg_box == 'yes':
                undo.clear()
                redo.clear()
                list_dir = os.listdir(r'C:/Users/User/PycharmProjects/pythonProject18/new')
                for i1 in list_dir:
                    os.remove("C:/Users/User/PycharmProjects/pythonProject18/new/" + i1)
                treedata = sg.TreeData()
                window["_TREE_"].update(
                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
            list_file_s = []
            window.un_hide()
        else :
            sg.popup("Error","You Should Be In Phase 1", keep_on_top=True,text_color="Red")




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
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/User/PycharmProjects/pythonProject18/new" , sor))
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
        window['_TREE_'].update(add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
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
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/User/PycharmProjects/pythonProject18/new" , sor))
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
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/User/PycharmProjects/pythonProject18/new" , sor))
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
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/User/PycharmProjects/pythonProject18/new" , sor))
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
        window['_TREE_'].update(add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))




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
                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/new", sor))
            elif faz2:
                window["_TREE_"].update(
                    add_files_in_folder('', "C:/Users/User/PycharmProjects/pythonProject18/Phase2", sor))
            exist2 = True
        list_file_s2 = []
        exist = False
        list_file_s2.append(values['-serch-'])
        for i in list_file_s:
            i = i[0].split('.')
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

