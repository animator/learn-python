# Apriori Algorithm
The Apriori Algorithm is one of the algorithms used for transaction data in Association Rule Learning. It helps us to mine the frequently 
occurring itemset in order to develop association rules between them.

The Apriori method generates association rules using common itemsets and is intended to be used with transactional databases. The association 
rules govern how strongly or weakly two objects are associated.

Example: A list of things purchased by consumers, Information about commonly frequented websites, etc.

# What is Frequent Itemset?
Frequent itemsets are ones whose support exceeds the threshold value or the user-specified minimum support.  It means if A & B are the 
frequent itemsets together, then individually A and B should also be the frequent itemset.
Suppose there are the two transactions: A= {1,2,3,4,5}, and B= {2,3,7}, in these two transactions, 2 and 3 are the frequent itemsets.

# Apriori Algorithm has three parts
1. Support: It is one of the two basic parameters of association rules. It is the ratio of the number of transactions containing both x and
y in All sample of dataset D to all transactions. If we have two data x and y that need to be analyzed for correlation, then the
corresponding support degree is:

**Support**(x, y) = `P(xy) = num(xy) / num(All Samples)`

$$
Support(X \Rightarrow Y) = P(X \cup Y) = \frac{\text{count}(X \cup Y)}{|D|}
$$

For example, a support rating of 28% means that “there is a 28% probability that an individual in the population will contain both X 
and Y”.

2. Confidence: Confidence: It is the ratio of the number of transactions including x and y to the number of transactions including y,
namely conditional probability.

$$
Confidence(x \Rightarrow y) = P(x|y) = \frac{P(xy)}{P(y)}
$$

$$
Confidence(X \Rightarrow Y) = P(X|Y) = \frac{Support(X \cup Y)}{Support(X)}
$$


Assuming that “52% of the terms containing X contain Y”, the confidence is 52%.

3. Lift: It is the ratio of the number of transactions containing x under the premise of including y to the total number of transactions
occurring in x.

$$
Lift(x \Rightarrow y) = \frac{P(x|y)}{P(x)}= \frac{Confidence(x \Rightarrow y)}{P(x)}
$$

> **Note:**
>
> Lift uses 1 as the target value to show the relationship between x and y. If the value is greater than 1, then \( x \Rightarrow y ) is a valid strong association rule. Conversely, ( x \Rightarrow y ) is an invalid strong association rule. When the value is equal to 1, however, there is a special case, that is, x and y are at independence, at the time ( P(x|y) = P(x) ), so Lift( x \Rightarrow y) = 1.


# Steps for Apriori Algorithm
1. Determine the support of itemsets in the transactional database, and select the minimum support and confidence.
2. Take all supports in the transaction with higher support value than the minimum or selected support value.
3. Find all the rules of these subsets that have higher confidence value than the threshold or minimum confidence.
4. Sort the rules as the decreasing order of lift.

# How it Works?
We will understand the apriori algorithm using an example and mathematical calculation:
