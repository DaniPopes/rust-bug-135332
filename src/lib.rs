use lazy_static::lazy_static;

mod long_macro_func;

lazy_static! {
    pub static ref JUST_A_SYMBOL: i64 = call_4097_lines_and_panic();
}

fn call_4097_lines_and_panic() -> i64 {
    let mut builder = Builder {};

    builder.add_4097_lines_and_panic();

    1
}

pub(crate) struct Builder {}

impl Builder {
    pub fn add_marco_result(&mut self, _code: i64, _err_code: Something) {}
}

#[derive(Clone, Debug, Default)]
pub struct Something {}

#[macro_export]
macro_rules! just_a_simple_macro {
    ($code:expr) => {
        Something::default()
    };
}
