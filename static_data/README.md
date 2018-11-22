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