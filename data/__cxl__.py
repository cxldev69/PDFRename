from colorama import Fore, Back, Style
import tkinter as tk
from os import name as os_name


def lin(value): print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}NFOL{Fore.WHITE}] {str(value)}")


def ler(value): print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}BADC{Fore.WHITE}] {str(value)}")


def les(value): print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}EVOK{Fore.WHITE}] {str(value)}")


if "nt" in os_name:

    les('DotSlash 8.1 wurde erfolgreich geladen')

else:
    print('[D/S] Error: Total Computing System Error. DotSlash only works with Operating System {nt}')


def tk_button_state(widget, state): widget.config(str(state))


def tk_set_text(widget, text):
    widget.delete(0, tk.END)
    widget.insert(0, str(text))
    return


class Configura:
    def __init__(self, path):
        self.path = str(path).replace("\\", "/")

    def read(self):
        try:
            with open(self.path) as file:
                lin(f'Konfigurationsdatei {self.path} wurde gelesen')
                return str(file.read())
        except FileNotFoundError:
            ler('Datei wurde nicht gefunden')
            return "FileNotFound"

    def write(self, new):
        try:
            with open(self.path, 'w+') as file:
                file.write(str(new))
                lin(f'Konfigurationsdatei {self.path} wurde zu {str(new)} umgeschrieben')
                return
        except:
            ler('Konnte Datei nicht erstellen')
