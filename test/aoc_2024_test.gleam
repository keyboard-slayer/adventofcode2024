import gleeunit
import gleeunit/should

import day1
import day2
import day3

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

pub fn day3_test() {
  let input =
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
  let input2 =
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
  day3.impl_p1(input) |> should.equal(161)
  day3.impl_p2(input2) |> should.equal(48)
}
