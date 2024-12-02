import gleeunit
import gleeunit/should

import day1
import day2

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

pub fn day2_test() {
  let input =
    "7 6 4 2 1
  1 2 7 8 9
  9 7 6 2 1
  1 3 2 4 5
  8 6 4 4 1
  3 5 8 11 11 15
  1 3 6 7 9"
  day2.impl_p1(input) |> should.equal(2)
  day2.impl_p2(input) |> should.equal(4)
}
