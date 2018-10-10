tm1722 review of ks5063 citibike project

#### Null and Alternative hypotheses:
Idea: Young people are more likely to be subscribers of Citibike

* Hypotheses are presented quite well in both words and formulas, but there is a room for imporvement. 

* The null hypothesis can be considered mathematically testable since it relies on what we can measure precisely (average ages for two samples -- users who are subscribers and users who are customers). To improve, I would also indicate a specific timeframe for analysis (the author uses June 2018 later on) and specify the significance level of \alpha = 0.05 right in the words formulation.

* The alternative hypothesis correctly states what the author's Idea in testable and mathematical terms.


#### Data -- Does it have proper features to answer the question? Was it properly modified to extract needed values for the analysis? 
* For the hypothesis testing, we need to see data relating to the age of user, indication of what kind of user they are (subscriber vs customer), and a specific timeframe. 

* The data manipulation ensures a specific dataframe, which takes care of the concern above. 

* From the graphs provided, it is obvious that there are a lot more datapoints for subscribers than for customers. However, since we are interested in comparing average means of two samples, this should be of minimal concern. 

* The histogram is helpful in understanding distributions of both samples.


#### Choosing a test:

* The author wants to know if there is a difference in average ages of riders between __two groups__. 

* It is an __unpaired situation__ since groups are parallel and independent.

* The author is working with numerical data (ages of riders).

* The histograms didn't suggest a normal (or any other common) distribution and we don't know parameters of the population. Thus, a __nonparametric analysis__ should be used.

* Based on all of the abouve, the author should use Mann-Whitney U Test or Wilcoxon's Rank Sum Test.