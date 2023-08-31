# SudokuSolver
 Algorithm to solve sudoku puzzles

Makes use of OOP and recursion. Concept involves iterating through every empty spot, and finding the spot with the least possible moves available and fill in that one first. 

A grid is invalid if there is a spot with value '0' and has no possible values that can be placed there. If so, algorithm backtracks and tries another number in the previous spot.

Recursion is repeated until the solution is found.

Grid test sets from https://github.com/dimitri/sudoku/tree/master