from os import path
import pandas as pd
from .schema import SCHEMA
from healthy_candies.path import DATA_FOLDER
from typing import List


def load_data(usecols: List[str] = None) -> pd.DataFrame:
    """
        Load the full CSV from openfoodfacts and returns it as a dataframe.

        If `usecols` is specified, then only the specified columns are loaded and returned.
    """
    return pd.read_csv(
        path.join(DATA_FOLDER, "en.openfoodfacts.org.products.csv"),
        sep="\t",
        dtype=SCHEMA,
        usecols=usecols)
