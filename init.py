from healthy_candies.path import DATA_FOLDER, MAIN_DATASET_FILE, WIKIDATA_CAT_TREE_CSV
from os.path import exists, join
import os
from subprocess import call
from healthy_candies.init_scipts.cat_hierarchy import compute_and_store_cat_hierarchy

# Setting up the data folder
if not exists(join(DATA_FOLDER)):
    print("Creating data folder")
    os.makedirs(DATA_FOLDER)
else:
    print("Found data folder")

# Downloading the dataset from open food facts
if not exists(MAIN_DATASET_FILE):
    print("Downloading open food facts dataset")
    call(['wget', '-O', MAIN_DATASET_FILE,
          'https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv'])
else:
    print("Found open food facts dataset")


# Compute the hierarchy file
if not exists(WIKIDATA_CAT_TREE_CSV):
    print("Computing the category tree from wikidata")
    compute_and_store_cat_hierarchy()
else:
    print("Existing category tree found")

# DONE
print("All systems are ready")