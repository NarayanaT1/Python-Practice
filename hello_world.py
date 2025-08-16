# src/utils/hello_world.py

def say_hello(name: str = "CloudByteHub") -> str:
    """
    Returns a simple greeting message.
    
    Args:
        name (str): The name to greet.
    
    Returns:
        str: Greeting message.
    """
    return f"👋 Hello, {name}! Welcome to the future of cloud automation."


if __name__ == "__main__":
    # Sample usage
    message = say_hello()
    print(message)
