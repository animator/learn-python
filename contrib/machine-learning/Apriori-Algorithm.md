# Apriori Algorithm
The Apriori Algorithm is one of the algorithms used for transaction data in Association Rule Learning. It helps us to mine the frequently occurring itemset in order to develop association rules between them.
The Apriori method generates association rules using common itemsets and is intended to be used with transactional databases. The association 
rules govern how strongly or weakly two objects are associated.

Example: A list of things purchased by consumers, Information about commonly frequented websites, etc.

## What is Frequent Itemset?
Frequent itemsets are ones whose support exceeds the threshold value or the user-specified minimum support.  It means if A & B are the 
frequent itemsets together, then individually A and B should also be the frequent itemset.
Suppose there are the two transactions: A= {1,2,3,4,5}, and B= {2,3,7}, in these two transactions, 2 and 3 are the frequent itemsets.

## Apriori Algorithm has three parts
1. Support: It is one of the two basic parameters of association rules. It is the ratio of the number of transactions containing both x and
y in All sample of dataset D to all transactions. If we have two data x and y that need to be analyzed for correlation, then the
corresponding support degree is:

**Support**(x, y) = `P(xy) = num(xy) / num(All Samples)`

$$
Support(X \Rightarrow Y) = P(X \cup Y) = \frac{\text{count}(X \cup Y)}{|D|}
$$

For example, a support rating of 28% means that “there is a 28% probability that an individual in the population will contain both X 
and Y”.

2. Confidence: It is the ratio of the number of transactions including x and y to the number of transactions including y,
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


## Steps for Apriori Algorithm
1. Determine the support of itemsets in the transactional database, and select the minimum support and confidence.
2. Take all supports in the transaction with higher support value than the minimum or selected support value.
3. Find all the rules of these subsets that have higher confidence value than the threshold or minimum confidence.
4. Sort the rules as the decreasing order of lift.

## How it Works?
We will understand the apriori algorithm using an example and mathematical calculation:
Example: Suppose we have the following dataset that has various transactions, and from this dataset, we need to find the frequent itemsets and generate the association rules using the Apriori algorithm:

| TID      | ITEMSETS |
|----------|----------|
| T1       | A,B      |
| T2       | B,D      |
| T3       | B,C      |
| T4       | A,B,D    |
| T5       | A,C      |
| T6       | B,C      |
| T7       | A,C      |
| T8       | A,B,C,E  |
| T9       | A,B,C    |

Given: Minimum Support=2, Minimum Confidence = 50%

### Solution
Step-1: Calculating C1 and L1 <br>
In the first stage, we will generate a table containing the support count (the frequency of each itemset individually in the dataset) for each itemset in the dataset. This table is known as the Candidate Set, or C1.

| Itemset  | Support Count |
|----------|---------------|
| A        | 6             |
| B        | 7             |
| C        | 5             |
| D        | 2             |
| E        | 1             |

We will now remove all itemsets with a support count greater than the Minimum Support (2). It will provide us with the table for the frequent itemset L1. Since all the itemsets have greater or equal support count than the minimum support, except the E, so E itemset will be removed.

| Itemset  | Support Count |
|----------|---------------|
| A        | 6             |
| B        | 7             |
| C        | 5             |
| D        | 2             |

Step-2: Candidate Generation C2, and L2 <br>
We will use L1 to help us generate C2 in this stage. We are going to construct the two itemsets of L1 as subsets in C2.
Once the subsets have been created, we will once more retrieve the support count—that is, the number of times these pairs have occurred together in the dataset—from the main transaction table. As a result, we will obtain the C2 table below:

| Itemset  | Support Count |
|----------|---------------|
| {A,B}    | 4             |
| {A,C}    | 4             |
| {A,D}    | 1             |
| {B,C}    | 4             |
| {B,D}    | 2             |
| {C,D}    | 0             |

Once more, we must compare the C2 Support count with the minimum Support count. The itemset with the lower Support count will be removed from the C2 table following the comparison. It will provide us with the L2 table below.

| Itemset  | Support Count |
|----------|---------------|
| {A,B}    | 4             |
| {A,C}    | 4             |
| {B,C}    | 4             |
| {B,D}    | 2             |

Step-3: Candidate generation C3, and L3 <br>
The two proccesses will be repeated for C3, but this time we will create the C3 table by combining subsets of the three item sets, and we will compute the support count from the dataset. It will display the table below:

| Itemset  | Support Count |
|----------|---------------|
| {A,B,C}  | 2             |
| {B,C,D}  | 1             |
| {A,C,D}  | 0             |
| {A,B,D}  | 0             |

We will now construct the L3 table. The C3 table above shows that there is only one possible combinations of itemsets for which the support count is equal to the required minimum. As a result, {A, B, C} will be the only combination that the L3 has. <br>

Step-4: Finding the association rules for the subsets
In order to produce the association rules, we must first make a new table containing all potential rules from the combination {A, B.C} that has occurred. We will use formula sup(A ^B)/A to determine the Confidence for each rule. We will eliminate the rules with confidence levels below the 50% threshold after determining the confidence value for each rule.

Consider the below table:

| Rules      | Support  | Confidence                              |
|------------|----------|-----------------------------------------|
| A ^ B → C  | 2        | Sup{(A ^B) ^C}/sup(A ^B)= 2/4=0.5=50%   |
| B ^ C → A  | 2        | Sup{(B^C) ^A}/sup(B ^C)= 2/4=0.5=50%    |
| A ^ C → B  | 2        | Sup{(A ^C) ^B}/sup(A ^C)= 2/4=0.5=50%   |
| C → A ^B   | 2        | Sup{(C^( A ^B)}/sup(C)= 2/5=0.4=40%     |
| A -> B ^ C | 2        | Sup{(A^( B ^C)}/sup(A)= 2/6=0.33=33.33% |
| B → B ^ C  | 2        | Sup{(B^( B ^C)}/sup(B)= 2/7=0.28=28%    |

The first three rules— A ^ B → C, B ^ C → A, and A ^ C → B can be considered as the strong association rules for the given situation because the specified threshold or minimal confidence is 50%. <br>

## Advantages of Apriori Algorithm <br>
This is easy to understand algorithm. Among association rule learning algorithms, this is the simplest and most straightforward algorithm. The resulting rules are simple to understand and express to the end-user.

## Disadvantages of Apriori Algorithm <br>
The main disadvantage is the slow process, to create candidates, the algorithm must continually search the database; this operation consumes a significant amount of time and memory, particularly if the pattern is very lengthy.

## Python Implementation of Apriori Algorithm <br>
