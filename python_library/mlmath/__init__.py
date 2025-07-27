"""
MLMath - A Custom Python Library for Machine Learning Mathematics
================================================================

A comprehensive library providing essential mathematical functions for machine learning,
including vector operations, matrix operations, and probability calculations.

Modules:
    - vector: Vector operations (dot product, vector addition, etc.)
    - matrix: Matrix operations (multiplication, transpose, etc.)
    - probability: Probability and statistics functions

Author: GitHub Copilot
Version: 1.0.0
Date: July 27, 2025
"""

from .vector import dot_product, vector_add, vector_subtract, vector_magnitude, vector_normalize
from .matrix import matrix_multiply, matrix_transpose, matrix_add, matrix_subtract, identity_matrix
from .probability import conditional_probability, bayes_theorem, joint_probability, marginal_probability

# Package metadata
__version__ = "1.0.0"
__author__ = "GitHub Copilot"
__email__ = "copilot@github.com"
__description__ = "A custom Python library for machine learning mathematics"

# Define what gets imported when using "from mlmath import *"
__all__ = [
    # Vector operations
    'dot_product',
    'vector_add', 
    'vector_subtract',
    'vector_magnitude',
    'vector_normalize',
    
    # Matrix operations
    'matrix_multiply',
    'matrix_transpose',
    'matrix_add',
    'matrix_subtract', 
    'identity_matrix',
    
    # Probability functions
    'conditional_probability',
    'bayes_theorem',
    'joint_probability',
    'marginal_probability'
]

def get_version():
    """
    Get the current version of the mlmath library.
    
    Returns:
        str: Version string
        
    Example:
        >>> import mlmath
        >>> mlmath.get_version()
        '1.0.0'
    """
    return __version__

def get_info():
    """
    Get information about the mlmath library.
    
    Returns:
        dict: Dictionary containing library information
        
    Example:
        >>> import mlmath
        >>> info = mlmath.get_info()
        >>> print(info['description'])
        A custom Python library for machine learning mathematics
    """
    return {
        'name': 'mlmath',
        'version': __version__,
        'author': __author__,
        'email': __email__,
        'description': __description__
    }
