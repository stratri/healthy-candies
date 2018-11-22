import json
import pandas as pd

from healthy_candies.path import CATEGORIES_OFF_FILE, CATEGORIES_TREE_WIKIDATA_FILE, WIKIDATA_CAT_TREE_CSV
from typing import Dict, Tuple, List, Callable


def compute_and_store_cat_hierarchy() -> None:
    """
        Function that computes the hierarchy dataframe with the data from wikimedia
        And stores the result as a CSV
    """

    # Open the raw data
    with open(CATEGORIES_TREE_WIKIDATA_FILE) as f:
        categories_tree_raw = json.load(f)

    def parseNode(node: Dict) -> Tuple[List[List[str]], List[Dict[str, str]]]:
        """
        Function that parses a node from the tree.
        It returns a tuple
            1. the hierarchy: a list that starts by the smallest grain category, 
                followed by its parent, the parent of its parent, etc.
            2. A dictionnary with keys the wikidata IDs, and values the matching names.
        """
        node_id = node['id']
        cat_names = {node['id']: node['catName']}
        h = []
        if 'childrens' in node.keys():
            for child in node['childrens']:
                h_children, cat_names_children = parseNode(child)
                cat_names = {**cat_names, **cat_names_children}
                for sub_h in h_children:
                    h.append(sub_h + [node_id])

        # Track also this node in the hiearchy
        h.append([node_id])

        return h, cat_names

    # Compute the hiearchy and the id <=> name dict
    hierarchy, id_name_mapping = parseNode(categories_tree_raw)

    # Handle the mapping of categories / name
    df_id_names = pd.DataFrame.from_dict(id_name_mapping, orient='index', columns=['wikidataName']) \
        .reset_index() \
        .rename(columns={'index': 'wikidataId'})

    ###
    # Convert the hiearchy to a pandas df
    ##

    max_depth = max(map(len, hierarchy))
    n_cat = len(hierarchy)

    df_hierarchy = pd.DataFrame(index=range(n_cat), columns=range(max_depth))

    def get_or_first(i: int) -> Callable:
        """
            Returns a function that...
        """
        def to_return(l: List[str]) -> str:
            """
                Returns the element that is at the ith position from the end of the list.
                If not possible returns, the first element.
            """
            if i < len(l):
                return l[len(l) - i - 1]
            else:
                return l[0]
        return to_return

    # Perform the mapping
    for i in range(1, max_depth+1):
        df_hierarchy[i-1] = list(map(get_or_first(i), hierarchy))

    # rename and merge
    df_hierarchy = df_hierarchy.rename(columns={max_depth-1: 'wikidataId'})
    df_hierarchy = df_hierarchy.merge(df_id_names, on='wikidataId')

    # export to CSV
    df_hierarchy.to_csv(WIKIDATA_CAT_TREE_CSV, index=False)
