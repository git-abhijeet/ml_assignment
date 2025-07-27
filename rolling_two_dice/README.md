# Rolling Two Dice Simulation

This project simulates rolling two 6-sided dice 10,000 times to estimate probabilities for specific sum outcomes.

## Objective

Estimate the following probabilities using simulation (not formula):

-   **P(Sum = 7)** - Probability that the sum of two dice equals 7
-   **P(Sum = 2)** - Probability that the sum equals 2
-   **P(Sum > 10)** - Probability that the sum is greater than 10 (i.e., 11 or 12)

## Files

-   `simple_dice.py` - Simple implementation following exact assignment instructions
-   `dice_simulation.py` - Comprehensive implementation with detailed analysis and helper functions
-   `test_dice.py` - Test suite to verify simulation accuracy and functionality
-   `README.md` - This documentation file

## Usage

### Run the simple version (matches assignment exactly):

```bash
python simple_dice.py
```

### Run the comprehensive version:

```bash
python dice_simulation.py
```

### Run tests:

```bash
python test_dice.py
```

## Expected Output Format

```
P(Sum = 7): 0.1678
P(Sum = 2): 0.0271
P(Sum > 10): 0.0836
```

_Note: The output values will vary slightly on each run due to randomness._

## Implementation Details

### Algorithm Steps:

1. Import random module
2. Loop 10,000 times:
    - Randomly generate two integers between 1 and 6
    - Compute the sum of the dice
    - Count how often the sum is 7, 2, or greater than 10
3. Divide each count by 10,000 to get the estimated probability
4. Print the results

### Theoretical Probabilities (for comparison):

-   **P(Sum = 7)**: 6/36 = 0.1667 (ways to get 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1)
-   **P(Sum = 2)**: 1/36 = 0.0278 (only way: 1+1)
-   **P(Sum > 10)**: 3/36 = 0.0833 (ways: 5+6, 6+5, 6+6)

## Features

### Simple Version (`simple_dice.py`):

-   Clean, minimal code following exact assignment instructions
-   Direct implementation without extra functions
-   Outputs exactly as specified

### Comprehensive Version (`dice_simulation.py`):

-   Modular function-based design
-   Detailed analysis showing all possible sum frequencies
-   Comparison with theoretical probabilities
-   Additional statistics and insights

### Test Suite (`test_dice.py`):

-   Validates simulation accuracy
-   Tests edge cases and bounds checking
-   Demonstrates reproducibility with random seeds
-   Shows variability across multiple trials

## Key Concepts Demonstrated

-   **Monte Carlo Simulation**: Using random sampling to estimate probabilities
-   **Law of Large Numbers**: As sample size increases, estimated probabilities converge to theoretical values
-   **Random Number Generation**: Using Python's `random` module for dice simulation
-   **Statistical Analysis**: Comparing simulated vs. theoretical results
