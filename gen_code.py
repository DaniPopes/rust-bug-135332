import sys

def generate_code(num_lines):
    code_lines = []
    for i in range(1, num_lines + 1):
        line = f"        self.add_marco_result({i}, just_a_simple_macro!({i}));"
        code_lines.append(line)

    rust_code = "use crate::{just_a_simple_macro, Builder, Something};\n\nimpl Builder {\n    pub fn add_4097_lines_and_panic(&mut self) {\n" + "\n".join(code_lines) + "\n    }\n}"
    return rust_code

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

    with open("src/long_macro_func.rs", "w") as file:
        file.write(generated_code)

    print("Rust code has been generated and saved to long_macro_func.rs")