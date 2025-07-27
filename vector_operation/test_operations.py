"""
Test file for vector operations and matrix multiplication functions.
"""

from vector_matrix_operations import add_vectors, dot_product, are_orthogonal, multiply_matrices


def test_vector_operations():
    """Test vector operations with the given sample input."""
    print("Testing Vector Operations:")
    print("-" * 30)
    
    # Sample input as specified
    a = [1, 2, 3]
    b = [4, 5, 6]
    
    print(f"a = {a}")
    print(f"b = {b}")
    print()
    
    # Test vector addition
    sum_result = add_vectors(a, b)
    print(f"Sum: {sum_result}")
    assert sum_result == [5, 7, 9], f"Expected [5, 7, 9], got {sum_result}"
    
    # Test dot product
    dot_result = dot_product(a, b)
    print(f"Dot Product: {dot_result}")
    assert dot_result == 32, f"Expected 32, got {dot_result}"
    
    # Test orthogonality
    orthogonal_result = are_orthogonal(a, b)
    print(f"Orthogonal: {orthogonal_result}")
    assert orthogonal_result == False, f"Expected False, got {orthogonal_result}"
    
    print("✓ All vector operation tests passed!")
    print()


def test_matrix_multiplication():
    """Test matrix multiplication with the given sample input."""
    print("Testing Matrix Multiplication:")
    print("-" * 30)
    
    # Sample input as specified
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    print("A =", A)
    print("B =", B)
    print()
    
    # Test matrix multiplication
    result = multiply_matrices(A, B)
    print("A × B =", result)
    
    # Expected result calculation:
    # [1*5 + 2*7, 1*6 + 2*8] = [19, 22]
    # [3*5 + 4*7, 3*6 + 4*8] = [43, 50]
    expected = [[19, 22], [43, 50]]
    
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ Matrix multiplication test passed!")
    print()


def test_edge_cases():
    """Test edge cases and additional scenarios."""
    print("Testing Edge Cases:")
    print("-" * 30)
    
    # Test orthogonal vectors
    ortho_a = [1, 0]
    ortho_b = [0, 1]
    assert are_orthogonal(ortho_a, ortho_b) == True, "Should be orthogonal"
    print("✓ Orthogonal vectors test passed!")
    
    # Test 1x1 matrices
    single_a = [[5]]
    single_b = [[3]]
    single_result = multiply_matrices(single_a, single_b)
    assert single_result == [[15]], f"Expected [[15]], got {single_result}"
    print("✓ 1x1 matrix multiplication test passed!")
    
    # Test identity matrix
    identity = [[1, 0], [0, 1]]
    test_matrix = [[2, 3], [4, 5]]
    identity_result = multiply_matrices(test_matrix, identity)
    assert identity_result == test_matrix, "Identity matrix multiplication failed"
    print("✓ Identity matrix test passed!")
    
    print("✓ All edge case tests passed!")
    print()


def main():
    """Run all tests."""
    print("=" * 50)
    print("RUNNING TESTS")
    print("=" * 50)
    
    try:
        test_vector_operations()
        test_matrix_multiplication()
        test_edge_cases()
        
        print("🎉 ALL TESTS PASSED! 🎉")
        
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
    except Exception as e:
        print(f"❌ Error occurred: {e}")


if __name__ == "__main__":
    main()
