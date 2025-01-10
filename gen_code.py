import subprocess
import sys


def generate_code(num_lines):
    count = 0

    def get_string():
        nonlocal count
        count += 1
        return f'"string{count}".to_owned()'

    return f"""\
pub type BigType = Vec<Vec<String>>;

pub fn big_function() -> BigType {{
    vec![
        {",\n        ".join(f"vec![{get_string()}]" for _ in range(num_lines))}
    ]
}}
"""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_code.py <number_of_lines>")
        sys.exit(1)

    try:
        num_lines = int(sys.argv[1])
        if num_lines <= 0:
            raise ValueError("Number of lines must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    generated_code = generate_code(num_lines)

    path = "src/long_macro_func.rs"
    with open(path, "w") as file:
        file.write(generated_code)

    # rustfmt
    subprocess.run(["cargo", "fmt"])

    print(f"Rust code has been generated and saved to {path}")
