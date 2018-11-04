# Title

**Healthy Candies**

# Abstract

Diet quality is, without a doubt, a major concern these days. Nutritional rating systems are among the tools that aim to guide consumers towards healthier products. However, such ratings often indicate how nutritional a generic group of products is, and may be less helpful when deciding among products of the same category. Let’s just say, you *really* want some candies; you get some from the rack, but can you tell - in the blink of an eye - that they were the healthiest candies you could have chosen?

In this project, we explore the different ways a product can be evaluated against its ‘peers’, rather than products that are predictably very different. We examine both homogeneity inside product categories and cross-category divergence, as well as their relationship. We also investigate whether similarities between products can transcend categories: we attempt to reveal nutritional “clusters,” compare them to categories and assess if they could provide a better context for evaluating products.

# Research questions

- What interesting insights do we get by looking at the distribution of the nutritional rating inside each product category?

  - Can we find a relevant level of granularity when speaking of product categories?

  - In terms of nutritional rating, how similar are products inside a category to each other? How much do they differ from products in other categories?

  - Are there products that diverge far from other products in their category? Do these products actually exist ("food extremists") or are they errors in the data?

- Can we produce a nutritional rating for each product in terms of the nutritional rating of its category?

  - How does the new rating change our view of the data?

  - Can we group the products based on the new score? What properties do the resulting groups share?

- How does the picture change when we attempt to cluster products directly based on their nutrition facts?

  - What do these groups resemble? (e.g. whole-grain products? protein-heavy products?)

  - Are there any unexpected clusters?

  - What can we tell from the distribution of the nutritional rating inside each cluster?

# Dataset

The dataset we are going to focus on is a CSV dump from the [*openfoodfacts*](https://world.openfoodfacts.org/) database (actually it’s more like a TSV file because the columns are separated using a `<TAB>` character). Therefore, the dataset itself is nicely structured. The full schema of the csv file is available [*here*](https://static.openfoodfacts.org/data/data-fields.txt). Among the data we can find for each product, there is:

- The name of the product,
- Some categories the product may fit in,
- Information on its ingredients,
- Information on nutritive facts (e.g. amount of saturated fat for 100 g, etc.)
- Two different nutrition scores. Those scores are computed through a process described [*here*](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/216094/dh_123492.pdf) (for the UK nutrition score) and [*here*](http://www.euro.who.int/__data/assets/pdf_file/0006/357243/PHP-Vol3-Issue4-December-2017-rus.pdf#page=178) (for the French nutrition score. It has to be said that some early exploration revealed (this would need to be double-checked) that the British nutrition score seems not to be filled for any products and for the French nutrition score, we have the information for $\approx 20\%$ of all of the $\approx 700\, 000$ products.

**It is also very important to note that the database is mainly built in a collaborative fashion:** a smartphone app is distributed and the community is free to add and modify products. The data itself is not really *checked*. As a result, it is full of inconsistencies (we will have to check this more in depth at the beginning of our work). This is especially true as some the fields are either filled *by hand* and/or using Optical Character Recognition (OCR) which can sometimes produce bad results. For example, if we look at [*this product*](https://world.openfoodfacts.org/product/0000000003827/suedois-saumon-crous) the list of ingredients has inconsistent values: “c)b'oulette” for “ciboulette”. On the other hand, the nutritive facts seems a bit better (there are still inconsistencies).

As a result, we will have to take a lot of care when using (and making conclusions about) the data and be realistic on the fact that some data might not be easily inferred (when missing or wrong).

The dataset also seems quite sparse (either missing values, or values that we would consider as missing; e.g.: `en:packaging-code-to-be-completed`). And some fields seem to have a specific internal structure that could be parsed too.

To put it in a nutshell, this dataset looks awesome from the outside, with very interesting data, but it is full of challenges in the inside.

We might use other (complementary) datasets in the future, but none has been identified at this time.

# A list of internal milestones up until project milestone 2

- Take a deeper look at the dataset:
  - Identify interesting columns and clean inconsistencies.

  - Confirm or redefine our initial research questions based on the exploration, and assess the need for complementary datasets.

  - Keep track of interesting facts for the final data story.

- Learn more about nutrition to better understand the issue at hand.
- Start analyzing the dataset in order to get some preliminary answers to our questions.
- Develop a provisional skeleton for the data story.

# Questions for TAs

- What do you think of the project idea? Sounds feasible/realistic?
- Would you have other research questions we should look at?
