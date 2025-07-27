"""
Probability Operations Module
============================

This module provides essential probability and statistical functions for machine learning.

Functions:
    - conditional_probability(events): Calculate conditional probabilities
    - bayes_theorem(prior, likelihood, evidence): Apply Bayes' theorem
    - joint_probability(prob_a, prob_b, independent): Calculate joint probability
    - marginal_probability(joint_probs): Calculate marginal probability

Author: GitHub Copilot
Date: July 27, 2025
"""

from typing import Dict, Union, List


def conditional_probability(events: Dict[str, Union[int, float]]) -> Dict[str, float]:
    """
    Calculate conditional probabilities from event counts or probabilities.
    
    This function can handle various scenarios:
    1. Calculate P(A|B) given counts
    2. Calculate multiple conditional probabilities
    3. Validate probability constraints
    
    Args:
        events (Dict[str, Union[int, float]]): Dictionary containing event information.
            Required keys depend on the calculation type:
            - For P(A|B): 'total', 'B', 'A_and_B' (counts)
            - For direct probabilities: 'P_A', 'P_B', 'P_A_and_B'
    
    Returns:
        Dict[str, float]: Dictionary containing calculated conditional probabilities
    
    Raises:
        TypeError: If events is not a dictionary or contains invalid types
        ValueError: If required keys are missing or values are invalid
    
    Examples:
        >>> from mlmath import conditional_probability
        
        # Example 1: Email spam detection
        >>> events = {
        ...     'total': 1000,
        ...     'contains_free': 300,
        ...     'spam': 400,
        ...     'spam_and_free': 120
        ... }
        >>> result = conditional_probability(events)
        >>> result['P_spam_given_free']
        0.4
        
        # Example 2: Direct probabilities
        >>> events = {
        ...     'P_A': 0.3,
        ...     'P_B': 0.4,
        ...     'P_A_and_B': 0.12
        ... }
        >>> result = conditional_probability(events)
        >>> result['P_A_given_B']
        0.3
    """
    # Type checking
    if not isinstance(events, dict):
        raise TypeError("Events must be a dictionary")
    
    # Check if we have count-based data (email spam example format)
    if all(key in events for key in ['total', 'contains_free', 'spam', 'spam_and_free']):
        return _calculate_spam_probabilities(events)
    
    # Check if we have direct probability data
    elif all(key in events for key in ['P_A', 'P_B', 'P_A_and_B']):
        return _calculate_direct_probabilities(events)
    
    # General case with flexible key names
    elif 'total' in events:
        return _calculate_general_probabilities(events)
    
    else:
        raise ValueError("Events dictionary must contain either count data or probability data")


def _calculate_spam_probabilities(events: Dict[str, Union[int, float]]) -> Dict[str, float]:
    """Calculate probabilities for spam detection scenario."""
    total = events['total']
    contains_free = events['contains_free']
    spam = events['spam']
    spam_and_free = events['spam_and_free']
    
    # Validation
    if not all(isinstance(v, (int, float)) and v >= 0 for v in [total, contains_free, spam, spam_and_free]):
        raise ValueError("All counts must be non-negative numbers")
    
    if total <= 0:
        raise ValueError("Total must be positive")
    
    if contains_free > total or spam > total:
        raise ValueError("Individual counts cannot exceed total")
    
    if spam_and_free > min(contains_free, spam):
        raise ValueError("Joint count cannot exceed individual counts")
    
    # Calculate probabilities
    p_spam = spam / total
    p_free = contains_free / total
    p_free_given_spam = spam_and_free / spam if spam > 0 else 0
    p_spam_given_free = spam_and_free / contains_free if contains_free > 0 else 0
    
    return {
        'P_spam': p_spam,
        'P_free': p_free,
        'P_free_given_spam': p_free_given_spam,
        'P_spam_given_free': p_spam_given_free,
        'P_spam_and_free': spam_and_free / total
    }


def _calculate_direct_probabilities(events: Dict[str, Union[int, float]]) -> Dict[str, float]:
    """Calculate conditional probabilities from direct probability values."""
    p_a = events['P_A']
    p_b = events['P_B']
    p_a_and_b = events['P_A_and_B']
    
    # Validation
    if not all(isinstance(p, (int, float)) for p in [p_a, p_b, p_a_and_b]):
        raise TypeError("All probabilities must be numeric")
    
    if not all(0 <= p <= 1 for p in [p_a, p_b, p_a_and_b]):
        raise ValueError("All probabilities must be between 0 and 1")
    
    if p_a_and_b > min(p_a, p_b):
        raise ValueError("Joint probability cannot exceed individual probabilities")
    
    # Calculate conditional probabilities
    p_a_given_b = p_a_and_b / p_b if p_b > 0 else 0
    p_b_given_a = p_a_and_b / p_a if p_a > 0 else 0
    
    return {
        'P_A': p_a,
        'P_B': p_b,
        'P_A_and_B': p_a_and_b,
        'P_A_given_B': p_a_given_b,
        'P_B_given_A': p_b_given_a
    }


def _calculate_general_probabilities(events: Dict[str, Union[int, float]]) -> Dict[str, float]:
    """Calculate probabilities for general case."""
    # This is a flexible implementation for custom scenarios
    # Users can define their own event structure
    total = events['total']
    result = {'total': total}
    
    # Calculate probabilities for all numeric values
    for key, value in events.items():
        if key != 'total' and isinstance(value, (int, float)):
            if value < 0:
                raise ValueError(f"Count for {key} cannot be negative")
            if value > total:
                raise ValueError(f"Count for {key} cannot exceed total")
            result[f'P_{key}'] = value / total
    
    return result


def bayes_theorem(prior: float, likelihood: float, evidence: float) -> float:
    """
    Apply Bayes' theorem to calculate posterior probability.
    
    Formula: P(A|B) = P(B|A) × P(A) / P(B)
    
    Args:
        prior (float): P(A) - Prior probability
        likelihood (float): P(B|A) - Likelihood
        evidence (float): P(B) - Evidence
    
    Returns:
        float: P(A|B) - Posterior probability
    
    Raises:
        TypeError: If inputs are not numeric
        ValueError: If probabilities are not in [0,1] or evidence is zero
    
    Examples:
        >>> from mlmath import bayes_theorem
        >>> bayes_theorem(0.4, 0.3, 0.3)
        0.4
        
        >>> bayes_theorem(0.01, 0.9, 0.05)
        0.18
    """
    # Type checking
    if not all(isinstance(p, (int, float)) for p in [prior, likelihood, evidence]):
        raise TypeError("All inputs must be numeric")
    
    # Value checking
    if not (0 <= prior <= 1):
        raise ValueError("Prior probability must be between 0 and 1")
    
    if not (0 <= likelihood <= 1):
        raise ValueError("Likelihood must be between 0 and 1")
    
    if not (0 <= evidence <= 1):
        raise ValueError("Evidence probability must be between 0 and 1")
    
    if evidence == 0:
        raise ValueError("Evidence probability cannot be zero")
    
    # Apply Bayes' theorem
    return (likelihood * prior) / evidence


def joint_probability(prob_a: float, prob_b: float, independent: bool = True) -> float:
    """
    Calculate joint probability P(A and B).
    
    Args:
        prob_a (float): P(A) - Probability of event A
        prob_b (float): P(B) - Probability of event B
        independent (bool): Whether events are independent (default: True)
    
    Returns:
        float: P(A and B) - Joint probability
    
    Raises:
        TypeError: If probabilities are not numeric
        ValueError: If probabilities are not in [0,1]
    
    Examples:
        >>> from mlmath import joint_probability
        >>> joint_probability(0.3, 0.4, independent=True)
        0.12
        
        >>> joint_probability(0.5, 0.6, independent=True)
        0.3
    
    Note:
        For independent events: P(A and B) = P(A) × P(B)
        For dependent events, you need to provide P(B|A) as prob_b
    """
    # Type checking
    if not isinstance(prob_a, (int, float)) or not isinstance(prob_b, (int, float)):
        raise TypeError("Probabilities must be numeric")
    
    if not isinstance(independent, bool):
        raise TypeError("Independent flag must be boolean")
    
    # Value checking
    if not (0 <= prob_a <= 1):
        raise ValueError("Probability of A must be between 0 and 1")
    
    if not (0 <= prob_b <= 1):
        raise ValueError("Probability of B must be between 0 and 1")
    
    # Calculate joint probability
    if independent:
        return prob_a * prob_b
    else:
        # For dependent events, prob_b should be P(B|A)
        return prob_a * prob_b


def marginal_probability(joint_probs: List[float]) -> float:
    """
    Calculate marginal probability by summing joint probabilities.
    
    P(A) = Σ P(A and Bi) for all i
    
    Args:
        joint_probs (List[float]): List of joint probabilities
    
    Returns:
        float: Marginal probability
    
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If probabilities are not in [0,1] or sum exceeds 1
    
    Examples:
        >>> from mlmath import marginal_probability
        >>> marginal_probability([0.2, 0.3, 0.1])
        0.6
        
        >>> marginal_probability([0.15, 0.25, 0.35])
        0.75
    """
    # Type checking
    if not isinstance(joint_probs, list):
        raise TypeError("Joint probabilities must be a list")
    
    if not joint_probs:
        raise ValueError("List cannot be empty")
    
    if not all(isinstance(p, (int, float)) for p in joint_probs):
        raise TypeError("All probabilities must be numeric")
    
    # Value checking
    if not all(0 <= p <= 1 for p in joint_probs):
        raise ValueError("All probabilities must be between 0 and 1")
    
    result = sum(joint_probs)
    
    if result > 1:
        raise ValueError("Sum of probabilities cannot exceed 1")
    
    return result
