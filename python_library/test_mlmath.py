"""
Comprehensive Test Suite for MLMath Library
==========================================

This test suite validates all functions in the mlmath library including:
- Vector operations
- Matrix operations  
- Probability calculations

Author: GitHub Copilot
Date: July 27, 2025
"""

import sys
import os

# Add the parent directory to the path so we can import mlmath
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mlmath


def test_vector_operations():
    """Test all vector operations."""
    print("Testing Vector Operations:")
    print("-" * 30)
    
    # Test dot_product
    print("Testing dot_product...")
    assert mlmath.dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert mlmath.dot_product([1, 0, 0], [0, 1, 0]) == 0
    assert mlmath.dot_product([2, 3], [4, 5]) == 23
    print("✓ dot_product tests passed")
    
    # Test vector_add
    print("Testing vector_add...")
    assert mlmath.vector_add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert mlmath.vector_add([1.5, 2.5], [0.5, 1.5]) == [2.0, 4.0]
    print("✓ vector_add tests passed")
    
    # Test vector_subtract
    print("Testing vector_subtract...")
    assert mlmath.vector_subtract([5, 7, 9], [1, 2, 3]) == [4, 5, 6]
    assert mlmath.vector_subtract([3.0, 4.0], [1.5, 2.5]) == [1.5, 1.5]
    print("✓ vector_subtract tests passed")
    
    # Test vector_magnitude
    print("Testing vector_magnitude...")
    assert mlmath.vector_magnitude([3, 4]) == 5.0
    assert mlmath.vector_magnitude([1, 2, 2]) == 3.0
    assert abs(mlmath.vector_magnitude([1, 1, 1]) - 1.732) < 0.001
    print("✓ vector_magnitude tests passed")
    
    # Test vector_normalize
    print("Testing vector_normalize...")
    result = mlmath.vector_normalize([3, 4])
    assert abs(result[0] - 0.6) < 0.001 and abs(result[1] - 0.8) < 0.001
    result = mlmath.vector_normalize([1, 0, 0])
    assert result == [1.0, 0.0, 0.0]
    print("✓ vector_normalize tests passed")
    
    print("✓ All vector operations tests passed!\n")


def test_matrix_operations():
    """Test all matrix operations."""
    print("Testing Matrix Operations:")
    print("-" * 30)
    
    # Test matrix_multiply
    print("Testing matrix_multiply...")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    result = mlmath.matrix_multiply(A, B)
    expected = [[19, 22], [43, 50]]
    assert result == expected
    
    A = [[1, 2, 3]]
    B = [[4], [5], [6]]
    assert mlmath.matrix_multiply(A, B) == [[32]]
    print("✓ matrix_multiply tests passed")
    
    # Test matrix_transpose
    print("Testing matrix_transpose...")
    A = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert mlmath.matrix_transpose(A) == expected
    print("✓ matrix_transpose tests passed")
    
    # Test matrix_add
    print("Testing matrix_add...")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert mlmath.matrix_add(A, B) == expected
    print("✓ matrix_add tests passed")
    
    # Test matrix_subtract
    print("Testing matrix_subtract...")
    A = [[5, 6], [7, 8]]
    B = [[1, 2], [3, 4]]
    expected = [[4, 4], [4, 4]]
    assert mlmath.matrix_subtract(A, B) == expected
    print("✓ matrix_subtract tests passed")
    
    # Test identity_matrix
    print("Testing identity_matrix...")
    assert mlmath.identity_matrix(2) == [[1, 0], [0, 1]]
    assert mlmath.identity_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print("✓ identity_matrix tests passed")
    
    print("✓ All matrix operations tests passed!\n")


def test_probability_operations():
    """Test all probability operations."""
    print("Testing Probability Operations:")
    print("-" * 35)
    
    # Test conditional_probability
    print("Testing conditional_probability...")
    
    # Spam detection example
    events = {
        'total': 1000,
        'contains_free': 300,
        'spam': 400,
        'spam_and_free': 120
    }
    result = mlmath.conditional_probability(events)
    assert abs(result['P_spam_given_free'] - 0.4) < 0.001
    
    # Direct probabilities
    events = {
        'P_A': 0.3,
        'P_B': 0.4,
        'P_A_and_B': 0.12
    }
    result = mlmath.conditional_probability(events)
    assert abs(result['P_A_given_B'] - 0.3) < 0.001
    print("✓ conditional_probability tests passed")
    
    # Test bayes_theorem
    print("Testing bayes_theorem...")
    result = mlmath.bayes_theorem(0.4, 0.3, 0.3)
    assert abs(result - 0.4) < 0.001
    
    result = mlmath.bayes_theorem(0.01, 0.9, 0.05)
    assert abs(result - 0.18) < 0.001
    print("✓ bayes_theorem tests passed")
    
    # Test joint_probability
    print("Testing joint_probability...")
    result = mlmath.joint_probability(0.3, 0.4, independent=True)
    assert abs(result - 0.12) < 0.001
    
    result = mlmath.joint_probability(0.5, 0.6, independent=True)
    assert abs(result - 0.3) < 0.001
    print("✓ joint_probability tests passed")
    
    # Test marginal_probability
    print("Testing marginal_probability...")
    result = mlmath.marginal_probability([0.2, 0.3, 0.1])
    assert abs(result - 0.6) < 0.001
    
    result = mlmath.marginal_probability([0.15, 0.25, 0.35])
    assert abs(result - 0.75) < 0.001
    print("✓ marginal_probability tests passed")
    
    print("✓ All probability operations tests passed!\n")


def test_error_handling():
    """Test error handling and edge cases."""
    print("Testing Error Handling:")
    print("-" * 25)
    
    # Test vector error cases
    try:
        mlmath.dot_product([1, 2], [1, 2, 3])  # Different lengths
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ Vector length mismatch error handled")
    
    try:
        mlmath.vector_magnitude([])  # Empty vector
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ Empty vector error handled")
    
    # Test matrix error cases
    try:
        mlmath.matrix_multiply([[1, 2]], [[1], [2], [3]])  # Incompatible dimensions
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ Matrix dimension mismatch error handled")
    
    try:
        mlmath.identity_matrix(0)  # Invalid size
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ Invalid matrix size error handled")
    
    # Test probability error cases
    try:
        mlmath.bayes_theorem(1.5, 0.5, 0.5)  # Invalid probability
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ Invalid probability value error handled")
    
    try:
        mlmath.marginal_probability([0.5, 0.7])  # Sum > 1
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ Probability sum overflow error handled")
    
    print("✓ All error handling tests passed!\n")


def test_library_info():
    """Test library metadata functions."""
    print("Testing Library Info:")
    print("-" * 21)
    
    version = mlmath.get_version()
    assert isinstance(version, str)
    print(f"✓ Library version: {version}")
    
    info = mlmath.get_info()
    assert isinstance(info, dict)
    assert 'name' in info
    assert 'version' in info
    print(f"✓ Library info: {info['name']} v{info['version']}")
    
    print("✓ Library info tests passed!\n")


def run_comprehensive_example():
    """Run a comprehensive example using multiple library functions."""
    print("Comprehensive Example:")
    print("-" * 22)
    
    print("Example: Machine Learning Pipeline Components")
    
    # Vector operations for feature processing
    features_1 = [1.5, 2.0, 3.5]
    features_2 = [2.5, 1.5, 2.0]
    
    similarity = mlmath.dot_product(features_1, features_2)
    print(f"Feature similarity (dot product): {similarity}")
    
    combined_features = mlmath.vector_add(features_1, features_2)
    print(f"Combined features: {combined_features}")
    
    # Matrix operations for transformations
    transformation_matrix = [[0.8, 0.2], [0.3, 0.7]]
    data_matrix = [[1, 2], [3, 4]]
    
    transformed_data = mlmath.matrix_multiply(transformation_matrix, data_matrix)
    print(f"Transformed data: {transformed_data}")
    
    # Probability calculations for model evaluation
    events = {
        'total': 1000,
        'contains_free': 300,
        'spam': 400,
        'spam_and_free': 120
    }
    
    spam_probs = mlmath.conditional_probability(events)
    print(f"P(Spam | Contains 'free'): {spam_probs['P_spam_given_free']:.3f}")
    
    # Bayes' theorem for updating beliefs
    posterior = mlmath.bayes_theorem(0.4, 0.3, 0.3)
    print(f"Updated probability (Bayes): {posterior:.3f}")
    
    print("✓ Comprehensive example completed!\n")


def main():
    """Run all tests."""
    print("=" * 60)
    print("MLMATH LIBRARY COMPREHENSIVE TEST SUITE")
    print("=" * 60)
    
    try:
        test_vector_operations()
        test_matrix_operations()
        test_probability_operations()
        test_error_handling()
        test_library_info()
        run_comprehensive_example()
        
        print("🎉 ALL TESTS PASSED! 🎉")
        print("The MLMath library is working correctly!")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
