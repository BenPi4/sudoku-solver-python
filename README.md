# 🧠 Sudoku Solver in Python

A robust Sudoku solver implemented in Python, leveraging a **hybrid approach** that combines a **heuristic one-stage filling method** with user interaction and a **recursive backtracking algorithm** for generating random boards.

This project offers a comprehensive solution for Sudoku puzzles, including solving given boards, validating their correctness, and generating random boards with initial numbers for new challenges. Empty cells in the board are represented by the value `-1`.

---

## 📁 Project Structure

* `sudoku.py` – The **main script** containing all core functionalities:
    * Sudoku board solving logic (combining heuristic filling and user interaction).
    * Board validation (`is_legit`).
    * Random board generation (`create_random_board`).
    * Functions for printing boards to console (`print_board`) and file (`print_board_to_file`).
    * **Main execution flow for testing various predefined and randomly generated boards.**

* `solved_sudoku.txt` – This file serves as the **output destination** for all program runs. It will contain:
    * Messages indicating whether a board is solvable, unsolvable, or invalid.
    * The solved board (if a solution is found), formatted clearly.

---

## 🎯 Features

* **Solves partially filled boards** using a two-phase approach:
    1.  **Heuristic filling (`one_stage`):** Automatically fills cells where only one legal digit is possible.
    2.  **User-guided filling (`fill_board`):** If the heuristic approach can't proceed, the user is prompted to choose from available options for a specific cell.
* **Validates initial board correctness** (`is_legit`) checking for duplicates in rows, columns, or 3x3 blocks.
* **Generates random Sudoku boards (`create_random_board`)** with 10–20 initial, legally placed digits, ensuring the resulting board is solvable.
* **Saves detailed output directly to `solved_sudoku.txt`**, including solution status and the solved board.
* **Interactive user prompts** during the solving process when multiple valid choices exist for a cell, allowing the user to guide the solution.

---

## ▶️ How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/BenPi4/sudoku-solver-python.git
    ```

2.  **Run the script:**
    ```bash
    python3 sudoku.py
    ```
    The script will automatically attempt to solve a series of **predefined Sudoku boards and one randomly generated board**. During the solving process for certain boards, you will be **prompted to interactively choose digits** for specific cells from the console. All results will be appended to `solved_sudoku.txt`.

---

## 🧪 Sample Output

The output for each board attempt will be appended to `solved_sudoku.txt`. You will see messages and formatted boards similar to these examples:

**Example 1: Solved Board**
```bash
---------------------
5|3|4|6|7|8|9|1|2
6|7|2|1|9|5|3|4|8
1|9|8|3|4|2|5|6|7
8|5|9|7|6|1|4|2|3
4|2|6|8|5|3|7|9|1
7|1|3|9|2|4|8|5|6
9|6|1|5|3|7|2|8|4
2|8|7|4|1|9|6|3|5
3|4|5|2|8|6|1|7|9
---------------------
```
**Example 2: Unsolvable Board**
Board is unsolvable

**Example 3: Invalid Initial Board**
Board is not legit!

**Example 4: User Interaction During Solving (appears in console)**
Choose one number from: [1, 2, 4, 8] for the location: (0, 2)

---

## 🧠 How It Works

The Sudoku solver operates through several key functions and constants:

**Core Functions:**

1.  **Initial Validation (`is_legit`):** Before attempting to solve, the input board is thoroughly checked for any initial duplicates in rows, columns, or 3x3 blocks. An invalid board is immediately flagged.
2.  **Generating Possibilities (`options`, `possible_digits`):**
    * `options(board, loc)` determines all legal digits (1-9) for a specific empty cell, considering its row, column, and 3x3 square. It returns `None` if no options exist, and an empty list `[]` if the cell is already filled.
    * `possible_digits(board)` creates an "options board" (a 9x9 matrix) where each empty cell is replaced by a list of its possible legal digits. Cells that are already filled will have an empty list, and cells with no legal options will be marked with `None`.
3.  **Heuristic Filling (`one_stage`):** This function repeatedly scans the "options board." If it finds any cell with **only one** possible legal digit, it automatically fills that digit into the main Sudoku board and updates the possibilities. This process continues until no more "single-option" cells can be filled. It returns a status (`NOT_FINISH`, `FINISH_SUCCESS`, `FINISH_FAILURE`) and coordinates if further user input is needed.
4.  **Interactive Filling (`fill_board`):**
    * This is the main solving loop. It repeatedly calls `one_stage`.
    * If `one_stage` returns `NOT_FINISH`, `fill_board` identifies the empty cell with the **minimum number of remaining legal options**.
    * The user is then prompted to choose one of these options interactively via the console.
    * This chosen digit is then placed on the board, and the `one_stage` process is re-run. This cycle continues until the board is solved or determined to be unsolvable (due to a user's incorrect choice leading to a contradiction).
5.  **Random Board Generation (`create_random_board`):** This function constructs a new Sudoku board by randomly placing a specified number (10-20) of initial digits in valid positions. It uses the `options` function to ensure each placed digit is legal at its location, thereby generating a solvable board.
6.  **Board Printing (`print_board`, `print_board_to_file`):** These functions format and display the Sudoku board to the console or append it to the specified output file, respectively. Empty cells are displayed as spaces.

**Constants:**

* `FINISH_FAILURE`: Indicates that the board is unsolvable (e.g., due to an invalid initial state or a user's choice leading to a contradiction).
* `FINISH_SUCCESS`: Indicates that the board has been successfully solved.
* `NOT_FINISH`: Indicates that the `one_stage` process cannot fill any more cells automatically, and user input or further backtracking is required.

---

## 🙋‍♂️ Author

Developed by Ben Pitkovsky
