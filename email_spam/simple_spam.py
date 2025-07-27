"""
Simple Email Spam Probability Calculator
=======================================

This is a simplified version that follows the exact assignment requirements:
- Ask for user inputs with validation
- Calculate P(Spam | Free) using Bayes' Theorem
- Print the result with 4 decimal places

Formula: P(Spam | Free) = P(Free | Spam) × P(Spam) / P(Free)

Author: GitHub Copilot
Date: July 27, 2025
"""


def get_validated_input(prompt, name, min_val=0, max_val=None):
    """Get and validate a single input value."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_val:
                print(f"Error: {name} must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Error: {name} cannot exceed {max_val}")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid integer")


def main():
    """Main function following exact assignment requirements."""
    print("Email Spam Probability Calculator")
    print("=" * 35)
    
    # Ask for inputs from user with validation
    total_emails = get_validated_input("Enter total emails: ", "total_emails", min_val=1)
    
    emails_with_free = get_validated_input("Enter emails with 'free': ", "emails_with_free", 
                                         min_val=0, max_val=total_emails)
    
    spam_emails = get_validated_input("Enter spam emails: ", "spam_emails", 
                                    min_val=0, max_val=total_emails)
    
    spam_and_free = get_validated_input("Enter emails that are both spam and contain 'free': ", 
                                      "spam_and_free", min_val=0)
    
    # Validate logical constraints
    if spam_and_free > emails_with_free:
        print("Error: spam_and_free cannot exceed emails_with_free")
        return
    if spam_and_free > spam_emails:
        print("Error: spam_and_free cannot exceed spam_emails")
        return
    
    # Calculate probabilities using Bayes' Theorem
    if emails_with_free == 0:
        print("Error: Cannot calculate probability when emails_with_free is 0")
        return
    
    p_spam = spam_emails / total_emails
    p_free = emails_with_free / total_emails
    p_free_given_spam = spam_and_free / spam_emails if spam_emails > 0 else 0
    
    # Apply Bayes' Theorem: P(Spam | Free) = P(Free | Spam) × P(Spam) / P(Free)
    p_spam_given_free = (p_free_given_spam * p_spam) / p_free
    
    # Print the result with 4 decimal places
    print(f"\nP(Spam | Free) = {p_spam_given_free:.4f}")


if __name__ == "__main__":
    main()
