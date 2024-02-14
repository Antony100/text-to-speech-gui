import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 125)


def speak_words(words):
    engine.say(words)
    engine.runAndWait()


class WordLengthError(Exception):
    def __init__(self, message="Word length in text is too long"):
        self.message = message
        super().__init__(self.message)


def check_word_length(lst):
    for word in lst:
        if len(word) >= 45:
            raise WordLengthError


def create_text_sample(text):
    word_list = text.split(' ')
    check_word_length(word_list)
    if len(word_list) > 10:
        shortened_text = ' '.join(word_list[:10])
        return shortened_text
    else:
        return text


def save_as_audio(text, file_path, file_name):
    engine.save_to_file(text, f'{file_path}\{file_name}.mp3')
    engine.runAndWait()


def change_speech_rate(rate):
    engine.setProperty('rate', rate)
