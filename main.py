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
stack=[]
stack_check=[]
stack_index=[]
Par=[]
inorder_list_phase3=[]
postorder_list_phase3=[]
preorderlist_phase3 =[]
for_faz3 = []
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
#txt_icon = b'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAABp0lEQVR4nGNgGAhw/fp1hatXrxy5evXKGUJ41fotZ3umLTQk2ZKrV68GXLt25T8xeP7Stf/DUip+9UybbUxTS1xCcki3iBxLXEi1iBRLlq3e9D8irQqOM0ravsxetFGFqpZcw4JB+kegJXsPHPpf3zGNaLz3wCHSLbl8+dL/Q0eOEY0vX75EuiVnz537v37zDqLx2XPnSLcE5LrOiXP/dxCBOyfOBasfPBH/LdRF7n1iyPTXFTkHyMXvE0Omf/N3k8Vpyacg58rPQS7/KcWfgpwr8VlSg6z46cSO//c2rwXjp5O6/j9aMAssDqKfTWhHyE3sQLekhmhLPkb7/X+4aM7/J1N7/3+K8f1/Z/eO/w8XzgLTn6J9weIgeZA6si0B4SezJv9/1t0EZr+qLQJH7quaQjAfJA6SxxJcZFoS7Pr/7vZN/x8sX/j/zvbNYD7VLHne1fj/VW3x/3fpMf/vr14KNvzB6iX/36dHgcVB8iRZ8jnQOZcaqetzoHMuTkv+h4ayPW+vy76/aslZcvHz9rpskDk4LQEBUlorWPCRq1evyuO1gFYAAJnylqtdIZ1TAAAAAElFTkSuQmCC'
txt_icon = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAABZ0lEQVR4nGNgQANXrlzhuXTpkiAu/OjRMU4GYsGNG5f0rl69/PfatSv/ceFpc5d9bOqZ5kOUgdevX3bAZxgI905d8N8/ruRvS98sf6oZ6BKSQ5yh14kwcNnqjf9L6vvBuK5j6tctW3YrUWQgOr5+/bID/Q1cvWHb/0kzF+PFIDVEG3j23Nn/h44cw4tBaog2cOHydf/rO6bhxYuWr6dzGP63t2d5lxFZ+7y56gAp+F1GZC1IL4aBn4Od9D4HufwnCwc76WEY+MXf1QCm4GOM//+7u7f9v3Xs0P+nU7r/P549GYyfTu4Ci4HkQGpg6r/4uxrgNRCE3xSm/38ya/L/z8Gu/+9tXvv/3qa1YDZIDCSHrPYLKQZ+ivL5f2fXVjD+GOVLvoEfUsL/v6opBGt+XZUPxm8K08BiIDmCBn7ysRf5HOp27GOk5zVSMEgPSC/WpENMAYuMQWpBerAaBgOEqgBkDFKLbgAAQ0AolZ/f/oEAAAAASUVORK5CYII='
treedata = sg.TreeData()
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


def make_window(theme="DarkBlue"):
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
        [sg.MenubarCustom(menu_def, pad=(0, 0), k='-CUST MENUBAR-'),sg.Input(background_color='white',text_color="Black",change_submits=True , key='-serch-'),sg.Button('Search')],
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
                 header_text_color='black', text_color='black',right_click_menu=['&Right', ["Delete",'&Sort',['&Name', ['A-Z', 'Z-A'], 'Date', ['Newest To Oldest', 'Oldest To Newest'], 'Type',
                  ['A_Z', 'Z_A']],'&Option',["&Inorder","Preorder","&Postorder"],'&Theme', ['Set A Theme', 'Default Theme'],'Exit']]), ],
        [sg.Text("Choose a ZipFile: ",key='ch' , visible=True), sg.Input(key="-IN2-", change_submits=True, size=(45),visible=True ,text_color="Black"),
         sg.FileBrowse (key="-IN-", file_types=(('Zip Files', '*.zip'), ('All Files', '*.*')),size=(7,1),visible=True)
            ,sg.Button("Extract" , key='Ex' ,visible=True,size=(7,1)),sg.Button('Save',size=(7,1))],#,sg.Button("SAVE" , key='SA',visible=True)
    ]
    layout = [
        [sg.Column(file_list_column), ]
    ]
    window = sg.Window("UNZIP PROJECT", layout, use_custom_titlebar=True,
              keep_on_top=True ,resizable=True,finalize=True)#, size=(530 , 530)) , right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT
    window["_TREE_"].expand(True, True)
    return window
def make_window_phase3(theme="DarkBlue"):
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
    window = sg.Window("Inorder_Preorder_postorder", layout, use_custom_titlebar=True,
              keep_on_top=True ,resizable=True,finalize=True)#, size=(530 , 530)) , right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT
    window["_TREE_"].expand(True, True)
    return window
add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new" , sor)
t = True
t2 = True
faz1 = True
faz2 = False
faz3 = False
faz4 = False
# THEME = 'Tan'
newpath = r'C:\Users\akgh1\PycharmProjects\unzip\new'
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
window = make_window('DarkBlue')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        if os.path.exists("C:/Users/akgh1/PycharmProjects/unzip/Phase2/"):
            shutil.rmtree("C:/Users/akgh1/PycharmProjects/unzip/Phase2/")
        break
    elif (event == "Extract" or event == 'Ex' ) and values["-IN2-"] != '':
        try:
            if faz1 == True:
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
                newpath = r'C:/Users/akgh1/PycharmProjects/unzip/dirname'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                newpath2 = r'C:/Users/akgh1/PycharmProjects/unzip/Phase3'
                if not os.path.exists(newpath2):
                    os.makedirs(newpath2)
                for member in zip.namelist():
                    zip.extract(member, 'dirname')
                for member in zip.namelist():
                    zip.extract(member, 'Phase3')

                newpath = r'C:/Users/akgh1/PycharmProjects/unzip/new'
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
                        os.remove("C:/Users/akgh1/PycharmProjects/unzip/new/" + i2)
                        list_file_s.remove(i)
                    # else:
                treedata = sg.TreeData()
                window["_TREE_"].update(
                    add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new", sor))
                window['-IN2-'].update('')
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
    elif event =='Set A Theme':
        # window.hide()
        event, values = sg.Window('Choose Theme',[[sg.Combo(sg.theme_list(), readonly=True, k='-THEME LIST-'), sg.OK(),sg.Cancel()]],keep_on_top=True).read(close=True)
        if event == 'OK':
            window.close()
            settheme(values['-THEME LIST-'])
            if faz3==False:
                window = make_window(values['-THEME LIST-'])
            if faz3==True:
                window =make_window_phase3(values['-THEME LIST-'])
        # else:
            # window.un_hide()a
    elif event =='Default Theme':
        window.close()
        settheme("DarkBlue")
        if faz3 == False :
            window = make_window()
        if faz3 ==True:
           window = make_window_phase3()
    elif event == 'Phase 1' and faz1 == False:
        if faz3 == True:
            window.close()
            window = make_window()
        faz1 = True
        faz2 = False
        faz3 = False
        faz4 = False
        set_year.clear()
        if os.path.exists("C:/Users/akgh1/PycharmProjects/unzip/Phase2/"):
            shutil.rmtree("C:/Users/akgh1/PycharmProjects/unzip/Phase2/")
        treedata = sg.TreeData()
        window["_TREE_"].update(add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new" , sor))
    elif event == 'A File':
        # window.hide()
        if faz1 == True:
            sg.theme(THEME)
            layout3 = [
                [sg.Text("Inter the name of file "), sg.Input(key="-IN3-", change_submits=False)],
                [sg.Button("Delete"), sg.T(""), sg.Button("Cancel")],
            ]
            window_delete = sg.Window('delete', layout3, size=(340, 75), keep_on_top=True)
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
                        tmp_str = os.listdir("C:/Users/akgh1/PycharmProjects/unzip/Phase3/")
                        if os.path.exists("C:/Users/akgh1/PycharmProjects/unzip/Phase3/" + tmp_str[0] + '/' + add2[0]):
                            os.remove("C:/Users/akgh1/PycharmProjects/unzip/Phase3/" + tmp_str[0] + '/' + add2[0])
                        os.remove("C:/Users/akgh1/PycharmProjects/unzip/new/" + add2[0])
                        treedata = sg.TreeData()
                        window["_TREE_"].update(
                            add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new", sor))
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

            if os.path.exists("C:/Users/akgh1/PycharmProjects/unzip/dirname/"):
                shutil.rmtree("C:/Users/akgh1/PycharmProjects/unzip/dirname/")
            if os.path.exists("C:/Users/akgh1/PycharmProjects/unzip/Phase3/"):
                shutil.rmtree("C:/Users/akgh1/PycharmProjects/unzip/Phase3/")
            window.hide()
            msg_box = tk.messagebox.askquestion('Delete All Files', 'Are you sure you want to Delete All Files ?',
                                                icon='warning')
            if msg_box == 'yes':
                list_dir = os.listdir(r'C:/Users/akgh1/PycharmProjects/unzip/new')
                for i1 in list_dir:
                    os.remove("C:/Users/akgh1/PycharmProjects/unzip/new/" + i1)
                treedata = sg.TreeData()
                window["_TREE_"].update(
                    add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new", sor))
            list_file_s = []
            window.un_hide()
        else :
            sg.popup("Error","You Should Be In Phase 1", keep_on_top=True,text_color="Red")


            # else:
            # tk.messagebox.showinfo('Return', 'You will now return to the application screen')

    elif event == 'Newest To Oldest' and faz1 == True:
        sor = 'date2'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/akgh1/PycharmProjects/unzip/new" , sor))
    elif event == 'Oldest To Newest' and faz1 == True:
        sor = 'date1'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new", sor))
    elif event == 'A-Z' and faz1 == True:
        sor = 'name1'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/akgh1/PycharmProjects/unzip/new" , sor))
    elif event == 'Z-A' and faz1 == True:
        sor = 'name2'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/akgh1/PycharmProjects/unzip/new" , sor))
    elif event == 'A_Z' and faz1 == True:
        sor = 'type1'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('' , "C:/Users/akgh1/PycharmProjects/unzip/new" , sor))
    elif event == 'Z_A' and faz1 == True:
        sor = 'type2'
        treedata = sg.TreeData()
        window['_TREE_'].update(add_files_in_folder('', "C:/Users/akgh1/PycharmProjects/unzip/new", sor))

    faz2 = True
    faz1 = False
    faz3 = False
    faz4 = False
    faz = 'Phase2'
    if not os.path.exists("C:/Users/sh/Desktop/project amm 2/" + faz):
        os.makedirs("C:/Users/sh/Desktop/project amm 2/" + faz)

    source = "C:/Users/sh/Desktop/project amm 2/new/"
    destination = "C:/Users/sh/Desktop/project amm 2/" + faz + '/'
    files = os.listdir(source)
    for folder in files:  # add year in set_type
        if '.txt' in folder or '.png' in folder or '.zip' in folder or '.pdf' in folder or '.aiff' in folder or '.jpeg' in folder \
                or '.wav' in folder or '.avl' in folder or '.mkv' in folder or '.mov' in folder or '.jpg' in folder or '.gif' in folder \
                or '.mp4' in folder:
            file2 = folder.split('.')
            set_year.add(int(file2[1]))

    for i in set_year:  # creat folders with date names
        newpath = "C:/Users/sh/Desktop/project amm 2/" + faz + '/' + str(i)
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for file in files:  # move file in new folders
        if '.txt' in file or '.png' in file or '.zip' in file or '.pdf' in file or '.aiff' in file or '.jpeg' in file \
                or '.wav' in file or '.avl' in file or '.mkv' in file or '.mov' in file or '.jpg' in file or '.gif' in file \
                or '.mp4' in file:
            file2 = file.split('.')
            file_name = os.path.join(source, file)
            shutil.copy(file_name, destination + file2[1] + '/')

    for file in set_year:
        source = "C:/Users/sh/Desktop/project amm 2/" + faz + '/' + str(file) + '/'
        destination = "C:/Users/sh/Desktop/project amm 2/" + faz
        files = os.listdir(source)
        set_type = ()
        set_type = set(set_type)

        for folder in files:  # add types in set_type
            if '.txt' in folder or '.png' in folder or '.zip' in folder or '.pdf' in folder or '.aiff' in folder or '.jpeg' in folder \
                    or '.wav' in folder or '.avl' in folder or '.mkv' in folder or '.mov' in folder or '.jpg' in folder or '.gif' in folder \
                    or '.mp4' in folder:
                file2 = folder.split('.')
                set_type.add('.' + file2[2])