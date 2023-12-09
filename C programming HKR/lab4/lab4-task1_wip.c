/*
 * lab4-task1.c
 *
 *  Created on:
 *      Author:
 */

#include <stdio.h>
#include "lifegame.h"

/* add whatever other includes here */

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

	initialize_world();
	/* evolutions*/
	for (n = 0; n < NUM_GENERATIONS; n++) {
		next_generation();
		output_world(); // output the world state to console
		printf("Press ENTER to continue...\n");
        getchar(); // program pauses, until you press ENTER key to continue
	}
	return (0);
}

	/* for every cell, set the state in the next
	   generation according to the Game of Life rules */
void next_generation(void) 
{
    int		x;
	int		y;
	int		next_state;

    for (x = 0; x < get_world_width(); x++) // move to next column
	{
        for (y = 0; y < get_world_height(); y++) // move to next row
		{
            next_state = get_next_state(x, y); // compute the state in next generation
            set_cell_state(x, y, next_state); // set the state in next generation
        }
    }
	finalize_evolution(); /* called at end to finalize */
}

/* for the specified cell, compute the state in
	the next generation using the rules

	   Use num_neighbors(x,y) to compute the number of live
	   neighbors */

int get_next_state(int x, int y)
{
    int alive_neighbors = num_neighbors(x, y); // get the number of live neighbors 
    
	if (get_cell_state(x, y) == ALIVE)
	{
        if (alive_neighbors < 2 || alive_neighbors > 3)
            return (DEAD); // cell with < 2 or > 3 neighbors dies
        else
            return (ALIVE); // cell with 2-3 neighbors lives to next generation
    }
	else
	{
        if (alive_neighbors == 3)
            return (ALIVE); // dead cell w exactly 3 live neighbors becomes a live cell
        else
            return (DEAD); // All other dead cells remain dead
    }

}
	/*for the specified cell, return the number of
	   neighbors that are ALIVE. Using get_cell_state(x,y)
	   to check state of neighbor cells */

int num_neighbors(int x, int y)
{
    int	count = 0;
    int	i;
	int	j;
	int	neighbor_x;
	int	neighbor_y;

    for (i = -1; i <= 1; i++) // checks surrounding cells
	{
        for (j = -1; j <= 1; j++)
		{
            if (i == 0 && j == 0)
                continue; // Skip the current cell

            neighbor_x = x + i;
            neighbor_y = y + j;

            if (neighbor_x >= 0 && neighbor_x < get_world_width() && neighbor_y >= 0 && neighbor_y < get_world_height())
                count += get_cell_state(neighbor_x, neighbor_y); 
        }
    }
    return (count);
}

