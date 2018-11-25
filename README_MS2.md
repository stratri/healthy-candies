Healthy Candies
========

*Milestone 2 is a big update to our project.*

*Disclaimer: the code blocks related to Google Colab at the beginning of each notebook are here to make them work locally and on Google Colab (tested and approved).* 

## From milestone 1 to milestone 2

### Summary 

We have explored the dataset in more detail, which has helped us better understand the challenges of the topic and the limitations of the dataset. We thus reformulated our research questions and are moving the project in a new direction that we feel is both more challenging and more interesting.


### Details

More precisely:

- In the [general exploration](./general_exploration.ipynb) notebook, you can find a general exploratory analysis of the dataset; it helps to better understand what the features that we can use are.
- In the [pruning categories](./pruning_categories.ipynb) notebook we examine the suitability of the product categories provided in the dataset. We explore alternative ways to create and balance a category tree that could be used in our research questions. However, we eventually concluded that the dataset cannot support a reliable categorization of the products at its current form. Inevitably, we drop this idea and the associated research questions.
- One of the main goals of our project was to provide, for each product, a relative view of the nutritional rating, based on its category. We explore this idea in the [categories exploration](./categories_exploration.ipynb) notebook. Not having a reliable category tree restricts us from effectively answering this question: we would need to work on manually curated categories. Also, after thinking about it, we consider this idea is a bit too simple. We cannot come up with ideas on what else we can do relative to that question. That's why in the future we won't focus on this one.
- For the previous milestone, we had wondered if a direct clustering on the nutrient information would yield interesting insights about latent nutrition categories. In the [nutrient clusters exploration](./nutrient_clusters_exploration.ipynb) notebook, we explore the suitability of the dataset for answering this question and describe the challenges we will have to address. A particularly serious challenge concerns defining and handling missing data. Our next step is to implement, tune and evaluate the clustering model, and interpret the results in terms of products, categories and nutritional value.
- In the [colorthief exploration](./colorthief_exploration.ipynb) notebook, we introduce a new direction we will explore. We draw inspiration from studies that reveal how consumers perceive the nutritional value of a product differently based on the colour of its packaging. The dataset enables us to explore if such a link actually exists. In the notebook, you can find a simple description of how we plan to extract colour information from the packaging of the products.
 - In the `health_candies` directory you can find some custom scripts required to run the project.

### Research questions - Revisited
- What interesting insights can we get from clustering products based on their nutrition facts?
    - What do these groups resemble? (e.g. whole-grain products? protein-heavy products?)
    - Are there any unexpected clusters?
    - What can we tell from the distribution of the nutritional rating inside each cluster?
- Is there a link between the colour palette of a product packaging and its nutritional value? How does this relate to past studies on how product packaging is perceived by consumers and influences their purchase decisions?


## Plan towards milestone 3

### Week 1

- Provisionally implement and evaluate the nutrient clustering models, interpret results.
- Extract colour palette for all products and explore obvious links to nutritional score.
- Compile literature sources on consumer perception of packaging colours.

### Week 2

- Use feedback from preliminary nutrient clustering tests to reach design decisions and extract final insights.
- Work on final insights about the link between packaging colour and nutritional rating, and connect it to consumer perception.
- Set up the website for the data story.
- Make a sketch of the visualizations and draft the textual content of the story.

### Week 3

- Put everything together. Have the final data story up and running.
- At the end, have a nice, sweet, cold :beer:.
