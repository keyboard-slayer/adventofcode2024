import gleam/int
import gleam/io
import gleam/list
import gleam/option
import gleam/string
import simplifile

fn is_safe(x1: Int, x2: Int, inc: Bool) -> Bool {
  let sum = x1 - x2
  { inc && sum > 0 && sum <= 3 } || { !inc && sum < 0 && sum >= -3 }
}

fn solve(l: List(Int), inc: option.Option(Bool)) -> Bool {
  case l {
    [x1, x2, ..xs] -> {
      let actual_inc = case inc {
        option.None -> x1 - x2 > 0
        option.Some(i) -> i
      }
      case is_safe(x1, x2, actual_inc) {
        True -> solve([x2, ..xs], option.Some(actual_inc))
        False -> False
      }
    }
    _ -> True
  }
}

pub fn impl_p1(in: String) -> Int {
  string.split(in, on: "\n")
  |> list.filter(fn(l) {
    string.split(l, on: " ")
    |> list.filter_map(int.parse)
    |> solve(option.None)
  })
  |> list.count(fn(x) { !string.is_empty(x) })
}

fn dampen_loop(
  l: List(Int),
  acc: List(Int),
  inc: option.Option(Bool),
) -> List(Int) {
  case l {
    [x, ..xs] -> {
      let newlst = list.append(list.reverse(acc), xs)
      case solve(newlst, inc) {
        True -> newlst
        False -> dampen_loop(xs, [x, ..acc], inc)
      }
    }
    [] -> list.reverse(acc)
  }
}

fn dampen(l: List(Int), inc: option.Option(Bool)) -> List(Int) {
  case solve(l, inc) {
    True -> l
    False -> dampen_loop(l, [], inc)
  }
}

pub fn impl_p2(in: String) -> Int {
  string.split(in, on: "\n")
  |> list.filter(fn(l) {
    string.split(l, on: " ")
    |> list.filter_map(int.parse)
    |> dampen(option.None)
    |> solve(option.None)
  })
  |> list.count(fn(x) { !string.is_empty(x) })
}

pub fn main() {
  let assert Ok(input) = simplifile.read("./src/d2input.txt")
  io.debug(impl_p1(string.trim_end(input)))
  io.debug(impl_p2(string.trim_end(input)))
}
