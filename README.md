 
<a href="https://github.com/lukeboxwalker/advent-of-code/actions">![example workflow](https://github.com/lukeboxwalker/advent-of-code/actions/workflows/main.yml/badge.svg)</a>
<a href="https://app.codecov.io/gh/lukeboxwalker/advent-of-code">![coverage](https://img.shields.io/codecov/c/github/lukeboxwalker/advent-of-code)</a>
<a href="https://github.com/lukeboxwalker/advent-of-code/search?l=python">![language](https://img.shields.io/github/languages/top/lukeboxwalker/advent-of-code)</a>
<a href="https://www.python.org/downloads/release/python-370/">![version](https://img.shields.io/badge/python-v3.7-blue)</a>
<a href="https://github.com/lukeboxwalker/advent-of-code/commits/master">![commit](https://img.shields.io/github/last-commit/lukeboxwalker/advent-of-code)</a>

#  Advent of Code 🎄

This repository contains my solutions for [Advent of Code](https://adventofcode.com/) by [Eric Wastl](http://was.tl/).

## Description 🎁
[Advent of Code](https://adventofcode.com/) is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like.

## Setup

To run setup for a given day use `.\aoc\setup.py <year> <day>` in main directory of the project.
This setup creates the following:
* Directory of the year if not exists
* Directory of the day if not exists
* A README.md file containing the puzzle explanation
* An input.txt file with the given user input
* An empty file for the test input mentioned in the puzzle
* A solution.txt to enter the solution for test validation
* The puzzle.py file to solve the puzzle in. Prepared with the basic skeleton structure part 1 and part 2

Note: For the setup to fetch the info a `session_key.yml` is required with the current session key formatted as yml:
```
session: <session_key>
```