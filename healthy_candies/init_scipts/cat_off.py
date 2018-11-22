import json
import pandas as pd
from healthy_candies.path import CATEGORIES_OFF_FILE, OFF_CAT_CSV

from typing import Dict


def compute_and_store_off_cat() -> None:
    """
        Function that computes the Open Food Facts categories
        and their corresponding wikidata id (if present).
        The resulting df is stored as CSV.
    """

    # Open the raw data
    with open(CATEGORIES_OFF_FILE) as f:
        cats = json.load(f)['tags']

    n_cat = len(cats)
    df = pd.DataFrame(index=range(n_cat), columns=['catIdOff', 'wikidataId'])

    # Filled the df with the relevent data
    df.catIdOff = list(map(lambda cat: cat['id'], cats))

    def extract_wikidata_id(cat: Dict) -> str:
        """
            Function that extracts the url of wikidata matching the off category
        """
        if 'sameAs' in cat.keys():
            # There should be only one here
            assert len(cat['sameAs']) == 1, "to many mapping of categories"
            return cat['sameAs'][0]
        else:
            return ''

    df.wikidataId = list(map(extract_wikidata_id, cats))

    # extract the id
    df.wikidataId = df.wikidataId.str.extract(
        r'https://www.wikidata.org/wiki/(.*)$')[0]
    df = df.fillna('')

    # export to CSV
    df.to_csv(OFF_CAT_CSV, index=False)
