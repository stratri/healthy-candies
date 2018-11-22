from os import path
import pandas as pd
import numpy as np
from .schema import SCHEMA
from healthy_candies.path import DATA_FOLDER
from typing import List


def load_data(usecols: List[str] = None, limit_have_nutri_score: bool = False) -> pd.DataFrame:
    """
        Load the full CSV from openfoodfacts and returns it as a dataframe.

        Parameters
        ----------
        usecols: List[str], default None
            Columns to return. If None, returns all columns
        limit_have_nutri_score: bool, default False
            Should the returned df be limited to products that have a nutri score
    """
    df = pd.read_csv(
        path.join(DATA_FOLDER, "en.openfoodfacts.org.products.csv"),
        sep="\t",
        dtype=SCHEMA)

    if limit_have_nutri_score:
        col = 'nutrition_grade_fr'
        df = df[df[col].replace(np.nan, '', regex=True) != '']

    if usecols is not None:
        df = df[usecols]

    return df
