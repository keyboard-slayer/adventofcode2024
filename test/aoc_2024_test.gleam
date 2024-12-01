import gleeunit
import gleeunit/should

import day1

pub fn main() {
  gleeunit.main()
}

// gleeunit test functions end in `_test`
pub fn day1_test() {
  let input =
    "3   4
    4   3
    2   5
    1   3
    3   9
    3   3"
  day1.impl_p1(input) |> should.equal(11)
  day1.impl_p2(input) |> should.equal(31)
}
