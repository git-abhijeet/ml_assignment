"""
Simple Dice Rolling Simulation
=============================

This is a simplified version that follows the exact instructions 
from the assignment.

Instructions followed:
1. Import random module
2. Loop 10,000 times:
   - Randomly generate two integers between 1 and 6
   - Compute the sum of the dice
   - Count how often the sum is 7, 2, or greater than 10
3. Divide each count by 10,000 to get estimated probability
4. Print the results

Author: GitHub Copilot
Date: July 26, 2025
"""

import random

def main():
    """
    Simple dice rolling simulation following exact assignment instructions.
    """
    # Initialize counters
    count_sum_7 = 0
    count_sum_2 = 0
    count_sum_greater_10 = 0
    
    # Loop 10,000 times
    for _ in range(10000):
        # Randomly generate two integers between 1 and 6
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        # Compute the sum of the dice
        dice_sum = dice1 + dice2
        
        # Count how often the sum is 7, 2, or greater than 10
        if dice_sum == 7:
            count_sum_7 += 1
        if dice_sum == 2:
            count_sum_2 += 1
        if dice_sum > 10:
            count_sum_greater_10 += 1
    
    # Divide each count by 10,000 to get the estimated probability
    prob_sum_7 = count_sum_7 / 10000
    prob_sum_2 = count_sum_2 / 10000
    prob_sum_greater_10 = count_sum_greater_10 / 10000
    
    # Print the results
    print(f"P(Sum = 7): {prob_sum_7:.4f}")
    print(f"P(Sum = 2): {prob_sum_2:.4f}")
    print(f"P(Sum > 10): {prob_sum_greater_10:.4f}")

if __name__ == "__main__":
    main()
