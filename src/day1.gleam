import gleam/int
import gleam/io
import gleam/list
import gleam/pair
import gleam/result
import gleam/string

import simplifile

pub fn impl_p1(in: String) {
  let lines =
    list.map(string.split(in, on: "\n"), fn(x) {
      string.split(string.trim_start(x), on: "   ")
    })

  let left =
    list.sort(
      list.map(lines, fn(x) {
        result.unwrap(result.try(list.first(x), int.parse), -1)
      }),
      int.compare,
    )

  let right =
    list.sort(
      list.map(lines, fn(x) {
        result.unwrap(result.try(list.last(x), int.parse), -1)
      }),
      int.compare,
    )

  int.sum(
    list.map(list.zip(left, right), fn(p) {
      int.absolute_value(pair.first(p) - pair.second(p))
    }),
  )
}

pub fn impl_p2(in: String) {
  let lines =
    list.map(string.split(in, on: "\n"), fn(x) {
      string.split(string.trim_start(x), on: "   ")
    })

  let left =
    list.map(lines, fn(x) {
      result.unwrap(result.try(list.first(x), int.parse), -1)
    })

  let right =
    list.map(lines, fn(x) {
      result.unwrap(result.try(list.last(x), int.parse), -1)
    })

  int.sum(list.map(left, fn(x) { x * list.count(right, fn(y) { x == y }) }))
}

pub fn main() {
  let assert Ok(input) = simplifile.read("./src/inputs/d1input.txt")
  io.debug(impl_p1(input))
  io.debug(impl_p2(input))
}
