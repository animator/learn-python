## Decision Trees

**Introduction**

Decision Tree is a supervised machine learning model, which means the model learns from labeled data. Decision trees are popular in machine learning because they are easy to understand and interpret. This can perform both regression and classification tasks. But most of the time decision trees are used for classification tasks. Decision tree performs classification tasks like predicting spam mails, etc and regression tasks like predicting house price, etc. Decision trees are flexible and can accept both categorical and continuous data for features. The type of target variable (categorical or continuous) depends on whether we’re performing a classification or regression task. Some of the decision tree algorithms are ID3, Random tree and more.

**Decision Tree Structure terminology**

Decision trees are tree like structures. Tree is formed using nodes and edges. Node represents an attribute and edge represents condition or outcome of a question. There are some technical terms to specify these nodes. Those are,
Root Node: This the top most node and starting point of the tree. It has no parent node but can have multiple child nodes. This node represents independent attribute.
Internal Nodes: This node has parent node and child nodes. These nodes are in between the root node and leaf nodes. This node represents independent attribute. Internal nodes specifically focus on the decision or question being asked about that attribute.
Leaf Nodes or Terminal Nodes: These are end points of the tree, representing the final outcome or prediction. They have a parent node but no child nodes. This node represents the target variable or dependent attribute.

![image](https://github.com/sarayusreeyadavpadala/learn-python/assets/134043600/bf2ffe03-6ae8-4c4e-962b-dbfc261d097b)

**Decision Tree Structure Formation**

Decision tree can be formed using the training dataset. How we can form a decision tree that can correctly predict the target variable? There are exponentially many decision trees that can be formed using
the given set of attributes. While some of the decision trees are accurate than others. Finding optimal decision tree (that is good in generalization) manually, is a time-consuming task. Some algorithms
were developed to induce decision tree. One of the algorithms is Hunt’s Algorithm, which is the basis of many popular decision tree algorithms like ID3, C4.5 and CART etc.

_**Hunt’s Algorithm**_

In Hunt’s algorithm, a decision tree is grown in a recursive fashion by partitioning the training records into successively purer subsets. Let Dt be the set of training records that are associated with 
node t and Y = {Y1, Y2, …., Yn} be the class labels.

The recursive definition of Hunt’s algorithm

Step 1: If all the records in Dt belong to the same class Yt, then t is a leaf node labeled as Yt.

Step 2: If Dt contains records that belong to more than one class, an attribute test condition is selected to partition the records into smaller subsets. A child node is created for each outcome of the
test condition and records in Dt are distributed to the children based on the outcomes. The algorithm is then recursively applied to each child node.

![image](https://github.com/sarayusreeyadavpadala/learn-python/assets/134043600/030c673e-841f-4aab-8b51-f6aa5c103a5f)

How do we split those attributes? Using some popular measures, we can easily find the best split.

**Measures for Selecting the Best Split**
There are three main ways to find the best split in a decision tree algorithm. They are,
1. Information Gain
2. Gini Impurity
3. Gain Ratio

_Information Gain:_

Before going to information gain, we need to understand entropy. Entropy basically tells us how impure a collection of data is. Here, impure means non-homogeneity. Entropy is the measurement of
homogeneity. Information gain is calculated using entropy. The formula of entropy is given as,

![image](https://github.com/sarayusreeyadavpadala/learn-python/assets/134043600/c01b83b0-0858-4500-89a4-d4b186ef2146)

Here, ‘S’ is the dataset. Positive and negative examples are the class labels.

In decision trees, information gain measures how much a specific feature helps you learn more about the target variable by reducing the overall uncertainty (entropy) in the data through effective 
splitting. Information Gain values are numerical scores between 0 and 1 that tell you how much a specific feature (attribute) in your data helps you learn about the target variable. Higher Information gain
(closer to 1) means when you split the data based on this feature, the entropy of the data reduces significantly. Lower information gain (closer to 0) means when splitting on this feature doesn't do much 
to separate the data points into distinct categories. Information gain of 0 means the feature doesn’t provide any information about the target variable. Here’s the formula for information gain,

![image](https://github.com/sarayusreeyadavpadala/learn-python/assets/134043600/6323d84f-f2a9-4261-ba28-e25c71cef3ef)

Thus, we can split the dataset using information gain and entropy.

_Gini Impurity:_

This is another way to find the best split. Gini impurity is the measure of the impurity or disorder in a set of elements. If G=0, then it indicates a perfectly pure node. If G=0.5, then it indicates 
maximum impurity. The gini impurity is calculated as follows,

![image](https://github.com/sarayusreeyadavpadala/learn-python/assets/134043600/5cad7821-35f8-4287-8ed8-95282d70a068)

_Gain Ratio:_

This is another way to find the best split. This can overcome the problems that we encounter while using information gain. We use gain ratio instead of information gain in some cases. The problems with
information gain are,
•	Biased towards attributes with many values.
•	Won’t work for new data.
In these cases, we cannot get good results by using information gain. That’s why we use gain ratio. Gain Ratio is a measure that takes into account both the information gain and the number of outcomes of a
feature to determine the best feature to split on. Gain ratio calculated using information gain and split entropy. The formula is given as,
                               Gain Ratio(A) = Information Gain(A) / Split Information(A)
                               
where split info = ![image](https://github.com/sarayusreeyadavpadala/learn-python/assets/134043600/36fcaf57-4487-49ab-9ffc-176c5be264c4)
D(i) is the probability of each outcome i in the attribute                            
                              
                              
The lower the value of split info, the better the split is considered to be.

So, these are the three ways to find or selecting the best split.

We can implement decision trees using scikit-learn and TensorFlow. Will cover some more concepts on decision tree like advantages and disadvantages, implementation using scikit-learn and TensorFlow,
Advanced concepts, random forest, etc. These are the basic concepts of Decision Trees. Thus how, we can create decision tree.
