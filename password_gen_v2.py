import tkinter as tk
from tkinter import ttk
import subprocess
import sys
from generate_password_functions import *
from errors import LengthLimitError

class PasswordGeneratorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.style = ttk.Style()
        self.window.iconbitmap('image/pattern.ico')

        self.window.resizable(False, False)
        self.window.title("Password Generation")

        self.defual_setting_dict = {
            "UpperCase": True,
            "LowerCase": False,
            "Number": True,
            "Symbol": True,
            "Space": False
        }

        # Initialize UI elements
        self.label_featurs_list = [
            {"text": "UpperCase:"},
            {"text": "LowerCase:"},
            {"text": "Number:"},
            {"text": "Symbol:"},
            {"text": "Space:"},
            {"text": "Length:"},
            {"text": "Random_Password:"}
        ]

        self.label_created_list = []
        self.setup_labels()

        self.yes_button_commands = [
            {"command": lambda: self.defual_setting_dict.update({"UpperCase": True})},
            {"command": lambda: self.defual_setting_dict.update({"LowerCase": True})},
            {"command": lambda: self.defual_setting_dict.update({"Number": True})},
            {"command": lambda: self.defual_setting_dict.update({"Symbol": True})},
            {"command": lambda: self.defual_setting_dict.update({"Space": True})},
        ]

        self.no_button_commands = [
            {"command": lambda: self.defual_setting_dict.update({"UpperCase": False})},
            {"command": lambda: self.defual_setting_dict.update({"LowerCase": False})},
            {"command": lambda: self.defual_setting_dict.update({"Number": False})},
            {"command": lambda: self.defual_setting_dict.update({"Symbol": False})},
            {"command": lambda: self.defual_setting_dict.update({"Space": False})},
        ]

        self.yes_btn_list = []
        self.no_btn_list = []

        self.create_buttons()

        # Add an entry for length
        self.length_ent = ttk.Entry(self.window, width=20)
        self.length_ent.grid(row=len(self.label_featurs_list) - 2, column=5, columnspan=20)

        self.random_password_txt = self.setup_text_widget()
        self.default_label_list = self.create_default_labels()

        # Buttons next to the reset button
        self.run_btn = self.create_run_button()
        self.quit_btn = self.create_quit_button()
        self.restart_btn = self.create_restart_button()

        # Bind keyboard shortcuts
        self.bind_shortcuts()

    def setup_labels(self):
        row_num = 0
        for label_obj in self.label_featurs_list:
            label_created = tk.Label(
                master=self.window,
                height=3,
                width=18,
                font=('calibre', 10, 'bold'),
                text=label_obj['text']
            )
            self.label_created_list.append(label_created)
            label_created.grid(row=row_num, column=0, columnspan=5)
            row_num += 1

    def create_buttons(self):
        row_num = 0
        for yes_btn in self.yes_button_commands:
            btn = tk.Button(
                master=self.window,
                text='yes',
                width=8,
                height=1,
                fg="blue",
                command=yes_btn["command"]
            )
            btn.grid(row=row_num, column=5, columnspan=15)
            self.yes_btn_list.append(btn)
            row_num += 1

        row_num = 0
        for no_btn in self.no_button_commands:
            btn = tk.Button(
                master=self.window,
                text='no',
                width=8,
                height=1,
                fg="blue",
                command=no_btn['command']
            )
            btn.grid(row=row_num, column=20, columnspan=5)
            self.no_btn_list.append(btn)
            row_num += 1

    def setup_text_widget(self):
        text_widget = tk.Text(
            master=self.window,
            height=1,
            width=20,
            bg=self.window.cget("bg"),
            borderwidth=0,
            highlightthickness=0,
        )
        text_widget.grid(row=len(self.label_featurs_list)-1, column=5, columnspan=20)
        text_widget.config(state=tk.DISABLED)
        return text_widget

    def create_default_labels(self):
        default_label_featurs = [
            {"text": "Default ==> Yes"},
            {"text": "Default ==> No"},
            {"text": "Default ==> Yes"},
            {"text": "Default ==> Yes"},
            {"text": "Default ==> No"},
            {"text": "Default ==> 8"},
        ]

        row_num = 0
        label_list = []
        for label_obj in default_label_featurs:
            lbl = tk.Label(
                master=self.window,
                height=3,
                width=20,
                text=label_obj['text'],
                font=('calibre', 10, 'bold')
            )
            lbl.grid(row=row_num, column=30, columnspan=10)
            label_list.append(lbl)
            row_num += 1
        return label_list

    def create_run_button(self):

        self.style.theme_use('default')


        self.style.configure(
            "Run.TButton",
            foreground="#009ACD",     # Light blue text
            background="#E0E0E0",     # Light gray background
            padding=5
        )
        self.style.map(
            "Run.TButton", 
            background=[('active', '#87CEEB')]  # Active state background (light blue)
        )
        
        return ttk.Button(
            master=self.window,
            width=4,
            style="Run.TButton",
            text="run",
            command=self.generate_random_password_gui
        )

    def create_quit_button(self):
        self.style.configure(
            "Quit.TButton",
            foreground="red",          # Red text
            background="#FFCCCC",      # Light red background
            padding=5
        )
        self.style.map(
            "Quit.TButton",
            background=[('active', '#FF6666')]  # Active state background (darker red)
        )
        
        return ttk.Button(
            master=self.window,
            width=4,
            text="quit",
            style="Quit.TButton",
            command=quit
        )

    def create_restart_button(self):
        self.style.configure(
            "Restart.TButton",
            foreground="blue",         # Blue text
            background="#CCFFFF",      # Light blue background
            padding=5
        )
        self.style.map(
            "Restart.TButton",
            background=[('active', '#66CCFF')]  # Active state background (darker blue)
        )
        return ttk.Button(
        master=self.window,
        width=4,
        text="reset",
        style="Restart.TButton",
        command=self.restart_program
        )

    def place_buttons(self):
        row = len(self.label_featurs_list)
        self.run_btn.grid(row=row - 1, column=27, columnspan=10)
        self.quit_btn.grid(row=row - 1, column=32, columnspan=10)
        self.restart_btn.grid(row=row - 1 , column=37, columnspan=10)

    def bind_shortcuts(self):
        self.window.bind("<Return>", self.generate_random_password_gui)
        self.window.bind("<q>", lambda e: quit())
        self.window.bind("<r>", self.restart_program)

    def generate_random_password_gui(self, event=None):
        on_options = [option for option in self.defual_setting_dict if self.defual_setting_dict[option]]
        try:
            length = self.length_ent.get()
            if int(length) > 20 or int(length) < 4:
                raise LengthLimitError
            result = generate_random_password(on_options, int(length))
        except ValueError:
            result = generate_random_password(on_options, 8)
        except LengthLimitError:
            self.display_message("Length: 4 to 20")
            return

        self.update_labels(on_options)
        self.save_password(result)
        self.display_message(result)

    def update_labels(self, on_options):
        for label in self.label_created_list:
            if (label['text'][:-1]) in on_options:
                label['fg'] = 'green'
            else:
                label['fg'] = 'red' if label['text'] not in ["Random_Password:", "Length:"] else 'black'

    def save_password(self, result):
        with open("passwords.txt", 'a') as file:
            file.write(f"\n{result}\n")
            file.write("\n--------------------------------------------\n")

    def display_message(self, message):
        self.random_password_txt.config(state=tk.NORMAL)
        self.random_password_txt.delete(1.0, tk.END)
        total_width = 20
        padding = (total_width - len(message)) // 2
        centered_result = " " * padding + message
        self.random_password_txt.insert(tk.END, centered_result)
        self.random_password_txt.config(state=tk.DISABLED)

    def restart_program(self, event=None):
        try:
            subprocess.Popen([sys.executable] + sys.argv)
        except Exception as e:
            print(f"Error restarting the program: {e}")
        finally:
            sys.exit()

    def run(self):
        self.place_buttons()
        self.window.mainloop()


# Instantiate and run the app
if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.run()
