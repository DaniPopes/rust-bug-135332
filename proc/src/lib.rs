use proc_macro::TokenStream;

#[proc_macro]
pub fn declare_big_function(_input: TokenStream) -> TokenStream {
    include_str!("../../src/long_macro_func.rs")
        .parse()
        .unwrap()
}
