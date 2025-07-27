"""
Test file for dice rolling simulation.
Tests the simulation functions and validates results.
"""

from dice_simulation import simulate_dice_rolls, calculate_probabilities
import random


def test_simulation_basic():
    """Test basic simulation functionality."""
    print("Testing Basic Simulation:")
    print("-" * 30)
    
    # Run a small simulation for testing
    counts = simulate_dice_rolls(1000)
    probabilities = calculate_probabilities(counts)
    
    print(f"Test simulation with 1,000 rolls:")
    print(f"P(Sum = 7): {probabilities['p_sum_7']:.4f}")
    print(f"P(Sum = 2): {probabilities['p_sum_2']:.4f}")
    print(f"P(Sum > 10): {probabilities['p_sum_greater_10']:.4f}")
    
    # Basic validation - probabilities should be between 0 and 1
    assert 0 <= probabilities['p_sum_7'] <= 1, "P(Sum = 7) should be between 0 and 1"
    assert 0 <= probabilities['p_sum_2'] <= 1, "P(Sum = 2) should be between 0 and 1"
    assert 0 <= probabilities['p_sum_greater_10'] <= 1, "P(Sum > 10) should be between 0 and 1"
    
    print("✓ Basic simulation test passed!")
    print()


def test_edge_cases():
    """Test edge cases and validate theoretical bounds."""
    print("Testing Edge Cases:")
    print("-" * 30)
    
    # Test with a larger sample to check if probabilities are reasonable
    counts = simulate_dice_rolls(100000)
    probabilities = calculate_probabilities(counts)
    
    # Theoretical probabilities
    theoretical_p_sum_7 = 6/36  # ≈ 0.1667
    theoretical_p_sum_2 = 1/36  # ≈ 0.0278
    theoretical_p_sum_greater_10 = 3/36  # ≈ 0.0833
    
    print(f"Large simulation with 100,000 rolls:")
    print(f"P(Sum = 7): {probabilities['p_sum_7']:.4f} (theoretical: {theoretical_p_sum_7:.4f})")
    print(f"P(Sum = 2): {probabilities['p_sum_2']:.4f} (theoretical: {theoretical_p_sum_2:.4f})")
    print(f"P(Sum > 10): {probabilities['p_sum_greater_10']:.4f} (theoretical: {theoretical_p_sum_greater_10:.4f})")
    
    # Check if simulated probabilities are reasonably close to theoretical
    # Allow for 5% tolerance
    tolerance = 0.05
    
    assert abs(probabilities['p_sum_7'] - theoretical_p_sum_7) < tolerance, "P(Sum = 7) too far from theoretical"
    assert abs(probabilities['p_sum_2'] - theoretical_p_sum_2) < tolerance, "P(Sum = 2) too far from theoretical"
    assert abs(probabilities['p_sum_greater_10'] - theoretical_p_sum_greater_10) < tolerance, "P(Sum > 10) too far from theoretical"
    
    print("✓ Edge case test passed!")
    print()


def test_reproducibility():
    """Test that setting random seed produces reproducible results."""
    print("Testing Reproducibility:")
    print("-" * 30)
    
    # Set seed and run simulation
    random.seed(42)
    counts1 = simulate_dice_rolls(1000)
    prob1 = calculate_probabilities(counts1)
    
    # Reset seed and run again
    random.seed(42)
    counts2 = simulate_dice_rolls(1000)
    prob2 = calculate_probabilities(counts2)
    
    # Results should be identical
    assert prob1['p_sum_7'] == prob2['p_sum_7'], "Results should be reproducible with same seed"
    assert prob1['p_sum_2'] == prob2['p_sum_2'], "Results should be reproducible with same seed"
    assert prob1['p_sum_greater_10'] == prob2['p_sum_greater_10'], "Results should be reproducible with same seed"
    
    print("✓ Reproducibility test passed!")
    print("Same seed produces identical results")
    print()


def run_multiple_trials():
    """Run multiple trials to show variability in results."""
    print("Multiple Trial Analysis:")
    print("-" * 30)
    print("Running 5 separate trials of 10,000 simulations each:")
    print()
    
    results = []
    for trial in range(5):
        counts = simulate_dice_rolls(10000)
        probabilities = calculate_probabilities(counts)
        results.append(probabilities)
        
        print(f"Trial {trial + 1}:")
        print(f"  P(Sum = 7): {probabilities['p_sum_7']:.4f}")
        print(f"  P(Sum = 2): {probabilities['p_sum_2']:.4f}")
        print(f"  P(Sum > 10): {probabilities['p_sum_greater_10']:.4f}")
    
    # Calculate average across trials
    avg_p_sum_7 = sum(r['p_sum_7'] for r in results) / len(results)
    avg_p_sum_2 = sum(r['p_sum_2'] for r in results) / len(results)
    avg_p_sum_greater_10 = sum(r['p_sum_greater_10'] for r in results) / len(results)
    
    print("\nAverage across 5 trials:")
    print(f"  P(Sum = 7): {avg_p_sum_7:.4f}")
    print(f"  P(Sum = 2): {avg_p_sum_2:.4f}")
    print(f"  P(Sum > 10): {avg_p_sum_greater_10:.4f}")
    print()


def main():
    """Run all tests."""
    print("=" * 50)
    print("DICE SIMULATION TESTS")
    print("=" * 50)
    
    try:
        test_simulation_basic()
        test_edge_cases()
        test_reproducibility()
        run_multiple_trials()
        
        print("🎉 ALL TESTS PASSED! 🎉")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
    except Exception as e:
        print(f"❌ Error occurred: {e}")


if __name__ == "__main__":
    main()
