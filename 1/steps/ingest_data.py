import logging
import pandas as pd

from zenml import steps

class IngestData:
    def __init__(self, data_path: str):
        self.data_path = data_path
    
    def run(self):
        logging.info(f"Ingesting Data from {self.data_path}")
        return pd.read_csv(self.data_path)