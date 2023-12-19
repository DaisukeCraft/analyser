from src.Frontend import GUI
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    # EXCLUDE: words that should not be analysed

    app = GUI(
        excluded_words=os.getenv('GLOBAL_EXCLUDE').split(',') + os.getenv('EXCLUDE').split(',')
    )

    app.mainloop()
