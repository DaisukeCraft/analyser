import string
import tkinter as tk
from tkinter import filedialog

import pandas as pd
from tqdm import tqdm

from Backend import DataContainer
from Output import Exporter
from Input import Importer
from . import Separator, Frame, Label, Button, Combobox, Checkbutton


class GUI(tk.Tk):
    DROPDOWN_OPTIONS = ["Company-Layer", "Generic-Layer", "Cluster-Layer"]
    KEYWORD_DETERMINATION_OPTIONS = ["Quantity", "Occurrence"]

    def __init__(self, excluded_words: list[str] = None):
        super().__init__()
        self.excluded_words: list[str] = excluded_words
        self.dataContainer = DataContainer()
        self.outputter = Exporter(self.dataContainer)
        self.importer = Importer()
        self.file_loaded = False

        self.create_display()

        self.update_options_visibility(None)

        for option in self.DROPDOWN_OPTIONS:
            query_method_name = f"query_{option.lower().replace('-', '_')}"
            query_method = self.create_query_method(option)
            setattr(self, query_method_name, query_method)

    def create_display(self):
        self.create_root_frame(title='Word Analysis Tool')

        self.create_top_frame()
        self.separator = Separator(self)
        self.create_bottom_frame()

        self.top_frame.pack(fill="both", expand=True, side=tk.TOP)
        self.separator.pack(fill="x")
        self.bottom_frame.pack(fill="both", side=tk.BOTTOM)

    def create_top_frame_pages(self):
        self.create_option_grid_1()
        self.create_option_grid_2()
        self.create_option_grid_3()

    def create_root_frame(self, title: str):
        self.title(title)
        self.geometry('300x400')
        self.minsize(width=300, height=400)
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=1)

    def create_bottom_frame(self):
        self.bottom_frame = Frame(self)

        self.data_state_label_text = tk.StringVar(value='No files loaded')
        self.data_state_label = Label(
            self.bottom_frame,
            textvariable=self.data_state_label_text
        )
        self.open_button = Button(
            self.bottom_frame,
            text="Open CSV Files",
            command=self.trigger_import
        )

        self.data_state_label.pack(pady=10)
        self.open_button.pack(pady=10)

    def create_top_frame(self):
        self.top_frame = Frame(self)

        self.dropdown_var = tk.StringVar(
            value=self.DROPDOWN_OPTIONS[0]
        )
        self.dropdown = Combobox(
            self.top_frame,
            textvariable=self.dropdown_var,
            values=self.DROPDOWN_OPTIONS,
        )
        self.dropdown.bind(
            "<<ComboboxSelected>>",
            self.update_options_visibility
        )
        self.query_button = Button(
            self.top_frame,
            text="Run",
            command=self.query_selected_option,
        )

        self.dropdown.pack(pady=(20, 60), side=tk.TOP)
        self.create_top_frame_pages()
        self.query_button.pack(pady=10, side=tk.BOTTOM)

    def create_query_method(self, option):
        def query_method():
            output_method_name = f"{option.lower().replace('-', '_')}"
            output_method = getattr(self.outputter, output_method_name, None)

            if output_method:
                output_method()
            else:
                print("Output method not available for this option")

        return query_method

    def create_option_grid_1(self):
        self.option_frame_1 = Frame(self.top_frame)

        word_rating_label = Label(
            self.option_frame_1,
            text="Word rating based on:"
        )
        self.word_rating_var = tk.StringVar(
            value=self.KEYWORD_DETERMINATION_OPTIONS[0]
        )
        word_rating_combobox = Combobox(
            self.option_frame_1,
            textvariable=self.word_rating_var,
            values=self.KEYWORD_DETERMINATION_OPTIONS,
        )
        count_in_percent_label = Label(
            self.option_frame_1,
            text="Count in percent:"
        )
        count_in_percent_var = tk.IntVar()
        count_in_percent_checkbox = Checkbutton(
            self.option_frame_1,
            variable=count_in_percent_var
        )

        word_rating_label.grid(row=0, column=0, pady=5, sticky='w')
        word_rating_combobox.grid(row=0, column=1, pady=5, sticky='w')
        count_in_percent_label.grid(row=1, column=0, pady=5, sticky='w')
        count_in_percent_checkbox.grid(row=1, column=1, pady=5, sticky='w')

        self.option_frame_1.pack()

    def create_option_grid_2(self):
        self.option_frame_2 = Frame(self.top_frame)

        keyword_in_percent_label = Label(
            self.option_frame_2,
            text="Keyword count in percent:"
        )
        keyword_count_in_percent_var = tk.IntVar()
        keyword_count_in_percent_checkbox = Checkbutton(
            self.option_frame_2,
            variable=keyword_count_in_percent_var,
        )
        company_in_percent_label = Label(
            self.option_frame_2,
            text="Company description count in percent:"
        )
        company_description_count_in_percent_var = tk.IntVar()
        company_description_count_in_percent_checkbox = Checkbutton(
            self.option_frame_2,
            variable=company_description_count_in_percent_var
        )

        keyword_in_percent_label.grid(row=0, column=0, pady=5, sticky='w')
        keyword_count_in_percent_checkbox.grid(row=0, column=1, pady=5, sticky='w')
        company_in_percent_label.grid(row=1, column=0, pady=5, sticky='w')
        company_description_count_in_percent_checkbox.grid(row=1, column=1, pady=5, sticky='w')
        self.option_frame_2.pack()

    def create_option_grid_3(self):
        self.option_frame_3 = Frame(self.top_frame)

        info_text = Label(
            self.option_frame_3,
            text="To be implemented"
        )

        info_text.grid(row=0, column=0, pady=5)

        self.option_frame_3.pack()

    def update_options_visibility(self, event):
        selected_option = self.dropdown_var.get()

        if selected_option == self.DROPDOWN_OPTIONS[0]:
            self.show_option_grid(self.option_frame_1)
        elif selected_option == self.DROPDOWN_OPTIONS[1]:
            self.show_option_grid(self.option_frame_2)
        elif selected_option == self.DROPDOWN_OPTIONS[2]:
            self.show_option_grid(self.option_frame_3)
        else:
            self.hide_option_grids()

    def show_option_grid(self, option_frame):
        self.hide_option_grids()
        option_frame.pack()

    def hide_option_grids(self):
        self.option_frame_1.pack_forget()
        self.option_frame_2.pack_forget()
        self.option_frame_3.pack_forget()

    def hide_option_grids_except(self, exception_frame):
        option_frames = [self.option_frame_1, self.option_frame_2, self.option_frame_3]
        for frame in option_frames:
            if frame != exception_frame:
                frame.pack_forget()

    def query_selected_option(self):
        selected_option = self.dropdown_var.get()
        query_method_name = f"query_{selected_option.lower().replace('-', '_')}"
        query_method = getattr(self, query_method_name, None)

        if query_method:
            query_method()
        else:
            print("Invalid option selected")

    def trigger_import(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Excel files", "*.xlsx")])
        file_paths = ('/home/bluealias/Downloads/Beispieldaten.xlsx',)
        try:
            self.importer.import_files(file_paths)
        except KeyError:
            print('Excel is the wrong fromat')
        except Exception as e:
            print(f"Failed to load and analyse data due to: '{e}'")
        else:
            self.data_state_label_text.set('Files loaded and analyed')
