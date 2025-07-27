"""
Vector Operations Module
========================

This module provides essential vector operations for machine learning and linear algebra.

Functions:
    - dot_product(a, b): Calculate dot product of two vectors
    - vector_add(a, b): Add two vectors element-wise
    - vector_subtract(a, b): Subtract two vectors element-wise
    - vector_magnitude(a): Calculate the magnitude (length) of a vector
    - vector_normalize(a): Normalize a vector to unit length

Author: GitHub Copilot
Date: July 27, 2025
"""

import math
from typing import List, Union


def dot_product(a: List[Union[int, float]], b: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate the dot product of two vectors.
    
    The dot product is the sum of the products of corresponding elements:
    dot_product([a1, a2, a3], [b1, b2, b3]) = a1*b1 + a2*b2 + a3*b3
    
    Args:
        a (List[Union[int, float]]): First vector
        b (List[Union[int, float]]): Second vector
    
    Returns:
        Union[int, float]: Dot product of the two vectors
    
    Raises:
        ValueError: If vectors have different lengths
        TypeError: If inputs are not lists or contain non-numeric values
    
    Examples:
        >>> from mlmath import dot_product
        >>> dot_product([1, 2, 3], [4, 5, 6])
        32
        
        >>> dot_product([1.5, 2.5], [2.0, 3.0])
        10.5
        
        >>> dot_product([1, 0, 0], [0, 1, 0])
        0
    """
    # Type checking
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Both inputs must be lists")
    
    # Length checking
    if len(a) != len(b):
        raise ValueError(f"Vectors must have the same length. Got {len(a)} and {len(b)}")
    
    # Check for empty vectors
    if len(a) == 0:
        return 0
    
    # Check that all elements are numeric
    for i, (x, y) in enumerate(zip(a, b)):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(f"All elements must be numeric. Found non-numeric values at index {i}")
    
    # Calculate dot product
    return sum(x * y for x, y in zip(a, b))


def vector_add(a: List[Union[int, float]], b: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Add two vectors element-wise.
    
    Args:
        a (List[Union[int, float]]): First vector
        b (List[Union[int, float]]): Second vector
    
    Returns:
        List[Union[int, float]]: Sum of the two vectors
    
    Raises:
        ValueError: If vectors have different lengths
        TypeError: If inputs are not lists or contain non-numeric values
    
    Examples:
        >>> from mlmath import vector_add
        >>> vector_add([1, 2, 3], [4, 5, 6])
        [5, 7, 9]
        
        >>> vector_add([1.5, 2.5], [0.5, 1.5])
        [2.0, 4.0]
    """
    # Type checking
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Both inputs must be lists")
    
    # Length checking
    if len(a) != len(b):
        raise ValueError(f"Vectors must have the same length. Got {len(a)} and {len(b)}")
    
    # Check that all elements are numeric
    for i, (x, y) in enumerate(zip(a, b)):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(f"All elements must be numeric. Found non-numeric values at index {i}")
    
    # Calculate element-wise addition
    return [x + y for x, y in zip(a, b)]


def vector_subtract(a: List[Union[int, float]], b: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Subtract two vectors element-wise (a - b).
    
    Args:
        a (List[Union[int, float]]): First vector (minuend)
        b (List[Union[int, float]]): Second vector (subtrahend)
    
    Returns:
        List[Union[int, float]]: Difference of the two vectors
    
    Raises:
        ValueError: If vectors have different lengths
        TypeError: If inputs are not lists or contain non-numeric values
    
    Examples:
        >>> from mlmath import vector_subtract
        >>> vector_subtract([5, 7, 9], [1, 2, 3])
        [4, 5, 6]
        
        >>> vector_subtract([3.0, 4.0], [1.5, 2.5])
        [1.5, 1.5]
    """
    # Type checking
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Both inputs must be lists")
    
    # Length checking
    if len(a) != len(b):
        raise ValueError(f"Vectors must have the same length. Got {len(a)} and {len(b)}")
    
    # Check that all elements are numeric
    for i, (x, y) in enumerate(zip(a, b)):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError(f"All elements must be numeric. Found non-numeric values at index {i}")
    
    # Calculate element-wise subtraction
    return [x - y for x, y in zip(a, b)]


def vector_magnitude(a: List[Union[int, float]]) -> float:
    """
    Calculate the magnitude (Euclidean norm) of a vector.
    
    The magnitude is calculated as: sqrt(a1² + a2² + ... + an²)
    
    Args:
        a (List[Union[int, float]]): Input vector
    
    Returns:
        float: Magnitude of the vector
    
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If vector is empty
    
    Examples:
        >>> from mlmath import vector_magnitude
        >>> vector_magnitude([3, 4])
        5.0
        
        >>> vector_magnitude([1, 2, 2])
        3.0
        
        >>> round(vector_magnitude([1, 1, 1]), 3)
        1.732
    """
    # Type checking
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    
    # Check for empty vector
    if len(a) == 0:
        raise ValueError("Cannot calculate magnitude of empty vector")
    
    # Check that all elements are numeric
    for i, x in enumerate(a):
        if not isinstance(x, (int, float)):
            raise TypeError(f"All elements must be numeric. Found non-numeric value at index {i}")
    
    # Calculate magnitude using Euclidean norm
    return math.sqrt(sum(x * x for x in a))


def vector_normalize(a: List[Union[int, float]]) -> List[float]:
    """
    Normalize a vector to unit length (magnitude = 1).
    
    The normalized vector is calculated by dividing each element by the vector's magnitude.
    
    Args:
        a (List[Union[int, float]]): Input vector
    
    Returns:
        List[float]: Normalized vector with magnitude 1
    
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If vector is empty or is a zero vector
    
    Examples:
        >>> from mlmath import vector_normalize
        >>> vector_normalize([3, 4])
        [0.6, 0.8]
        
        >>> vector_normalize([1, 0, 0])
        [1.0, 0.0, 0.0]
        
        >>> result = vector_normalize([1, 1, 1])
        >>> [round(x, 3) for x in result]
        [0.577, 0.577, 0.577]
    """
    # Type checking
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    
    # Check for empty vector
    if len(a) == 0:
        raise ValueError("Cannot normalize empty vector")
    
    # Check that all elements are numeric
    for i, x in enumerate(a):
        if not isinstance(x, (int, float)):
            raise TypeError(f"All elements must be numeric. Found non-numeric value at index {i}")
    
    # Calculate magnitude
    magnitude = vector_magnitude(a)
    
    # Check for zero vector
    if magnitude == 0:
        raise ValueError("Cannot normalize zero vector")
    
    # Normalize by dividing each element by magnitude
    return [x / magnitude for x in a]
