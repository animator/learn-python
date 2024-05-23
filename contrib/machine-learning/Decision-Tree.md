# Decision Trees
Decision trees are a type of supervised machine learning algorithm that is mostly used in classification problems. They work for both categorical and continuous input and output variables.

It is also interpreted as acyclic graph that can be utilized for decision-making is called a decision tree. Every branching node in the graph looks at a particular feature (j) of the feature vector. The left branch is taken when the feature's value is less than a certain threshold; the right branch is taken when it is higher. The class to which the example belongs is decided upon as soon as the leaf node is reached.

## Key Components of a Decision Tree
**Root Node:** This is the decision tree's first node, and it symbolizes the whole population or sample.

**Internal Nodes:** These are the nodes that make decisions and they stand in for the characteristics or features.

**Leaf Nodes:** These are the nodes that make decisions and they stand in for the characteristics or features.

**Branches:** These are the lines that connect the nodes, and they show how the choice was made depending on the feature value.

### Example: Predicting Loan Approval

In this example, we will use a decision tree to forecast the approval or denial of a loan application based on a number of features, including job status, credit score, and income.

```
                      Root Node
                  (All Applications)
               /                     \
      Internal Node                  Internal Node
     (Credit Score)                 (Employment Status)
     /                \                 /             \
 Leaf Node           Leaf Node       Leaf Node       Leaf Node
(Approve Loan)      (Deny Loan)     (Approve Loan)   (Deny Loan)
```
> There are various formulations of the decision tree learning algorithm.    Here, we consider just one, called ID3.

## Appropriate Problems For Decision Tree Learning
In general, decision tree learning works best on issues that have the following characteristics:
1. ***Instances*** are represented by ***key-value pairs***
2. The ***output values of the target function are discrete***. Each sample is given a Boolean categorization (yes or no) by the decision tree. Learning functions with multiple possible output values can be effortlessly integrated into decision tree approaches.
3. ***Disjunctive descriptions may be required***
4. The ***training data may contain errors*** – ***Decision tree learning methods are robust to errors,*** both errors in classifications of the training examples and errors in the attribute
values that describe these examples.
5. ***Missing attribute values could be present in the training data.*** Using decision tree approaches is possible even in cases where some training examples have missing values.

# Decision Tree Algorithm
The decision tree method classifies the data according to a tree structure. The root node, that holds the complete dataset, is where it all begins. The algorithm then determines which feature, according to a certain criterion like information gain or Gini impurity, is appropriate for splitting the dataset. Subsets of the dataset are then created according to the values of the chosen feature. Until a halting condition is satisfied—for example, obtaining a minimal number of samples per leaf node or a maximum tree depth—this procedure is repeated recursively for every subset.


### Which Attribute Is the Best Classifier?
- The ID3 algorithm's primary idea is choose which characteristic to test at each tree node.
- Information gain, a statistical feature that quantifies how well a certain attribute divides the training samples into groups based on the target classification.
- When building the tree, ID3 chooses a candidate attribute  using the information gain metric.

## Entropy & Information

**Entropy** is a metric that quantifies the level of impurity or uncertainty present in a given dataset. When it comes to decision trees, entropy measures how similar the target variable is within a specific node or subset of the data. It is utilized for assessing the quality of potential splits during the tree construction process.

The entropy of a node is calculated as:   
__Entropy = -Σ(p<sub>i</sub> * log<sub>2</sub>(p<sub>i</sub>))__

where `p`<sub>`i`</sub> is the proportion of instances belonging to class `i` in the current node. The entropy is at its maximum when all classes are equally represented in the node, indicating maximum impurity or uncertainty.

**Information Gain** is a measure used to estimate the possible reduction in entropy achieved by separating the data according to a certain attribute. It quantifies the projected decrease in impurity or uncertainty after the separation.

The information gain for a feature `A` is calculated as:  
__Information Gain = Entropy(parent) - Σ(weight(child) * Entropy(child))__

### Example of a Decision Tree
Let us look at a basic decision tree example that predicts a person's likelihood of playing tennis based on climate conditions

**Data Set:**
---
| Day | Outlook | Temperature | Humidity | Wind | PlayTennis |
|-----|---------|-------------|----------|------|------------|
| D1  | Sunny   | Hot         | High     | Weak | No         |
| D2  | Sunny   | Hot         | High     | Strong | No       |
| D3  | Overcast| Hot         | High     | Weak | Yes        |
| D4  | Rain    | Mild        | High     | Weak | Yes        |
| D5  | Rain    | Cool        | Normal   | Weak | Yes        |
| D6  | Rain    | Cool        | Normal   | Strong | No       |
| D7  | Overcast| Cool        | Normal   | Strong | Yes      |
| D8  | Sunny   | Mild        | High     | Weak | No         |
| D9  | Sunny   | Cool        | Normal   | Weak | Yes        |
| D10 | Rain    | Mild        | Normal   | Weak | Yes        |
| D11 | Sunny   | Mild        | Normal   | Strong | Yes      |
| D12 | Overcast| Mild        | High     | Strong | Yes      |
| D13 | Overcast| Hot         | Normal   | Weak | Yes        |
| D14 | Rain    | Mild        | High     | Strong | No       |
---


1. Calculate the entropy of the entire dataset.
2. For each feature, calculate the information gain by splitting the data based on that feature.
3. Select the feature with the highest information gain to create the root node.
4. Repeat steps 1-3 for each child node until a stopping criterion is met (e.g., all instances in a node belong to the same class, or the maximum depth is reached).

Let's start with calculating the entropy of the entire dataset:
Total instances: 14
No instances: 5
Yes instances: 9

**Entropy** = -((5/14) * log2(5/14) + (9/14) * log2(9/14)) = 0.940

Now, we'll calculate the information gain for each feature:

**Outlook**:
- Sunny: 2 No, 3 Yes (Entropy = 0.971)
- Overcast: 0 No, 4 Yes (Entropy = 0)
- Rain: 3 No, 2 Yes (Entropy = 0.971)

Information Gain = 0.940 - ((5/14) * 0.971 + (4/14) * 0 + (5/14) * 0.971) = 0.246

**Temperature**:
- Hot: 2 No, 2 Yes (Entropy = 1)
- Mild: 2 No, 4 Yes (Entropy = 0.811)
- Cool: 1 No, 3 Yes (Entropy = 0.918)

Information Gain = 0.940 - ((4/14) * 1 + (6/14) * 0.811 + (4/14) * 0.918) = 0.029

**Humidity**:
- High: 3 No, 4 Yes (Entropy = 0.985)
- Normal: 2 No, 5 Yes (Entropy = 0.971)

Information Gain = 0.940 - ((7/14) * 0.985 + (7/14) * 0.971) = 0.012

**Wind**:
- Weak: 2 No, 6 Yes (Entropy = 0.811)
- Strong: 3 No, 3 Yes (Entropy = 1)

Information Gain = 0.940 - ((8/14) * 0.811 + (6/14) * 1) = 0.048

The feature with the highest information gain is Outlook, so we'll create the root node based on that.

**Step 1: Root Node (Outlook)**
```
                Root Node (Outlook)
             /          |           \
          Sunny         Overcast      Rain
      Entropy: 0.971   Entropy: 0   Entropy: 0.971
      5 instances      4 instances   5 instances

```

Now, we'll continue building the tree by recursively splitting the child nodes based on the feature with the highest information gain within each subset.

**Step 2: Splitting Sunny and Rain Nodes**

For the Sunny node:
- Temperature: 
    - Hot: 2 No, 0 Yes (Entropy = 0)
    - Mild: 0 No, 3 Yes (Entropy = 0)
    - Cool: 0 No, 0 Yes (Entropy = 0)
    Information Gain = 0.971

- Humidity:
    - High: 1 No, 2 Yes (Entropy = 0.918)
    - Normal: 1 No, 1 Yes (Entropy = 1)
    Information Gain = 0.153

- Wind:
    - Weak: 1 No, 2 Yes (Entropy = 0.918)
    - Strong: 1 No, 1 Yes (Entropy = 1)
    Information Gain = 0.153

The highest information gain is achieved by splitting on Temperature, so we'll create child nodes for Sunny based on Temperature.

For the Rain node:
- Wind:
    - Weak: 1 No, 3 Yes (Entropy = 0.918)
    - Strong: 2 No, 0 Yes (Entropy = 0)
    Information Gain = 0.153

Since there is only one feature left (Wind), we'll create child nodes for Rain based on Wind.

**Step 3: Updated Decision Tree**
```
                  Root Node (Outlook)
             /            |             \
          Sunny         Overcast       Rain
      /    |    \      Entropy: 0     /    \
    Hot   Mild  Cool 4   instances   Weak Strong
  Entropy: 0 Entropy: 0             Entropy: 0.918 Entropy: 0
  2 instances 3 instances           4 instances 1 instance
```
At this point, all leaf nodes are either pure (entropy = 0) or have instances belonging to a single class. Therefore, we can stop the tree construction process.

**Step 4: Pruning the Decision Tree**

The decision tree we constructed in the previous steps is a complete tree that perfectly classifies the training data. However, this can lead to overfitting, meaning the tree may perform poorly on new, unseen data due to its complexity and memorization of noise in the training set.

To address this, we can prune the tree by removing some of the leaf nodes or branches that contribute little to the overall classification accuracy. Pruning helps to generalize the tree and improve its performance on unseen data.

There are various pruning techniques, such as:

1. **Pre-pruning**: Stopping the tree growth based on a pre-defined criterion (e.g., maximum depth, minimum instances in a node, etc.).
2. **Post-pruning**: Growing the tree to its full depth and then removing subtrees or branches based on a pruning criterion.

>We can observe that the "Cool" node under the "Sunny" branch has no instances in the training data. Removing this node will not affect the classification accuracy on the training set, and it may help generalize the tree better.

**Step 5: Pruned Decision Tree**
```
                   Root Node (Outlook)
              /           |              \
             /            |               \
         Sunny       Overcast              Rain
       /       \       Entropy: 0       /          \
     Hot      Mild     4 instances     Weak      Strong
Entropy: 0    Entropy: 0.918        Entropy: 0     Entropy: 0
 2 instances   4 instances         3 instances    2 instances
```

**Step 6: Visualizing the Decision Tree**

Decision trees can be visualized graphically to provide a clear representation of the hierarchical structure and the decision rules. This visualization can aid in understanding the tree's logic and interpreting the results.

There are various tools and libraries available for visualizing decision trees. One popular library in Python is `graphviz`, which can create tree-like diagrams and visualizations.

Here's an example of how to visualize our pruned decision tree using `graphviz` in Python:

```python
import graphviz
from sklearn import tree

# Create a decision tree classifier
decision_tree_classifier = tree.DecisionTreeClassifier()

# Train the classifier on the dataset X and labels y
decision_tree_classifier.fit(X, y)

# Visualize the decision tree
tree_dot_data = tree.export_graphviz(decision_tree_classifier, out_file=None, 
                                     feature_names=['Outlook', 'Temperature', 'Humidity', 'Wind'], 
                                     class_names=['No', 'Yes'], filled=True, rounded=True, special_characters=True)

# Create a graph from the DOT data
graph = graphviz.Source(tree_dot_data)

# Render and save the decision tree as an image file
graph.render("decision_tree")

```
```
                 Outlook
            /       |      \
          Sunny  Overcast  Rain
         /          |      /    \
    Humidity       Yes    Wind  Wind
   /     \                /       \
High   Normal          Weak     Strong
 No      Yes            Yes        No
```

The final decision tree classifies instances based on the following rules:

- If Outlook is Overcast, PlayTennis is Yes
- If Outlook is Sunny and Temperature is Hot, PlayTennis is No
- If Outlook is Sunny and Temperature is Mild, PlayTennis is Yes
- If Outlook is Sunny and Temperature is Cool, PlayTennis is Yes (no instances in the dataset)
- If Outlook is Rain and Wind is Weak, PlayTennis is Yes
- If Outlook is Rain and Wind is Strong, PlayTennis is No

> Note that the calculated entropies and information gains may vary slightly depending on the specific implementation and rounding methods used.