import gleam/int
import gleam/io
import gleam/list
import gleam/regexp
import gleam/string

import simplifile

pub fn impl_p1(input: String) -> Int {
  let assert Ok(regex) = regexp.from_string("mul\\([0-9]{1,3},[0-9]{1,3}\\)")
  regexp.scan(regex, input)
  |> list.map(fn(x) {
    string.slice(
      from: x.content,
      at_index: 4,
      length: string.length(x.content) - 5,
    )
    |> string.split(on: ",")
    |> list.filter_map(int.parse)
  })
  |> list.map(list.fold(_, 1, int.multiply))
  |> int.sum
}

fn zip_instr(in: List(String), acc: List(String), need_do: Bool) -> List(String) {
  case in {
    [x1, x2, ..xs] -> {
      case x1 == "do()" {
        True -> zip_instr(xs, [x2, ..acc], False)
        False ->
          case x1 == "don't()" {
            True -> zip_instr(xs, acc, True)
            False ->
              case need_do {
                True -> zip_instr([x2, ..xs], acc, need_do)
                False -> zip_instr([x2, ..xs], [x1, ..acc], need_do)
              }
          }
      }
    }

    [_] -> list.reverse(acc)
    [] -> list.reverse(acc)
  }
}

pub fn impl_p2(input: String) -> Int {
  let assert Ok(regex) =
    regexp.from_string(
      "(don\\'t\\(\\)|do\\(\\))|(mul\\([0-9]{1,3},[0-9]{1,3}\\))",
    )

  regexp.scan(regex, input)
  |> list.map(fn(x) { x.content })
  |> zip_instr([], False)
  |> list.map(fn(x) {
    string.slice(from: x, at_index: 4, length: string.length(x) - 5)
    |> string.split(on: ",")
    |> list.filter_map(int.parse)
  })
  |> list.map(list.fold(_, 1, int.multiply))
  |> int.sum
}

pub fn main() {
  let assert Ok(input) = simplifile.read("./src/inputs/d3input.txt")
  impl_p1(input) |> io.debug
  impl_p2(input) |> io.debug
}
