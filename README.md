### Conway's Game of Life Simulation

This program implements a version of John Conway's Game of Life using Pygame. The simulation allows users to interact with the grid by activating and deactivating cells with the mouse. This script was almost entirely written using GPT 3.5.

The game follows the rules of the Game of Life:
- A cell is activated if it has exactly three active neighboring cells.
- A cell remains active if it has two or three active neighboring cells and is deactivated otherwise.

#### Instructions:
1. Run the program (jogo_da_vida.py).
2. Click cells to turn them on or off.
3. Observe the evolution of the simulation based on the rules of the Game of Life.

#### Controls:
- Click and drag the mouse to activate the cells.

#### Dependencies:
- Pygame 2.5.2

#### Code Overview:
- The program initializes a grid with cells that can be activated or deactivated.
- The `update_grid` function applies the rules of the Game of Life to update cell states.
- The grid is updated every 0.25 seconds, updating cell states accordingly.
- Users can interact with the grid using the mouse to change cell states.
