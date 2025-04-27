def print_board(board):
    """Print the Sudoku board in a readable format"""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                
            if j == 8:
                print(board[i][j] if board[i][j] != 0 else '.')
            else:
                print(str(board[i][j]) if board[i][j] != 0 else '.', end=" ")

def find_empty(board):
    """Find an empty cell in the board (represented by 0)"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, column
    return None

def is_valid(board, num, pos):
    """Check if a number is valid in a given position"""
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve(board):
    """Solve the Sudoku using backtracking"""
    find = find_empty(board)
    if not find:
        return True  # Puzzle is solved
    else:
        row, col = find
    
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            
            if solve(board):
                return True
            
            board[row][col] = 0  # Reset if solution not found
    
    return False

def get_user_input():
    """Get Sudoku puzzle input from user"""
    print("Enter your Sudoku puzzle row by row.")
    print("Use numbers 1-9 for filled cells and 0 or . for empty cells.")
    print("Separate numbers with spaces.")
    
    board = []
    for i in range(9):
        while True:
            row_input = input(f"Row {i+1}: ").strip()
            if not row_input:
                print("Please enter a row.")
                continue
            
            # Replace dots with zeros and split into list
            row = row_input.replace('.', '0').split()
            
            # Validate input
            if len(row) != 9:
                print("Error: Each row must have exactly 9 numbers.")
                continue
            
            try:
                row = [int(num) for num in row]
                if any(num < 0 or num > 9 for num in row):
                    print("Error: Numbers must be between 0-9.")
                    continue
                board.append(row)
                break
            except ValueError:
                print("Error: Please enter numbers only.")
    
    return board

def main():
    print("SUDOKU SOLVER")
    print("-------------")
    
    board = get_user_input()
    
    print("\nUnsolved Sudoku:")
    print_board(board)
    print("\nSolving...\n")
    
    if solve(board):
        print("Solved Sudoku:")
        print_board(board)
    else:
        print("No solution exists for this Sudoku.")

if __name__ == "__main__":
    main()
