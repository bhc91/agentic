# agentic

This repository contains a simple interpreter for a custom programming language with `.ai` file extensions. The language supports basic variable assignment, arithmetic operations, and printing values.

## Features

- **Variable Assignment**: Assign integer values to variables.
- **Arithmetic Operations**: Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Printing**: Print variables or evaluated expressions to the console.
- **Simple Syntax**: Easy-to-learn syntax for quick scripting.

## Example Program (`hello_world.ai`)

```ai
x = 10
y = x + 5
print y
```

### Expected Output
```
15
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/simple-language-interpreter.git
   cd simple-language-interpreter
   ```

2. Make the main script executable:
   ```bash
   chmod +x agentic
   ```

3. Optionally, move the `agentic` script to a directory in your PATH to run it globally:
   ```bash
   sudo mv agentic /usr/local/bin
   ```

## Usage

1. Create a `.ai` program file in the `examples/` directory or elsewhere.
2. Run the program using:
   ```bash
   ./agentic examples/hello_world.ai
   ```

If you've moved the `agentic` script to a global PATH directory, you can run:
```bash
agentic examples/hello_world.ai
```

## Project Structure

```
simple_language/
├── tokenizer.py          # Handles tokenization of the source code
├── parser.py             # Builds the abstract syntax tree (AST)
├── interpreter.py        # Executes the AST
├── agentic               # Main entry point for executing `.ai` programs
├── examples/
│   └── hello_world.ai    # Example `.ai` program
└── README.md             # Project documentation
```

## Language Syntax

- **Variable Assignment**:
  ```ai
  x = 10
  ```
- **Arithmetic Operations**:
  ```ai
  result = x + y - 3 * z / 2
  ```
- **Print Statement**:
  ```ai
  print x
  ```

## Error Handling

The interpreter provides meaningful error messages for:
- **Syntax Errors**: Incorrect program syntax.
- **Name Errors**: Use of undefined variables.
- **File Errors**: Missing or unreadable `.ai` files.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
