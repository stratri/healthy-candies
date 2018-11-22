from os import path

file_dir = path.dirname(path.abspath(__file__))
ROOT_PROJECT_FOLDER = path.realpath(path.join(file_dir + '/../'))

DATA_FOLDER = path.join(ROOT_PROJECT_FOLDER + '/data/')
STATIC_DATA_FOLDER = path.join(ROOT_PROJECT_FOLDER + '/static_data/')

MAIN_DATASET_FILE = path.join(DATA_FOLDER, "en.openfoodfacts.org.products.csv")
CATEGORIES_OFF_FILE = path.join(STATIC_DATA_FOLDER, 'categoriesOFF.json')
CATEGORIES_TREE_WIKIDATA_FILE = path.join(
    STATIC_DATA_FOLDER, 'categoriesTreeWikiData.json')
WIKIDATA_CAT_TREE_CSV = path.join(DATA_FOLDER, "wikidata_cat_tree.csv")
