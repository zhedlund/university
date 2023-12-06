/*
 * lab4-task1.c
 *
 *  Created on:
 *      Author:
 */

#include <stdio.h>

/* include helper functions for game */
#include "lifegame.h"

/* add whatever other includes here */

#define WORLDWIDTH 39
#define WORLDHEIGHT 20

/* number of generations to evolve the world */
#define NUM_GENERATIONS 50

/* functions to implement */

/* this function should set the state of all
   the cells in the next generation and call
   finalize_evolution() to update the current
   state of the world to the next generation */
void next_generation(void);

/* this function should return the state of the cell
   at (x,y) in the next generation, according to the
   rules of Conway's Game of Life (see handout) */
/* Rules of the Game of Life */
int get_next_state(int x, int y);

/* this function should calculate the number of alive
   neighbors of the cell at (x,y) */
int num_neighbors(int x, int y);

int main(void)
{
	int n;

	/* TODO: initialize the world by hard-coded function initialize_world() in lifegame.c*/
	initialize_world();
	/* evolutions*/
	for (n = 0; n < NUM_GENERATIONS; n++) {
		next_generation();
		output_world(); // output the world state to console
		printf("Press ENTER to continue...\n");
        getchar(); // program pauses, until you press ENTER key to continue
	}
	return 0;
}

void next_generation(void) 
{
	/* for every cell, set the state in the next
	   generation according to the Game of Life rules

	   Hint: use get_next_state(x,y) */
    int i, j;

    for (i = 0; i < WORLDWIDTH; i++) {
        for (j = 0; j < WORLDHEIGHT; j++) {
            int next_state = get_next_state(i, j);
            set_cell_state(i, j, next_state);
        }
    }
	finalize_evolution(); /* called at end to finalize */
}

int get_next_state(int x, int y) {
    int alive_neighbors = num_neighbors(x, y);
    if (world[x][y] == ALIVE) {
        if (alive_neighbors < 2 || alive_neighbors > 3)
            return DEAD; // Any live cell with fewer than two live neighbors dies, as if by underpopulation. Or, any live cell with more than three live neighbors dies, as if by overpopulation.
        else
            return ALIVE; // Any live cell with two or three live neighbors lives on to the next generation.
    } else {
        if (alive_neighbors == 3)
            return ALIVE; // Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        else
            return DEAD; // All other dead cells remain dead.
    }

}
	/* TODO: for the specified cell, return the number of
	   neighbors that are ALIVE

	   Use get_cell_state(x,y) */

int num_neighbors(int x, int y) {
    int count = 0;
    int i, j;

    for (i = -1; i <= 1; i++) {
        for (j = -1; j <= 1; j++) {
            if (i == 0 && j == 0)
                continue; // Skip the current cell itself

            int neighbor_x = x + i;
            int neighbor_y = y + j;

            if (neighbor_x >= 0 && neighbor_x < WORLDWIDTH && neighbor_y >= 0 && neighbor_y < WORLDHEIGHT) {
                count += get_cell_state(neighbor_x, neighbor_y); // Use get_cell_state to check the state of the neighbor
            }
        }
    }
    return count;
}

