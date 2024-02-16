import PySimpleGUI as sg
import text_to_speech as tts

sg.theme('DarkBlue3')

speech_rates = {
    "slowest": 80, "slow": 100, "normal": 125, "fast": 155, "faster": 185,
    "fastest": 210}


layout = [
    [sg.Text('Text to speech converter',
             size=(30, 1),
             font=("Helvetica", 25),
             )
     ],
    [sg.HorizontalSeparator()],
    [sg.Text('Enter text here to be converted to speech:')],
    [sg.Multiline(
        size=(30, 20), key='-TEXT_INPUT-',
        expand_x=True, expand_y=True)
     ],
    [sg.Button('Play sample'), sg.Push(), sg.Text('Set speech rate:'),
     sg.OptionMenu(speech_rates.keys(), default_value='normal',
                   key='-OPTION MENU-')
     ],
    [sg.HorizontalSeparator()],
    [sg.Text('Convert to audio:',
             size=(15, 1),
             font=("Helvetica", 15),
             )
     ],
    [sg.Text('file name:'), sg.InputText(key='-FILE_NAME-'), sg.Text('.mp3')],
    [sg.Text('file path:', pad=((6, 11), (0, 0))), sg.In(enable_events=True,
     key='-LOCATION-'), sg.FolderBrowse()
     ],
    [sg.Button('Convert')],
        ]

window = sg.Window(
    'Text To Speech', layout, resizable=True, grab_anywhere=True
    )

try:
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if values is not None:
            tts.set_speech_rate(speech_rates.get(values.get('-OPTION MENU-')))
            text_input = values.get('-TEXT_INPUT-')
            location = values.get('-LOCATION-')
            file_name = values.get('-FILE_NAME-')

            if event == 'Play sample':
                if text_input:
                    text_sample = tts.create_text_sample(text_input)
                    tts.speak_words(text_sample)
                else:
                    sg.popup_ok("Please enter text to play sample")
            elif event == 'Convert':
                if all((text_input, location, file_name)):
                    tts.save_as_audio(text_input, location, file_name)
                    sg.popup_ok(f"{file_name}.mp3 created!")
                else:
                    sg.popup_ok("Please fill all fields")

except Exception as e:
    sg.Print(
        'The following error occurred,:\n',
        sg.__file__, e,
        '\n\nThe program will now close',
        keep_on_top=True,
        wait=True,
    )

window.close()
