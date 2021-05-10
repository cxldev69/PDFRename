__name__ = "PDFRename"
__author__ = "CXLDEV"
__version__ = "D-3.1"

from __cxl__ import Configura, lin, ler, les
import tkinter as tk
import tkinter.messagebox
import os
import sys

appdata_dir = os.getenv('APPDATA')


class RegisterWindow(tk.Frame):
    """
    Fenster zum registrieren vom Nutzer
    """

    def __init__(self, parent, username_var, root, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        tk.Label(self, font=("Arial black", 20), text="Name eingeben", width=200).place(anchor="center", x=150, y=25)

        self.username_entry = tk.Entry(self, width=35, textvariable=username_var)
        self.username_entry.place(anchor="center", x=150, y=79)

        self.register_button = tk.Button(self, text='Registrieren')
        self.register_button.configure(
            command=lambda: Configura(f'{appdata_dir}\\pdfre_uname.ini').write(username_var.get()) and root.destroy)
        self.register_button.place(anchor="center", x=150, y=115)


class MainWindow(tk.Frame):
    """
    Hauptfenster
    """

    def __init__(self, parent, var, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)

        FachListe = [
            "Mathe",
            "Deutsch",
            "Englisch",
            "Physik",
            "Chemie",
            "Kunst",
            "Arbeitslehre",
            "Biologie",
            "Religion",
            "Bili",
            "Wahlpflicht",
            "Geschichte",
        ]

        self.parent = parent

        tk.Label(self, font=("Arial black", 20), text="Fach auswählen", width=200).place(anchor="center", x=250, y=25)
        tk.Label(self, font=("Arial black", 10), text=os.path.basename(sys.argv[1]), width=200).place(anchor="center",
                                                                                                      x=250, y=60)

        # Standard Wert bestimmen
        var.set('Fächer Liste')

        self.fach_auswahl = tk.OptionMenu(self, var, *FachListe)
        self.fach_auswahl.place(anchor="center", x=250, y=100)

        self.rename_button = tk.Button(self, text='Umbenennen')
        self.rename_button.configure(command=lambda: rename(var))
        self.rename_button.place(anchor="center", x=250, y=150)


def rename(fach):
    from datetime import date
    datum = date.today().strftime("%d.%m.%Y")

    if "Fächer Liste" in fach.get(): fach.set('Mathe')  # Wenn kein Fach genommen wurde
    name = f'{fach.get()} {run.Username} - {datum}'

    lin(f'{sys.argv[1]} wird umbenannt zu {name}')

    os.rename(sys.argv[1], f'{name}.pdf')
    exit(0)

def run_register_window(root):
    register_root = tk.Toplevel(root)
    register_root.geometry('300x150')
    register_root.title('Registerer')

    run_register_window.username_var = tk.StringVar()

    register_window = RegisterWindow(register_root, run_register_window.username_var, register_root)
    register_window.pack(side="top", fill="both", expand=True)
    register_window.mainloop()


def run():
    root = tk.Tk()
    root.geometry('500x200')
    root.title(f'{__name__} {__version__}')
    choosen_fach = tk.StringVar()

    app = MainWindow(root, choosen_fach)
    app.pack(side="top", fill="both", expand=True)

    try: run.Username = Configura(f"{appdata_dir}\\pdfre_uname.ini").read()
    except: lin('Lese nach Nutzername')

    if "FileNotFound" in run.Username:  # Datei exestiert garnicht
        ler('Neuer Nutzer erkannt')
        run_register_window(root)
    else:
        if os.stat(f"{appdata_dir}\\pdfre_uname.ini").st_size == 0:  # Datei exestiert ist aber leer
            ler('Neuer Nutzer erkannt')
            run_register_window(root)
        else:
            les(f'Nutzer bereits regestiert: {run.Username}')  # Keine Probleme, Nutzer Komplett regestiert
            pass

    root.mainloop()


def message_box_error(error):
    root = tk.Tk()
    root.withdraw()

    tkinter.messagebox.showerror(title="PDFRename", message=str(error))


if __name__ == "PDFRename":
    lin(__name__ + __version__)

    try:
        les(sys.argv[1])
    except Exception as e:
        ler(f'Es muss eine PDF auf das Programm gelegt werden {e}')
        message_box_error("Es muss eine PDF auf das Programm abgelegt werden")
    else:
        les(f'Datei akzeptiert {sys.argv[1]}')
    try:
        run()
    except Exception as f:
        ler(f'Das Programm hatte einen Fehler {f}')
    else:
        les('Das Programm wurde erfolgreich genutzt')





