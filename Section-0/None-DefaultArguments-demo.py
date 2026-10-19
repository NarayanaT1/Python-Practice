# Example 1: Understanding None

print("None Value:", None)
print("None Type:", type(None))


# Example 2: Function with default arguments

def email(subject, content, to, cc=None, bcc=None):
    print(f"Subject: {subject}")
    print(f"Content: {content}")
    print(f"To: {to}")
    print(f"CC: {cc}")
    print(f"BCC: {bcc}")
    print("--------------------")


# Example 3: Calling function without optional arguments

email("subject", "great work", "in28minutes@gmail.com")


# Example 4: Calling function with all arguments

email("subject", "great work", "in28minutes@gmail.com", None, None)


# Example 5: Passing None explicitly

email(None, "great work", "in28minutes@gmail.com", None, None)


# Example 6: Checking None using 'is'

var = "123"

if var is None:
    print("Do something")

var = None

if var is None:
    print("Do something")