# compare_list_and_dictionary.py

code_snippets = {
    "Working Dictionary Example": {
        "code": """
numbers = {}
numbers[0] = -5
numbers[1] = 10.5
""",
        "explanation": "This snippet works because dictionaries allow assignments to keys, and the keys do not need to exist initially. Values are directly mapped to keys.",
        "fixed_code": None
    },
    "Non-working List Example": {
        "code": """
other_numbers = []
other_numbers[0] = -5
other_numbers[1] = 10.5
""",
        "explanation": "This code does not work because you cannot assign to list indices that don't exist yet. Lists must first be populated or expanded before assignment.",
        "fixed_code": """
other_numbers = []
other_numbers.append(-5)
other_numbers.append(10.5)
"""
    }
}

# Looping over the dictionary and printing results
for title, details in code_snippets.items():
    print(f"Title: {title}")
    print("Code Snippet:")
    print(details['code'])
    print("\nExplanation:")
    print(details['explanation'])

    if details['fixed_code']:
        print("\nFixed Code:")
        print(details['fixed_code'])

    print("\n" + "-" * 50 + "\n")
