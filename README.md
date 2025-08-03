# 🧩 Sudoku Solver in Python

A clean, efficient Sudoku solver written in Python that uses a recursive **backtracking algorithm** enhanced with the **Minimum Remaining Values (MRV)** heuristic to solve any standard 9x9 Sudoku board automatically.

---

## 🚀 Features

- ✅ **Fully automatic solving** — no user input required
- 🧠 **MRV heuristic** — selects the next empty cell with the fewest valid options to improve efficiency
- 🔍 **Board validation** — checks whether a given board is valid before attempting to solve
- 🎲 **Random board generation** — builds random boards with valid placements (not guaranteed to be solvable)
- 🖨️ **Console and file output** — solved boards are printed and saved to `solved_soduko.txt`

---

## 📁 Project Structure

- `sudoku_solver.py` — the main script, includes:

  - `solve_sudoku(board)` — recursive solver with MRV
  - `options(board, loc)` — legal values for a cell
  - `is_legit(board)` — checks for duplicates
  - `create_random_board(board)` — fills random digits legally
  - `print_board()` and `print_board_to_file()` — formatting
  - Predefined test boards and run logic

- `solved_soduko.txt` — generated output with solved boards

---

## ▶️ How to Run

```bash
python3 sudoku.py
```

This will attempt to solve several predefined boards and one random board. The results will be printed to `solved_soduko.txt`.

---

## 🧪 Example Output (solved\_soduko.txt)

```
Here is the solved board!
-----------------
5|3|4|6|7|8|9|1|2
6|7|2|1|9|5|3|4|8
1|9|8|3|4|2|5|6|7
8|5|9|7|6|1|4|2|3
4|2|6|8|5|3|7|9|1
7|1|3|9|2|4|8|5|6
9|6|1|5|3|7|2|8|4
2|8|7|4|1|9|6|3|5
3|4|5|2|8|6|1|7|9
-----------------
```

If the board is unsolvable or invalid, a message will be written instead:

```
Board is unsolvable
Board is not legit
```

---

## 🧠 Algorithm Summary

- **Backtracking:** Tries every legal option for the next cell recursively.

- **MRV (Minimum Remaining Values):** Chooses the next cell with the fewest legal digits to minimize branching.

---

## 👨‍💻 Author
