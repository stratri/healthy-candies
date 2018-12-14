from healthy_candies.path import DATA_FOLDER, EXPORT_FOLDER, MAIN_DATASET_FILE, WIKIDATA_CAT_TREE_CSV, OFF_CAT_CSV
from os.path import exists, join
import os
from subprocess import call
from healthy_candies.init_scipts.cat_hierarchy import compute_and_store_cat_hierarchy
from healthy_candies.init_scipts.cat_off import compute_and_store_off_cat

# Setting up the data folder
if not exists(join(DATA_FOLDER)):
    print("Creating data folder")
    os.makedirs(DATA_FOLDER)
else:
    print("Found data folder")

# Setting up the data folder
if not exists(join(EXPORT_FOLDER)):
    print("Creating export folder")
    os.makedirs(EXPORT_FOLDER)
else:
    print("Found data folder")

# Downloading the dataset from open food facts
if not exists(MAIN_DATASET_FILE):
    print("Downloading open food facts dataset")
    call(['wget', '-O', MAIN_DATASET_FILE,
          'https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv'])
else:
    print("Found open food facts dataset")


# Compute the hierarchy csv
if not exists(WIKIDATA_CAT_TREE_CSV):
    print("Computing the category tree from wikidata")
    compute_and_store_cat_hierarchy()
else:
    print("Existing category tree found")

# Compute the off categories csv
if not exists(OFF_CAT_CSV):
    print("Computing the categories CSV from Open Food Facts")
    compute_and_store_off_cat()
else:
    print("Existing category CSV from Open Food Facts found")

# DONE
print("All systems are ready")
