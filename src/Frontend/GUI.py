import tkinter as tk
from tkinter import filedialog

from src.Global import (DROPDOWN_OPTIONS,
                        KEYWORD_DETERMINATION_OPTIONS,
                        GENERIC_LAYER,
                        COMPANY_LAYER,
                        CLUSTER_LAYER,
                        validate_int_input)
from src.Backend import DataContainer
from src.Output import Exporter
from src.Input import Importer
from . import (Separator,
               Frame,
               Label,
               Button,
               Combobox,
               Checkbutton)


class GUI(tk.Tk):
    def __init__(self, excluded_words: list[str] = None):
        super().__init__()
        self.excluded_words: list[str] = excluded_words
        self.dataContainer = DataContainer(self.excluded_words)
        self.outputter = Exporter(self.dataContainer)
        self.importer = Importer(self.dataContainer)
        self.file_loaded = False

        self.create_display()

        self.update_options_visibility(None)

        for option in DROPDOWN_OPTIONS:
            query_method_name = f"query_{option.lower().replace('-', '_')}"
            query_method = self.create_query_method(option)
            setattr(self, query_method_name, query_method)

    def create_display(self):
        self.create_root_frame(title='Word Analysis Tool')

        self.validate_int_input_cmd = self.register(validate_int_input)

        self.create_export_control_frame()
        self.separator = Separator(self)
        self.create_file_control_frame()

        self.file_control_frame.pack(fill="both", side=tk.TOP)
        self.separator.pack(fill="x")
        self.export_control_frame.pack(fill="both", expand=True, side=tk.BOTTOM)

    def create_export_control_frame_pages(self):
        self.create_option_grid_company()
        self.create_option_grid_generic()
        self.create_option_grid_cluster()

    def create_root_frame(self, title: str):
        self.title(title)
        self.geometry('300x400')
        self.minsize(width=300, height=400)
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=1)

    def create_file_control_frame(self):
        self.file_control_frame = Frame(self)

        self.bottom_frame_info_label_text = tk.StringVar(value='No files loaded')
        self.bottom_frame_info_label = Label(
            self.file_control_frame,
            textvariable=self.bottom_frame_info_label_text
        )
        self.bottom_frame_open_file_button = Button(
            self.file_control_frame,
            text="Open CSV Files",
            command=self.trigger_import
        )

        self.bottom_frame_info_label.pack(pady=10)
        self.bottom_frame_open_file_button.pack(pady=10)

    def create_export_control_frame(self):
        self.export_control_frame = Frame(self)

        self.top_frame_dropdown_var = tk.StringVar(
            value=DROPDOWN_OPTIONS[0]
        )
        self.top_frame_dropdown = Combobox(
            self.export_control_frame,
            textvariable=self.top_frame_dropdown_var,
            values=DROPDOWN_OPTIONS,
        )
        self.top_frame_dropdown.bind(
            "<<ComboboxSelected>>",
            self.update_options_visibility
        )
        self.top_frame_export_button = Button(
            self.export_control_frame,
            text="Export",
            command=self.query_selected_option,
        )
        self.top_frame_export_all_button = Button(
            self.export_control_frame,
            text="Export All",
            command=self.query_all_options,
        )

        self.top_frame_dropdown.pack(pady=(20, 60), side=tk.TOP)
        self.create_export_control_frame_pages()
        self.top_frame_export_all_button.pack(pady=10, side=tk.BOTTOM)
        self.top_frame_export_button.pack(pady=10, side=tk.BOTTOM)

    def create_query_method(self, option):
        def query_method():
            output_method_name = f"{option.lower().replace('-', '_')}"
            output_method = getattr(self.outputter, output_method_name, None)

            if output_method:
                output_method()
            else:
                print("Output method not available for this option")

        return query_method

    def create_option_grid_company(self):
        self.option_frame_company = Frame(self.export_control_frame)

        self.option_frame_company_key_word_count_label = Label(
            self.option_frame_company,
            text="Key word amount:"
        )
        self.option_frame_company_key_word_count_int_var = tk.IntVar(
            value=3
        )
        self.option_frame_company_key_word_count_entry = tk.Entry(
            self.option_frame_company,
            textvariable=self.option_frame_company_key_word_count_int_var,
            validate='key',
            validatecommand=(self.validate_int_input_cmd, "%S", "%P")
        )

        self.option_frame_company_word_rating_label = Label(
            self.option_frame_company,
            text="Word rating based on:"
        )
        self.option_frame_company_word_rating_var = tk.StringVar(
            value=KEYWORD_DETERMINATION_OPTIONS[0]
        )
        self.option_frame_company_word_rating_combobox = Combobox(
            self.option_frame_company,
            textvariable=self.option_frame_company_word_rating_var,
            values=KEYWORD_DETERMINATION_OPTIONS,
        )

        self.option_frame_company_count_in_percent_label = Label(
            self.option_frame_company,
            text="Count in percent:"
        )
        self.option_frame_company_count_in_percent_var = tk.IntVar()
        self.option_frame_company_count_in_percent_checkbox = Checkbutton(
            self.option_frame_company,
            variable=self.option_frame_company_count_in_percent_var
        )

        self.option_frame_company_key_word_count_label.grid(row=0, column=0, pady=5, sticky='w')
        self.option_frame_company_key_word_count_entry.grid(row=0, column=1, pady=5, sticky='w')
        self.option_frame_company_word_rating_label.grid(row=1, column=0, pady=5, sticky='w')
        self.option_frame_company_word_rating_combobox.grid(row=1, column=1, pady=5, sticky='w')
        self.option_frame_company_count_in_percent_label.grid(row=2, column=0, pady=5, sticky='w')
        self.option_frame_company_count_in_percent_checkbox.grid(row=2, column=1, pady=5, sticky='w')

        self.option_frame_company.pack()

    def create_option_grid_generic(self):
        self.option_frame_generic = Frame(self.export_control_frame)

        self.option_frame_generic_keyword_in_percent_label = Label(
            self.option_frame_generic,
            text="Keyword count in percent:"
        )
        self.option_frame_generic_keyword_count_in_percent_var = tk.IntVar()
        self.option_frame_generic_keyword_count_in_percent_checkbox = Checkbutton(
            self.option_frame_generic,
            variable=self.option_frame_generic_keyword_count_in_percent_var,
        )
        self.option_frame_generic_company_in_percent_label = Label(
            self.option_frame_generic,
            text="Company description count in percent:"
        )
        self.option_frame_generic_company_description_count_in_percent_var = tk.IntVar()
        self.option_frame_generic_company_description_count_in_percent_checkbox = Checkbutton(
            self.option_frame_generic,
            variable=self.option_frame_generic_company_description_count_in_percent_var
        )

        self.option_frame_generic_keyword_in_percent_label.grid(row=0, column=0, pady=5, sticky='w')
        self.option_frame_generic_keyword_count_in_percent_checkbox.grid(row=0, column=1, pady=5, sticky='w')
        self.option_frame_generic_company_in_percent_label.grid(row=1, column=0, pady=5, sticky='w')
        self.option_frame_generic_company_description_count_in_percent_checkbox.grid(row=1, column=1, pady=5, sticky='w')
        self.option_frame_generic.pack()

    def create_option_grid_cluster(self):
        self.option_frame_cluster = Frame(self.export_control_frame)

        self.option_frame_cluster_info_text = Label(
            self.option_frame_cluster,
            text="To be implemented"
        )

        self.option_frame_cluster_info_text.grid(row=0, column=0, pady=5)

        self.option_frame_cluster.pack()

    def update_options_visibility(self, event):
        selected_option = self.top_frame_dropdown_var.get()

        if selected_option == COMPANY_LAYER:
            self.show_option_grid(self.option_frame_company)
        elif selected_option == GENERIC_LAYER:
            self.show_option_grid(self.option_frame_generic)
        elif selected_option == CLUSTER_LAYER:
            self.show_option_grid(self.option_frame_cluster)
        else:
            self.hide_option_grids()

    def show_option_grid(self, option_frame):
        self.hide_option_grids()
        option_frame.pack()

    def hide_option_grids(self):
        self.option_frame_company.pack_forget()
        self.option_frame_generic.pack_forget()
        self.option_frame_cluster.pack_forget()

    def hide_option_grids_except(self, exception_frame):
        option_frames = [self.option_frame_company, self.option_frame_generic, self.option_frame_cluster]
        for frame in option_frames:
            if frame != exception_frame:
                frame.pack_forget()

    def query_selected_option(self):
        if not self.file_loaded:
            print("No file has been loaded yet")
            return

        selected_option = self.top_frame_dropdown_var.get()

        if selected_option == COMPANY_LAYER:
            self.outputter.export_company_layer(
                self.option_frame_company_key_word_count_int_var.get(),
                self.option_frame_company_word_rating_combobox.get(),
                self.option_frame_company_count_in_percent_var.get()
            )
            self.bottom_frame_info_label_text.set('Company Layer exported')
        elif selected_option == GENERIC_LAYER:
            self.outputter.export_generic_layer(
                self.option_frame_generic_keyword_count_in_percent_var.get(),
                self.option_frame_generic_company_description_count_in_percent_var.get()
            )
            self.bottom_frame_info_label_text.set('Generic Layer exported')
        elif selected_option == CLUSTER_LAYER:
            self.show_option_grid(self.option_frame_cluster)
        else:
            print("Invalid option selected")

    def query_all_options(self):
        if not self.file_loaded:
            print("No file has been loaded yet")
            return

        # Execute option 1
        self.outputter.export_company_layer(
            self.option_frame_company_key_word_count_int_var.get(),
            self.option_frame_company_word_rating_combobox.get(),
            self.option_frame_company_count_in_percent_var.get()
        )

        # Execute option 2
        self.outputter.export_generic_layer(
            self.option_frame_generic_keyword_count_in_percent_var.get(),
            self.option_frame_generic_company_description_count_in_percent_var.get()
        )

        # Update status message
        self.bottom_frame_info_label_text.set('All layers exported')

    def trigger_import(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Excel files", "*.xlsx")])

        self.importer.import_files(file_paths)
        self.bottom_frame_info_label_text.set('Analysing file(s)...')
        self.trigger_analysis()
        self.bottom_frame_info_label_text.set('File(s) loaded and analysed')
        self.file_loaded = True

    def trigger_analysis(self, rerun: bool = True):
        if rerun:
            self.trigger_analysis(self.dataContainer.analyse(self.excluded_words))

