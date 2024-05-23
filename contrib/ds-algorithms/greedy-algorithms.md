# Greedy Algorithms

Greedy algorithms are simple, intuitive algorithms that make a sequence of choices at each step with the hope of finding a global optimum. They are called "greedy" because at each step, they choose the most advantageous option without considering the future consequences. Despite their simplicity, greedy algorithms are powerful tools for solving optimization problems, especially when the problem exhibits the greedy-choice property.

## Real-Life Examples of Greedy Algorithms
- **Coin Change:** Finding the minimum number of coins to make a certain amount of change.
- **Job Scheduling:** Assigning tasks to machines to minimize completion time.
- **Huffman Coding:** Constructing an optimal prefix-free binary code for data compression.
- **Fractional Knapsack:** Selecting items to maximize the value within a weight limit.

# Some Common Greedy Algorithms

# 1. Coin Change Problem

The coin change problem is a classic example of a greedy algorithm. Given a set of coin denominations and a target amount, the objective is to find the minimum number of coins required to make up that amount.

**Algorithm Overview:**
- **Greedy Strategy:** At each step, the algorithm selects the largest denomination coin that is less than or equal to the remaining amount.
- **Repeat Until Amount is Zero:** The process continues until the remaining amount becomes zero.

## Coin Change Code in Python

```python
def coin_change(coins, amount):
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        num_coins += amount // coin
        amount %= coin
    if amount == 0:
        return num_coins
    else:
        return -1

coins = [1, 5, 10, 25]
amount = 63
result = coin_change(coins, amount)
if result != -1:
    print(f"Minimum number of coins required: {result}.")
else:
    print("It is not possible to make the amount with the given denominations.")
```

## Complexity Analysis
- **Time Complexity**: O(n log n) for sorting (if not pre-sorted), O(n) for iteration
- **Space Complexity**: O(1)

</br>
<hr>
</br>

# 2. Activity Selection Problem

The activity selection problem involves selecting the maximum number of mutually compatible activities that can be performed by a single person or machine, assuming that a person can only work on one activity at a time.

**Algorithm Overview:**
- **Greedy Strategy:** Sort the activities based on their finish times.
- **Selecting Activities:** Iterate through the sorted activities, selecting each activity if it doesn't conflict with the previously selected ones.

## Activity Selection Code in Python

```python
def activity_selection(start, finish):
    n = len(start)
    activities = []
    i = 0
    activities.append(i)
    for j in range(1, n):
        if start[j] >= finish[i]:
            activities.append(j)
            i = j
    return activities

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
selected_activities = activity_selection(start, finish)
print("Selected activities:", selected_activities)
```

## Complexity Analysis
- **Time Complexity**: O(n log n) for sorting (if not pre-sorted), O(n) for iteration
- **Space Complexity**: O(1)

</br>
<hr>
</br>

# 3. Huffman Coding

Huffman coding is a method of lossless data compression that efficiently represents characters or symbols in a file. It uses variable-length codes to represent characters, with shorter codes assigned to more frequent characters.

**Algorithm Overview:**
- **Frequency Analysis:** Determine the frequency of each character in the input data.
- **Building the Huffman Tree:** Construct a binary tree where each leaf node represents a character and the path to the leaf node determines its code.
- **Assigning Codes:** Traverse the Huffman tree to assign codes to each character, with shorter codes for more frequent characters.

## Huffman Coding Code in Python

```python
from heapq import heappush, heappop, heapify
from collections import defaultdict

def huffman_coding(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapify(heap)

    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

data = "Huffman coding is a greedy algorithm"
encoded_data = huffman_coding(data)
print("Huffman Codes:")
for symbol, code in encoded_data:
    print(f"{symbol}: {code}")
```

## Complexity Analysis
- **Time Complexity**: O(n log n) for heap operations, where n is the number of unique characters
- **Space Complexity**: O(n) for the heap

</br>
<hr>
</br>
