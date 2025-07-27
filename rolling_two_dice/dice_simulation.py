"""
Simulate Rolling Two Dice
========================

This program simulates rolling two 6-sided dice 10,000 times and estimates
probabilities for specific sum outcomes.

Objectives:
- Estimate P(Sum = 7): Probability that the sum of two dice equals 7
- Estimate P(Sum = 2): Probability that the sum equals 2  
- Estimate P(Sum > 10): Probability that the sum is greater than 10 (i.e., 11 or 12)

Author: GitHub Copilot
Date: July 26, 2025
"""

import random


def simulate_dice_rolls(num_simulations=10000):
    """
    Simulate rolling two dice multiple times and count specific outcomes.
    
    Args:
        num_simulations (int): Number of times to roll the dice (default: 10000)
    
    Returns:
        dict: Dictionary containing counts for each tracked outcome
    """
    # Initialize counters
    count_sum_7 = 0
    count_sum_2 = 0
    count_sum_greater_10 = 0
    
    # Simulate rolling dice num_simulations times
    for _ in range(num_simulations):
        # Roll two dice (generate random integers between 1 and 6)
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        # Calculate the sum
        dice_sum = dice1 + dice2
        
        # Count specific outcomes
        if dice_sum == 7:
            count_sum_7 += 1
        elif dice_sum == 2:
            count_sum_2 += 1
        
        if dice_sum > 10:  # Sum is 11 or 12
            count_sum_greater_10 += 1
    
    return {
        'sum_7': count_sum_7,
        'sum_2': count_sum_2,
        'sum_greater_10': count_sum_greater_10,
        'total_simulations': num_simulations
    }


def calculate_probabilities(counts):
    """
    Calculate probabilities from count data.
    
    Args:
        counts (dict): Dictionary containing counts and total simulations
    
    Returns:
        dict: Dictionary containing estimated probabilities
    """
    total = counts['total_simulations']
    
    return {
        'p_sum_7': counts['sum_7'] / total,
        'p_sum_2': counts['sum_2'] / total,
        'p_sum_greater_10': counts['sum_greater_10'] / total
    }


def print_results(probabilities):
    """
    Print the estimated probabilities in the required format.
    
    Args:
        probabilities (dict): Dictionary containing estimated probabilities
    """
    print("Dice Rolling Simulation Results:")
    print("=" * 40)
    print(f"P(Sum = 7): {probabilities['p_sum_7']:.4f}")
    print(f"P(Sum = 2): {probabilities['p_sum_2']:.4f}")
    print(f"P(Sum > 10): {probabilities['p_sum_greater_10']:.4f}")


def print_theoretical_probabilities():
    """
    Print the theoretical probabilities for comparison.
    """
    print("\nTheoretical Probabilities (for comparison):")
    print("=" * 40)
    print("P(Sum = 7): 0.1667 (6/36)")
    print("P(Sum = 2): 0.0278 (1/36)")
    print("P(Sum > 10): 0.0833 (3/36)")


def detailed_analysis(num_simulations=10000):
    """
    Perform a detailed analysis showing all possible sums and their frequencies.
    
    Args:
        num_simulations (int): Number of simulations to run
    """
    # Initialize counters for all possible sums (2 through 12)
    sum_counts = {i: 0 for i in range(2, 13)}
    
    # Simulate rolling dice
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sum_counts[dice_sum] += 1
    
    print(f"\nDetailed Analysis ({num_simulations:,} simulations):")
    print("=" * 50)
    print("Sum | Count    | Probability | Theoretical")
    print("-" * 50)
    
    theoretical_probs = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }
    
    for sum_val in range(2, 13):
        count = sum_counts[sum_val]
        estimated_prob = count / num_simulations
        theoretical_prob = theoretical_probs[sum_val]
        print(f"{sum_val:2d}  | {count:8d} | {estimated_prob:11.4f} | {theoretical_prob:11.4f}")


def main():
    """
    Main function to run the dice rolling simulation.
    """
    print("Simulating Rolling Two Dice 10,000 Times")
    print("=" * 50)
    
    # Set random seed for reproducible results (optional)
    # random.seed(42)  # Uncomment for reproducible results
    
    # Run the simulation
    num_simulations = 10000
    print(f"Running {num_simulations:,} simulations...")
    print()
    
    counts = simulate_dice_rolls(num_simulations)
    probabilities = calculate_probabilities(counts)
    
    # Print main results
    print_results(probabilities)
    
    # Print theoretical probabilities for comparison
    print_theoretical_probabilities()
    
    # Show detailed analysis
    detailed_analysis(num_simulations)
    
    # Additional information
    print(f"\nSimulation Details:")
    print("=" * 20)
    print(f"Total rolls: {counts['total_simulations']:,}")
    print(f"Sum = 7 occurred: {counts['sum_7']:,} times")
    print(f"Sum = 2 occurred: {counts['sum_2']:,} times")
    print(f"Sum > 10 occurred: {counts['sum_greater_10']:,} times")


if __name__ == "__main__":
    main()
