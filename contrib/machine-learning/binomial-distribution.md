# Binomial Distribution

## Introduction

The binomial distribution is a discrete probability distribution that describes the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success. It is commonly used in statistics and probability theory.

### Key Characteristics

- **Number of trials (n):** The number of independent experiments or trials.
- **Probability of success (p):** The probability of success on an individual trial.
- **Number of successes (k):** The number of successful outcomes in n trials.

The binomial distribution is defined by the probability mass function (PMF):

P(X = k) = (n choose k) p^k (1 - p)^(n - k)

where:
- (n choose k) is the binomial coefficient, calculated as n! / (k!(n-k)!).

## Properties of Binomial Distribution

- **Mean:** μ = np
- **Variance:** σ² = np(1 - p)
- **Standard Deviation:** σ = √(np(1 - p))

## Python Implementation

Let's implement the binomial distribution using Python. We'll use the `scipy.stats` library to compute the binomial PMF and CDF, and `matplotlib` to visualize it.

### Step-by-Step Implementation

1. **Import necessary libraries:**

    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import binom
    ```

2. **Define parameters:**

    ```python
    # Number of trials
    n = 10
    # Probability of success
    p = 0.5
    # Number of successes
    k = np.arange(0, n + 1)
    ```

3. **Compute the PMF:**

    ```python
    pmf = binom.pmf(k, n, p)
    ```

4. **Plot the PMF:**

    ```python
    plt.bar(k, pmf, color='blue')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.title('Binomial Distribution PMF')
    plt.show()
    ```

5. **Compute the CDF:**

    ```python
    cdf = binom.cdf(k, n, p)
    ```

6. **Plot the CDF:**

    ```python
    plt.plot(k, cdf, marker='o', linestyle='--', color='blue')
    plt.xlabel('Number of Successes')
    plt.ylabel('Cumulative Probability')
    plt.title('Binomial Distribution CDF')
    plt.grid(True)
    plt.show()
    ```

### Complete Code

Here is the complete code for the binomial distribution implementation:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Parameters
n = 10  # Number of trials
p = 0.5  # Probability of success

# Number of successes
k = np.arange(0, n + 1)

# Compute PMF
pmf = binom.pmf(k, n, p)

# Plot PMF
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(k, pmf, color='blue')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title('Binomial Distribution PMF')

# Compute CDF
cdf = binom.cdf(k, n, p)

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(k, cdf, marker='o', linestyle='--', color='blue')
plt.xlabel('Number of Successes')
plt.ylabel('Cumulative Probability')
plt.title('Binomial Distribution CDF')
plt.grid(True)

plt.tight_layout()
plt.show()
