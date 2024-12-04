# Gmail Variations Generator

The **Gmail Variations Generator** is a Python script for generating all possible Gmail address variations using dots (`.`) and plus suffixes (`+`). This tool can help developers or testers who need bulk Gmail variations for testing purposes or email campaigns.

## Features

- Generates all valid Gmail variations with dots (`.`).
- Appends plus (`+`) suffixes to create even more variations.
- Efficient progress tracking to handle large datasets.
- Saves generated variations to a text file for easy use.

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Output](#output)
- [License](#license)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gmail-variations-generator.git
   cd gmail-variations-generator
   ```

2. **Ensure you have Python 3.6+ installed.**

3. **No additional dependencies required!**

---

## Usage

Run the script from your terminal:

```bash
python script.py
```

The script will prompt for the following inputs:

1. **Folder path**: Where the output file will be saved. Leave empty to use the current directory.
2. **Gmail username**: The base Gmail username (e.g., `example` for `example@gmail.com`).
3. **Number of plus suffix variations**: Determines how many `+suffix` combinations to generate.

### Example Input:

```plaintext
Enter the folder path to save the file (leave empty for current directory):
Enter the Gmail username (e.g., example@gmail.com): example
How many plus suffix variations do you want to generate? 50
```

### Example Command:

```bash
python script.py
```

---

## Examples

### Input Example:

- **Folder path**: `/path/to/output`
- **Gmail username**: `testuser`
- **Plus suffix count**: `5`

### Output Example:

A file named `generated_emails.txt` will be created, containing:

```plaintext
t.e.s.t.u.s.e.r@gmail.com
t.e.s.t.u.s.er@gmail.com
testuser+a@gmail.com
testuser+b@gmail.com
testuser+c@gmail.com
...
```

---

## Output

- The generated email variations will be saved in a text file named `generated_emails.txt`.
- The file will contain one variation per line.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for improvements.

---

## Author

Created by [Your Name](https://github.com/yourusername).

---

## Feedback

If you find this tool helpful or encounter any issues, please feel free to open an issue or reach out via GitHub!

