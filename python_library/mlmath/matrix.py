"""
Matrix Operations Module
========================

This module provides essential matrix operations for machine learning and linear algebra.

Functions:
    - matrix_multiply(A, B): Multiply two matrices
    - matrix_transpose(A): Transpose a matrix
    - matrix_add(A, B): Add two matrices element-wise
    - matrix_subtract(A, B): Subtract two matrices element-wise
    - identity_matrix(n): Create an n×n identity matrix

Author: GitHub Copilot
Date: July 27, 2025
"""

from typing import List, Union

# Type alias for matrix
Matrix = List[List[Union[int, float]]]


def matrix_multiply(A: Matrix, B: Matrix) -> Matrix:
    """
    Multiply two matrices using the standard matrix multiplication algorithm.
    
    For matrices A (m×n) and B (n×p), the result is a matrix C (m×p) where:
    C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    
    Args:
        A (Matrix): First matrix (m × n)
        B (Matrix): Second matrix (n × p)
    
    Returns:
        Matrix: Product matrix (m × p)
    
    Raises:
        TypeError: If inputs are not lists of lists or contain non-numeric values
        ValueError: If matrices have incompatible dimensions or are empty
    
    Examples:
        >>> from mlmath import matrix_multiply
        >>> A = [[1, 2], [3, 4]]
        >>> B = [[5, 6], [7, 8]]
        >>> matrix_multiply(A, B)
        [[19, 22], [43, 50]]
        
        >>> A = [[1, 2, 3]]
        >>> B = [[4], [5], [6]]
        >>> matrix_multiply(A, B)
        [[32]]
        
        >>> A = [[2, 0], [0, 3]]
        >>> B = [[1, 4], [2, 5]]
        >>> matrix_multiply(A, B)
        [[2, 8], [6, 15]]
    """
    # Type and structure validation
    if not isinstance(A, list) or not isinstance(B, list):
        raise TypeError("Both inputs must be lists")
    
    if not A or not B:
        raise ValueError("Matrices cannot be empty")
    
    if not all(isinstance(row, list) for row in A):
        raise TypeError("First matrix must be a list of lists")
    
    if not all(isinstance(row, list) for row in B):
        raise TypeError("Second matrix must be a list of lists")
    
    # Check for empty rows
    if any(len(row) == 0 for row in A) or any(len(row) == 0 for row in B):
        raise ValueError("Matrix rows cannot be empty")
    
    # Check matrix dimensions consistency
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    # All rows in A must have same length
    if not all(len(row) == cols_A for row in A):
        raise ValueError("All rows in first matrix must have the same length")
    
    # All rows in B must have same length
    if not all(len(row) == cols_B for row in B):
        raise ValueError("All rows in second matrix must have the same length")
    
    # Check compatibility for multiplication
    if cols_A != rows_B:
        raise ValueError(f"Cannot multiply matrices: {rows_A}×{cols_A} and {rows_B}×{cols_B}. "
                        f"Number of columns in first matrix ({cols_A}) must equal "
                        f"number of rows in second matrix ({rows_B})")
    
    # Check that all elements are numeric
    for i, row in enumerate(A):
        for j, val in enumerate(row):
            if not isinstance(val, (int, float)):
                raise TypeError(f"All elements must be numeric. Found non-numeric value in A at [{i}][{j}]")
    
    for i, row in enumerate(B):
        for j, val in enumerate(row):
            if not isinstance(val, (int, float)):
                raise TypeError(f"All elements must be numeric. Found non-numeric value in B at [{i}][{j}]")
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result


def matrix_transpose(A: Matrix) -> Matrix:
    """
    Transpose a matrix (swap rows and columns).
    
    For matrix A (m×n), the transpose A^T is (n×m) where A^T[j][i] = A[i][j]
    
    Args:
        A (Matrix): Input matrix (m × n)
    
    Returns:
        Matrix: Transposed matrix (n × m)
    
    Raises:
        TypeError: If input is not a list of lists or contains non-numeric values
        ValueError: If matrix is empty or has inconsistent row lengths
    
    Examples:
        >>> from mlmath import matrix_transpose
        >>> A = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_transpose(A)
        [[1, 4], [2, 5], [3, 6]]
        
        >>> A = [[1, 2], [3, 4], [5, 6]]
        >>> matrix_transpose(A)
        [[1, 3, 5], [2, 4, 6]]
    """
    # Type and structure validation
    if not isinstance(A, list):
        raise TypeError("Input must be a list")
    
    if not A:
        raise ValueError("Matrix cannot be empty")
    
    if not all(isinstance(row, list) for row in A):
        raise TypeError("Matrix must be a list of lists")
    
    # Check for empty rows
    if any(len(row) == 0 for row in A):
        raise ValueError("Matrix rows cannot be empty")
    
    # Check dimensions consistency
    cols = len(A[0])
    if not all(len(row) == cols for row in A):
        raise ValueError("All rows must have the same length")
    
    # Check that all elements are numeric
    for i, row in enumerate(A):
        for j, val in enumerate(row):
            if not isinstance(val, (int, float)):
                raise TypeError(f"All elements must be numeric. Found non-numeric value at [{i}][{j}]")
    
    # Create transposed matrix
    rows = len(A)
    return [[A[i][j] for i in range(rows)] for j in range(cols)]


def matrix_add(A: Matrix, B: Matrix) -> Matrix:
    """
    Add two matrices element-wise.
    
    Args:
        A (Matrix): First matrix
        B (Matrix): Second matrix
    
    Returns:
        Matrix: Sum of the two matrices
    
    Raises:
        TypeError: If inputs are not lists of lists or contain non-numeric values
        ValueError: If matrices have different dimensions
    
    Examples:
        >>> from mlmath import matrix_add
        >>> A = [[1, 2], [3, 4]]
        >>> B = [[5, 6], [7, 8]]
        >>> matrix_add(A, B)
        [[6, 8], [10, 12]]
    """
    # Validate inputs
    _validate_same_dimensions(A, B, "addition")
    
    # Add matrices element-wise
    rows = len(A)
    cols = len(A[0])
    return [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]


def matrix_subtract(A: Matrix, B: Matrix) -> Matrix:
    """
    Subtract two matrices element-wise (A - B).
    
    Args:
        A (Matrix): First matrix (minuend)
        B (Matrix): Second matrix (subtrahend)
    
    Returns:
        Matrix: Difference of the two matrices
    
    Raises:
        TypeError: If inputs are not lists of lists or contain non-numeric values
        ValueError: If matrices have different dimensions
    
    Examples:
        >>> from mlmath import matrix_subtract
        >>> A = [[5, 6], [7, 8]]
        >>> B = [[1, 2], [3, 4]]
        >>> matrix_subtract(A, B)
        [[4, 4], [4, 4]]
    """
    # Validate inputs
    _validate_same_dimensions(A, B, "subtraction")
    
    # Subtract matrices element-wise
    rows = len(A)
    cols = len(A[0])
    return [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]


def identity_matrix(n: int) -> Matrix:
    """
    Create an n×n identity matrix.
    
    An identity matrix has 1s on the diagonal and 0s elsewhere.
    
    Args:
        n (int): Size of the square matrix
    
    Returns:
        Matrix: n×n identity matrix
    
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is not positive
    
    Examples:
        >>> from mlmath import identity_matrix
        >>> identity_matrix(2)
        [[1, 0], [0, 1]]
        
        >>> identity_matrix(3)
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    # Type checking
    if not isinstance(n, int):
        raise TypeError("Size must be an integer")
    
    # Value checking
    if n <= 0:
        raise ValueError("Size must be positive")
    
    # Create identity matrix
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def _validate_same_dimensions(A: Matrix, B: Matrix, operation: str) -> None:
    """
    Helper function to validate that two matrices have the same dimensions.
    
    Args:
        A (Matrix): First matrix
        B (Matrix): Second matrix
        operation (str): Name of the operation for error messages
    
    Raises:
        TypeError: If inputs are not lists of lists or contain non-numeric values
        ValueError: If matrices have different dimensions
    """
    # Type and structure validation
    if not isinstance(A, list) or not isinstance(B, list):
        raise TypeError("Both inputs must be lists")
    
    if not A or not B:
        raise ValueError("Matrices cannot be empty")
    
    if not all(isinstance(row, list) for row in A):
        raise TypeError("First matrix must be a list of lists")
    
    if not all(isinstance(row, list) for row in B):
        raise TypeError("Second matrix must be a list of lists")
    
    # Check for empty rows
    if any(len(row) == 0 for row in A) or any(len(row) == 0 for row in B):
        raise ValueError("Matrix rows cannot be empty")
    
    # Check dimensions
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    # Check consistency within matrices
    if not all(len(row) == cols_A for row in A):
        raise ValueError("All rows in first matrix must have the same length")
    
    if not all(len(row) == cols_B for row in B):
        raise ValueError("All rows in second matrix must have the same length")
    
    # Check that matrices have same dimensions
    if rows_A != rows_B or cols_A != cols_B:
        raise ValueError(f"Cannot perform {operation} on matrices with different dimensions: "
                        f"{rows_A}×{cols_A} and {rows_B}×{cols_B}")
    
    # Check that all elements are numeric
    for i, row in enumerate(A):
        for j, val in enumerate(row):
            if not isinstance(val, (int, float)):
                raise TypeError(f"All elements must be numeric. Found non-numeric value in A at [{i}][{j}]")
    
    for i, row in enumerate(B):
        for j, val in enumerate(row):
            if not isinstance(val, (int, float)):
                raise TypeError(f"All elements must be numeric. Found non-numeric value in B at [{i}][{j}]")
