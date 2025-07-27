# MLMath - Machine Learning Mathematics Library

A comprehensive Python library providing essential mathematical functions for machine learning, including vector operations, matrix operations, and probability calculations.

## 🚀 Features

### Vector Operations

-   **`dot_product(a, b)`** - Calculate dot product of two vectors
-   **`vector_add(a, b)`** - Add two vectors element-wise
-   **`vector_subtract(a, b)`** - Subtract two vectors element-wise
-   **`vector_magnitude(a)`** - Calculate the magnitude (length) of a vector
-   **`vector_normalize(a)`** - Normalize a vector to unit length

### Matrix Operations

-   **`matrix_multiply(A, B)`** - Multiply two matrices
-   **`matrix_transpose(A)`** - Transpose a matrix
-   **`matrix_add(A, B)`** - Add two matrices element-wise
-   **`matrix_subtract(A, B)`** - Subtract two matrices element-wise
-   **`identity_matrix(n)`** - Create an n×n identity matrix

### Probability Functions

-   **`conditional_probability(events)`** - Calculate conditional probabilities
-   **`bayes_theorem(prior, likelihood, evidence)`** - Apply Bayes' theorem
-   **`joint_probability(prob_a, prob_b, independent)`** - Calculate joint probability
-   **`marginal_probability(joint_probs)`** - Calculate marginal probability

## 📦 Installation

### Option 1: Direct Usage (Recommended for this assignment)

Simply copy the `mlmath` directory to your project and import:

```python
import mlmath

# Or import specific functions
from mlmath import dot_product, matrix_multiply, conditional_probability
```

### Option 2: Install as Package (Optional)

```bash
pip install -e .
```

## 🔧 Usage Examples

### Vector Operations

```python
import mlmath

# Vector operations
a = [1, 2, 3]
b = [4, 5, 6]

# Dot product
result = mlmath.dot_product(a, b)  # 32
print(f"Dot product: {result}")

# Vector addition
sum_vec = mlmath.vector_add(a, b)  # [5, 7, 9]
print(f"Sum: {sum_vec}")

# Vector magnitude
magnitude = mlmath.vector_magnitude(a)  # 3.742
print(f"Magnitude: {magnitude:.3f}")

# Normalize vector
normalized = mlmath.vector_normalize(a)  # [0.267, 0.535, 0.802]
print(f"Normalized: {[round(x, 3) for x in normalized]}")
```

### Matrix Operations

```python
import mlmath

# Matrix operations
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Matrix multiplication
product = mlmath.matrix_multiply(A, B)  # [[19, 22], [43, 50]]
print("Matrix multiplication:")
for row in product:
    print(f"  {row}")

# Matrix transpose
transpose = mlmath.matrix_transpose(A)  # [[1, 3], [2, 4]]
print("Transpose:")
for row in transpose:
    print(f"  {row}")

# Identity matrix
identity = mlmath.identity_matrix(3)
print("3×3 Identity matrix:")
for row in identity:
    print(f"  {row}")
```

### Probability Operations

```python
import mlmath

# Conditional probability (spam detection example)
events = {
    'total': 1000,
    'contains_free': 300,
    'spam': 400,
    'spam_and_free': 120
}

probs = mlmath.conditional_probability(events)
print(f"P(Spam | Contains 'free'): {probs['P_spam_given_free']:.3f}")

# Bayes' theorem
posterior = mlmath.bayes_theorem(
    prior=0.01,      # P(Disease) = 1%
    likelihood=0.95, # P(Test+ | Disease) = 95%
    evidence=0.05    # P(Test+) = 5%
)
print(f"P(Disease | Test+): {posterior:.3f}")

# Joint probability
joint = mlmath.joint_probability(0.3, 0.4, independent=True)
print(f"P(A and B): {joint}")
```

## 📁 Project Structure

```
python_library/
├── mlmath/                 # Main library package
│   ├── __init__.py        # Package initialization and exports
│   ├── vector.py          # Vector operations module
│   ├── matrix.py          # Matrix operations module
│   └── probability.py     # Probability functions module
├── test_mlmath.py         # Comprehensive test suite
├── demo_mlmath.py         # Demonstration script
├── setup.py              # Package setup configuration
└── README.md             # This documentation
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
python test_mlmath.py
```

The test suite includes:

-   ✅ All function validations
-   ✅ Error handling tests
-   ✅ Edge case verification
-   ✅ Mathematical property checks

## 🎯 Demo

Run the demonstration script to see all features in action:

```bash
python demo_mlmath.py
```

The demo includes:

-   Vector operations examples
-   Matrix operations examples
-   Probability calculations
-   Real-world ML pipeline example

## 📊 Real-World Example: Neural Network Forward Pass

```python
import mlmath

# Input features
input_features = [0.5, 0.8, 0.2]

# Weights (3 inputs → 2 hidden neurons)
weights = [
    [0.2, 0.4, 0.1],  # Hidden neuron 1 weights
    [0.3, 0.1, 0.5]   # Hidden neuron 2 weights
]

# Calculate hidden layer activations
hidden_layer = []
for neuron_weights in weights:
    activation = mlmath.dot_product(input_features, neuron_weights)
    hidden_layer.append(activation)

print(f"Hidden layer: {hidden_layer}")

# Output layer (2 hidden → 1 output)
output_weights = [[0.6, 0.9]]
output = mlmath.matrix_multiply(output_weights, [[h] for h in hidden_layer])

print(f"Final output: {output[0][0]:.3f}")
```

## ✨ Key Features

### 🔒 **Robust Error Handling**

-   Type checking for all inputs
-   Dimension compatibility validation
-   Meaningful error messages
-   Edge case protection

### 📝 **Comprehensive Documentation**

-   Detailed docstrings for all functions
-   Type hints for better IDE support
-   Usage examples in every function
-   Mathematical explanations

### 🎯 **Pure Python Implementation**

-   No external dependencies
-   Easy to understand and modify
-   Suitable for educational purposes
-   Lightweight and portable

### 🧮 **Mathematical Accuracy**

-   Implements standard algorithms
-   Handles floating-point precision
-   Validates mathematical constraints
-   Tested against known results

## 🎓 Educational Value

This library is perfect for:

-   **Learning ML mathematics** - Clear implementations of core concepts
-   **Understanding algorithms** - Pure Python code without black boxes
-   **Building intuition** - Step-by-step mathematical operations
-   **Prototyping** - Quick implementation of mathematical operations

## 🤝 Contributing

This library was created as an educational project. Feel free to:

-   Extend functionality
-   Add new mathematical operations
-   Improve documentation
-   Optimize algorithms

## 📜 License

MIT License - Feel free to use this library for educational and commercial purposes.

## 👨‍💻 Author

**GitHub Copilot**  
Version: 1.0.0  
Date: July 27, 2025

---

_Built with ❤️ for the machine learning community_
