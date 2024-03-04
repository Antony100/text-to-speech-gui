# Text to Speech Converter

### This project allows you to convert text into speech and save it as an audio file. It provides a simple graphical user interface (GUI) for easy interaction.

### Prerequisites

Before running the program, make sure you have the following dependencies installed:

    Python 3.x
    Pyttsx3
    PySimpleGUI

You can install the dependencies using pip:

```
pip install pyttsx3
pip install PySimpleGUI
```
### Usage

- Run tts-gui.py to launch the application.
- Enter the text you want to convert into speech in the provided text area.
- Set the desired speech rate using the dropdown menu.
- Optionally, you can play a sample of the text to hear how it sounds.
- Enter a file name and select a location to save the audio file.
- Click the "Convert" button to generate the audio file.
- Once the conversion is complete, a message will pop up indicating the successful creation of the audio file.

### Speech Rate Options

You can choose from the following speech rates:

    Slowest
    Slow
    Normal
    Fast
    Faster
    Fastest

### Error Handling

The program includes error handling for the following scenarios:

    Empty text input
    Missing file name or location during conversion
    Words with a length exceeding 45 characters

### Contributors

Antony Angeli

### License

This project is licensed under the MIT License.
