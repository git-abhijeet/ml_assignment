"""
Simple demonstration script showing the exact expected output format.
"""

from vector_matrix_operations import add_vectors, dot_product, are_orthogonal, multiply_matrices


def main():
    """Demonstrate the exact sample input/output as specified."""
    
    # Sample Input as specified
    a = [1, 2, 3]
    b = [4, 5, 6]
    
    print("Sample Input:")
    print(f"a = {a}")
    print(f"b = {b}")
    print()
    
    # Expected Output
    print("Expected Output:")
    
    # Vector operations
    vector_sum = add_vectors(a, b)
    print(f"Sum: {vector_sum}")
    
    dot_prod = dot_product(a, b)
    print(f"Dot Product: {dot_prod}")
    
    orthogonal = are_orthogonal(a, b)
    print(f"Orthogonal: {orthogonal}")
    
    print()
    print("-" * 40)
    print()
    
    # Matrix Multiplication Test
    print("Matrix Multiplication Test:")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    print(f"A = {A}")
    print(f"B = {B}")
    print()
    
    result = multiply_matrices(A, B)
    print(f"A × B = {result}")


if __name__ == "__main__":
    main()
