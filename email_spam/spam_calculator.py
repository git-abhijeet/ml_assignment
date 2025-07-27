"""
Email Word Spam Probability using Bayes' Theorem
===============================================

This program calculates the probability that an email is spam given that it 
contains a specific word (e.g., "free") using Bayes' Theorem.

Formula: P(Spam | Free) = P(Free | Spam) × P(Spam) / P(Free)

Where:
- P(Spam) = spam_emails / total_emails
- P(Free) = emails_with_free / total_emails  
- P(Free | Spam) = spam_and_free / spam_emails

Author: GitHub Copilot
Date: July 27, 2025
"""


def validate_input(value, name, min_value=0, max_value=None):
    """
    Validate user input for numerical values.
    
    Args:
        value (int): The value to validate
        name (str): Name of the parameter for error messages
        min_value (int): Minimum allowed value
        max_value (int): Maximum allowed value (optional)
    
    Returns:
        bool: True if valid, False otherwise
    """
    if value < min_value:
        print(f"Error: {name} must be at least {min_value}")
        return False
    
    if max_value is not None and value > max_value:
        print(f"Error: {name} cannot exceed {max_value}")
        return False
    
    return True


def validate_logical_constraints(total_emails, emails_with_free, spam_emails, spam_and_free):
    """
    Validate logical constraints between the input values.
    
    Args:
        total_emails (int): Total number of emails
        emails_with_free (int): Number of emails containing "free"
        spam_emails (int): Number of spam emails
        spam_and_free (int): Number of emails that are both spam and contain "free"
    
    Returns:
        bool: True if all constraints are satisfied, False otherwise
    """
    # Check if individual counts don't exceed total
    if emails_with_free > total_emails:
        print("Error: emails_with_free cannot exceed total_emails")
        return False
    
    if spam_emails > total_emails:
        print("Error: spam_emails cannot exceed total_emails")
        return False
    
    # Check if intersection doesn't exceed individual sets
    if spam_and_free > emails_with_free:
        print("Error: spam_and_free cannot exceed emails_with_free")
        return False
    
    if spam_and_free > spam_emails:
        print("Error: spam_and_free cannot exceed spam_emails")
        return False
    
    return True


def get_user_input():
    """
    Get and validate user input for email statistics.
    
    Returns:
        tuple: (total_emails, emails_with_free, spam_emails, spam_and_free)
    """
    while True:
        try:
            print("Enter email dataset statistics:")
            print("-" * 35)
            
            total_emails = int(input("Total emails: "))
            if not validate_input(total_emails, "total_emails", min_value=1):
                continue
            
            emails_with_free = int(input("Emails containing 'free': "))
            if not validate_input(emails_with_free, "emails_with_free", min_value=0, max_value=total_emails):
                continue
            
            spam_emails = int(input("Spam emails: "))
            if not validate_input(spam_emails, "spam_emails", min_value=0, max_value=total_emails):
                continue
            
            spam_and_free = int(input("Emails that are both spam and contain 'free': "))
            if not validate_input(spam_and_free, "spam_and_free", min_value=0):
                continue
            
            # Validate logical constraints
            if validate_logical_constraints(total_emails, emails_with_free, spam_emails, spam_and_free):
                return total_emails, emails_with_free, spam_emails, spam_and_free
            else:
                print("\nPlease enter valid values that satisfy all constraints.\n")
                
        except ValueError:
            print("Error: Please enter valid integer values.\n")


def calculate_spam_probability(total_emails, emails_with_free, spam_emails, spam_and_free):
    """
    Calculate P(Spam | Free) using Bayes' Theorem.
    
    Args:
        total_emails (int): Total number of emails
        emails_with_free (int): Number of emails containing "free"
        spam_emails (int): Number of spam emails
        spam_and_free (int): Number of emails that are both spam and contain "free"
    
    Returns:
        dict: Dictionary containing all calculated probabilities
    """
    # Calculate individual probabilities
    p_spam = spam_emails / total_emails
    p_free = emails_with_free / total_emails
    p_free_given_spam = spam_and_free / spam_emails if spam_emails > 0 else 0
    
    # Apply Bayes' Theorem: P(Spam | Free) = P(Free | Spam) × P(Spam) / P(Free)
    p_spam_given_free = (p_free_given_spam * p_spam) / p_free if p_free > 0 else 0
    
    return {
        'p_spam': p_spam,
        'p_free': p_free,
        'p_free_given_spam': p_free_given_spam,
        'p_spam_given_free': p_spam_given_free
    }


def print_detailed_results(total_emails, emails_with_free, spam_emails, spam_and_free, probabilities):
    """
    Print detailed calculation results.
    
    Args:
        total_emails (int): Total number of emails
        emails_with_free (int): Number of emails containing "free"
        spam_emails (int): Number of spam emails
        spam_and_free (int): Number of emails that are both spam and contain "free"
        probabilities (dict): Dictionary containing calculated probabilities
    """
    print("\n" + "=" * 60)
    print("BAYES' THEOREM SPAM PROBABILITY CALCULATION")
    print("=" * 60)
    
    print(f"\nInput Data:")
    print(f"- Total emails: {total_emails:,}")
    print(f"- Emails containing 'free': {emails_with_free:,}")
    print(f"- Spam emails: {spam_emails:,}")
    print(f"- Emails that are both spam and contain 'free': {spam_and_free:,}")
    
    print(f"\nCalculated Probabilities:")
    print(f"- P(Spam) = {spam_emails}/{total_emails} = {probabilities['p_spam']:.4f}")
    print(f"- P(Free) = {emails_with_free}/{total_emails} = {probabilities['p_free']:.4f}")
    print(f"- P(Free | Spam) = {spam_and_free}/{spam_emails} = {probabilities['p_free_given_spam']:.4f}")
    
    print(f"\nBayes' Theorem:")
    print(f"P(Spam | Free) = P(Free | Spam) × P(Spam) / P(Free)")
    print(f"P(Spam | Free) = {probabilities['p_free_given_spam']:.4f} × {probabilities['p_spam']:.4f} / {probabilities['p_free']:.4f}")
    print(f"P(Spam | Free) = {probabilities['p_spam_given_free']:.4f}")
    
    print(f"\n🎯 RESULT:")
    print(f"P(Spam | Email contains 'free') = {probabilities['p_spam_given_free']:.4f}")
    print(f"This means {probabilities['p_spam_given_free']:.1%} of emails containing 'free' are spam.")


def run_default_example():
    """
    Run the calculation with the default example from the problem statement.
    """
    print("Running with default example from problem statement:")
    print("- 1000 total emails")
    print("- 300 emails contain 'free'")
    print("- 400 emails are spam")
    print("- 120 emails are both spam and contain 'free'")
    
    probabilities = calculate_spam_probability(1000, 300, 400, 120)
    print_detailed_results(1000, 300, 400, 120, probabilities)


def main():
    """
    Main function to run the spam probability calculator.
    """
    print("Email Spam Probability Calculator using Bayes' Theorem")
    print("=" * 55)
    
    while True:
        print("\nChoose an option:")
        print("1. Use default example (1000 emails, 300 with 'free', 400 spam, 120 both)")
        print("2. Enter custom values")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            run_default_example()
            
        elif choice == '2':
            total_emails, emails_with_free, spam_emails, spam_and_free = get_user_input()
            probabilities = calculate_spam_probability(total_emails, emails_with_free, spam_emails, spam_and_free)
            print_detailed_results(total_emails, emails_with_free, spam_emails, spam_and_free, probabilities)
            
        elif choice == '3':
            print("Thank you for using the spam probability calculator!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
