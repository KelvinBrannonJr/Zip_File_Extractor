import PySimpleGUI as gui
from zip_extractor import extract_archive

gui.theme("Black")

# Choose archive file elements
label_select_archive = gui.Text("Select Archive")
input_select_archive = gui.Input(key="archive_input")
choose_archive_file = gui.FileBrowse("Choose", key='archive')

# Choose destination folder elements
label_select_destination = gui.Text("Select Destination")
input_select_destination = gui.Input(key="folder_input")
choose_destination = gui.FolderBrowse("Choose", key='folder')

# Extract elements
extract_button = gui.Button("Extract")
label_output = gui.Text(key='output', text_color="green")

# Layout
layout = [
    [label_select_archive, input_select_archive, choose_archive_file],
    [label_select_destination, input_select_destination, choose_destination],
    [extract_button, label_output]
]

window = gui.Window("Zip File Extractor", layout=layout)

# Event loop
while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break
    else:
        print(event, values)
        archive_path = values['archive']
        destination_dir = values['folder']
        extract_archive(archive_path, destination_dir)
        window['output'].Update(value="Extraction completed!")
        window['archive_input'].Update(value="")
        window['folder_input'].Update(value="")


window.close()
