# Vector Operations and Matrix Multiplication

This directory contains Python implementations for vector operations and matrix multiplication without using NumPy.

## Features

### Vector Operations

-   **Vector Addition**: Add two vectors element-wise
-   **Dot Product**: Compute the dot product of two vectors
-   **Orthogonality Check**: Check if two vectors are orthogonal (perpendicular)

### Matrix Operations

-   **Matrix Multiplication**: Multiply two matrices using nested loops (without NumPy)

## Files

-   `vector_matrix_operations.py` - Main implementation with all functions and comprehensive examples
-   `test_operations.py` - Test file to verify all functions work correctly
-   `demo.py` - Simple demonstration showing exact expected output format

## Usage

### Run the main program:

```bash
python vector_matrix_operations.py
```

### Run tests:

```bash
python test_operations.py
```

### Run simple demo:

```bash
python demo.py
```

## Sample Input/Output

### Vector Operations

```
Sample Input:
a = [1, 2, 3]
b = [4, 5, 6]

Expected Output:
Sum: [5, 7, 9]
Dot Product: 32
Orthogonal: False
```

### Matrix Multiplication

```
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

A × B = [[19, 22], [43, 50]]
```

## Functions

### Vector Operations

-   `add_vectors(a, b)` - Returns the element-wise sum of two vectors
-   `dot_product(a, b)` - Returns the dot product of two vectors
-   `are_orthogonal(a, b)` - Returns True if vectors are orthogonal, False otherwise

### Matrix Operations

-   `multiply_matrices(A, B)` - Returns the result of matrix multiplication A × B

## Implementation Details

-   All functions include proper error handling for incompatible vector/matrix dimensions
-   Matrix multiplication is implemented using three nested loops for clarity
-   No external libraries (like NumPy) are used for the core mathematical operations
-   Comprehensive test cases verify correctness including edge cases
