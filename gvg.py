import os

def generate_dot_suffixes(username):
    """Generate all valid dot suffix variations of a Gmail username systematically."""
    results = set()
    n = len(username) - 1  # Number of positions for dots
    total_combinations = 1 << n  # Total number of combinations (2^n)

    # Generate all combinations using bit masking
    for mask in range(total_combinations):
        dotted_username = username[0]  # Start with the first character
        for i in range(n):
            if mask & (1 << i):  # Check if the i-th bit is set
                dotted_username += "."  # Add a dot
            dotted_username += username[i + 1]  # Add the next character
        results.add(dotted_username)

    return sorted(results)

def generate_plus_suffixes(username, count):
    """Generate plus suffix variations for a Gmail username."""
    results = []
    for i in range(count):
        suffix = f"+{i}"
        results.append(suffix)
    return results

def generate_combined_variations(username, plus_count):
    """Generate combined dot and plus suffixes for a Gmail username with progress."""
    dot_variations = generate_dot_suffixes(username)
    plus_variations = generate_plus_suffixes(username, plus_count)

    total_variations = len(dot_variations) * (1 + len(plus_variations))
    processed = 0

    # Incrementally process combinations
    for variant in dot_variations:
        yield f"{variant}@gmail.com"
        processed += 1
        if processed % 100 == 0 or processed == total_variations:
            print(f"\rGenerating combined variations... {processed}/{total_variations} ({processed / total_variations:.2%})", end="")
    
    for plus in plus_variations:
        for variant in dot_variations:
            yield f"{variant}{plus}@gmail.com"
            processed += 1
            if processed % 100 == 0 or processed == total_variations:
                print(f"\rGenerating combined variations... {processed}/{total_variations} ({processed / total_variations:.2%})", end="")
    
    print("\nGeneration complete!")

def save_to_file(file_path, variations):
    """Save the generated variations to a text file."""
    with open(file_path, 'w') as file:
        for variation in variations:
            file.write(f"{variation}\n")
    print(f"\nGenerated variations and saved to {file_path}")

def main():
    folder = input("Enter the folder path to save the file (leave empty for current directory): ").strip()
    if not folder:
        folder = os.getcwd()

    username = input("Enter the Gmail username (e.g., example@gmail.com): ").strip()
    if not username:
        username = "example"
    username = username.split('@')[0]

    plus_count = int(input("How many plus suffix variations do you want to generate? "))

    print("Generating email addresses...\n")
    file_path = os.path.join(folder, "generated_emails.txt")
    variations = generate_combined_variations(username, plus_count)

    save_to_file(file_path, variations)

if __name__ == "__main__":
    main()
