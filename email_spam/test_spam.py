"""
Test file for email spam probability calculations.
Tests the Bayes' Theorem implementation with known examples.
"""

from spam_calculator import calculate_spam_probability
import math


def test_default_example():
    """Test with the default example from the problem statement."""
    print("Testing Default Example:")
    print("-" * 25)
    
    # Problem statement example:
    # 1000 emails total, 300 with "free", 400 spam, 120 both spam and "free"
    total_emails = 1000
    emails_with_free = 300
    spam_emails = 400
    spam_and_free = 120
    
    probabilities = calculate_spam_probability(total_emails, emails_with_free, spam_emails, spam_and_free)
    
    # Expected calculations:
    # P(Spam) = 400/1000 = 0.4
    # P(Free) = 300/1000 = 0.3
    # P(Free | Spam) = 120/400 = 0.3
    # P(Spam | Free) = (0.3 × 0.4) / 0.3 = 0.4
    
    expected_p_spam = 0.4
    expected_p_free = 0.3
    expected_p_free_given_spam = 0.3
    expected_p_spam_given_free = 0.4
    
    print(f"Input: {total_emails} total, {emails_with_free} with 'free', {spam_emails} spam, {spam_and_free} both")
    print(f"P(Spam | Free) = {probabilities['p_spam_given_free']:.4f}")
    print(f"Expected: {expected_p_spam_given_free:.4f}")
    
    # Verify calculations
    assert abs(probabilities['p_spam'] - expected_p_spam) < 0.0001, f"P(Spam) mismatch"
    assert abs(probabilities['p_free'] - expected_p_free) < 0.0001, f"P(Free) mismatch"
    assert abs(probabilities['p_free_given_spam'] - expected_p_free_given_spam) < 0.0001, f"P(Free|Spam) mismatch"
    assert abs(probabilities['p_spam_given_free'] - expected_p_spam_given_free) < 0.0001, f"P(Spam|Free) mismatch"
    
    print("✓ Default example test passed!")
    print()


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    print("Testing Edge Cases:")
    print("-" * 18)
    
    # Test case 1: No spam emails contain "free"
    probabilities1 = calculate_spam_probability(1000, 200, 300, 0)
    expected1 = 0.0  # If no spam emails contain "free", P(Spam | Free) should be 0
    print(f"No spam with 'free': P(Spam | Free) = {probabilities1['p_spam_given_free']:.4f}")
    assert abs(probabilities1['p_spam_given_free'] - expected1) < 0.0001, "Edge case 1 failed"
    
    # Test case 2: All emails with "free" are spam
    probabilities2 = calculate_spam_probability(1000, 100, 500, 100)
    expected2 = 1.0  # If all emails with "free" are spam, P(Spam | Free) should be 1.0
    print(f"All 'free' emails are spam: P(Spam | Free) = {probabilities2['p_spam_given_free']:.4f}")
    assert abs(probabilities2['p_spam_given_free'] - expected2) < 0.0001, "Edge case 2 failed"
    
    # Test case 3: Half and half
    probabilities3 = calculate_spam_probability(1000, 200, 400, 100)
    # P(Spam) = 400/1000 = 0.4
    # P(Free) = 200/1000 = 0.2
    # P(Free | Spam) = 100/400 = 0.25
    # P(Spam | Free) = (0.25 × 0.4) / 0.2 = 0.5
    expected3 = 0.5
    print(f"Half spam scenario: P(Spam | Free) = {probabilities3['p_spam_given_free']:.4f}")
    assert abs(probabilities3['p_spam_given_free'] - expected3) < 0.0001, "Edge case 3 failed"
    
    print("✓ Edge case tests passed!")
    print()


def test_mathematical_properties():
    """Test mathematical properties of Bayes' Theorem."""
    print("Testing Mathematical Properties:")
    print("-" * 32)
    
    # Test that probabilities are between 0 and 1
    test_cases = [
        (1000, 300, 400, 120),
        (500, 100, 200, 50),
        (2000, 600, 800, 240)
    ]
    
    for i, (total, free, spam, both) in enumerate(test_cases):
        probabilities = calculate_spam_probability(total, free, spam, both)
        
        # All probabilities should be between 0 and 1
        assert 0 <= probabilities['p_spam'] <= 1, f"P(Spam) out of range in test {i+1}"
        assert 0 <= probabilities['p_free'] <= 1, f"P(Free) out of range in test {i+1}"
        assert 0 <= probabilities['p_free_given_spam'] <= 1, f"P(Free|Spam) out of range in test {i+1}"
        assert 0 <= probabilities['p_spam_given_free'] <= 1, f"P(Spam|Free) out of range in test {i+1}"
        
        print(f"Test {i+1}: P(Spam | Free) = {probabilities['p_spam_given_free']:.4f} ✓")
    
    print("✓ Mathematical properties test passed!")
    print()


def test_manual_calculation():
    """Test with manual calculation verification."""
    print("Manual Calculation Verification:")
    print("-" * 32)
    
    # Simple example for manual verification
    total = 100
    free = 30
    spam = 40
    both = 15
    
    # Manual calculation:
    p_spam_manual = spam / total  # 40/100 = 0.4
    p_free_manual = free / total  # 30/100 = 0.3
    p_free_given_spam_manual = both / spam  # 15/40 = 0.375
    p_spam_given_free_manual = (p_free_given_spam_manual * p_spam_manual) / p_free_manual
    # = (0.375 × 0.4) / 0.3 = 0.15 / 0.3 = 0.5
    
    probabilities = calculate_spam_probability(total, free, spam, both)
    
    print(f"Manual calculation: P(Spam | Free) = {p_spam_given_free_manual:.4f}")
    print(f"Function result:    P(Spam | Free) = {probabilities['p_spam_given_free']:.4f}")
    
    assert abs(probabilities['p_spam_given_free'] - p_spam_given_free_manual) < 0.0001, "Manual calculation mismatch"
    
    print("✓ Manual calculation verification passed!")
    print()


def main():
    """Run all tests."""
    print("=" * 50)
    print("EMAIL SPAM PROBABILITY TESTS")
    print("=" * 50)
    
    try:
        test_default_example()
        test_edge_cases()
        test_mathematical_properties()
        test_manual_calculation()
        
        print("🎉 ALL TESTS PASSED! 🎉")
        print("\nThe Bayes' Theorem implementation is working correctly!")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
    except Exception as e:
        print(f"❌ Error occurred: {e}")


if __name__ == "__main__":
    main()
