from typing import List


class Importer:
    def __init__(self):
        self.loaded = False
        self.analysed = False

    def import_files(self, file_paths: List[str]) -> List[bool]:
        file_paths = filedialog.askopenfilenames(filetypes=[("Excel files", "*.xlsx")])

        if file_paths:
            self.file_loaded = True
            self.label.config(text="Files loaded")

            for file_path in tqdm(file_paths, desc="Loading files"):
                self.analyze_excel(file_path)
