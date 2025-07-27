"""
MLMath Library Demo
==================

This demonstration script shows how to use the MLMath library
for various machine learning mathematical operations.

Author: GitHub Copilot
Date: July 27, 2025
"""

import sys
import os

# Add the current directory to path to import mlmath
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mlmath


def demo_vector_operations():
    """Demonstrate vector operations."""
    print("=" * 50)
    print("VECTOR OPERATIONS DEMO")
    print("=" * 50)
    
    # Define some example vectors
    vector_a = [1, 2, 3]
    vector_b = [4, 5, 6]
    
    print(f"Vector A: {vector_a}")
    print(f"Vector B: {vector_b}")
    print()
    
    # Dot product
    dot_prod = mlmath.dot_product(vector_a, vector_b)
    print(f"Dot Product (A · B): {dot_prod}")
    
    # Vector addition
    sum_vec = mlmath.vector_add(vector_a, vector_b)
    print(f"Vector Addition (A + B): {sum_vec}")
    
    # Vector subtraction
    diff_vec = mlmath.vector_subtract(vector_b, vector_a)
    print(f"Vector Subtraction (B - A): {diff_vec}")
    
    # Vector magnitude
    mag_a = mlmath.vector_magnitude(vector_a)
    mag_b = mlmath.vector_magnitude(vector_b)
    print(f"Magnitude of A: {mag_a:.3f}")
    print(f"Magnitude of B: {mag_b:.3f}")
    
    # Vector normalization
    norm_a = mlmath.vector_normalize(vector_a)
    norm_b = mlmath.vector_normalize(vector_b)
    print(f"Normalized A: {[round(x, 3) for x in norm_a]}")
    print(f"Normalized B: {[round(x, 3) for x in norm_b]}")
    
    # Demonstrate orthogonal vectors
    ortho_a = [1, 0, 0]
    ortho_b = [0, 1, 0]
    ortho_dot = mlmath.dot_product(ortho_a, ortho_b)
    print(f"\nOrthogonal vectors {ortho_a} · {ortho_b} = {ortho_dot}")
    print()


def demo_matrix_operations():
    """Demonstrate matrix operations."""
    print("=" * 50)
    print("MATRIX OPERATIONS DEMO")
    print("=" * 50)
    
    # Define example matrices
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    
    print("Matrix A:")
    for row in matrix_a:
        print(f"  {row}")
    
    print("\nMatrix B:")
    for row in matrix_b:
        print(f"  {row}")
    print()
    
    # Matrix multiplication
    product = mlmath.matrix_multiply(matrix_a, matrix_b)
    print("Matrix Multiplication (A × B):")
    for row in product:
        print(f"  {row}")
    
    # Matrix addition
    sum_matrix = mlmath.matrix_add(matrix_a, matrix_b)
    print("\nMatrix Addition (A + B):")
    for row in sum_matrix:
        print(f"  {row}")
    
    # Matrix subtraction
    diff_matrix = mlmath.matrix_subtract(matrix_b, matrix_a)
    print("\nMatrix Subtraction (B - A):")
    for row in diff_matrix:
        print(f"  {row}")
    
    # Matrix transpose
    transpose_a = mlmath.matrix_transpose(matrix_a)
    print("\nTranspose of A:")
    for row in transpose_a:
        print(f"  {row}")
    
    # Identity matrix
    identity_3 = mlmath.identity_matrix(3)
    print("\n3×3 Identity Matrix:")
    for row in identity_3:
        print(f"  {row}")
    print()


def demo_probability_operations():
    """Demonstrate probability operations."""
    print("=" * 50)
    print("PROBABILITY OPERATIONS DEMO")
    print("=" * 50)
    
    # Email spam detection example
    print("Example 1: Email Spam Detection")
    print("-" * 32)
    
    events = {
        'total': 1000,
        'contains_free': 300,
        'spam': 400,
        'spam_and_free': 120
    }
    
    print(f"Dataset: {events['total']} emails")
    print(f"- {events['contains_free']} contain 'free'")
    print(f"- {events['spam']} are spam")
    print(f"- {events['spam_and_free']} are spam AND contain 'free'")
    print()
    
    spam_probs = mlmath.conditional_probability(events)
    print("Calculated Probabilities:")
    print(f"- P(Spam): {spam_probs['P_spam']:.3f}")
    print(f"- P(Free): {spam_probs['P_free']:.3f}")
    print(f"- P(Free | Spam): {spam_probs['P_free_given_spam']:.3f}")
    print(f"- P(Spam | Free): {spam_probs['P_spam_given_free']:.3f}")
    print()
    
    # Bayes' theorem example
    print("Example 2: Bayes' Theorem")
    print("-" * 26)
    
    prior = 0.01  # P(Disease) = 1%
    likelihood = 0.95  # P(Positive Test | Disease) = 95%
    evidence = 0.05  # P(Positive Test) = 5%
    
    posterior = mlmath.bayes_theorem(prior, likelihood, evidence)
    
    print(f"Medical Test Scenario:")
    print(f"- Prior P(Disease): {prior}")
    print(f"- Likelihood P(Test+ | Disease): {likelihood}")
    print(f"- Evidence P(Test+): {evidence}")
    print(f"- Posterior P(Disease | Test+): {posterior:.3f}")
    print()
    
    # Joint probability example
    print("Example 3: Joint Probability")
    print("-" * 28)
    
    prob_rain = 0.3
    prob_cold = 0.4
    
    joint_independent = mlmath.joint_probability(prob_rain, prob_cold, independent=True)
    joint_dependent = mlmath.joint_probability(prob_rain, 0.6, independent=False)  # P(Cold | Rain) = 0.6
    
    print(f"P(Rain): {prob_rain}")
    print(f"P(Cold): {prob_cold}")
    print(f"P(Rain AND Cold) [independent]: {joint_independent:.3f}")
    print(f"P(Rain AND Cold) [dependent]: {joint_dependent:.3f}")
    print()
    
    # Marginal probability example
    print("Example 4: Marginal Probability")
    print("-" * 31)
    
    # P(A) = P(A,B1) + P(A,B2) + P(A,B3)
    joint_probs = [0.15, 0.25, 0.10]
    marginal = mlmath.marginal_probability(joint_probs)
    
    print(f"Joint probabilities: {joint_probs}")
    print(f"Marginal probability: {marginal:.3f}")
    print()


def demo_real_world_example():
    """Demonstrate a real-world machine learning example."""
    print("=" * 50)
    print("REAL-WORLD ML EXAMPLE")
    print("=" * 50)
    
    print("Scenario: Simple Neural Network Forward Pass")
    print("-" * 42)
    
    # Input layer (3 features)
    input_features = [0.5, 0.8, 0.2]
    print(f"Input features: {input_features}")
    
    # Weights matrix (3 inputs → 2 hidden neurons)
    weights_input_hidden = [
        [0.2, 0.4, 0.1],  # Weights for hidden neuron 1
        [0.3, 0.1, 0.5]   # Weights for hidden neuron 2
    ]
    
    print("Weights (Input → Hidden):")
    for i, row in enumerate(weights_input_hidden):
        print(f"  Hidden neuron {i+1}: {row}")
    
    # Calculate hidden layer activations using dot product
    hidden_layer = []
    for neuron_weights in weights_input_hidden:
        activation = mlmath.dot_product(input_features, neuron_weights)
        hidden_layer.append(activation)
    
    print(f"\nHidden layer activations: {[round(x, 3) for x in hidden_layer]}")
    
    # Weights matrix (2 hidden → 1 output)
    weights_hidden_output = [[0.6, 0.9]]  # Weights for output neuron
    
    print(f"Weights (Hidden → Output): {weights_hidden_output[0]}")
    
    # Calculate output using matrix multiplication
    output_matrix = mlmath.matrix_multiply(weights_hidden_output, [[h] for h in hidden_layer])
    output = output_matrix[0][0]
    
    print(f"Final output: {output:.3f}")
    print()
    
    # Feature engineering example
    print("Feature Engineering Example:")
    print("-" * 28)
    
    # Normalize features
    feature_magnitude = mlmath.vector_magnitude(input_features)
    normalized_features = mlmath.vector_normalize(input_features)
    
    print(f"Original features: {input_features}")
    print(f"Feature magnitude: {feature_magnitude:.3f}")
    print(f"Normalized features: {[round(x, 3) for x in normalized_features]}")
    print()
    
    # Feature combination
    additional_features = [0.1, 0.9, 0.4]
    combined_features = mlmath.vector_add(input_features, additional_features)
    
    print(f"Additional features: {additional_features}")
    print(f"Combined features: {combined_features}")
    print()


def demo_library_info():
    """Demonstrate library information functions."""
    print("=" * 50)
    print("LIBRARY INFORMATION")
    print("=" * 50)
    
    version = mlmath.get_version()
    info = mlmath.get_info()
    
    print(f"Library: {info['name']}")
    print(f"Version: {version}")
    print(f"Author: {info['author']}")
    print(f"Description: {info['description']}")
    print()
    
    print("Available Functions:")
    print("- Vector Operations: dot_product, vector_add, vector_subtract, vector_magnitude, vector_normalize")
    print("- Matrix Operations: matrix_multiply, matrix_transpose, matrix_add, matrix_subtract, identity_matrix")
    print("- Probability: conditional_probability, bayes_theorem, joint_probability, marginal_probability")
    print()


def main():
    """Run all demonstrations."""
    print("MLMath Library Demonstration")
    print("Python Library for Machine Learning Mathematics")
    print("Author: GitHub Copilot")
    print()
    
    demo_library_info()
    demo_vector_operations()
    demo_matrix_operations()
    demo_probability_operations()
    demo_real_world_example()
    
    print("=" * 50)
    print("DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 50)
    print("You can now use the MLMath library in your own projects!")
    print("Import with: import mlmath")


if __name__ == "__main__":
    main()
