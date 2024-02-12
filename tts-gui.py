import PySimpleGUI as sg
import text_to_speech as tts

sg.theme('DarkBlue3')

layout = [
    [sg.Text('Text to speech converter',
             size=(30, 1),
             font=("Helvetica", 25),
             )
     ],
    [sg.HorizontalSeparator(key='-HR-')],
    [sg.Text('Enter text here to be converted to speech:')],
    [sg.Multiline(
        size=(30, 20), key='-TEXT_INPUT-',
        expand_x=True, expand_y=True)
     ],
    [sg.Button('Play sample'), sg.Button('Close')],
    [sg.HorizontalSeparator(key='-HR-')],
    [sg.Text('Convert to audio:',
             size=(15, 1),
             font=("Helvetica", 15),
             )
     ],
    [sg.Text('file name:'), sg.InputText(key='-FILE_NAME-'), sg.Text('.mp3')],
    [sg.Text('file path:', pad=((6, 11), (0, 0))), sg.In(enable_events=True,
     key='-LOCATION-'), sg.FolderBrowse()
     ],
    [sg.Button('Convert', key='-CONVERT-')],
        ]

# Create the Window
window = sg.Window(
    'Text To Speech', layout, resizable=True, grab_anywhere=True
    )

try:
    while True:
        event, values = window.read()
        text_sample = tts.create_text_sample(values['-TEXT_INPUT-'])

        if event == sg.WIN_CLOSED or event == 'Close':
            break
        elif event == 'Play sample':
            tts.speak_words(text_sample)

except Exception as e:
    # sg.popup_error_with_traceback(f"The following error occurred: {e}")
    sg.Print(
        'The following error occurred,:\n',
        sg.__file__, e,
        '\n\nThe program will now close',
        keep_on_top=True,
        wait=True,
        )


window.close()
