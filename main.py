from googletrans import Translator


def text_translator(text, src='en', dest='ru'):
    try:
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)
        return translation.text
    except Exception as ex:
        return ex


def main():
    while True:
        text = input("Enter your text: ")
        print(text_translator(text))


if __name__ == "__main__":
    main()