def validate_choice(prompt: str, min_val: int, max_val: int) -> int:
    """
    Validate menu choice input
    Args:
        prompt (str): Message to display
        min_val (int): Minimum valid choice
        max_val (int): Maximum valid choice
    Returns:
        int: Validated user choice
    """
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input. Please enter a number.")

def validate_username(username: str) -> bool:
    """
    Validate username format
    Args:
        username (str): Username to validate
    Returns:
        bool: True if valid, False otherwise
    """
    # Check if empty
    if not username:
        print("Username can't be empty!")
        return False
    
    # Check length
    if len(username) < 3:
        print("Username must be at least 3 characters")
        return False
    
    # Check for invalid characters
    invalid_chars = set("!@#$%^&*()+={}[]|\\:;\"'<>,?/ ")
    if any(char in invalid_chars for char in username):
        print("Username contains invalid characters")
        return False
    
    return True

def format_time(seconds: int) -> str:
    """
    Format time in seconds to MM:SS format
    Args:
        seconds (int): Time in seconds
    Returns:
        str: Formatted time string
    """
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02d}:{secs:02d}"

def display_header(title: str) -> None:
    """
    Display a formatted header
    Args:
        title (str): Title to display
    """
    print("\n" + "=" * 40)
    print(title.center(40))
    print("=" * 40)

# Test function for validation
def test_validation() -> None:
    """Test validation functions"""
    print("\nTesting choice validation...")
    choice = validate_choice("Enter a number between 1-5: ", 1, 5)
    print(f"Valid choice: {choice}")
    
    print("\nTesting username validation:")
    test_usernames = ["", "ab", "valid_name", "invalid@name"]
    for username in test_usernames:
        print(f"\nTesting '{username}':")
        if validate_username(username):
            print("Valid username")

if __name__ == "__main__":
    test_validation()