Rustc bug: https://github.com/rust-lang/rust/issues/132900

## How to reproduce

```bash
python3 gen_code.py 4097
RUSTFLAGS="-g" cargo build --release
```

While if the number is less than 4097, it will work fine.
```bash
python3 gen_code.py 4096
RUSTFLAGS="-g" cargo build --release
```


## What's the problem

A function with 4097 lines of code will cause a panic when the macro is expanded.
