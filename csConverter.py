import PySimpleGUI as sg 

layout = [
    [1],
    [2],
    [3]       
]

window = sg.Window('Text to Binary Converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
