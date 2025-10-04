import logging
import pandas as pd

from zenml import step

@step
def evaluate_model(df: pd.DataFrame) -> None:
    '''
    Evaluates the model on injested data

    Args:
        df: ingested data
    '''
    pass