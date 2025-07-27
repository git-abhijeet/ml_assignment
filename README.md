# ML Assignment

This repository contains various machine learning related projects and implementations.

## Projects

### 📁 `vector_operation/`

Vector operations and matrix multiplication implementations without using NumPy.

#### Features:

-   **Vector Operations**: Addition, dot product, orthogonality check
-   **Matrix Operations**: Matrix multiplication using nested loops

#### Quick Start:

```bash
cd vector_operation
python vector_matrix_operations.py
```

### 📁 `rolling_two_dice/`

Dice rolling simulation to estimate probabilities using Monte Carlo methods.

#### Features:

-   **Probability Estimation**: P(Sum = 7), P(Sum = 2), P(Sum > 10)
-   **Monte Carlo Simulation**: 10,000 dice roll simulations
-   **Statistical Analysis**: Compare simulated vs theoretical probabilities

#### Quick Start:

```bash
cd rolling_two_dice
python simple_dice.py
```

### 📁 `email_spam/`

Email spam probability calculation using Bayes' Theorem.

#### Features:

-   **Bayes' Theorem**: Calculate P(Spam | Contains "free")
-   **Input Validation**: Comprehensive data validation and constraint checking
-   **Statistical Analysis**: Step-by-step probability calculations

#### Quick Start:

```bash
cd email_spam
python simple_spam.py
```

### 📁 `python_library/`

Custom Python library (MLMath) for machine learning mathematics.

#### Features:

-   **Vector Operations**: dot_product, vector_add, vector_subtract, vector_magnitude, vector_normalize
-   **Matrix Operations**: matrix_multiply, matrix_transpose, matrix_add, matrix_subtract, identity_matrix
-   **Probability Functions**: conditional_probability, bayes_theorem, joint_probability, marginal_probability

#### Quick Start:

```bash
cd python_library
python demo_mlmath.py
```

## Directory Structure

```
ml_assignment/
├── README.md
├── vector_operation/
│   ├── README.md
│   ├── vector_matrix_operations.py
│   ├── test_operations.py
│   └── demo.py
├── rolling_two_dice/
│   ├── README.md
│   ├── simple_dice.py
│   ├── dice_simulation.py
│   └── test_dice.py
├── email_spam/
│   ├── README.md
│   ├── simple_spam.py
│   ├── spam_calculator.py
│   ├── test_spam.py
│   └── demo.py
└── python_library/
    ├── README.md
    ├── mlmath/
    │   ├── __init__.py
    │   ├── vector.py
    │   ├── matrix.py
    │   └── probability.py
    ├── test_mlmath.py
    ├── demo_mlmath.py
    └── setup.py
```

## Getting Started

Each project directory contains its own README with specific instructions. Navigate to the respective directory to explore individual projects.

## Projects Overview

| Project            | Description                              | Key Concepts                                       |
| ------------------ | ---------------------------------------- | -------------------------------------------------- |
| `vector_operation` | Linear algebra operations without NumPy  | Vector math, matrix multiplication                 |
| `rolling_two_dice` | Probability estimation via simulation    | Monte Carlo methods, statistical analysis          |
| `email_spam`       | Spam detection using Bayes' Theorem      | Conditional probability, Bayesian inference        |
| `python_library`   | Custom MLMath library for ML mathematics | Package development, comprehensive ML math toolkit |
