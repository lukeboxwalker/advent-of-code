<a href="https://github.com/lukeboxwalker/advent-of-code/search?l=python">![language](https://img.shields.io/github/languages/top/lukeboxwalker/advent-of-code)</a>
<a href="https://www.python.org/downloads/release/python-31212">![version](https://img.shields.io/badge/python-v3.12-blue)</a>
<a href="https://github.com/lukeboxwalker/advent-of-code/commits/master">![commit](https://img.shields.io/github/last-commit/lukeboxwalker/advent-of-code)</a>

#  Advent of Code 🎄

This repository contains my solutions for [Advent of Code](https://adventofcode.com/) by [Eric Wastl](http://was.tl/).

## Description 🎁
[Advent of Code](https://adventofcode.com/) is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like.

## Setup ⚙️

To set up a puzzle for a given day, run the following command in the main directory of the project:

```bash
.\aoc\setup.py <year> <day>
```
This setup creates the following:
- **Year directory** – Created if it does not already exist.  
- **Day directory** – Created inside the Year directory if it does not already exist.  
- **README.md** – Contains the puzzle explanation.  
- **input.txt** – Contains your personal puzzle input.  
- **test_input.txt** – Empty file to store any example input mentioned in the puzzle.  
- **solution.txt** – File to enter the solution for test validation.  
- **puzzle.py** – Prepared with the basic skeleton structure for Part 1 and Part 2.

> Note: For the setup to fetch the info a `session_key.yml` is required with the current session key provided as yml: `session: <session_key>`
