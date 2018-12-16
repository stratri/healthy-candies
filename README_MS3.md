~~Healthy Candies~~ Tales from the *Open Food Facts* universe*
========
*\* (unofficially) retitled in order to reflect our data analysis*

*This is the README file for milestone 3 of the project ([link to milestone 2 README](https://github.com/striantafyllouEPFL/healthy-candies/blob/master/README_MS2.md)).*

## Summary


### Data story

We decided to use a *data story* as the medium to convey our findings.

[**Here is the repo of the data story**](https://github.com/ADA-Healthy-Candies/ADA-Healthy-Candies.github.io) and [**here is a direct link to the story**](https://ada-healthy-candies.github.io/). 

We hope you will enjoy it.


:warning: Spoiler alert: the next section might spoil a bit of the data story, just saying. :angel:


### Final research questions & quick preview of our findings

Our project finally focused on two following main dimensions:

1. Colour:
    - Different colours have different perceptual impact on consumers. Having this in mind, we were interested in investigating the dominant colours on the product’s packagings.
        - We found strong evidence of a dominant use of *red*, *orange* and *yellow* on the packagings; which is far from innocent.
        - We also found that some colours are kind of food category specific. 
    - We were interested in assessing the link between the colour on the packaging and the nutritional properties of a product.
        - Generally speaking, we didn't find a strong link except for very specific colours.
    - Following the previous research question, we were interested in the existence of "greenwashing" in the food industry.
        - We didn't find a statistical evidence of it; however, by exploring the dataset, we found clear examples of it. 

2. Nutritional consistency of product categories:
    - How consistent are food product categories nutritionally? Are products of the same food category similar nutrition-wise?
        - If the answer is yes, then it should be possible to think of categories as groups of products with strong nutritional similarities.
        - Density-based clustering of products based on their nutrition facts results in clusters that point to actual categories. This indicates that categories are consistent.
        - In practice, this strong connection between categories and nutrition facts could be used as an alternative way to derive product hierarchies.



### Work achieved

To reflect our two research questions, and because they are quite independent, we have gathered our work in two separate, self-contained notebooks. Very few `Python` scripts are outside those notebooks to have cleaner code; those very few scripts will be linked inside the notebooks.

The two notebooks are:

1. One about [the colour part of the project](./notebooks/color.ipynb).

2. One about [the nutrient clusters part of the project](./notebooks/nutrient_clusters.ipynb)



#### Future work

- Explore the issue of Greenwashing even more.
- Modify our clustering model to use a (density-based) algorithm that can perform well with clusters of varying density, such as OPTICS or HDBSCAN.



## Contributions

- Florent:
    - Early exploration of dead ends,
    - Scraping of the products images,
    - Extraction process of the hues on each image,
    - Main exploration related to the *colour* side of the project,
    - Contributed to the data story set up,
    - Cooperation on the *colour* related story.

- Stratos:
    - Formulated the initial research questions,
    - Author of the nutritional consistency notebook, 
    - Main author of the corresponding story,
    - Briefly contributed to the *colour* related story.

- Ouiame:
    - Exploration of the nutritional facts category-wise,
    - Contributed to the exploration of *colour* side of the project, 
    - Main data story set up,
    - Cooperation on the *colour* related story.

*And... we all have reviewed each other's work. :smile:*


## Remaining work towards the presentation

- Making the poster,
- Writing our presentation,
- Rehearsing the presentation.

*That last part will be achieved in a collaborative fashion.* 
