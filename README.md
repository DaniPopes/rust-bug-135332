Rustc bug: https://github.com/rust-lang/rust/issues/135332

## How to reproduce

```bash
# Threshold for the LLVM error.
N=1366

# If on nightly:
#export RUSTFLAGS="-Zverify-llvm-ir"

# OK.
python3 gen_code.py $((N - 1))
cargo build --release

# Not OK.
python3 gen_code.py $N
cargo build --release
```

Error:
```
inlinable function call in a function with debug info must have a !dbg location
  tail call fastcc void @_ZN5alloc5alloc18handle_alloc_error17hfb68ebdb2cc3f698E(i64 noundef 8, i64 noundef 24) #83
inlinable function call in a function with debug info must have a !dbg location
  tail call fastcc void @_ZN5alloc5alloc18handle_alloc_error17hfb68ebdb2cc3f698E(i64 noundef 8, i64 noundef 24) #83
rustc-LLVM ERROR: Broken module found, compilation aborted!
```
