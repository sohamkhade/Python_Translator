# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from translate import Translator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    to_lan = input("Enter your language you want to translate in this format ISO 639-1 (example: en or es)  ~ ")

    from_lan = input("Enter the language you want translate from in this format ISO 639-1 ~ ")

    translator = Translator(to_lang=to_lan, from_lang=from_lan)
    text = input(f"Enter the text you want to translate to {to_lan} ~ ")

    translation = translator.translate(text)
    print(f"Your translated text is ~ {translation}")




