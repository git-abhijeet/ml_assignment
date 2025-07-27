"""
Demo script showing the email spam probability calculation
with the default example from the problem statement.
"""

from spam_calculator import calculate_spam_probability, print_detailed_results


def main():
    """Run the default example calculation."""
    print("Email Spam Probability - Default Example")
    print("=" * 40)
    
    # Default example from problem statement
    total_emails = 1000
    emails_with_free = 300
    spam_emails = 400
    spam_and_free = 120
    
    print("Problem Statement:")
    print(f"- Total emails: {total_emails}")
    print(f"- Emails containing 'free': {emails_with_free}")
    print(f"- Spam emails: {spam_emails}")
    print(f"- Emails that are both spam and contain 'free': {spam_and_free}")
    
    # Calculate probabilities
    probabilities = calculate_spam_probability(total_emails, emails_with_free, spam_emails, spam_and_free)
    
    # Show detailed calculation
    print_detailed_results(total_emails, emails_with_free, spam_emails, spam_and_free, probabilities)


if __name__ == "__main__":
    main()
