import pandas as pd

from src.config import RAW_DATA
from src.logger import logger


def load_dataset():
    """
    Load Titanic dataset.
    """

    try:
        df = pd.read_csv(RAW_DATA)

        logger.info("Dataset loaded successfully.")

        return df

    except Exception as e:
        logger.error(e)
        raise