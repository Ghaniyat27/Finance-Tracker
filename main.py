import pandas as pd
import csv
from datetime import datetime


class csv:
    CSV_FILE = "finance_data.csv"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "catergory" "description"])
            df.to_csv(cls.CSV_FILE, index=False)

            CSV.initialize_csv()
