# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python educational project called "数字猜猜乐" (Number Guessing Game) designed to teach 19 key Python keywords through interactive gameplay. The project contains two implementations:

- `guess_num_simple.py`: Basic procedural implementation for beginners
- `guess_num.py`: Object-oriented implementation using classes

Both files implement the same number guessing game (1-100) but demonstrate different programming paradigms and complexity levels.

## Development Commands

### Environment Setup
```bash
uv sync                    # Install dependencies
```

### Running the Applications
```bash
uv run guess_num_simple.py  # Run the simple version
uv run guess_num.py         # Run the object-oriented version
```

### Dependencies
- Python >= 3.13
- colorama >= 0.4.6 (for colored terminal output)

## Architecture Notes

### Simple Version (`guess_num_simple.py`)
- Procedural programming approach
- Global variables for game state
- Single file with linear flow
- Designed for absolute beginners

### Standard Version (`guess_num.py`)
- Object-oriented design with `GuessGame` class
- Encapsulated state management (number, tries)
- Separated game logic from main execution
- Demonstrates proper Python class structure

### Common Patterns
Both files demonstrate:
- Input validation using `isdigit()` and range checking
- Colorama for terminal styling with `Fore.COLOR` constants
- `while True` loops with `break` for game flow
- Exception-free user input handling

## Educational Purpose

This codebase specifically targets teaching these Python keywords:
`import`, `from`, `global`, `class`, `def`, `return`, `if`, `else`, `while`, `not`, `and`, `or`, `continue`, `break`, `pass`, `print`, `None`, `True`, `False`

When modifying code, preserve the educational value and ensure both versions remain distinct examples of different programming approaches.