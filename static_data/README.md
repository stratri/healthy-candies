Static data
=======

This folder holds data that is statically associated to the project.

## File: `categoriesTreeWikiData.json`

`Last updated: Thu Nov 22`

This file contains a tree like structure holding the hierachy of food categories according to Wikidata.

The script (and documention) used to get it is available in the `scripts` folder.


## File: `categoriesOFF.json`

This file contains all the directory listed on open food facts.

To get it, inside the directory (where this `README` is) run:

```sh
wget -O ./categoriesOFF.json https://world.openfoodfacts.org/categories.json
```

## File: `colors.csv.zip`

This file contains the hues extracted from the images of the products.

To get it, you first need to run the `scrap_images.py` script to get all the images for all products.
Then you should run the `extract_colors.py` script (takes a lot of time).


## File: `clusters.csv.zip`

This file contains the resulting mapping from products to cluster using DBSCAN.