# Email Word Spam Probability using Bayes' Theorem

This project calculates the probability that an email is spam given that it contains a specific word (e.g., "free") using Bayes' Theorem.

## Problem Statement

From a dataset of emails, calculate the probability that an email is spam given that it contains the word "free": **P(Spam | Free)**

### Default Example:

-   1000 total emails
-   300 emails contain the word "free"
-   400 emails are spam
-   120 emails are both spam and contain the word "free"

## Objective

Calculate: **P(Spam | Email contains "free")** using Bayes' Theorem

## Formula (Bayes' Theorem)

```
P(Spam | Free) = P(Free | Spam) × P(Spam) / P(Free)
```

Where:

-   **P(Spam)** = spam_emails / total_emails
-   **P(Free)** = emails_with_free / total_emails
-   **P(Free | Spam)** = spam_and_free / spam_emails

## Files

-   `simple_spam.py` - Simple implementation following exact assignment requirements
-   `spam_calculator.py` - Comprehensive implementation with detailed calculations and validation
-   `test_spam.py` - Test suite to verify calculation accuracy
-   `README.md` - This documentation file

## Usage

### Run the simple version:

```bash
python simple_spam.py
```

### Run the comprehensive version:

```bash
python spam_calculator.py
```

### Run tests:

```bash
python test_spam.py
```

## Input Requirements

The program asks for the following inputs with validation:

1. **total_emails** - Total number of emails in the dataset
2. **emails_with_free** - Number of emails containing the word "free"
3. **spam_emails** - Number of spam emails
4. **spam_and_free** - Number of emails that are both spam and contain "free"

### Input Validation:

-   All values must be non-negative integers
-   `emails_with_free` cannot exceed `total_emails`
-   `spam_emails` cannot exceed `total_emails`
-   `spam_and_free` cannot exceed `emails_with_free`
-   `spam_and_free` cannot exceed `spam_emails`

## Expected Output

```
P(Spam | Free) = 0.4000
```

_Result printed with 4 decimal places precision_

## Default Example Calculation

Using the default values:

-   Total emails: 1000
-   Emails with "free": 300
-   Spam emails: 400
-   Both spam and "free": 120

**Step-by-step calculation:**

1. P(Spam) = 400/1000 = 0.4000
2. P(Free) = 300/1000 = 0.3000
3. P(Free | Spam) = 120/400 = 0.3000
4. P(Spam | Free) = (0.3000 × 0.4000) / 0.3000 = **0.4000**

**Interpretation:** 40% of emails containing the word "free" are spam.

## Features

### Simple Version (`simple_spam.py`):

-   Clean, minimal implementation
-   User input with validation
-   Direct calculation and output
-   Follows exact assignment requirements

### Comprehensive Version (`spam_calculator.py`):

-   Interactive menu system
-   Detailed step-by-step calculations
-   Default example option
-   Extensive input validation
-   Clear mathematical explanations

### Test Suite (`test_spam.py`):

-   Validates calculation accuracy
-   Tests edge cases and boundary conditions
-   Verifies mathematical properties
-   Manual calculation verification

## Key Concepts Demonstrated

-   **Bayes' Theorem**: Conditional probability calculation
-   **Input Validation**: Ensuring data integrity and logical constraints
-   **Statistical Analysis**: Interpreting probabilistic results
-   **Mathematical Verification**: Testing with known examples and edge cases

## Mathematical Properties

-   All calculated probabilities are between 0 and 1
-   P(Spam | Free) = 0 when no spam emails contain "free"
-   P(Spam | Free) = 1 when all emails with "free" are spam
-   Results are consistent with manual calculations
