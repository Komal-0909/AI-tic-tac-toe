AI - Based Tic Tac Toe Game

# Features
1. Graphical User Interface using Pygame
2. AI opponent using Minimax Algorithm
3. Restart and Exit Button
4. Tracks wins, loosses and draws
5. Clean and user-friendly interface

# Techonologies used
1. Python
2. Pygame
3. Minimax Algorithm

# Working of Project
1. Game starts with an empty 3*3 Tic Tac Toe board displayed using a graphical user interface build with Pygame.
2. The Human player makes a move by clicking on an empty cell in the board. The Human player uses the symbol "O".
3. After human moves, the AI player automatically makes its move using the 'Minimax Algorithm'. The AI evaluates all possible future game states and choose the optimal move to maximize its chances of winning. AI uses the symbol "X".
4. After every move, the game checks for a winning condition by comparing rows,columns and diagonals. If a player satisfies a winning condition, the game ends.
5. If all cells are filled and no player wins, the game is declared a "Drwa".
6. The result (Win/Loss/Draw) is displayed using a popup message at the center of the game board.
7. The game keeps track of the total number of 'human wins, AI wins and Draws', which are displayed at the top of the screen.
8. After the match ends,the user can click the 'Restart'button to start a new game or click the 'Exit' button to close the application.

# How to Run the Project
1. Install Python
2. Install pygame:
    '''bash
        pip install pygame
3. Run the Game
        python tic_tac_toe.py