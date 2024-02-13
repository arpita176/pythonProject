import PySimpleGUI as sg
from zip_creator import *

label1 = sg.Text('Select Files to compress:')
input1 = sg.InputText(tooltip='select files')
choose_button1 = sg.FilesBrowse('Choose', key='file')
label2 = sg.Text('Select Destination Folder:')
input2 = sg.InputText(tooltip='choose folder')
choose_button2 = sg.FolderBrowse('Choose', key='folder')
compress_button = sg.Button('Compress')
window = sg.Window('File Compressor', layout=[[label1, input1, choose_button1], [label2, input2, choose_button2],
                                              [compress_button]])
output_label=sg.Text(key='Output',text_color='green')
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    else:
        filepath = value['file'].split(';')
        print(filepath)
        print(value['folder'])
        make_archive(filepath, value['folder'])
        print('Zip successfully created')
        window['Output'].update(value='Compression Completed')

window.close()
