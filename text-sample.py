text = """Kierkegaard'snotionoffinitudecomesclosetoKant'scriticalphilosophy. Kierkegaard's notion of finitude comes close to Kant's critical philosophy."""


class WordLengthError(Exception):
    def __init__(self, message="Word length in list is too long"):
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


print(create_text_sample(text))
