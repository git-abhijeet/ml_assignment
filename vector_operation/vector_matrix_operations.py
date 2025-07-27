"""
Vector Operations and Matrix Multiplication
==========================================

This module contains functions for:
1. Vector operations (addition, dot product, orthogonality check)
2. Matrix multiplication using nested loops (without NumPy)

Author: GitHub Copilot
Date: July 26, 2025
"""


def add_vectors(a, b):
    """
    Add two vectors element-wise.
    
    Args:
        a (list): First vector
        b (list): Second vector
    
    Returns:
        list: Sum of the two vectors
    
    Raises:
        ValueError: If vectors have different lengths
    """
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    
    return [a[i] + b[i] for i in range(len(a))]


def dot_product(a, b):
    """
    Compute the dot product of two vectors.
    
    Args:
        a (list): First vector
        b (list): Second vector
    
    Returns:
        float/int: Dot product of the two vectors
    
    Raises:
        ValueError: If vectors have different lengths
    """
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    
    return sum(a[i] * b[i] for i in range(len(a)))


def are_orthogonal(a, b):
    """
    Check if two vectors are orthogonal (perpendicular).
    Two vectors are orthogonal if their dot product is zero.
    
    Args:
        a (list): First vector
        b (list): Second vector
    
    Returns:
        bool: True if vectors are orthogonal, False otherwise
    """
    return dot_product(a, b) == 0


def multiply_matrices(A, B):
    """
    Multiply two matrices using nested loops (without NumPy).
    
    Args:
        A (list): First matrix (list of lists)
        B (list): Second matrix (list of lists)
    
    Returns:
        list: Result of matrix multiplication
    
    Raises:
        ValueError: If matrices cannot be multiplied (incompatible dimensions)
    """
    # Check if matrices can be multiplied
    if len(A[0]) != len(B):
        raise ValueError(f"Cannot multiply matrices: {len(A)}x{len(A[0])} and {len(B)}x{len(B[0])}")
    
    # Initialize result matrix with zeros
    rows_A = len(A)
    cols_B = len(B[0])
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform matrix multiplication using nested loops
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result


def print_matrix(matrix, title="Matrix"):
    """
    Helper function to print a matrix in a readable format.
    
    Args:
        matrix (list): Matrix to print
        title (str): Title for the matrix
    """
    print(f"{title}:")
    for row in matrix:
        print(row)
    print()


def main():
    """
    Main function to demonstrate vector operations and matrix multiplication.
    """
    print("=" * 50)
    print("VECTOR OPERATIONS DEMONSTRATION")
    print("=" * 50)
    
    # Sample vectors
    a = [1, 2, 3]
    b = [4, 5, 6]
    
    print(f"Vector a: {a}")
    print(f"Vector b: {b}")
    print()
    
    # Vector addition
    vector_sum = add_vectors(a, b)
    print(f"Sum: {vector_sum}")
    
    # Dot product
    dot_prod = dot_product(a, b)
    print(f"Dot Product: {dot_prod}")
    
    # Orthogonality check
    orthogonal = are_orthogonal(a, b)
    print(f"Orthogonal: {orthogonal}")
    
    print()
    print("=" * 50)
    print("MATRIX MULTIPLICATION DEMONSTRATION")
    print("=" * 50)
    
    # Sample matrices
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")
    
    # Matrix multiplication
    result = multiply_matrices(A, B)
    print_matrix(result, "Result (A × B)")
    
    # Additional examples
    print("=" * 50)
    print("ADDITIONAL EXAMPLES")
    print("=" * 50)
    
    # Example with orthogonal vectors
    print("Testing orthogonal vectors:")
    orthogonal_a = [1, 0, 0]
    orthogonal_b = [0, 1, 0]
    print(f"Vector a: {orthogonal_a}")
    print(f"Vector b: {orthogonal_b}")
    print(f"Orthogonal: {are_orthogonal(orthogonal_a, orthogonal_b)}")
    print()
    
    # Example with 3x3 matrices
    print("3x3 Matrix multiplication example:")
    C = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    D = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    print_matrix(C, "Matrix C")
    print_matrix(D, "Matrix D")
    
    result_3x3 = multiply_matrices(C, D)
    print_matrix(result_3x3, "Result (C × D)")


if __name__ == "__main__":
    main()
