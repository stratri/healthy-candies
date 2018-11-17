from os import path
import pandas as pd
from .schema import SCHEMA
from healthy_candies.path import DATA_FOLDER


def load_data() -> pd.DataFrame:
    return pd.read_csv(
        path.join(DATA_FOLDER, "en.openfoodfacts.org.products.csv"),
        sep="\t",
        dtype=SCHEMA)
